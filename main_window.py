import datetime
import sqlite3
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5 import QtWidgets
from PyQt5 import QtCore
from PyQt5.QtWidgets import QMainWindow
from PyQt5.QtWidgets import QApplication
# from db_handler import DBHandler
import sys
from os import path
from PyQt5.uic import loadUiType

from add_accounts import AddAccountsWindow
from add_roznamcha import RozNamchaWindow
from account_details import AccountDetailsWindow
from create_business import NewBusinessWindow

FORM_MAIN, _ = loadUiType('ui/main_window.ui')


class MainWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.showMaximized()
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_home.clicked.connect(self.home)
        self.btn_accounts.clicked.connect(self.accounts)
        self.btn_roznamcha.clicked.connect(self.roznamcha)
        self.btn_settings.clicked.connect(self.settings)

        self.btn_add_accounts.clicked.connect(self.add_accounts)
        self.btn_add_roznamcha.clicked.connect(self.add_roznamcha)
        
        self.accounts_table.doubleClicked.connect(self.account_details)
        
        self.btn_business_details.clicked.connect(self.business_details)

    def home(self):
        self.stackedWidget.setCurrentWidget(self.home_page)

    def accounts(self):
        self.stackedWidget.setCurrentWidget(self.accounts_page)

    def roznamcha(self):
        self.stackedWidget.setCurrentWidget(self.roznamcha_page)

    def settings(self):
        self.stackedWidget.setCurrentWidget(self.settings_page)

    def add_accounts(self):
        self.window = AddAccountsWindow()
        self.window.show()

    def add_roznamcha(self):
        self.window = RozNamchaWindow()
        self.window.show()
        
    def account_details(self):
        self.window = AccountDetailsWindow()
        self.window.show()
        
    def business_details(self):
        self.window = NewBusinessWindow()
        self.window.show()


def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()
