
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
from update_roznamcha import UpdateRozNamchaWindow
from update_accounts import UpdateAccountsWindow
# from cash_paid import CashPaidWindow
from PyQt5.uic import loadUiType
from resources_rc import *
from datetime import datetime

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

        #
        self.btn_change_business_details.hide()
        
        # 
        roznomcha_scrollBar = self.roznamcha_table.verticalScrollBar()
        roznomcha_scrollBar.rangeChanged.connect(
            lambda: roznomcha_scrollBar.setValue(roznomcha_scrollBar.maximum()))

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
        self.btn_print_accounts.clicked.connect(self.print_accounts_table_pdf)

        # tables double clicked
        self.accounts_table.doubleClicked.connect(self.account_details)
        self.roznamcha_table.doubleClicked.connect(self.roznamcha_update)
        self.btn_edit_accounts.clicked.connect(self.update_account)

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
        # self.select_range_roznamcha.currentTextChanged.connect(
        #     lambda: self.search_roznamcha(self.txt_search_RN.text(), "range"))
        self.btn_refresh_RN.clicked.connect(self.update)
        self.btn_refresh_accounts.clicked.connect(self.update)
        self.txt_search.textChanged.connect(self.search_accounts)

    def update_account(self):
        # Check if there is a selected item in the table
        if self.accounts_table.currentItem() is not None:
            id = self.accounts_table.item(
                self.accounts_table.currentRow(), 0).text()
            self.window_update = UpdateAccountsWindow(id)
            self.window_update.show()
            self.window_update.btn_save.clicked.connect(self.update)
        else:
            QMessageBox.warning(
                self, "warning", "Please Select Account")


    def roznamcha_update(self):
        row_id = self.roznamcha_table.currentRow()
        id = self.roznamcha_table.item(row_id, 0).text()
        self.update_roznamcha = UpdateRozNamchaWindow(id)
        self.update_roznamcha.show()
        self.update_roznamcha.btn_update.clicked.connect(self.update)
        self.update_roznamcha.btn_clear.clicked.connect(self.update)

    def print_accounts_table_pdf(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <style>
                .td:nth-child(7) {
                    color: green;
                }
                .td:nth-child(8) {
                    color: red;
                }
            </style>
            </head>
            
            <body>
                <h1 style="text-align: center;"> """ + self.lbl_business_name.text() + """</h1>
                <h2 style="text-align: right; font-weight: 400;">Contact : """ + self.lbl_business_contact.text() + """</h2>
                <h1 style="text-align: center;">Accounts</h1>
                <h3 style="text-align: right;"> Total Accounts : <span> """ + self.lbl_total_accounts.text() + """</span></h3>
                <h3 style="text-align: right;"> Payable Balance : <span style=" color: green;"> """ + self.lbl_total_payable.text() + """</span></h3>
                <h3 style="text-align: right;"> Receivable Balance : <span style=" color: red;"> """ + self.lbl_total_receivable.text() + """</span></h3>
                <h3 style="text-align: left;">Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <table style="border-bottom: 1px solid gray;
                    border-collapse: collapse;
                    width: 100%;">
                    <thead style="width: 100%;">
                        <tr style="background-color: #29b6f6; font-size: 10px; width: 100%;">
                            <th style="padding: 4px; text-align: left;">S/NO</th>
                            <th style="padding: 4px; text-align: left;">Name</th>
                            <th style="padding: 4px; text-align: left;">Mobile</th>
                            <th style="padding: 4px; text-align: left;">Address</th>
                            <th style="padding: 4px; text-align: left;">Remaining Balance</th>
                        </tr>
                    </thead>
                    <tbody style="font-size: 10px; width: 100%;">
                    """
            for i in range(self.accounts_table.rowCount()):
                html += "<tr>"
                for j in range(self.accounts_table.columnCount()):
                    html += """<td style="padding: 4px; text-align: left;">""" + \
                        self.accounts_table.item(i, j).text()+"</td>"
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

    def print_roznamcha_table_pdf(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(
                QtPrintSupport.QPrinter.PrinterResolution)
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPaperSize(QtPrintSupport.QPrinter.A4)
            printer.setOrientation(QtPrintSupport.QPrinter.Portrait)
            printer.setOutputFileName(filename[0])
            document = QtGui.QTextDocument()
            html = """
            <!DOCTYPE html>
            <html lang="en">
            <head>
            <style>
                .td:nth-child(7) {
                    color: green;
                }
                .td:nth-child(8) {
                    color: red;
                }
            </style>
            </head>
            
            <body>
                <h1 style="text-align: center;"> """ + self.lbl_business_name.text() + """</h1>
                <h2 style="text-align: right; font-weight: 400;">Contact : """ + self.lbl_business_contact.text() + """</h2>
                <h1 style="text-align: center;">Roznamcha</h1>
                <h3 style="text-align: right;"> Cash In : <span style=" color: green;"> """ + self.lbl_total_cash_In.text() + """</span></h3>
                <h3 style="text-align: right;"> Cash Out : <span style=" color: red;"> """ + self.lbl_total_cash_out.text() + """</span></h3>
                <h3 style="text-align: left;">Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                <table style="border-bottom: 1px solid gray;
                    border-collapse: collapse;
                    width: 100%;">
                    <thead>
                        <tr style="background-color: #29b6f6; font-size: 10px;">
                            <th style="padding: 4px; text-align: left;">S/NO</th>
                            <th style="padding: 4px; text-align: left;">Date</th>
                            <th style="padding: 4px; text-align: left;">Cash IN/Out</th>
                            <th style="padding: 4px; text-align: left;">Name</th>
                            <th style="padding: 4px; text-align: left;">Refrence</th>
                            <th style="padding: 4px; text-align: left;">Description</th>
                            <th style="padding: 4px; text-align: left;">Cash In</th>
                            <th style="padding: 4px; text-align: left;">Cash Out</th>
                            <th style="padding: 4px; text-align: left;">Remaining</th>
                        </tr>
                    </thead>
                    <tbody style="font-size: 10px;">
                    """
            for i in range(self.roznamcha_table.rowCount()):
                html += "<tr>"
                for j in range(self.roznamcha_table.columnCount()):
                    html += """<td style="padding: 4px; text-align: left;">""" + \
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

    def update_account_table(self, data):
        payable = 0
        receivable = 0
        if data:
            self.accounts_table.setRowCount(0)
            for index, row in enumerate(data):
                self.accounts_table.insertRow(index)
                for idx, i in enumerate(row):
                    # if idx == 4 and i > 0:
                    #     payable += i
                    #     print(payable)
                    # elif idx == 4 and i < 0:
                    #     receivable += i
                    if idx == len(row)-1:
                        print(row[0])
                        accounts_last_balance = self.db.conn.execute(
                            f"SELECT accounts_remaining FROM roznamcha WHERE accounts_id={row[0]} ORDER BY roznamcha_id DESC LIMIT 1").fetchone()
                        if accounts_last_balance:
                            i = accounts_last_balance[0]+row[4]
                            print("update",i)
                            if i >= 0:
                                payable += i
                            else:
                                receivable += i
                    if isinstance(i, (float, int)):
                        i = f"{int(i):,}"
                    self.accounts_table.setItem(
                        index, idx, QTableWidgetItem(str(i)))
            # print(payable, receivable)
            self.lbl_total_receivable.setText(str(f"{int(receivable):,}"))
            self.lbl_total_payable.setText(str(f"{int(payable):,}"))
            self.lbl_net_balance.setText(str(f"{int(receivable+payable):,}"))
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

    def search_accounts(self):
        search = self.txt_search.text()
        if self.khata_options.currentText() != "Select Business":
            if self.khata_options.currentText() == "":
                self.update()
                return
            data = self.db.conn.execute(
                f"SELECT accounts_id,name,phone,address,balance FROM accounts WHERE khata_id={self.get_khata_id(self.khata_options.currentText())} and name LIKE '%{search}%' or phone LIKE '%{search}%' or address LIKE '%{search}%'").fetchall()
            if data:
                self.update_account_table(data=data)

        else:
            self.accounts_table.setRowCount(0)

    def search_roznamcha(self, search, types="all"):
        if types == "all" and search != "":
            data = self.db.conn.execute(
                f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and a.name LIKE '%{search}%' or r.description LIKE '%{search}%' or r.refrences LIKE '%{search}%'").fetchall()

        elif types == "date":
            from_date = self.txt_date_from_RN.date().toString("yyyy-MM-dd")
            to_date = self.txt_date_to_RN.date().toString("yyyy-MM-dd")
            print(type(from_date), to_date)
            # print(from_date)
            data = self.db.conn.execute(
                f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date BETWEEN '{from_date}' and '{to_date}' order by r.date").fetchall()
            
            record = self.db.conn.execute(
                    f"SELECT SUM(r.cash_in),SUM(r.cash_out) FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date < '{from_date}' order by r.date").fetchone()
            # print(record)
            if record[0]:
                record =[("","","previous","","","",'0','0',record[0]-record[1])]
                data = record + data

            for row in data:
                print(row[1])
        else:
            self.update()
            return
        self.tabel_update_reznamcha(data=data)

    def update(self):
        data = self.db.select(table_name='business',
                              columns="*", condition="id=1")
        if data:
            self.lbl_business_name.setText(data[0][1])
            self.lbl_business_contact.setText(data[0][4])
            self.lbl_business_address.setText(data[0][3])

        # khata table
        if self.khata_options.currentText() != "Select Business":
            data = self.db.select(table_name='accounts', columns="accounts_id,name,phone,address,balance",
                                  condition=f"khata_id={self.get_khata_id(self.khata_options.currentText())}")
            if data:
                self.update_account_table(data=data)
        else:
            self.accounts_table.setRowCount(0)

        # roznamcha table
        if self.khata_options.currentText() != "Select Business":
            today = QDate.currentDate().toString("yyyy-MM-dd")
            data = self.db.conn.execute(
                    f"SELECT r.roznamcha_id,r.date,r.cash_type,a.name,r.refrences,r.description,r.cash_in,r.cash_out,r.remaining FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date = '{QDate.currentDate().toString('yyyy-MM-dd')}' ").fetchall()
            record = self.db.conn.execute(
                    f"SELECT SUM(r.cash_in),SUM(r.cash_out) FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.khata_id={self.get_khata_id(self.khata_options.currentText())} and r.date < '{today}' order by r.date").fetchone()
            if record[0]:
                record =[("","","previous","","","",'0','0',record[0]-record[1])]
                data = record + data
            
            if data:
                self.tabel_update_reznamcha(data=data)
            else:
                self.roznamcha_table.setRowCount(0)

        

    def tabel_update_reznamcha(self, data):
        self.roznamcha_table.setRowCount(0)
        cash_in = 0
        cash_out = 0
        previous_amount = 0

        for index, row in enumerate(data):
            if row[2] == "previous":
                previous_amount = row[-1]
            else:
                cash_in += row[6]
                cash_out += row[7]
                if row[6] == 0:
                    previous_amount -= row[7]
                else:
                    previous_amount += row[6]

            table_row = [str(i) for i in row[:-1]] + [str(previous_amount)]
            self.roznamcha_table.insertRow(index)

            for idx, value in enumerate(table_row):
                self.roznamcha_table.setItem(index, idx, QTableWidgetItem(value))

            self.roznamcha_table.item(index, 6).setForeground(QColor(0, 255, 0))
            self.roznamcha_table.item(index, 7).setForeground(QColor(255, 0, 0))

        self.lbl_total_cash_In.setText(str(f"{cash_in:,}"))
        self.lbl_total_cash_out.setText(str(f"{cash_out:,}"))
        self.lbl_total_rem_balance.setText(str(f"{previous_amount:,}"))

        self.lbl_total_cash_In.setStyleSheet("color: green")
        self.lbl_total_cash_out.setStyleSheet("color: red")


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
            self.khata_options.addItem("Select Business")
            self.khata_options.addItems([i[0] for i in data])

    def logout(self):
        from login_page import LoginWindow
        self.login = LoginWindow()
        self.login.show()
        self.close()

    def get_khata(self):
        khata = self.khata_options.currentText()
        if khata != "Select Business":
            self.lbl_user_khata.setText(khata)
            self.update()

        else:
            self.khata_select_update()
            self.update()

    def get_khata_id(self, name):
        if name != "Select Business":
            return self.db.select(table_name='khata', columns="khata_id", condition=f"khata_name='{name}'")[0][0]
        # return self.db.select(table_name='khata',columns="khata_id",condition=f"khata_name='{name}'")[0][0]

    def add_accounts(self):
        try:
            khata_id = self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.add_accounts = AddAccountsWindow(khata_id=khata_id)
                self.add_accounts.show()
                self.add_accounts.btn_save.clicked.connect(self.update)
                self.add_accounts.btn_clear.clicked.connect(self.update)
                self.add_accounts.btn_cancel.clicked.connect(self.update)

            else:
                QMessageBox.warning(
                    self, "warning", f"Please Select Business {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Please Select Business {e}")

    def add_khata(self):
        self.window = KhataWindow()
        self.window.show()
        self.window.btn_save.clicked.connect(self.khata_select_update)

    def add_roznamcha(self):
        try:
            khata_id = self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.roznamcha_window = RozNamchaWindow(khata_id=khata_id)
                self.roznamcha_window.show()
                # update main ui when roznamcha window is closed
                self.roznamcha_window.btn_save.clicked.connect(self.update)
                self.roznamcha_window.btn_cancel.clicked.connect(self.update)
                self.roznamcha_window.btn_clear.clicked.connect(self.update)

            else:
                QMessageBox.warning(
                    self, "warning", f"Please Select Business {e}")
        except Exception as e:
            QMessageBox.warning(self, "Error", f"Please Select Business {e}")

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
            self.lbl_user_name.setText(data[0][1])

        data = db.select_all('business', "*")
        if data:
            self.txt_business_name.setText(data[0][1])
            self.txt_business_email.setText(data[0][2])
            self.txt_business_contact.setText(data[0][4])
            self.txt_business_address.setText(data[0][3])
            self.txt_business_owner.setText(data[0][5])
            self.btn_business_details.hide()
            self.btn_change_business_details.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()

