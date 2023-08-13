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

FORM_MAIN, _ = loadUiType('ui/update_roznamcha.ui')


class UpdateRozNamchaWindow(QMainWindow, FORM_MAIN):
    def __init__(self,roznamcha_id):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.db= DBHandler()
        
        self.roznamcha_id = roznamcha_id
        self.khata_id = self.db.conn.execute(f"SELECT khata_id FROM roznamcha WHERE roznamcha_id={self.roznamcha_id}").fetchone()[0]
        self.Handle_Buttons()
        self.fill_fields()

    def fill_fields(self):
        data=self.db.conn.execute(f"SELECT r.date, r.cash_type, a.name, r.refrences, r.description, r.cash_in,r.cash_out FROM roznamcha r INNER JOIN accounts a ON r.accounts_id=a.accounts_id WHERE r.roznamcha_id={self.roznamcha_id}").fetchone()
        print(data)
        self.txt_date.setDate(QDate.fromString(data[0],'yyyy-MM-dd'))
        # self.cashInOut_option.addItems([data[1]])
        if data[1] == 'Cash In':
            self.cashInOut_option.setCurrentIndex(0)
        else:
            self.cashInOut_option.setCurrentIndex(1)
        self.names_list_option.addItems([data[2]])
        self.txt_reference.setText(data[3])
        self.txt_description.setText(data[4])
        if data[5] == 0:
            self.txt_amount.setText(str(data[6]))
        else:
            self.txt_amount.setText(str(data[5]))

    def Handle_Buttons(self):
        self.btn_update.clicked.connect(self.update_roznamcha)
        self.btn_clear.clicked.connect(self.delete_roznamcha)
        self.btn_cancel.clicked.connect(self.close)
        self.txt_amount.textChanged.connect(self.add_comma_separator)

    def add_comma_separator(self):
        amount = self.txt_amount.text()
        if amount != '':
            amount = amount.replace(',', '')
            amount = int(amount)
            amount = "{:,}".format(amount)
            self.txt_amount.setText(amount)
            self.txt_amount.setCursorPosition(len(amount))

    def previous_calculation(self,previous_balance,amount,cash_type):
        if previous_balance>=0:
            if cash_type=="Cash In":
                previous_balance+=amount
            else:
                previous_balance-=amount
        else:
            if cash_type=="Cash In":
                previous_balance+=amount
            else:
                previous_balance-=amount
        return previous_balance

    def update_roznamcha(self):
        try:
            account_id = self.db.conn.execute(f"SELECT accounts_id FROM accounts WHERE name='{self.names_list_option.currentText()}'").fetchone()[0]
            record = self.db.conn.execute(f"SELECT * FROM roznamcha WHERE roznamcha_id>={self.roznamcha_id} and khata_id={self.khata_id}").fetchall()
            account_previous_balance = self.db.conn.execute(f"SELECT accounts_remaining from roznamcha where roznamcha_id<{self.roznamcha_id} and khata_id={self.khata_id} and accounts_id={account_id} order by roznamcha_id desc limit 1").fetchone()
            previous_balance = self.db.conn.execute(f"SELECT remaining from roznamcha where roznamcha_id<{self.roznamcha_id} and khata_id={self.khata_id} order by roznamcha_id desc limit 1").fetchone()
            if previous_balance is None:
                previous_balance = 0
            else:
                previous_balance = float(previous_balance[0])

            if account_previous_balance is None:
                account_previous_balance = 0
            else:
                account_previous_balance = float(account_previous_balance[0])
            date=self.txt_date.date().toString('yyyy-MM-dd')
            cash_type=self.cashInOut_option.currentText()
            refrences=self.txt_reference.text()
            description=self.txt_description.text()
            amount = self.txt_amount.text().replace(',', '')
            amount = float(amount)


            previous_balance=self.previous_calculation(previous_balance,amount,cash_type)
            account_previous_balance=self.previous_calculation(account_previous_balance,amount,cash_type)
            self.db.conn.execute(f"UPDATE roznamcha SET date='{date}',cash_type='{cash_type}',accounts_id={account_id},refrences='{refrences}',description='{description}',cash_in={amount if cash_type=='Cash In' else 0},cash_out={amount if cash_type=='Cash Out' else 0},remaining={previous_balance},accounts_remaining={account_previous_balance} WHERE roznamcha_id={self.roznamcha_id}")
            self.db.conn.commit()
            for rec in record[1:]:
                # (27, 2, 4, '12/01/2023', 'Cash In', 'asdf', 'asdf', 7000, 0, 12000)
                if rec[4]=="Cash In":
                    amount=float(rec[7])
                else:
                    amount=float(rec[8])
                previous_balance=self.previous_calculation(previous_balance,amount,rec[4])
                self.db.conn.execute(f"UPDATE roznamcha SET remaining={previous_balance} WHERE roznamcha_id={rec[0]}")
                self.db.conn.commit()


            record = self.db.conn.execute(f"SELECT * FROM roznamcha WHERE roznamcha_id>={self.roznamcha_id} and khata_id={self.khata_id} and accounts_id={account_id}").fetchall()
            for rec in record[1:]:
                if rec[4]=="Cash In":
                    amount=float(rec[7])
                else:
                    amount=float(rec[8])
                account_previous_balance=self.previous_calculation(account_previous_balance,amount,rec[4])
                self.db.conn.execute(f"UPDATE roznamcha SET accounts_remaining={account_previous_balance} WHERE roznamcha_id={rec[0]}")
                self.db.conn.commit()





            # account_details_id=self.db.conn.execute
            QMessageBox.information(self, "Success", "Roznamcha Updated Successfully")
            self.close()
        except Exception as e:
            QMessageBox.information(self, "Error", str(e))


    def delete_roznamcha(self):
        try:
            # ask user yes or no before detele
            ret = QMessageBox.question(self,'', "Are You sure to Delete the Entry?", QMessageBox.Yes | QMessageBox.No)
            if ret==QMessageBox.Yes:
                account_id = self.db.conn.execute(f"SELECT accounts_id FROM accounts WHERE name='{self.names_list_option.currentText()}'").fetchone()[0]
                record = self.db.conn.execute(f"SELECT * FROM roznamcha WHERE roznamcha_id>={self.roznamcha_id} and khata_id={self.khata_id}").fetchall()
                previous_balance = self.db.conn.execute(f"SELECT remaining from roznamcha where roznamcha_id<{self.roznamcha_id} and khata_id={self.khata_id} order by roznamcha_id desc limit 1").fetchone()
                account_previous_balance = self.db.conn.execute(f"SELECT accounts_remaining from roznamcha where roznamcha_id<{self.roznamcha_id} and khata_id={self.khata_id} and accounts_id={account_id} order by roznamcha_id desc limit 1").fetchone()
                if previous_balance is None:
                    previous_balance = 0
                else:
                    previous_balance = float(previous_balance[0])
                # delete record from roznamcha where roznamcha_id= self.roznamcha_id
                if account_previous_balance is None:
                    account_previous_balance = 0
                else:
                    account_previous_balance = float(account_previous_balance[0])
                self.db.conn.execute(f"DELETE FROM roznamcha WHERE roznamcha_id={self.roznamcha_id}")
                self.db.conn.commit()
                for rec in record[1:]:
                    # (27, 2, 4, '12/01/2023', 'Cash In', 'asdf', 'asdf', 7000, 0, 12000)
                    if rec[4]=="Cash In":
                        amount=float(rec[7])
                    else:
                        amount=float(rec[8])
                    previous_balance=self.previous_calculation(previous_balance,amount,rec[4])
                    self.db.conn.execute(f"UPDATE roznamcha SET remaining={previous_balance} WHERE roznamcha_id={rec[0]}")
                    self.db.conn.commit()

                record = self.db.conn.execute(f"SELECT * FROM roznamcha WHERE roznamcha_id>{self.roznamcha_id} and khata_id={self.khata_id} and accounts_id={account_id}").fetchall()
                print(record)
                for rec in record:
                    if rec[4]=="Cash In":
                        amount=float(rec[7])
                    else:
                        amount=float(rec[8])
                    account_previous_balance=self.previous_calculation(account_previous_balance,amount,rec[4])
                    self.db.conn.execute(f"UPDATE roznamcha SET accounts_remaining={account_previous_balance} WHERE roznamcha_id={rec[0]}")
                    self.db.conn.commit()

                
                QMessageBox.information(self, "Success", "Entry Deleted Successfully")
                self.close()
            else:
                self.close()
        except Exception as e:
            QMessageBox.warning(self,"error",f"record not deleted {e}")
        


    def clear_fields(self):
        pass


