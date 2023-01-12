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
    def __init__(self,id,name):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.account_id = id
        self.db= DBHandler()
        self.update(self.account_id)
        self.lbl_account_name.setText(name)
        self.txt_search_date.setDate(QDate.currentDate())
        self.btn_refresh.clicked.connect(lambda: self.update(self.account_id))
        self.account_details_table.setColumnWidth(0, 50)
        self.account_details_table.setColumnWidth(1, 120)
        self.account_details_table.setColumnWidth(2, 200)
        self.account_details_table.setColumnWidth(3, 200)
        self.account_details_table.setColumnWidth(6, 100)
        self.txt_search.textChanged.connect(lambda: self.search_table(self.account_id,self.txt_search.text()))
        self.txt_search_date.dateChanged.connect(lambda: self.search_table(self.account_id,self.txt_search_date.text(),'date'))

    def search_table(self,id,search,type='all'):
        if type=='all':
            data= self.db.conn.execute(
                f"SELECT account_details_id,date,refrence,description,cash_in,cash_out,remaining from account_details where account_id = {id} and (refrence like '%{search}%' or description like '%{search}%') "
            ).fetchall()
        elif type=='date':
            print("date")
            data= self.db.conn.execute(
                f"SELECT account_details_id,date,refrence,description,cash_in,cash_out,remaining from account_details where account_id = {id} and date like '%{search}%'"
            ).fetchall()
            print(data)
        else:
            self.update(id)
        # print(len(data))
        # opening=0
        remaing=0
        cash_in=0
        cash_out=0
        self.account_details_table.setRowCount(0)
        for row_number, row_data in enumerate(data):
            cash_in+=row_data[4]
            cash_out+=row_data[5]
            if row_number ==len(data)-1:
                remaing = row_data[6]
            self.account_details_table.insertRow(row_number)
            for column_number, value in enumerate(row_data):
                self.account_details_table.setItem(row_number, column_number, QTableWidgetItem(str(value)))
            self.account_details_table.item(row_number,4).setForeground(QColor(0,255,0))
            self.account_details_table.item(row_number,5).setForeground(QColor(255,0,0))
        # self.lbl_opening_balance.setText(str(opening))
        self.lbl_total_cash_In.setText(str(cash_in))
        self.lbl_total_cash_out.setText(str(cash_out))
        self.lbl_remaining.setText(str(remaing))

    def update(self,id):
        data= self.db.conn.execute(
            f"SELECT account_details_id,date,refrence,description,cash_in,cash_out,remaining from account_details where account_id = {id}"
        ).fetchall()
        print(len(data))
        if data:
            opening=0
            remaing=0
            cash_in=0
            cash_out=0
            self.account_details_table.setRowCount(0)
            for row_number, row_data in enumerate(data):
                cash_in+=row_data[4]
                cash_out+=row_data[5]
                if row_number == 0:
                    opening = row_data[6]
                elif row_number ==len(data)-1:
                    remaing = row_data[6]
                self.account_details_table.insertRow(row_number)
                for column_number, value in enumerate(row_data):
                    self.account_details_table.setItem(row_number, column_number, QTableWidgetItem(str(value)))
                self.account_details_table.item(row_number,4).setForeground(QColor(0,255,0))
                self.account_details_table.item(row_number,5).setForeground(QColor(255,0,0))
            self.lbl_opening_balance.setText(str(opening))
            self.lbl_total_cash_In.setText(str(cash_in))
            self.lbl_total_cash_out.setText(str(cash_out))
            self.lbl_remaining.setText(str(remaing))
def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
