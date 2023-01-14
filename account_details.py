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
    def __init__(self,id,name):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.account_id = id
        self.db= DBHandler()
        self.opening=self.db.select(table_name='accounts',columns="balance",condition=f"accounts_id={self.account_id}")[0][0]
        self.search_table(self.account_id,type='start')
        self.lbl_account_name.setText(name)
        self.txt_search_date.setDate(QDate.currentDate())
        self.btn_refresh.clicked.connect(lambda: self.search_table(self.account_id,type='start'))
        self.lbl_opening_balance.setText(str(self.opening))




        self.account_details_table.setColumnWidth(0, 50)
        self.account_details_table.setColumnWidth(1, 120)
        self.account_details_table.setColumnWidth(2, 200)
        self.account_details_table.setColumnWidth(3, 200)
        self.account_details_table.setColumnWidth(6, 100)
        self.txt_search.textChanged.connect(lambda: self.search_table(self.account_id,self.txt_search.text()))
        self.txt_search_date.dateChanged.connect(lambda: self.search_table(self.account_id,self.txt_search_date.text(),'date'))
        self.btn_print.clicked.connect(self.print_accounts_table_pdf)
        
    def print_accounts_table_pdf(self):
        filename = QFileDialog.getSaveFileName(
            self, "Save File", "", "PDF(*.pdf)")
        if filename[0]:
            # printer = QtPrintSupport.QPrinter(QtPrintSupport.QPrinter.PrinterResolution)
            # printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            # printer.setFullPage(True)
            # printer.setOrientation(QtPrintSupport.QPrinter.Landscape)
            # # table not print correctly in pdf 
            # printer.setPaperSize(QSizeF(self.account_details_table.width(), self.account_details_table.height()), QtPrintSupport.QPrinter.DevicePixel)


            # printer.setOutputFileName(filename[0])
            # doc = QtGui.QTextDocument()
            
            # convert qtwidgettable to pandas dataframe
            df = pd.DataFrame(
                # first row is header
                [[self.account_details_table.horizontalHeaderItem(column).text() for column in range(self.account_details_table.columnCount())]] +
                # rest of the rows
                [[self.account_details_table.item(row, column).text() for column in range(self.account_details_table.columnCount())] for row in range(self.account_details_table.rowCount())]
            )
            # convert pandas dataframe to html
            # print(df)
            html = df.to_html(index=False, header=False)

            # add heaqder and footer to html
            html = """<html>
            <body>
            <style>

                body {
                    font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
                    width: 100%;
                    
                }
                table,
                th,
                td {
                    border-bottom: 1px solid gray;
                    border-collapse: collapse;
                    width: 100%;
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
                    width: 100%;
                }
                h1 {
                    text-align: center;
                    font-size: 30px;
                    font-weight: 700;
                }
                h2 {
                    text-align: center;
                    font-size: 20px;
                    font-weight: 700;
                }
                h3 {
                    text-align: center;
                    font-size: 15px;
                    font-weight: 700;
                }
                h4 {
                    text-align: center;
                    font-size: 10px;
                    font-weight: 700;
                }
            </style>
            <h1 style="background-color: red;">Account Details</h1>
            <h2>Account Name: """+self.lbl_account_name.text()+"""</h2>
            <h3>Opening Balance: """+self.lbl_opening_balance.text()+"""</h3>
            <h4>Print Date: """+str(QDate.currentDate().toString('dd-MM-yyyy'))+"""</h4>
            """+html+"""
            </body>
            </html>"""
            # document.setHtml(html)
            # document.print_(printer)
            # pdf.from_string(html, 'accounts.pdf')
            doc = QTextDocument()
            doc.setHtml(html)
            printer = QtPrintSupport.QPrinter()
            printer.setOutputFileName(filename[0])
            printer.setOutputFormat(QtPrintSupport.QPrinter.PdfFormat)
            printer.setPageSize(QtPrintSupport.QPrinter.A4)
            printer.setPageMargins(15, 15, 15, 15, QtPrintSupport.QPrinter.Millimeter)

            doc.print_(printer)
            print("done!")












            # html = """<html>
            # <head>
            # <style>
            #     body {
            #         font-family: Cambria, Cochin, Georgia, Times, 'Times New Roman', serif;
            #     }
            #     table,
            #     th,
            #     td {
            #         border-bottom: 1px solid gray;
            #         border-collapse: collapse;
            #         width: 100%;
            #     }
            #     th,
            #     td {
            #         padding: 10px 2px;
            #         text-align: left;
            #     }
            #     td:nth-child(7) {
            #         color: green;
            #     }
            #     td:nth-child(8) {
            #         color: red;
            #     }
            #     thead {
            #         background-color: #29b6f6;
            #         font-size: 20px;
            #         font-weight: 700;
            #     }
            #     tbody {
            #         font-size: 18px;
            #         font-weight: 600;
            #     }
            #     h1 {
            #         text-align: center;
            #     }
            #     h2 {
            #         text-align: right;
            #     }
            # </style>
            
            # </head>
        
            # <body>
            #     <div>
            #         <h1>Business Name</h1>
            #         <h2>Business Contact</h2>
            #     </div>
            #     <div>
            #     <h1> - Accounts</h1>
            #         <h2>Opening Balance</h2>
            #     </div>
            #     <table">
            #         <thead>
            #             <tr>
            #                 <th>S/NO</th>
            #                 <th>Date</th>
            #                 <th>Refrence</th>
            #                 <th>Description</th>
            #                 <th>Cash In</th>
            #                 <th>Cash Out</th>
            #                 <th>Remaining</th>
            #             </tr>
            #         </thead>
            #         <tbody>
            # """
            # for i in range(self.account_details_table.rowCount()):
            #     html += "<tr>"
            #     for j in range(self.account_details_table.columnCount()):
            #         html += "<td>" + \
            #             self.account_details_table.item(i, j).text()+"</td>"
            #     html += "</tr>"
            # html += """
            #         </tbody>
    
            #     </table>
            
            # </body>
            # </html>
            # """
            # document.setHtml(html)
            # document.print_(printer)
            QMessageBox.information(self, "Success", "PDF Saved Successfully")

    def search_table(self,id,search=None,type='all'):
        if type=='all':
            data= self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id} and (refrences like '%{search}%' or description like '%{search}%') "
            ).fetchall()
        elif type=='date':
            print("date")
            data= self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id} and date like '%{search}%'"
            ).fetchall()
            print(data)
        else:
            data= self.db.conn.execute(
                f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,accounts_remaining from roznamcha where accounts_id = {id}"
                ).fetchall()
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
        opening=self.opening
        print(opening)
        if opening >=0:
            self.lbl_remaining.setText(str(float(opening)+float(remaing)))
        else:
            self.lbl_remaining.setText(str(float(opening)-float(remaing)))

        if cash_in < 0:
            self.lbl_total_cash_In.setStyleSheet("color: red")
        else:
            self.lbl_total_cash_In.setStyleSheet("color: green")
        if cash_out > 0:
            self.lbl_total_cash_out.setStyleSheet("color: red")
        else:
            self.lbl_total_cash_out.setStyleSheet("color: green")
        if remaing <0:
            self.lbl_remaining.setStyleSheet("color: red")
        else:
            self.lbl_remaining.setStyleSheet("color: green")

    # def update(self,id):
    #     data= self.db.conn.execute(
    #         f"SELECT roznamcha_id,date,refrences,description,cash_in,cash_out,remaining from roznamcha where accounts_id = {id}"
    #     ).fetchall()
    #     # print(len(data))
    #     if data:
            
def main():
    app = QApplication(sys.argv)
    window = AccountDetailsWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