def main():
    app = QApplication(sys.argv)
    window = UpdateRozNamchaWindow(1)
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()





# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
#                             QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
#                            QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *


# class Ui_UpdateRozNamchaWindow(object):
#     def setupUi(self, UpdateRozNamchaWindow):
#         UpdateRozNamchaWindow.setObjectName("UpdateRozNamchaWindow")
#         UpdateRozNamchaWindow.resize(500, 500)
#         UpdateRozNamchaWindow.setMinimumSize(QtCore.QSize(500, 500))
#         UpdateRozNamchaWindow.setMaximumSize(QtCore.QSize(500, 500))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         UpdateRozNamchaWindow.setWindowIcon(icon)
#         UpdateRozNamchaWindow.setIconSize(QtCore.QSize(32, 32))
#         self.centralwidget = QtWidgets.QWidget(UpdateRozNamchaWindow)
#         self.centralwidget.setStyleSheet("#label_widget {\n"
# "    background-color: #80deea;\n"
# "}\n"
# "\n"
# "#label_5 {\n"
# "    color: #fff;\n"
# "}\n"
# "\n"
# "#btn_update {\n"
# "    background-color: #26a69a;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_clear {\n"
# "    background-color: #81d4fa;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_cancel {\n"
# "    background-color: #b0bec5;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "QLineEdit {\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 5px;\n"
# "}\n"
# "\n"
# "QDateEdit {\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 5px;\n"
# "}\n"
# "\n"
# "QComboBox {\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 5px;\n"
# "}\n"
# "\n"
# "QTextEdit {\n"
# "    border-radius: 10px;\n"
# "    padding: 0px 0px;\n"
# "}")
#         self.centralwidget.setObjectName("centralwidget")
#         self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_4.setSpacing(0)
#         self.verticalLayout_4.setObjectName("verticalLayout_4")
#         self.label_widget = QtWidgets.QWidget(self.centralwidget)
#         self.label_widget.setObjectName("label_widget")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.label_widget)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.label_5 = QtWidgets.QLabel(self.label_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(16)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_5.setFont(font)
#         self.label_5.setAlignment(QtCore.Qt.AlignCenter)
#         self.label_5.setObjectName("label_5")
#         self.verticalLayout.addWidget(self.label_5)
#         self.verticalLayout_4.addWidget(self.label_widget)
#         self.details_widget = QtWidgets.QWidget(self.centralwidget)
#         self.details_widget.setObjectName("details_widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
#         self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
#         self.horizontalLayout.setSpacing(10)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.lbl_frame = QtWidgets.QFrame(self.details_widget)
#         self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_frame.setObjectName("lbl_frame")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_frame)
#         self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
#         self.verticalLayout_2.setSpacing(6)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_date.setFont(font)
#         self.lbl_date.setObjectName("lbl_date")
#         self.verticalLayout_2.addWidget(self.lbl_date)
#         self.lbl_cashInOut = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_cashInOut.setFont(font)
#         self.lbl_cashInOut.setObjectName("lbl_cashInOut")
#         self.verticalLayout_2.addWidget(self.lbl_cashInOut)
#         self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_name.setFont(font)
#         self.lbl_name.setObjectName("lbl_name")
#         self.verticalLayout_2.addWidget(self.lbl_name)
#         self.lbl_reference = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_reference.setFont(font)
#         self.lbl_reference.setObjectName("lbl_reference")
#         self.verticalLayout_2.addWidget(self.lbl_reference)
#         self.lbl_description = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_description.setFont(font)
#         self.lbl_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
#         self.lbl_description.setObjectName("lbl_description")
#         self.verticalLayout_2.addWidget(self.lbl_description)
#         self.lbl_amount = QtWidgets.QLabel(self.lbl_frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_amount.setFont(font)
#         self.lbl_amount.setObjectName("lbl_amount")
#         self.verticalLayout_2.addWidget(self.lbl_amount)
#         self.horizontalLayout.addWidget(self.lbl_frame)
#         self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
#         self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.lbl_inputs.setObjectName("lbl_inputs")
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lbl_inputs)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
#         self.txt_date.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_date.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_date.setFont(font)
#         self.txt_date.setMinimumDate(QtCore.QDate(2000, 9, 14))
#         self.txt_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
#         self.txt_date.setCalendarPopup(True)
#         self.txt_date.setTimeSpec(QtCore.Qt.LocalTime)
#         self.txt_date.setObjectName("txt_date")
#         self.verticalLayout_3.addWidget(self.txt_date)
#         self.cashInOut_option = QtWidgets.QComboBox(self.lbl_inputs)
#         self.cashInOut_option.setMinimumSize(QtCore.QSize(0, 0))
#         self.cashInOut_option.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.cashInOut_option.setFont(font)
#         self.cashInOut_option.setObjectName("cashInOut_option")
#         self.cashInOut_option.addItem("")
#         self.cashInOut_option.addItem("")
#         self.cashInOut_option.addItem("")
#         self.verticalLayout_3.addWidget(self.cashInOut_option)
#         self.names_list_option = QtWidgets.QComboBox(self.lbl_inputs)
#         self.names_list_option.setMinimumSize(QtCore.QSize(0, 0))
#         self.names_list_option.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.names_list_option.setFont(font)
#         self.names_list_option.setObjectName("names_list_option")
#         self.names_list_option.addItem("")
#         self.names_list_option.addItem("")
#         self.names_list_option.addItem("")
#         self.verticalLayout_3.addWidget(self.names_list_option)
#         self.txt_reference = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_reference.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_reference.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_reference.setFont(font)
#         self.txt_reference.setObjectName("txt_reference")
#         self.verticalLayout_3.addWidget(self.txt_reference)
#         self.txt_description = QtWidgets.QTextEdit(self.lbl_inputs)
#         self.txt_description.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_description.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_description.setFont(font)
#         self.txt_description.setObjectName("txt_description")
#         self.verticalLayout_3.addWidget(self.txt_description)
#         self.txt_amount = QtWidgets.QLineEdit(self.lbl_inputs)
#         self.txt_amount.setMinimumSize(QtCore.QSize(0, 0))
#         self.txt_amount.setMaximumSize(QtCore.QSize(1000, 40))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_amount.setFont(font)
#         self.txt_amount.setObjectName("txt_amount")
#         self.verticalLayout_3.addWidget(self.txt_amount)
#         self.horizontalLayout.addWidget(self.lbl_inputs)
#         self.verticalLayout_4.addWidget(self.details_widget)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.btn_update = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_update.setFont(font)
#         self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_update.setIcon(icon1)
#         self.btn_update.setIconSize(QtCore.QSize(32, 32))
#         self.btn_update.setObjectName("btn_update")
#         self.horizontalLayout_2.addWidget(self.btn_update)
#         self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_clear.setFont(font)
#         self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_clear.setIcon(icon2)
#         self.btn_clear.setIconSize(QtCore.QSize(32, 32))
#         self.btn_clear.setObjectName("btn_clear")
#         self.horizontalLayout_2.addWidget(self.btn_clear)
#         self.btn_cancel = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_cancel.setFont(font)
#         self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon3 = QtGui.QIcon()
#         icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cancel.setIcon(icon3)
#         self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cancel.setObjectName("btn_cancel")
#         self.horizontalLayout_2.addWidget(self.btn_cancel)
#         self.verticalLayout_4.addWidget(self.bottom_widget)
#         UpdateRozNamchaWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(UpdateRozNamchaWindow)
#         self.statusbar.setObjectName("statusbar")
#         UpdateRozNamchaWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(UpdateRozNamchaWindow)
#         QtCore.QMetaObject.connectSlotsByName(UpdateRozNamchaWindow)

