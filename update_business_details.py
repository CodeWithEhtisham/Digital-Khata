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

FORM_MAIN, _ = loadUiType('ui/update_business_details.ui')


class UpdateBusinessWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

        db= DBHandler()
        data= db.select_all('business','*')[0]
        if data:
            self.txt_business_name.setText(data[1])
            self.txt_business_email.setText(data[2])
            self.txt_business_contact.setText(data[3])
            self.txt_business_address.setText(data[4])
            self.txt_business_owner.setText(data[5])
        db.close()

    def Handle_Buttons(self):
        self.btn_update.clicked.connect(self.Update_Business)
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_cancel.clicked.connect(self.Cancel)

    def Update_Business(self):
        business_name = self.txt_business_name.text()
        business_email = self.txt_business_email.text()
        business_phone = self.txt_business_contact.text()
        business_address = self.txt_business_address.text()
        business_owner = self.txt_business_owner.text()

        if business_name and business_email and business_address and business_phone and business_owner:
            try:
                db= DBHandler()
                db.conn.execute("UPDATE business SET business_name=?, business_email=?, business_contact=?, business_address=?, business_owner=? WHERE id=1", (business_name, business_email, business_phone, business_address, business_owner))
                db.conn.commit()
                db.close()
                QMessageBox.information(self, "Success", "Business Details Updated")
                self.close()
            except Exception as e:
                QMessageBox.information(self, "Warning", f"Business Details Not Updated {e}")
        else:
            QMessageBox.information(self, "Warning", "Fields cannot be empty")

    def Clear(self):
        self.txt_business_name.setText("")
        self.txt_business_email.setText("")
        self.txt_business_address.setText("")
        self.txt_business_contact.setText("")
        self.txt_business_owner.setText("")

    def Cancel(self):
        self.close()
        

def main():
    app = QApplication(sys.argv)
    window = UpdateBusinessWindow()
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


# class Ui_UpdateBusinessWindow(object):
#     def setupUi(self, UpdateBusinessWindow):
#         UpdateBusinessWindow.setObjectName("UpdateBusinessWindow")
#         UpdateBusinessWindow.resize(500, 450)
#         UpdateBusinessWindow.setMinimumSize(QtCore.QSize(500, 450))
#         UpdateBusinessWindow.setMaximumSize(QtCore.QSize(500, 450))
#         self.centralwidget = QtWidgets.QWidget(UpdateBusinessWindow)
#         self.centralwidget.setStyleSheet("\n"
# "\n"
# "#label {\n"
# "    background-color: #81d4fa;\n"
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
#         self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
#         self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
#         self.verticalLayout_3.setSpacing(1)
#         self.verticalLayout_3.setObjectName("verticalLayout_3")
#         self.label = QtWidgets.QLabel(self.centralwidget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(18)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label.setFont(font)
#         self.label.setAlignment(QtCore.Qt.AlignCenter)
#         self.label.setObjectName("label")
#         self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setObjectName("widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.frame = QtWidgets.QFrame(self.widget)
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.frame)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.lbl_name = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_name.setFont(font)
#         self.lbl_name.setObjectName("lbl_name")
#         self.verticalLayout.addWidget(self.lbl_name)
#         self.lbl_email = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_email.setFont(font)
#         self.lbl_email.setObjectName("lbl_email")
#         self.verticalLayout.addWidget(self.lbl_email)
#         self.lbl_contact = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_contact.setFont(font)
#         self.lbl_contact.setObjectName("lbl_contact")
#         self.verticalLayout.addWidget(self.lbl_contact)
#         self.lbl_username = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_username.setFont(font)
#         self.lbl_username.setObjectName("lbl_username")
#         self.verticalLayout.addWidget(self.lbl_username)
#         self.lbl_password = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_password.setFont(font)
#         self.lbl_password.setObjectName("lbl_password")
#         self.verticalLayout.addWidget(self.lbl_password)
#         self.horizontalLayout.addWidget(self.frame)
#         self.frame_2 = QtWidgets.QFrame(self.widget)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.txt_name = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_name.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_name.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_name.setFont(font)
#         self.txt_name.setObjectName("txt_name")
#         self.verticalLayout_2.addWidget(self.txt_name)
#         self.txt_email = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_email.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_email.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_email.setFont(font)
#         self.txt_email.setObjectName("txt_email")
#         self.verticalLayout_2.addWidget(self.txt_email)
#         self.txt_contact = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_contact.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_contact.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_contact.setFont(font)
#         self.txt_contact.setObjectName("txt_contact")
#         self.verticalLayout_2.addWidget(self.txt_contact)
#         self.txt_username = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_username.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_username.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_username.setFont(font)
#         self.txt_username.setObjectName("txt_username")
#         self.verticalLayout_2.addWidget(self.txt_username)
#         self.txt_password = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_password.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_password.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_password.setFont(font)
#         self.txt_password.setObjectName("txt_password")
#         self.verticalLayout_2.addWidget(self.txt_password)
#         self.horizontalLayout.addWidget(self.frame_2)
#         self.verticalLayout_3.addWidget(self.widget)
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
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_update.setIcon(icon)
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
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_clear.setIcon(icon1)
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
#         icon2 = QtGui.QIcon()
#         icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_cancel.setIcon(icon2)
#         self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
#         self.btn_cancel.setObjectName("btn_cancel")
#         self.horizontalLayout_2.addWidget(self.btn_cancel)
#         self.verticalLayout_3.addWidget(self.bottom_widget)
#         UpdateBusinessWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(UpdateBusinessWindow)
#         self.statusbar.setObjectName("statusbar")
#         UpdateBusinessWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(UpdateBusinessWindow)
#         QtCore.QMetaObject.connectSlotsByName(UpdateBusinessWindow)

#     def retranslateUi(self, UpdateBusinessWindow):
#         _translate = QtCore.QCoreApplication.translate
#         UpdateBusinessWindow.setWindowTitle(_translate("UpdateBusinessWindow", "Update Business"))
#         self.label.setText(_translate("UpdateBusinessWindow", "Update Business Details"))
#         self.lbl_name.setText(_translate("UpdateBusinessWindow", "Business Name"))
#         self.lbl_email.setText(_translate("UpdateBusinessWindow", "Business Email"))
#         self.lbl_contact.setText(_translate("UpdateBusinessWindow", "Business Contact"))
#         self.lbl_username.setText(_translate("UpdateBusinessWindow", "Business Address"))
#         self.lbl_password.setText(_translate("UpdateBusinessWindow", "Business Owner"))
#         self.btn_update.setText(_translate("UpdateBusinessWindow", "UPDATE"))
#         self.btn_clear.setText(_translate("UpdateBusinessWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("UpdateBusinessWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UpdateBusinessWindow = QtWidgets.QMainWindow()
#     ui = Ui_UpdateBusinessWindow()
#     ui.setupUi(UpdateBusinessWindow)
#     UpdateBusinessWindow.show()
#     sys.exit(app.exec_())
