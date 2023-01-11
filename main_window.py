
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
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
        self.roznamcha_table.setColumnWidth(3, 250)
        self.roznamcha_table.setColumnWidth(6, 170)
        self.roznamcha_table.setColumnWidth(7, 170)
    
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

        # tables double clicked
        self.accounts_table.doubleClicked.connect(self.account_details)

        # business btns
        self.btn_business_details.clicked.connect(self.business_details)
        self.btn_change_business_details.clicked.connect(self.edit_business)
        self.btn_change_user_details.clicked.connect(self.change_user_details)
        self.btn_change_pwd.clicked.connect(self.change_password)



    def update(self):
        data=self.db.select(table_name='business',columns="*",condition="id=1")
        if data:
            self.lbl_business_name.setText(data[0][1])
            self.lbl_business_contact.setText(data[0][4])
            self.lbl_business_address.setText(data[0][3])

        
        if self.khata_options.currentText()!="Select Khata":
            data = self.db.select(table_name='accounts', columns="accounts_id,name,phone,address,balance", condition=f"khata_id={self.get_khata_id(self.khata_options.currentText())}")
            if data:
                self.update_table(data=data,obj=self.accounts_table)
            else:
                self.accounts_table.setRowCount(0)
        else:
            self.accounts_table.setRowCount(0)

    def account_details(self):
        # get selected row first cell
        id = self.accounts_table.item(self.accounts_table.currentRow(), 0).text()
        self.window = AccountDetailsWindow(id)
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
        khata=self.khata_options.currentText()
        if khata!="Select Khata":
            self.lbl_user_khata.setText(khata)
            self.update()

        else:
            self.khata_select_update()
            self.update()
            
    def get_khata_id(self,name):
        if name!="Select Khata":
            return self.db.select(table_name='khata',columns="khata_id",condition=f"khata_name='{name}'")[0][0]
        # return self.db.select(table_name='khata',columns="khata_id",condition=f"khata_name='{name}'")[0][0]

    def add_accounts(self):
        try:
            khata_id=self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.add_accounts = AddAccountsWindow(khata_id=khata_id)
                self.add_accounts.show()
            else:
                QMessageBox.warning(self,"warning",f"Please Select Khata {e}")
        except Exception as e:
            QMessageBox.warning(self,"Error",f"Please Select Khata {e}")



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
            khata_id=self.get_khata_id(self.khata_options.currentText())
            if khata_id:
                self.roznamcha_window=RozNamchaWindow(khata_id=khata_id)
                self.roznamcha_window.show()
            else:
                QMessageBox.warning(self,"warning",f"Please Select Khata {e}")
        except Exception as e:
            QMessageBox.warning(self,"Error",f"Please Select Khata {e}")
        


        
    def update_table(self,data,obj):
        obj.setRowCount(0)
        for index,row in enumerate(data):
            obj.insertRow(index)
            for idx,i in enumerate(row):
                obj.setItem(index,idx,QTableWidgetItem(str(i)))
        # main page
    

        
        
        
        

        


    
    def change_user_details(self):
        self.changeuserdetaisls = UpdateUserWindow()
        self.changeuserdetaisls.show()

    def change_password(self):
        self.changepassword= ChangePasswordWindow()
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
        db=DBHandler()
        data=db.select_all('users',"*")
        if data:
            self.txt_user_name.setText(data[0][1])
            self.txt_user_email.setText(data[0][2])
            self.txt_user_contact.setText(data[0][3])
            self.txt_user_username.setText(data[0][4])

        data = db.select_all('business',"*")
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
