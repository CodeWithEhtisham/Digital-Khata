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
from main_window import MainWindow
from PyQt5.uic import loadUiType
from resources_rc import *
# from main import MainWindow
FORM_MAIN, _ = loadUiType('ui/login_page.ui')



class LoginWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
    
    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.login_user)
        self.btn_cancel.clicked.connect(self.close_window)
        self.btn_clear.clicked.connect(self.clear_text)

    def close_window(self):
        self.close()
    
    def clear_text(self):
        self.txt_username.clear()
        self.txt_password.clear()

    def login_user(self):
        print("login")
        username = self.txt_username.text()
        password = self.txt_password.text()

        if username and password != "":
            try:
                db=DBHandler()
                data=db.authenticate(username=username, password=password)
                db.close()
                print(data)
                if data:
                    self.mainpage = MainWindow()
                    self.mainpage.show()
                    self.close_window()
                else:
                    QMessageBox.information(self, "Info", "Login credentials are incorrect")
                    self.clear_text()
                
            except Exception as e:
                QMessageBox.information(self, "Info", f"Login credentials error {e}")
        else:
            QMessageBox.information(self, "Info", "Fields cannot be empty")
        



# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_MainWindow()
#         self.ui.setupUi(self)

#         # HOME PAGE BUTTON
#         self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

#         # HOME PAGE BUTTON
#         self.ui.btn_product.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.product_page))

#         # HOME PAGE BUTTON
#         self.ui.btn_sales.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.sales_page))

#         # CUSTOMER PAGE BUTTON
#         self.ui.btn_customer.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.customer_page))

#         # ROZNAMCHA PAGE BUTTON
#         self.ui.btn_roznamcha.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roznamcha_page))

#         # SETTINGS PAGE BUTTON
#         self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

#         # ## SHOW ==> MAIN WINDOW
#         # ########################################################################
#         self.show


def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()







# from PyQt5 import QtCore, QtGui, QtWidgets
# from PySide2 import *
# from PySide2.QtCore import *
# from PySide2.QtGui import *
# from PySide2.QtWidgets import *


# class Ui_LoginWindow(object):
#     def setupUi(self, LoginWindow):
#         LoginWindow.setObjectName("LoginWindow")
#         LoginWindow.resize(500, 300)
#         LoginWindow.setMinimumSize(QtCore.QSize(500, 300))
#         LoginWindow.setMaximumSize(QtCore.QSize(500, 300))
#         self.centralwidget = QtWidgets.QWidget(LoginWindow)
#         self.centralwidget.setStyleSheet("\n"
# "\n"
# "#label {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#label_5 {\n"
# "    color: #fff;\n"
# "}\n"
# "\n"
# "#btn_save {\n"
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
# "#btn_create_business {\n"
# "    background-color: #4dd0e1;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_create_business {\n"
# "    background-color: #4dd0e1;\n"
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
#         self.verticalLayout_3.addWidget(self.label)
#         self.widget = QtWidgets.QWidget(self.centralwidget)
#         self.widget.setObjectName("widget")
#         self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
#         self.horizontalLayout.setObjectName("horizontalLayout")
#         self.frame = QtWidgets.QFrame(self.widget)
#         self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame.setObjectName("frame")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_username = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_username.setFont(font)
#         self.lbl_username.setObjectName("lbl_username")
#         self.verticalLayout_2.addWidget(self.lbl_username)
#         self.lbl_password = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_password.setFont(font)
#         self.lbl_password.setObjectName("lbl_password")
#         self.verticalLayout_2.addWidget(self.lbl_password)
#         self.horizontalLayout.addWidget(self.frame)
#         self.frame_2 = QtWidgets.QFrame(self.widget)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.txt_username = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_username.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_username.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_username.setFont(font)
#         self.txt_username.setObjectName("txt_username")
#         self.verticalLayout.addWidget(self.txt_username)
#         self.txt_password = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_password.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_password.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_password.setFont(font)
#         self.txt_password.setObjectName("txt_password")
#         self.verticalLayout.addWidget(self.txt_password)
#         self.horizontalLayout.addWidget(self.frame_2)
#         self.verticalLayout_3.addWidget(self.widget)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.btn_save = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_save.setFont(font)
#         self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_save.setIcon(icon)
#         self.btn_save.setIconSize(QtCore.QSize(32, 32))
#         self.btn_save.setObjectName("btn_save")
#         self.horizontalLayout_2.addWidget(self.btn_save)
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
#         LoginWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(LoginWindow)
#         self.statusbar.setObjectName("statusbar")
#         LoginWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(LoginWindow)
#         QtCore.QMetaObject.connectSlotsByName(LoginWindow)

#     def retranslateUi(self, LoginWindow):
#         _translate = QtCore.QCoreApplication.translate
#         LoginWindow.setWindowTitle(_translate("LoginWindow", "MainWindow"))
#         self.label.setText(_translate("LoginWindow", "Login"))
#         self.lbl_username.setText(_translate("LoginWindow", "User"))
#         self.lbl_password.setText(_translate("LoginWindow", "Password"))
#         self.btn_save.setText(_translate("LoginWindow", "Login"))
#         self.btn_clear.setText(_translate("LoginWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("LoginWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     LoginWindow = QtWidgets.QMainWindow()
#     ui = Ui_LoginWindow()
#     ui.setupUi(LoginWindow)
#     LoginWindow.show()
#     sys.exit(app.exec_())

# # -*- coding: utf-8 -*-

