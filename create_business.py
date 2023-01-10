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
from resources_rc import *
FORM_MAIN, _ = loadUiType('ui/create_business.ui')


class NewBusinessWindow(QMainWindow, FORM_MAIN):
    def __init__(self):
        QMainWindow.__init__(self)
        self.setupUi(self)
        self.Handle_Buttons()

    def Handle_Buttons(self):
        self.btn_save.clicked.connect(self.save_business)
        self.btn_clear.clicked.connect(self.clear_fields)
        self.btn_cancel.clicked.connect(self.close)

    def save_business(self):
        business_name = self.txt_business_name.text()
        business_email = self.txt_business_email.text()
        business_address = self.txt_business_address.text()
        business_phone = self.txt_business_contact.text()
        business_owner = self.txt_business_owner.text()

        print(f"Business Name: {business_name} , Business Email: {business_email} , Business Address: {business_address} , Business Phone: {business_phone} , Business Owner: {business_owner}")

        if business_name == '' or business_email == '' or business_address == '' or business_phone == '' or business_owner == '':
            QMessageBox.warning(self, 'Error', 'All fields are required')
        else:
            try:
                db=DBHandler()
                if not db.check_table('business'):
                    db.create_table('business', 'id INTEGER PRIMARY KEY AUTOINCREMENT, business_name TEXT, business_email TEXT, business_address TEXT, business_contact TEXT, business_owner TEXT')
                db.insert('business', 'business_name, business_email, business_address, business_contact, business_owner', f"'{business_name}', '{business_email}', '{business_address}', '{business_phone}', '{business_owner}'")
                QMessageBox.information(self, 'Success', 'Business Added Successfully')
                db.close()
                self.close()
            except Exception:
                QMessageBox.warning(self, 'Error', 'Business Not Added')

    def clear_fields(self):
        self.txt_business_name.setText('')
        self.txt_business_email.setText('')
        self.txt_business_address.setText('')
        self.txt_business_contact.setText('')
        self.txt_business_owner.setText('')

    
        

def main():
    app = QApplication(sys.argv)
    window = NewBusinessWindow()
    window.show()
    app.exec_()


if __name__ == '__main__':
    main()


# import datetime
# import sqlite3
# from PyQt5.QtWidgets import *
# from PyQt5.QtGui import *
# from PyQt5.QtCore import *
# from PyQt5 import QtWidgets
# from PyQt5 import QtCore
# from PyQt5.QtWidgets import QMainWindow
# from PyQt5.QtWidgets import QApplication
# # from db_handler import DBHandler
# import sys
# from os import path
# from PyQt5.uic import loadUiType

# FORM_MAIN, _ = loadUiType('ui/create_business.ui')


# class NewBusinessWindow(QMainWindow, FORM_MAIN):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.setupUi(self)


# def main():
#     app = QApplication(sys.argv)
#     window = NewBusinessWindow()
#     window.show()
#     app.exec_()


# if __name__ == '__main__':
#     main()
