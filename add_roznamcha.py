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

FORM_MAIN, _ = loadUiType('ui/add_roznamcha.ui')


class RozNamchaWindow(QMainWindow, FORM_MAIN):
    def __init__(self,khata_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db = DBHandler()
        self.khata_id=khata_id
        self.txt_date.setDate(QDate.currentDate())
        self.names_list_option.addItems([i[0] for i in self.db.select("accounts",'name',condition=f"khata_id={self.khata_id}")])
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_roznamcha)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def clear_fields(self):
        self.txt_date.setDate(QDate.currentDate())
        self.cashInOut_option.setCurrentIndex(0)
        self.names_list_option.setCurrentIndex(0)
        self.txt_reference.setText('')
        self.txt_description.setText('')
        self.txt_amount.setText('')
    

    def save_roznamcha(self):
        date=self.txt_date.text()
        cash_type=self.cashInOut_option.currentText()
        name=self.names_list_option.currentText()
        refrences=self.txt_reference.text()
        description=self.txt_description.text()
        amount=float(self.txt_amount.text())
        if name=="Select Option":
            QMessageBox.warning(self,"Error","Please Select Account Name")
            return
        if refrences != '' and description != "" and amount!='':
            try:    
                acccount_id=self.db.select(
                    table_name="accounts",
                    columns="account_id",
                    condition=f"name='{name}' and khata_id={self.khata_id}"
                )[0][0]
                if cash_type=="Cash In":
                    self.db.insert(
                        table_name='roznamcha',
                        columns="khata_id,accounts_id,date,refrences,description,cash_in,remaining",
                        values=f"'{self.khata_id}','{acccount_id}','{date}','{refrences}','{description}',{float(amount)},{float(222.222)}"
                        )
                else:
                    self.db.insert(
                        table_name='roznamcha',
                        columns="khata_id,accounts_id,date,refrences,description,cash_out,remaining",
                        values=f"'{self.khata_id}','{acccount_id}','{date}','{refrences}','{description}',{float(amount)},{float(222.222)}"
                        )
                QMessageBox.information(self,"Success","record added successully")
                self.close()
            except Exception as e:
                QMessageBox.warning(self,"Error",f"record not added {e}")




def main():
    app = QApplication(sys.argv)
    window = RozNamchaWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':

    main()