# # Form implementation generated from reading ui file 'login_page.ui'
# #
# # Created by: PyQt5 UI code generator 5.15.4
# #
# # WARNING: Any manual changes made to this file will be lost when pyuic5 is
# # run again.  Do not edit this file unless you know what you are doing.


# from PyQt5 import QtCore, QtGui, QtWidgets


# class Ui_LoginWindow(object):
#     def setupUi(self, LoginWindow):
#         LoginWindow.setObjectName("LoginWindow")
#         LoginWindow.resize(500, 400)
#         LoginWindow.setMinimumSize(QtCore.QSize(500, 400))
#         LoginWindow.setMaximumSize(QtCore.QSize(500, 400))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         LoginWindow.setWindowIcon(icon)
#         self.centralwidget = QtWidgets.QWidget(LoginWindow)
#         self.centralwidget.setStyleSheet("\n"
# "\n"
# "#label {\n"
# "    background-color: #80cbc4;\n"
# "}\n"
# "\n"
# "#label_5 {\n"
# "    color: #fff;\n"
# "}\n"
# "\n"
# "#btn_save {\n"
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
# "#btn_create_business {\n"
# "    background-color: #4dd0e1;\n"
# "    border-radius: 5px;\n"
# "    padding: 5px 0px;\n"
# "    color: white;\n"
# "}\n"
# "\n"
# "#btn_create_business {\n"
# "    background-color: #4dd0e1;\n"
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
#         self.verticalLayout_3.setSpacing(0)
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
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.lbl_username = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_username.setFont(font)
#         self.lbl_username.setObjectName("lbl_username")
#         self.verticalLayout_2.addWidget(self.lbl_username)
#         self.lbl_password = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_password.setFont(font)
#         self.lbl_password.setObjectName("lbl_password")
#         self.verticalLayout_2.addWidget(self.lbl_password)
#         self.horizontalLayout.addWidget(self.frame)
#         self.frame_2 = QtWidgets.QFrame(self.widget)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
#         self.verticalLayout.setObjectName("verticalLayout")
#         self.txt_username = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_username.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_username.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_username.setFont(font)
#         self.txt_username.setObjectName("txt_username")
#         self.verticalLayout.addWidget(self.txt_username)
#         self.txt_password = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_password.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_password.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_password.setFont(font)
#         self.txt_password.setObjectName("txt_password")
#         self.verticalLayout.addWidget(self.txt_password)
#         self.horizontalLayout.addWidget(self.frame_2)
#         self.verticalLayout_3.addWidget(self.widget)
#         self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
#         self.bottom_widget.setObjectName("bottom_widget")
#         self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
#         self.horizontalLayout_2.setContentsMargins(-1, 0, -1, 0)
#         self.horizontalLayout_2.setSpacing(5)
#         self.horizontalLayout_2.setObjectName("horizontalLayout_2")
#         self.btn_save = QtWidgets.QPushButton(self.bottom_widget)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         font.setBold(True)
#         font.setWeight(75)
#         self.btn_save.setFont(font)
#         self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/user.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         self.btn_save.setIcon(icon1)
#         self.btn_save.setIconSize(QtCore.QSize(32, 32))
#         self.btn_save.setObjectName("btn_save")
#         self.horizontalLayout_2.addWidget(self.btn_save)
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
#         self.verticalLayout_3.addWidget(self.bottom_widget)
#         self.frame_3 = QtWidgets.QFrame(self.centralwidget)
#         self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_3.setObjectName("frame_3")
#         self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_3)
#         self.horizontalLayout_3.setContentsMargins(20, 0, 20, 0)
#         self.horizontalLayout_3.setSpacing(0)
#         self.horizontalLayout_3.setObjectName("horizontalLayout_3")
#         self.label_2 = QtWidgets.QLabel(self.frame_3)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_2.setFont(font)
#         self.label_2.setObjectName("label_2")
#         self.horizontalLayout_3.addWidget(self.label_2, 0, QtCore.Qt.AlignLeft)
#         self.label_3 = QtWidgets.QLabel(self.frame_3)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(12)
#         font.setBold(True)
#         font.setWeight(75)
#         self.label_3.setFont(font)
#         self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
#         self.label_3.setObjectName("label_3")
#         self.horizontalLayout_3.addWidget(self.label_3)
#         self.verticalLayout_3.addWidget(self.frame_3)
#         LoginWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(LoginWindow)
#         self.statusbar.setObjectName("statusbar")
#         LoginWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(LoginWindow)
#         QtCore.QMetaObject.connectSlotsByName(LoginWindow)

#     def retranslateUi(self, LoginWindow):
#         _translate = QtCore.QCoreApplication.translate
#         LoginWindow.setWindowTitle(_translate("LoginWindow", "Login"))
#         self.label.setText(_translate("LoginWindow", "Login"))
#         self.lbl_username.setText(_translate("LoginWindow", "User"))
#         self.lbl_password.setText(_translate("LoginWindow", "Password"))
#         self.btn_save.setText(_translate("LoginWindow", "Login"))
#         self.btn_clear.setText(_translate("LoginWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("LoginWindow", "CANCEL"))
#         self.label_2.setText(_translate("LoginWindow", "+92 335 2321360"))
#         self.label_3.setText(_translate("LoginWindow", "Software Developed"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     LoginWindow = QtWidgets.QMainWindow()
#     ui = Ui_LoginWindow()
#     ui.setupUi(LoginWindow)
#     LoginWindow.show()
#     sys.exit(app.exec_())
