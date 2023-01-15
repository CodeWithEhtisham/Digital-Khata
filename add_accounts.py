import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

FORM_MAIN, _ = loadUiType('ui/add_accounts.ui')


class AddAccountsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,khata_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db= DBHandler()
        self.khata_id = khata_id
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_account)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_balance.textChanged.connect(self.add_comma_separator)
    
    def add_comma_separator(self):
        balance = self.txt_balance.text()
        if balance != '':
            balance = balance.replace(',', '')
            balance = int(balance)
            balance = "{:,}".format(balance)
            self.txt_balance.setText(balance)
            self.txt_balance.setCursorPosition(len(balance))

    def save_account(self):
        name=self.txt_name.text()
        phone=self.txt_mobile.text()
        address=self.txt_address.text()
        balance_type=self.select_balance_type.currentText()
        balance = self.txt_balance.text().replace(',', '')
        balance=float(balance)

        if name != '' and phone != '' and balance_type != '' and balance != '':
            try:
                if balance_type == 'Payable':
                    balance = float(balance)
                else:
                    balance=-float(balance)
                self.db.insert(
                    table_name='accounts',
                    columns="name, phone, address, balance_type, balance,khata_id",
                    values=f"'{name}', '{phone}', '{address}', '{balance_type}', '{balance}', '{self.khata_id}'"
                )
                # self.db.conn.execute(f"INSERT INTO account_details (account_id, date,description,remaining) VALUES ('{ self.db.cursor.lastrowid }', '{QDate.currentDate().toString('dd/MM/yyyy')}', '{balance_type}', '{balance}')")
                self.db.conn.commit()
                QMessageBox.information(self, 'Success', 'Account added successfully')
                self.close()
            except Exception as e:
                QMessageBox.warning(self, 'Error', f"error in accounts {e}")

        else:
            QMessageBox.warning(self, 'Error', 'All fields are required')

    def clear_fields(self):
        self.txt_name.setText('')
        self.txt_mobile.setText('')
        self.txt_address.setText('')
        self.select_balance_type.setCurrentIndex(0)
        self.txt_balance.setText('')


def main():
    app = QApplication(sys.argv)
    window = AddAccountsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
