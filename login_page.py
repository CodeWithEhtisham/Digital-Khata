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
FORM_MAIN, _ = loadUiType('ui/login_page.ui')


class LoginWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()
    
        self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.show_password.toggled.connect(self.toggle_password_visibility)
        # REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        
    def toggle_password_visibility(self, checked):
        if checked:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Normal)
        else:
            self.txt_password.setEchoMode(QtWidgets.QLineEdit.Password)
    
    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Return:
            self.login_user()
    
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
    
def main():
    app = QApplication(sys.argv)
    window = LoginWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
