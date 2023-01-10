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

FORM_MAIN, _ = loadUiType('ui/account_details.ui')


class AccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self,id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.account_id = id
        self.db= DBHandler()
        self.update(self.account_id)

    def update(self,id):
        data= self.db.conn.execute(
            f"SELECT account_details_id,date,refrence,description,cash_in,cash_out,remaining from account_details where account_id = {id}"
        )
        if data:
            self.account_details_table.setRowCount(0)
            for row_number, row_data in enumerate(data):
                self.account_details_table.insertRow(row_number)
                for column_number, data in enumerate(row_data):
                    self.account_details_table.setItem(row_number, column_number, QTableWidgetItem(str(data)))


def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
