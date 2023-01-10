from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_UpdateAccountsWindow(object):
    def setupUi(self, UpdateAccountsWindow):
        UpdateAccountsWindow.setObjectName("UpdateAccountsWindow")
        UpdateAccountsWindow.resize(500, 400)
        UpdateAccountsWindow.setMinimumSize(QtCore.QSize(500, 400))
        UpdateAccountsWindow.setMaximumSize(QtCore.QSize(500, 400))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateAccountsWindow.setWindowIcon(icon)
        UpdateAccountsWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(UpdateAccountsWindow)
        self.centralwidget.setStyleSheet("#label_widget {\n"
"    background-color: #80deea;\n"
"}\n"
"\n"
"#label_5 {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#btn_save {\n"
"    background-color: #26a69a;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"#btn_clear {\n"
"    background-color: #81d4fa;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"#btn_cancel {\n"
"    background-color: #b0bec5;\n"
"    border-radius: 5px;\n"
"    padding: 5px 0px;\n"
"    color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"    border-radius: 5px;\n"
"    padding: 5px 5px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_widget = QtWidgets.QWidget(self.centralwidget)
        self.label_widget.setObjectName("label_widget")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.label_widget)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label_5 = QtWidgets.QLabel(self.label_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout_3.addWidget(self.label_5, 0, QtCore.Qt.AlignTop)
        self.verticalLayout_4.addWidget(self.label_widget, 0, QtCore.Qt.AlignTop)
        self.details_widget = QtWidgets.QWidget(self.centralwidget)
        self.details_widget.setObjectName("details_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_frame = QtWidgets.QFrame(self.details_widget)
        self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_frame.setObjectName("lbl_frame")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.lbl_frame)
        self.verticalLayout.setObjectName("verticalLayout")
        self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout.addWidget(self.lbl_name)
        self.lbl_mobile = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_mobile.setFont(font)
        self.lbl_mobile.setObjectName("lbl_mobile")
        self.verticalLayout.addWidget(self.lbl_mobile)
        self.lbl_address = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_address.setFont(font)
        self.lbl_address.setObjectName("lbl_address")
        self.verticalLayout.addWidget(self.lbl_address)
        self.lbl_balance = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_balance.setFont(font)
        self.lbl_balance.setObjectName("lbl_balance")
        self.verticalLayout.addWidget(self.lbl_balance)
        self.horizontalLayout.addWidget(self.lbl_frame)
        self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
        self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_inputs.setObjectName("lbl_inputs")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_inputs)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.txt_name = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_name.setFont(font)
        self.txt_name.setObjectName("txt_name")
        self.verticalLayout_2.addWidget(self.txt_name)
        self.txt_mobile = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_mobile.setFont(font)
        self.txt_mobile.setObjectName("txt_mobile")
        self.verticalLayout_2.addWidget(self.txt_mobile)
        self.txt_address = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_address.setFont(font)
        self.txt_address.setObjectName("txt_address")
        self.verticalLayout_2.addWidget(self.txt_address)
        self.txt_balance = QtWidgets.QLineEdit(self.lbl_inputs)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_balance.setFont(font)
        self.txt_balance.setObjectName("txt_balance")
        self.verticalLayout_2.addWidget(self.txt_balance)
        self.horizontalLayout.addWidget(self.lbl_inputs)
        self.verticalLayout_4.addWidget(self.details_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_save = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_save.setFont(font)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QtCore.QSize(32, 32))
        self.btn_save.setObjectName("btn_save")
        self.horizontalLayout_2.addWidget(self.btn_save)
        self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/icons/assets/icons/clear.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_clear.setIcon(icon2)
        self.btn_clear.setIconSize(QtCore.QSize(32, 32))
        self.btn_clear.setObjectName("btn_clear")
        self.horizontalLayout_2.addWidget(self.btn_clear)
        self.btn_cancel = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_cancel.setFont(font)
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout_4.addWidget(self.bottom_widget)
        UpdateAccountsWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UpdateAccountsWindow)
        self.statusbar.setObjectName("statusbar")
        UpdateAccountsWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UpdateAccountsWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateAccountsWindow)

    def retranslateUi(self, UpdateAccountsWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateAccountsWindow.setWindowTitle(_translate("UpdateAccountsWindow", "Update Accounts"))
        self.label_5.setText(_translate("UpdateAccountsWindow", "Update Account"))
        self.lbl_name.setText(_translate("UpdateAccountsWindow", "Name"))
        self.lbl_mobile.setText(_translate("UpdateAccountsWindow", "Mobile"))
        self.lbl_address.setText(_translate("UpdateAccountsWindow", "Address"))
        self.lbl_balance.setText(_translate("UpdateAccountsWindow", "Opening Balance"))
        self.btn_save.setText(_translate("UpdateAccountsWindow", "UPDATE"))
        self.btn_clear.setText(_translate("UpdateAccountsWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("UpdateAccountsWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateAccountsWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdateAccountsWindow()
    ui.setupUi(UpdateAccountsWindow)
    UpdateAccountsWindow.show()
    sys.exit(app.exec_())
