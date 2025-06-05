import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
from PyQt5 import QtCore, QtGui, QtWidgets, QtPrintSupport
from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType
from resources_rc import *
import pandas as pd
FORM_MAIN, _ = loadUiType('ui/account_details.ui')


class AccountDetailsWindow(QMainWindow, FORM_MAIN):
    def __init__(self, id, name):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.account_id = id
        self.db = DBHandler()
        self.opening = self.db.select(
            table_name='accounts', columns="balance", condition=f"accounts_id={self.account_id}")[0][0]
        self.search_table(self.account_id, type='start')
        self.lbl_account_name.setText(name)
        self.from_date.setDate(QDate.currentDate())
        self.to_date.setDate(QDate.currentDate())
        self.btn_refresh.clicked.connect(
            lambda: self.search_table(self.account_id, type='start'))
        self.lbl_opening_balance.setText(str(f"{float(self.opening):,}"))

        self.account_details_table.setColumnWidth(0, 50)
        self.account_details_table.setColumnWidth(1, 120)
        self.account_details_table.setColumnWidth(2, 200)
        self.account_details_table.setColumnWidth(3, 200)
        self.account_details_table.setColumnWidth(6, 100)
        
        accounts_scrollBar = self.account_details_table.verticalScrollBar()
        accounts_scrollBar.rangeChanged.connect(
            lambda: accounts_scrollBar.setValue(accounts_scrollBar.maximum()))

        self.txt_search.textChanged.connect(
            lambda: self.search_table(self.account_id, self.txt_search.text()))
        self.btn_search.clicked.connect(lambda: self.search_table(
            self.account_id, self.from_date.text(), 'date'))
        self.btn_print.clicked.connect(self.print_accounts_table_pdf)
    
    def print_accounts_table_pdf(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
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
                
                <h1 style="text-align: center;">Accounts : <span style="font-size: 22px; color: blue;">"""+self.lbl_account_name.text()+"""</span></h1>
                <h3 style="text-align: right;"> Opening Balance : <span> """+self.lbl_opening_balance.text()+"""</span></h3>
                <h3 style="text-align: right;"> Total Cash In : <span style=" color: green;"> """ + self.lbl_total_cash_In.text() + """</span></h3>
                <h3 style="text-align: right;"> Total Cash Out : <span style=" color: red;"> """ + self.lbl_total_cash_out.text() + """</span></h3>
                <h3 style="text-align: right;"> Remaining Balance : <span style=" color: red;"> """ + self.lbl_remaining.text() + """</span></h3>
                <h3 style="text-align: left;">Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h3>
                
                <div style="width: 100%;">
                <table style="border-bottom: 1px solid gray;
                    border-collapse: collapse;
                    width: 100%;">
                    <thead style="width: 100%;">
                        <tr style="background-color: #29b6f6; font-size: 10px; width: 100%;">
                            <th style="padding: 4px; text-align: left;">S/NO</th>
                            <th style="padding: 4px; text-align: left;">Date</th>
                            <th style="padding: 4px; text-align: left;">Refrence</th>
                            <th style="padding: 4px; text-align: left;">Description</th>
                            <th style="padding: 4px; text-align: left;">Cash In</th>
                            <th style="padding: 4px; text-align: left;">Cash Out</th>
                            <th style="padding: 4px; text-align: left;">Remaining</th>
                        </tr>
                    </thead>
                    <tbody style="font-size: 10px; width: 100%;">
                    """
            for i in range(self.account_details_table.rowCount()):
                html += "<tr>"
                for j in range(self.account_details_table.columnCount()):
                    html += """<td style="padding: 4px; text-align: left;">""" + \
                        self.account_details_table.item(i, j).text()+"</td>"
                html += "</tr>"
            html += """
                    </tbody>
    
                </table>
                </div>
            
            </body>
            </html>
            """
            document.setHtml(html)
            document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")


    def search_table(self, id, search=None, type='all'):
        if type == 'all':
            data = self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id} and (refrences like '%{search}%' or description like '%{search}%')  order by date asc"
            ).fetchall()
        elif type == 'date':
            # print("date")
            from_date=self.from_date.date().toString('yyyy-MM-dd')
            to_date=self.to_date.date().toString('yyyy-MM-dd')
            data = self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id} and date between '{from_date}' and '{to_date}' order by date asc"
            ).fetchall()
            record = self.db.conn.execute(
                    f"SELECT SUM(cash_in),SUM(cash_out) FROM roznamcha WHERE accounts_id={id} and date < '{from_date}' order by date").fetchone()
            print(record)
            if record[0]:
                record =[("","","","previous",'0','0',record[0]-record[1])]
                data = record + data
            
        else:
            data = self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id} order by date asc"
            ).fetchall()
        
        remaning = 0
        cash_in = 0
        cash_out = 0
        self.account_details_table.setRowCount(0)
        previous_amount=0
        for row_number, row_data in enumerate(data):
            if row_data[3]=="previous":
                previous_amount=row_data[-1]
            else:
                cash_in += row_data[4]
                cash_out += row_data[5]
                if row_data[4] == 0:
                    previous_amount -= row_data[5]
                else:
                    previous_amount += row_data[4]
                remaning += row_data[4]
                remaning -= row_data[5]
            self.account_details_table.insertRow(row_number)
            for column_number, value in enumerate(row_data):
                if len(row_data)==column_number+1:
                    self.account_details_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(previous_amount)))
                else:
                    self.account_details_table.setItem(
                        row_number, column_number, QTableWidgetItem(str(value)))
                
            self.account_details_table.item(
                row_number, 4).setForeground(QColor(0, 255, 0))
            self.account_details_table.item(
                row_number, 5).setForeground(QColor(255, 0, 0))
        self.lbl_total_cash_In.setText(str(f"{int(cash_in):,}"))
        self.lbl_total_cash_out.setText(str(f"{int(cash_out):,}"))
        opening = self.opening
        self.lbl_remaining.setText(str(float(opening)+float(previous_amount)))
        if cash_in < 0:
            self.lbl_total_cash_In.setStyleSheet("color: red")
        else:
            self.lbl_total_cash_In.setStyleSheet("color: green")
        if cash_out > 0:
            self.lbl_total_cash_out.setStyleSheet("color: red")
        else:
            self.lbl_total_cash_out.setStyleSheet("color: green")
        if remaning < 0:
            self.lbl_remaining.setStyleSheet("color: red")
        else:
            self.lbl_remaining.setStyleSheet("color: green")



def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
