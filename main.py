
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *
from db_handler import DBHandler
from create_user import CreateUserWindow


from splash_screen import Ui_SplashScreen
from login_page import LoginWindow
## ==> GLOBALS
counter = 0

class SplashScreen(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        self.ui = Ui_SplashScreen()
        self.ui.setupUi(self)

        ## UI ==> INTERFACE CODES
        ########################################################################

        ## REMOVE TITLE BAR
        self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
        self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


        ## DROP SHADOW EFFECT
        self.shadow = QGraphicsDropShadowEffect(self)
        self.shadow.setBlurRadius(20)
        self.shadow.setXOffset(0)
        self.shadow.setYOffset(0)
        self.shadow.setColor(QColor(0, 0, 0, 60))
        self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

        ## QTIMER ==> START
        self.timer = QtCore.QTimer()
        self.timer.timeout.connect(self.progress)
        # TIMER IN MILLISECONDS
        self.timer.start(35)

        # CHANGE DESCRIPTION

        # Initial Text
        self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

        # Change Texts
        QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
        QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


        ## SHOW ==> MAIN WINDOW
        ########################################################################
        self.show()
        ## ==> END ##

    ## ==> APP FUNCTIONS
    ########################################################################
    def progress(self):

        global counter

        # SET VALUE TO PROGRESS BAR
        self.ui.progressBar.setValue(counter)

        # CLOSE SPLASH SCREE AND OPEN APP
        if counter > 100:
            # STOP TIMER
            self.timer.stop()

            # SHOW MAIN WINDOW
            # self.main = MainWindow()
            # self.main.show()
            db= DBHandler()
            if db.select_all("users",'*') == []:
                self.create_user = CreateUserWindow()
                self.create_user.show()
            else:
                self.login = LoginWindow()
                self.login.show()

            # CLOSE SPLASH SCREEN
            self.close()

        # INCREASE COUNTER
        counter += 1




if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SplashScreen()
    sys.exit(app.exec_())


# import sys
# from PyQt5 import QtCore, QtGui, QtWidgets
# from PyQt5.QtWidgets import QApplication, QMainWindow
# from PySide2 import QtCore, QtGui, QtWidgets
# from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime, QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
# from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
# from PySide2.QtWidgets import *


# from main_window import MainWindow
# from splash_screen import Ui_SplashScreen

# ## ==> GLOBALS
# counter = 0

# class MainWindow(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = MainWindow()
#         self.ui.setupUi(self)

#         # HOME PAGE BUTTON
#         self.ui.btn_home.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.home_page))

#         # CUSTOMER PAGE BUTTON
#         self.ui.btn_accounts.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.accounts_page))

#         # SALES PAGE BUTTON
#         self.ui.btn_roznamcha.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.roznamcha_page))

#         # PRODUCT PAGE BUTTON
#         self.ui.btn_settings.clicked.connect(lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.settings_page))

#         ## SHOW ==> MAIN WINDOW
#         ########################################################################
#         self.show

# class SplashScreen(QMainWindow):
#     def __init__(self):
#         QMainWindow.__init__(self)
#         self.ui = Ui_SplashScreen()
#         self.ui.setupUi(self)

#         ## UI ==> INTERFACE CODES
#         ########################################################################

#         ## REMOVE TITLE BAR
#         self.setWindowFlag(QtCore.Qt.FramelessWindowHint)
#         self.setAttribute(QtCore.Qt.WA_TranslucentBackground)


#         ## DROP SHADOW EFFECT
#         self.shadow = QGraphicsDropShadowEffect(self)
#         self.shadow.setBlurRadius(20)
#         self.shadow.setXOffset(0)
#         self.shadow.setYOffset(0)
#         self.shadow.setColor(QColor(0, 0, 0, 60))
#         self.ui.dropShadowFrame.setGraphicsEffect(self.shadow)

#         ## QTIMER ==> START
#         self.timer = QtCore.QTimer()
#         self.timer.timeout.connect(self.progress)
#         # TIMER IN MILLISECONDS
#         self.timer.start(35)

#         # CHANGE DESCRIPTION

#         # Initial Text
#         self.ui.label_description.setText("<strong>WELCOME</strong> TO MY APPLICATION")

#         # Change Texts
#         QtCore.QTimer.singleShot(1500, lambda: self.ui.label_description.setText("<strong>LOADING</strong> DATABASE"))
#         QtCore.QTimer.singleShot(3000, lambda: self.ui.label_description.setText("<strong>LOADING</strong> USER INTERFACE"))


#         ## SHOW ==> MAIN WINDOW
#         ########################################################################
#         self.show()
#         ## ==> END ##

#     ## ==> APP FUNCTIONS
#     ########################################################################
#     def progress(self):

#         global counter

#         # SET VALUE TO PROGRESS BAR
#         self.ui.progressBar.setValue(counter)

#         # CLOSE SPLASH SCREE AND OPEN APP
#         if counter > 100:
#             # STOP TIMER
#             self.timer.stop()

#             # SHOW MAIN WINDOW
#             self.main = MainWindow()
#             self.main.show()

#             # CLOSE SPLASH SCREEN
#             self.close()

#         # INCREASE COUNTER
#         counter += 1


# if __name__ == "__main__":
#     app = QApplication(sys.argv)
#     window = SplashScreen()
#     sys.exit(app.exec_())