#     def retranslateUi(self, UpdateRozNamchaWindow):
#         _translate = QtCore.QCoreApplication.translate
#         UpdateRozNamchaWindow.setWindowTitle(_translate("UpdateRozNamchaWindow", "Update Roznamcha"))
#         self.label_5.setText(_translate("UpdateRozNamchaWindow", "Update RozNamcha"))
#         self.lbl_date.setText(_translate("UpdateRozNamchaWindow", "Date"))
#         self.lbl_cashInOut.setText(_translate("UpdateRozNamchaWindow", "Cash In / Out"))
#         self.lbl_name.setText(_translate("UpdateRozNamchaWindow", "Name"))
#         self.lbl_reference.setText(_translate("UpdateRozNamchaWindow", "Reference"))
#         self.lbl_description.setText(_translate("UpdateRozNamchaWindow", "Description"))
#         self.lbl_amount.setText(_translate("UpdateRozNamchaWindow", "Amount"))
#         self.cashInOut_option.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Option"))
#         self.cashInOut_option.setItemText(1, _translate("UpdateRozNamchaWindow", "Cash In"))
#         self.cashInOut_option.setItemText(2, _translate("UpdateRozNamchaWindow", "Cash Out"))
#         self.names_list_option.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Option"))
#         self.names_list_option.setItemText(1, _translate("UpdateRozNamchaWindow", "Cash In"))
#         self.names_list_option.setItemText(2, _translate("UpdateRozNamchaWindow", "Cash Out"))
#         self.btn_update.setText(_translate("UpdateRozNamchaWindow", "UPDATE"))
#         self.btn_clear.setText(_translate("UpdateRozNamchaWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("UpdateRozNamchaWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UpdateRozNamchaWindow = QtWidgets.QMainWindow()
#     ui = Ui_UpdateRozNamchaWindow()
#     ui.setupUi(UpdateRozNamchaWindow)
#     UpdateRozNamchaWindow.show()
#     sys.exit(app.exec_())
