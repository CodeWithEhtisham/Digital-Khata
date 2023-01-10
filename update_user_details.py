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

FORM_MAIN, _ = loadUiType('ui/update_user_details.ui')


class UpdateUserWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

        db=DBHandler()
        user = db.select(table_name="users", columns="*", condition="id=1")[0]
        self.txt_name.setText(user[1])
        self.txt_email.setText(user[2])
        self.txt_contact.setText(user[3])
        self.txt_username.setText(user[4])

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.Save_User)
        self.btn_clear.clicked.connect(self.Clear_User)
        self.btn_cancel.clicked.connect(self.close)

    def Save_User(self):
        name = self.txt_name.text()
        email = self.txt_email.text()
        contact = self.txt_contact.text()
        username = self.txt_username.text()
        if name and email and contact and username != "":
            try:
                db=DBHandler()
                db.conn.execute("UPDATE users SET name=?, email=?, contact=?, username=? WHERE id=1", (name, email, contact, username))
                db.conn.commit()
                QMessageBox.information(self, "Success", "User has been added")
                db.close()
                self.close()
            except Exception as e:
                QMessageBox.warning(self, "Error", f"User has not been added {e}")
        else:
            QMessageBox.warning(self, "Error", "Fields cannot be empty")
        
    def Clear_User(self):
        self.txt_name.setText("")
        self.txt_email.setText("")
        self.txt_contact.setText("")
        self.txt_username.setText("")

def main():
    app = QApplication(sys.argv)
    window = UpdateUserWindow()
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


# class Ui_UpdateUserWindow(object):
#     def setupUi(self, UpdateUserWindow):
#         UpdateUserWindow.setObjectName("UpdateUserWindow")
#         UpdateUserWindow.resize(500, 450)
#         UpdateUserWindow.setMinimumSize(QtCore.QSize(500, 450))
#         UpdateUserWindow.setMaximumSize(QtCore.QSize(500, 450))
#         icon = QtGui.QIcon()
#         icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
#         UpdateUserWindow.setWindowIcon(icon)
#         self.centralwidget = QtWidgets.QWidget(UpdateUserWindow)
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
#         UpdateUserWindow.setCentralWidget(self.centralwidget)
#         self.statusbar = QtWidgets.QStatusBar(UpdateUserWindow)
#         self.statusbar.setObjectName("statusbar")
#         UpdateUserWindow.setStatusBar(self.statusbar)

#         self.retranslateUi(UpdateUserWindow)
#         QtCore.QMetaObject.connectSlotsByName(UpdateUserWindow)

#     def retranslateUi(self, UpdateUserWindow):
#         _translate = QtCore.QCoreApplication.translate
#         UpdateUserWindow.setWindowTitle(_translate("UpdateUserWindow", "Update User Details"))
#         self.label.setText(_translate("UpdateUserWindow", "Update User Details"))
#         self.lbl_name.setText(_translate("UpdateUserWindow", "Name"))
#         self.lbl_email.setText(_translate("UpdateUserWindow", "Email"))
#         self.lbl_contact.setText(_translate("UpdateUserWindow", "Contact"))
#         self.lbl_username.setText(_translate("UpdateUserWindow", "Username"))
#         self.btn_save.setText(_translate("UpdateUserWindow", "UPDATE"))
#         self.btn_clear.setText(_translate("UpdateUserWindow", "CLEAR"))
#         self.btn_cancel.setText(_translate("UpdateUserWindow", "CANCEL"))
# import resources_rc


# if __name__ == "__main__":
#     import sys
#     app = QtWidgets.QApplication(sys.argv)
#     UpdateUserWindow = QtWidgets.QMainWindow()
#     ui = Ui_UpdateUserWindow()
#     ui.setupUi(UpdateUserWindow)
#     UpdateUserWindow.show()
#     sys.exit(app.exec_())
