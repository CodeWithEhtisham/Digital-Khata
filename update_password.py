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

FORM_MAIN, _ = loadUiType('ui/update_password.ui')


class ChangePasswordWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.change_password)
        self.btn_clear.clicked.connect(self.Clear)
        self.btn_cancel.clicked.connect(self.close)

    def change_password(self):
        old_password = self.txt_old_pwd.text()
        new_password = self.txt_new_pwd.text()
        confirm_password = self.txt_confirm_pwd.text()

        db = DBHandler()
        password = db.conn.execute(f"SELECT password FROM users WHERE password = '{old_password}'").fetchone()

        if password == None:
            QMessageBox.warning(self, "Error", "Old password is incorrect")
        else: password = password[0]
        if password == old_password:
            if new_password == confirm_password:
                db.conn.execute(f"UPDATE users SET password = '{new_password}' WHERE password = '{old_password}'")
                db.conn.commit()
                QMessageBox.information(self, "Success", "Password changed successfully")
                self.Clear()
            else:
                QMessageBox.warning(self, "Error", "New password and confirm password do not match")

        

    def Clear(self):
        self.txt_old_pwd.setText('')
        self.txt_new_pwd.setText('')
        self.txt_confirm_pwd.setText('')

def main():
    app = QApplication(sys.argv)
    window = ChangePasswordWindow()
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


# class Ui_ChangePasswordWindow(object):
#     def setupUi(self, ChangePasswordWindow):
#         ChangePasswordWindow.setObjectName("ChangePasswordWindow")
#         ChangePasswordWindow.resize(500, 350)
#         ChangePasswordWindow.setMinimumSize(QtCore.QSize(500, 350))
#         ChangePasswordWindow.setMaximumSize(QtCore.QSize(500, 350))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         ChangePasswordWindow.setWindowIcon(icon)
#         self.centralwidget = QtWidgets.QWidget(ChangePasswordWindow)
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
#         self.lbl_old_pwd = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_old_pwd.setFont(font)
#         self.lbl_old_pwd.setObjectName("lbl_old_pwd")
#         self.verticalLayout.addWidget(self.lbl_old_pwd)
#         self.lbl_new_pwd = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_new_pwd.setFont(font)
#         self.lbl_new_pwd.setObjectName("lbl_new_pwd")
#         self.verticalLayout.addWidget(self.lbl_new_pwd)
#         self.lbl_confirm_pwd = QtWidgets.QLabel(self.frame)
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.lbl_confirm_pwd.setFont(font)
#         self.lbl_confirm_pwd.setObjectName("lbl_confirm_pwd")
#         self.verticalLayout.addWidget(self.lbl_confirm_pwd)
#         self.horizontalLayout.addWidget(self.frame)
#         self.frame_2 = QtWidgets.QFrame(self.widget)
#         self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
#         self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
#         self.frame_2.setObjectName("frame_2")
#         self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame_2)
#         self.verticalLayout_2.setObjectName("verticalLayout_2")
#         self.txt_old_pwd = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_old_pwd.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_old_pwd.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_old_pwd.setFont(font)
#         self.txt_old_pwd.setObjectName("txt_old_pwd")
#         self.verticalLayout_2.addWidget(self.txt_old_pwd)
#         self.txt_new_pwd = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_new_pwd.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_new_pwd.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_new_pwd.setFont(font)
#         self.txt_new_pwd.setObjectName("txt_new_pwd")
#         self.verticalLayout_2.addWidget(self.txt_new_pwd)
#         self.txt_confirm_pwd = QtWidgets.QLineEdit(self.frame_2)
#         self.txt_confirm_pwd.setMinimumSize(QtCore.QSize(0, 35))
#         self.txt_confirm_pwd.setMaximumSize(QtCore.QSize(16777215, 35))
#         font = QtGui.QFont()
#         font.setFamily("Calibri")
#         font.setPointSize(14)
#         self.txt_confirm_pwd.setFont(font)
#         self.txt_confirm_pwd.setObjectName("txt_confirm_pwd")
#         self.verticalLayout_2.addWidget(self.txt_confirm_pwd)
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
#         icon1 = QtGui.QIcon()
#         icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
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
#         self.verticalLayout_3.addWidget(self.bottom_widget, 0, QtCore.Qt.AlignBottom)
#         ChangePasswordWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(ChangePasswordWindow)
#         self.statusbar.setObjectName("statusbar")
#         ChangePasswordWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(ChangePasswordWindow)
#         QtCore.QMetaObject.connectSlotsByName(ChangePasswordWindow)

#     def retranslateUi(self, ChangePasswordWindow):
#         _translate = QtCore.QCoreApplication.translate
#         ChangePasswordWindow.setWindowTitle(_translate("ChangePasswordWindow", "Change Password"))
#         self.label.setText(_translate("ChangePasswordWindow", "Change Password"))
#         self.lbl_old_pwd.setText(_translate("ChangePasswordWindow", "Old Password"))
#         self.lbl_new_pwd.setText(_translate("ChangePasswordWindow", "New Password"))
#         self.lbl_confirm_pwd.setText(_translate("ChangePasswordWindow", "Confirm Password"))
#         self.btn_save.setText(_translate("ChangePasswordWindow", "UPDATE"))
#         self.btn_clear.setText(_translate("ChangePasswordWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("ChangePasswordWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     ChangePasswordWindow = QtWidgets.QMainWindow()
#     ui = Ui_ChangePasswordWindow()
#     ui.setupUi(ChangePasswordWindow)
#     ChangePasswordWindow.show()
#     sys.exit(app.exec_())
