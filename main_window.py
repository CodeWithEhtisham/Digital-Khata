
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
import sys
from create_business import NewBusinessWindow
from update_business_details import UpdateBusinessWindow
from update_user_details import UpdateUserWindow
from update_password import ChangePasswordWindow
from add_roznamcha import RozNamchaWindow
from account_details import AccountDetailsWindow
from add_accounts import AddAccountsWindow
from khata_details import KhataWindow
# from cash_paid import CashPaidWindow
from PyQt5.uic import loadUiType
from resources_rc import *

FORM_MAIN, _ = loadUiType('ui/main_window.ui')


class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.showMaximized()
        self.update()
        self.khata_select_update()
        # home page show when window open on load
        self.Handle_Buttons()

        # Set column width for specific column
        self.accounts_table.setColumnWidth(0, 50)
        self.accounts_table.setColumnWidth(1, 300)
        self.accounts_table.setColumnWidth(2, 200)
        self.accounts_table.setColumnWidth(3, 300)
        self.accounts_table.setColumnWidth(4, 200)

        self.roznamcha_table.setColumnWidth(0, 50)
        self.roznamcha_table.setColumnWidth(1, 120)
        self.roznamcha_table.setColumnWidth(2, 130)
        self.roznamcha_table.setColumnWidth(3, 230)
        self.roznamcha_table.setColumnWidth(5, 190)
        self.roznamcha_table.setColumnWidth(6, 160)
        self.roznamcha_table.setColumnWidth(7, 160)

    def Handle_Buttons(self):
        self.btn_home.clicked.connect(self.home)
        self.btn_roznamcha.clicked.connect(self.roznamcha)
        self.btn_settings.clicked.connect(self.settings)
        self.btn_add_roznamcha.clicked.connect(self.add_roznamcha)
        self.btn_logout.clicked.connect(self.logout)
        self.btn_accounts.clicked.connect(self.accounts)

        # option selection btns
        self.khata_options.activated.connect(self.get_khata)

        # add btns
        self.btn_add_khata.clicked.connect(self.add_khata)
        self.btn_add_accounts.clicked.connect(self.add_accounts)
        self.btn_print_RN.clicked.connect(self.print_roznamcha_table_pdf)

        # tables double clicked
        self.accounts_table.doubleClicked.connect(self.account_details)
        

        # business btns
        self.btn_business_details.clicked.connect(self.business_details)
        self.btn_change_business_details.clicked.connect(self.edit_business)
        self.btn_change_user_details.clicked.connect(self.change_user_details)
        self.btn_change_pwd.clicked.connect(self.change_password)
        self.txt_date_from_RN.setDate(QDate.currentDate())
        self.txt_date_to_RN.setDate(QDate.currentDate())

        # search opton table
        self.txt_search_RN.textChanged.connect(
            lambda: self.search_roznamcha(self.txt_search_RN.text()))
        self.btn_search_RN.clicked.connect(
            lambda: self.search_roznamcha(self.txt_search_RN.text(), "date"))
        self.btn_refresh_RN.clicked.connect(self.update)
        self.btn_refresh_accounts.clicked.connect(self.update)
        self.txt_search.textChanged.connect(self.search_accounts)

    def print_roznamcha_table_pdf(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <style>
                body {
                    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                }
                table,
                th,
                td {
                    border-bottom: 1px solid gray;
                    border-collapse: collapse;
                }
                th,
                td {
                    padding: 10px 2px;
                    text-align: left;
                }
                td:nth-child(7) {
                    color: green;
                }
                td:nth-child(8) {
                    color: red;
                }
                thead {
                    background-color: #29b6f6;
                    font-size: 20px;
                    font-weight: 700;
                }
                tbody {
                    font-size: 18px;
                    font-weight: 600;
                }
                h1 {
                    text-align: center;
                }
                h2 {
                    text-align: right;
                }
            </style>
            </head>
            
            <body>
                <div>
                    <h1>Business Name</h1>
                    <h2>Business Contact</h2>
                </div>
                <div>
                    <h1>Roznamcha</h1>
                    <h2>Balance</h2>
                </div>
                <table style="width:100%">
                    <thead>
                        <tr>
                            <th>S/NO</th>
                            <th>Date</th>
                            <th>Cash IN/Out</th>
                            <th>Name</th>
                            <th>Refrence</th>
                            <th>Description</th>
                            <th>Cash In</th>
                            <th>Cash Out</th>
                            <th>Remaining</th>
                        </tr>
                    </thead>
                    <tbody>
                    """
            for i in range(self.roznamcha_table.rowCount()):
                html += "<tr>"
                for j in range(self.roznamcha_table.columnCount()):
                    html += "<td>" + \
                        self.roznamcha_table.item(i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
            
            </body>
            </html>
            """
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")

    def search_accounts(self):
        search = self.txt_search.text()
        if self.khata_options.currentText() != "Select Khata":
            if self.khata_options.currentText() == "":
                self.update()
                return
            # data = self.db.select(table_name='accounts', columns="accounts_id,name,phone,address,balance", condition=f"khata_id={self.get_khata_id(self.khata_options.currentText())} and name LIKE '%{search}%' or phone LIKE '%{search}%' or address LIKE '%{search}%'")
            data = self.db.conn.execute(
                f"SELECT accounts_id,name,phone,address,balance FROM accounts WHERE khata_id={self.get_khata_id(self.khata_options.currentText())} and name LIKE '%{search}%' or phone LIKE '%{search}%' or address LIKE '%{search}%'").fetchall()
            if data:
                self.update_table(data=data, obj=self.accounts_table)
                payable = sum([i[4] for i in data if i[4] < 0])
                receivable = sum([i[4] for i in data if i[4] > 0])
                self.lbl_total_receivable.setText(str(receivable))
                self.lbl_total_payable.setText(str(payable))
                self.lbl_total_accounts.setText(str(len(data)))

                if receivable < 0:
                    self.lbl_total_receivable.setStyleSheet("color: red")
                else:
                    self.lbl_total_receivable.setStyleSheet("color: green")

                if payable < 0:
                    self.lbl_total_payable.setStyleSheet("color: red")
                else:
                    self.lbl_total_payable.setStyleSheet("color: green")
            else:
                self.accounts_table.setRowCount(0)

        else:
            self.accounts_table.setRowCount(0)

    def search_roznamcha(self, search, type="all"):
        if type == "all":
            data = self.db.conn.execute(
                f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and a.name LIKE '%{search}%' or r.description LIKE '%{search}%' or r.refrences LIKE '%{search}%'").fetchall()
        elif type == "date":
            from_date = self.txt_date_from_RN.text()
            to_date = self.txt_date_to_RN.text()
            data = self.db.conn.execute(
                f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date BETWEEN '{from_date}' and '{to_date}'").fetchall()
        else:
            self.update()
            return

        cash_in = 0
        cash_out = 0
        self.roznamcha_table.setRowCount(0)
        for index, row in enumerate(data):
            self.roznamcha_table.insertRow(index)
            cash_in += row[6]
            cash_out += row[7]
            for idx, i in enumerate(row):
                self.roznamcha_table.setItem(
                    index, idx, QTableWidgetItem(str(i)))
            self.roznamcha_table.item(
                index, 6).setForeground(QColor(0, 255, 0))
            self.roznamcha_table.item(
                index, 7).setForeground(QColor(255, 0, 0))

        self.lbl_total_cash_In.setText(str(cash_in))
        self.lbl_total_cash_out.setText(str(cash_out))
        self.lbl_total_cash_In.setStyleSheet("color: green")
        self.lbl_total_cash_out.setStyleSheet("color: red")

    def update(self):
        data = self.db.select(table_name='business',
                              columns="*", condition="id=1")
        if data:
            self.lbl_business_name.setText(data[0][1])
            self.lbl_business_contact.setText(data[0][4])
            self.lbl_business_address.setText(data[0][3])

        # khata table
        if self.khata_options.currentText() != "Select Khata":
            data = self.db.select(table_name='accounts', columns="accounts_id,name,phone,address,balance",
                                  condition=f"khata_id={self.get_khata_id(self.khata_options.currentText())}")

            if data:
                self.update_table(data=data, obj=self.accounts_table)
                payable = sum([i[4] for i in data if i[4] < 0])
                receivable = sum([i[4] for i in data if i[4] > 0])

                self.lbl_total_receivable.setText(str(receivable))
                self.lbl_total_payable.setText(str(payable))
                self.lbl_total_accounts.setText(str(len(data)))

                # self.accounts_table.item(
                #     index, 7).setForeground(QColor(255, 0, 0))

                if receivable < 0:
                    self.lbl_total_receivable.setStyleSheet("color: red")
                else:
                    self.lbl_total_receivable.setStyleSheet("color: green")

                if payable < 0:
                    self.lbl_total_payable.setStyleSheet("color: red")
                else:
                    self.lbl_total_payable.setStyleSheet("color: green")

            else:
                self.accounts_table.setRowCount(0)
        else:
            self.accounts_table.setRowCount(0)

        # roznamcha table
        if self.khata_options.currentText() != "Select Khata":
            previous_day = QDate.currentDate().addDays(-1).toString('dd/MM/yyyy')
            last_id = self.db.conn.execute(
                f"SELECT r.roznamcha_id FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date = '{previous_day}'").fetchall()
            if last_id:
                last_id = last_id[-1][0]
                data = self.db.conn.execute(
                    f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date = '{QDate.currentDate().toString('dd/MM/yyyy')}' or r.roznamcha_id = {last_id}")
            else:
                data = self.db.conn.execute(
                    f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date = '{QDate.currentDate().toString('dd/MM/yyyy')}'").fetchall()

            if data:
                cash_in = 0
                cash_out = 0
                self.roznamcha_table.setRowCount(0)
                for index, row in enumerate(data):
                    self.roznamcha_table.insertRow(index)
                    cash_in += row[6]
                    cash_out += row[7]
                    for idx, i in enumerate(row):
                        self.roznamcha_table.setItem(
                            index, idx, QTableWidgetItem(str(i)))
                    self.roznamcha_table.item(
                        index, 6).setForeground(QColor(0, 255, 0))
                    self.roznamcha_table.item(
                        index, 7).setForeground(QColor(255, 0, 0))
                self.lbl_total_cash_In.setText(str(cash_in))
                self.lbl_total_cash_out.setText(str(cash_out))
                self.lbl_total_cash_In.setStyleSheet("color: green")
                self.lbl_total_cash_out.setStyleSheet("color: red")
            else:
                self.roznamcha_table.setRowCount(0)

    def account_details(self):
        # get selected row first cell
        id = self.accounts_table.item(
            self.accounts_table.currentRow(), 0).text()
        name = self.accounts_table.item(
            self.accounts_table.currentRow(), 1).text()
        self.window = AccountDetailsWindow(id, name)
        self.window.show()

    def khata_select_update(self):
        data = self.db.select_all(table_name='khata', columns="khata_name")
        if data:
            self.khata_options.clear()
            self.khata_options.addItem("Select Khata")
            self.khata_options.addItems([i[0] for i in data])

    def logout(self):
        from login_page import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def get_khata(self):
        khata = self.khata_options.currentText()
        if khata != "Select Khata":
            self.lbl_user_khata.setText(khata)
            self.update()

        else:
            self.khata_select_update()
            self.update()

    def get_khata_id(self, name):
        if name != "Select Khata":
            return self.db.select(table_name='khata', columns="khata_id", condition=f"khata_name='{name}'")[0][0]
        # return self.db.select(table_name='khata',columns="khata_id",condition=f"khata_name='{name}'")[0][0]

    def add_accounts(self):
        try:
            khata_id = self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.add_accounts = AddAccountsWindow(khata_id=khata_id)
                self.add_accounts.show()
            else:
                QMessageBox.warning(
                    self, "warning", f"Please Select Khata {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Please Select Khata {e}")

    # def search_roznamcha_by_date(self):
    #     from_date=self.txt_date_from_rn.date().toString("dd/MM/yyyy")
    #     to_date=self.txt_date_to_rn.date().toString("dd/MM/yyyy")
    #     db=DBHandler()
    #     data=db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id WHERE roznamcha.date BETWEEN '{from_date}' AND '{to_date}'").fetchall()
    #     self.roznamcha_table.setRowCount(0)
    #     for index,row in enumerate(data):
    #             self.roznamcha_table.insertRow(index)
    #             for idx,i in enumerate(row):
    #                 self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))

    # def search_roznamcha_by_name(self):
    #     option=self.search_option_rn.currentText()
    #     if option=="Select Option":
    #         QMessageBox.warning(self,"Error","Please Select Search Option")
    #     else:
    #         value=self.txt_search_rn.text()
    #         db=DBHandler()
    #         data=db.conn.execute(f"SELECT date,products.product_name,quantity,rate,total_amount,customers.name,cash_paid,cash_received FROM roznamcha LEFT JOIN customers ON roznamcha.customer_id=customers.custmer_id LEFT JOIN products ON roznamcha.product_id=products.product_id Where customers.name LIKE '%{value}%'").fetchall()
    #         self.roznamcha_table.setRowCount(0)
    #         for index,row in enumerate(data):
    #             self.roznamcha_table.insertRow(index)
    #             for idx,i in enumerate(row):
    #                 self.roznamcha_table.setItem(index,idx,QTableWidgetItem(str(i)))

    def add_khata(self):
        self.window = KhataWindow()
        self.window.show()

    def add_roznamcha(self):
        try:
            khata_id = self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.roznamcha_window = RozNamchaWindow(khata_id=khata_id)
                self.roznamcha_window.show()
            else:
                QMessageBox.warning(
                    self, "warning", f"Please Select Khata {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Please Select Khata {e}")

    def update_table(self, data, obj):
        obj.setRowCount(0)
        for index, row in enumerate(data):
            obj.insertRow(index)
            for idx, i in enumerate(row):
                obj.setItem(index, idx, QTableWidgetItem(str(i)))
        # main page

    def change_user_details(self):
        self.changeuserdetaisls = UpdateUserWindow()
        self.changeuserdetaisls.show()

    def change_password(self):
        self.changepassword = ChangePasswordWindow()
        self.changepassword.show()

    def business_details(self):
        self.business_details = NewBusinessWindow()
        self.business_details.show()

    def edit_business(self):
        self.edit_business = UpdateBusinessWindow()
        self.edit_business.show()

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)
        self.update()

    def accounts(self):
        self.stackedWidget.setCurrentWidget(self.accounts_page)
        self.update()

    def roznamcha(self):
        self.stackedWidget.setCurrentWidget(self.roznamcha_page)
        self.update()

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)
        self.update()
        db = DBHandler()
        data = db.select_all('users', "*")
        if data:
            self.txt_user_name.setText(data[0][1])
            self.txt_user_email.setText(data[0][2])
            self.txt_user_contact.setText(data[0][3])
            self.txt_user_username.setText(data[0][4])

        data = db.select_all('business', "*")
        if data:
            self.txt_business_name.setText(data[0][1])
            self.txt_business_email.setText(data[0][2])
            self.txt_business_contact.setText(data[0][4])
            self.txt_business_address.setText(data[0][3])
            self.txt_business_owner.setText(data[0][5])
            self.btn_business_details.hide()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


# import datetime
# import sqlite3
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QApplication
# # from db_handler import DBHandler
# import sys
# from os import path
# from PyQt5.uic import loadUiType

# from add_accounts import AddAccountsWindow
# from add_roznamcha import RozNamchaWindow
# from account_details import AccountDetailsWindow
# from create_business import NewBusinessWindow

# FORM_MAIN, _ = loadUiType('ui/main_window.ui')


# class MainWindow(QMainWindow, FORM_MAIN):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setupUi(self)
#         self.showMaximized()
#         self.Handle_Buttons()

#     def Handle_Buttons(self):
#         self.btn_home.clicked.connect(self.home)
#         self.btn_accounts.clicked.connect(self.accounts)
#         self.btn_roznamcha.clicked.connect(self.roznamcha)
#         self.btn_settings.clicked.connect(self.settings)

#         self.btn_add_accounts.clicked.connect(self.add_accounts)
#         self.btn_add_roznamcha.clicked.connect(self.add_roznamcha)

#         self.accounts_table.doubleClicked.connect(self.account_details)

#         self.btn_business_details.clicked.connect(self.business_details)

#     def home(self):
#         self.stackedWidget.setCurrentWidget(self.home_page)

#     def accounts(self):
#         self.stackedWidget.setCurrentWidget(self.accounts_page)

#     def roznamcha(self):
#         self.stackedWidget.setCurrentWidget(self.roznamcha_page)

#     def settings(self):
#         self.stackedWidget.setCurrentWidget(self.settings_page)

#     def add_accounts(self):
#         self.window = AddAccountsWindow()
#         self.window.show()

#     def add_roznamcha(self):
#         self.window = RozNamchaWindow()
#         self.window.show()

#     def account_details(self):
#         self.window = AccountDetailsWindow()
#         self.window.show()

#     def business_details(self):
#         self.window = NewBusinessWindow()
#         self.window.show()


# def main():
#     app = QApplication(sys.argv)
#     window = MainWindow()
#     window.show()
#     app.exec_()


# if __name__ == '__main__':
#     main()
