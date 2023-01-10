from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_UpdateRozNamchaWindow(object):
    def setupUi(self, UpdateRozNamchaWindow):
        UpdateRozNamchaWindow.setObjectName("UpdateRozNamchaWindow")
        UpdateRozNamchaWindow.resize(500, 500)
        UpdateRozNamchaWindow.setMinimumSize(QtCore.QSize(500, 500))
        UpdateRozNamchaWindow.setMaximumSize(QtCore.QSize(500, 500))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        UpdateRozNamchaWindow.setWindowIcon(icon)
        UpdateRozNamchaWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(UpdateRozNamchaWindow)
        self.centralwidget.setStyleSheet("#label_widget {\n"
"    background-color: #80deea;\n"
"}\n"
"\n"
"#label_5 {\n"
"    color: #fff;\n"
"}\n"
"\n"
"#btn_update {\n"
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
"}\n"
"\n"
"QDateEdit {\n"
"    border-radius: 5px;\n"
"    padding: 5px 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"    border-radius: 5px;\n"
"    padding: 5px 5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"    border-radius: 10px;\n"
"    padding: 0px 0px;\n"
"}")
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(0)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.label_widget = QtWidgets.QWidget(self.centralwidget)
        self.label_widget.setObjectName("label_widget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.label_widget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.label_5 = QtWidgets.QLabel(self.label_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(QtCore.Qt.AlignCenter)
        self.label_5.setObjectName("label_5")
        self.verticalLayout.addWidget(self.label_5)
        self.verticalLayout_4.addWidget(self.label_widget)
        self.details_widget = QtWidgets.QWidget(self.centralwidget)
        self.details_widget.setObjectName("details_widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.details_widget)
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lbl_frame = QtWidgets.QFrame(self.details_widget)
        self.lbl_frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_frame.setObjectName("lbl_frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.lbl_frame)
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_date = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_date.setFont(font)
        self.lbl_date.setObjectName("lbl_date")
        self.verticalLayout_2.addWidget(self.lbl_date)
        self.lbl_cashInOut = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_cashInOut.setFont(font)
        self.lbl_cashInOut.setObjectName("lbl_cashInOut")
        self.verticalLayout_2.addWidget(self.lbl_cashInOut)
        self.lbl_name = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_name.setFont(font)
        self.lbl_name.setObjectName("lbl_name")
        self.verticalLayout_2.addWidget(self.lbl_name)
        self.lbl_reference = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_reference.setFont(font)
        self.lbl_reference.setObjectName("lbl_reference")
        self.verticalLayout_2.addWidget(self.lbl_reference)
        self.lbl_description = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_description.setFont(font)
        self.lbl_description.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.lbl_description.setObjectName("lbl_description")
        self.verticalLayout_2.addWidget(self.lbl_description)
        self.lbl_amount = QtWidgets.QLabel(self.lbl_frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_amount.setFont(font)
        self.lbl_amount.setObjectName("lbl_amount")
        self.verticalLayout_2.addWidget(self.lbl_amount)
        self.horizontalLayout.addWidget(self.lbl_frame)
        self.lbl_inputs = QtWidgets.QFrame(self.details_widget)
        self.lbl_inputs.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QtWidgets.QFrame.Raised)
        self.lbl_inputs.setObjectName("lbl_inputs")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.lbl_inputs)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.txt_date = QtWidgets.QDateEdit(self.lbl_inputs)
        self.txt_date.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_date.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_date.setFont(font)
        self.txt_date.setMinimumDate(QtCore.QDate(2000, 9, 14))
        self.txt_date.setCurrentSection(QtWidgets.QDateTimeEdit.DaySection)
        self.txt_date.setCalendarPopup(True)
        self.txt_date.setTimeSpec(QtCore.Qt.LocalTime)
        self.txt_date.setObjectName("txt_date")
        self.verticalLayout_3.addWidget(self.txt_date)
        self.cashInOut_option = QtWidgets.QComboBox(self.lbl_inputs)
        self.cashInOut_option.setMinimumSize(QtCore.QSize(0, 0))
        self.cashInOut_option.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.cashInOut_option.setFont(font)
        self.cashInOut_option.setObjectName("cashInOut_option")
        self.cashInOut_option.addItem("")
        self.cashInOut_option.addItem("")
        self.cashInOut_option.addItem("")
        self.verticalLayout_3.addWidget(self.cashInOut_option)
        self.names_list_option = QtWidgets.QComboBox(self.lbl_inputs)
        self.names_list_option.setMinimumSize(QtCore.QSize(0, 0))
        self.names_list_option.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.names_list_option.setFont(font)
        self.names_list_option.setObjectName("names_list_option")
        self.names_list_option.addItem("")
        self.names_list_option.addItem("")
        self.names_list_option.addItem("")
        self.verticalLayout_3.addWidget(self.names_list_option)
        self.txt_reference = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_reference.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_reference.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_reference.setFont(font)
        self.txt_reference.setObjectName("txt_reference")
        self.verticalLayout_3.addWidget(self.txt_reference)
        self.txt_description = QtWidgets.QTextEdit(self.lbl_inputs)
        self.txt_description.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_description.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_description.setFont(font)
        self.txt_description.setObjectName("txt_description")
        self.verticalLayout_3.addWidget(self.txt_description)
        self.txt_amount = QtWidgets.QLineEdit(self.lbl_inputs)
        self.txt_amount.setMinimumSize(QtCore.QSize(0, 0))
        self.txt_amount.setMaximumSize(QtCore.QSize(1000, 40))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_amount.setFont(font)
        self.txt_amount.setObjectName("txt_amount")
        self.verticalLayout_3.addWidget(self.txt_amount)
        self.horizontalLayout.addWidget(self.lbl_inputs)
        self.verticalLayout_4.addWidget(self.details_widget)
        self.bottom_widget = QtWidgets.QWidget(self.centralwidget)
        self.bottom_widget.setObjectName("bottom_widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_update = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_update.setFont(font)
        self.btn_update.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/icons/assets/icons/save.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_update.setIcon(icon1)
        self.btn_update.setIconSize(QtCore.QSize(32, 32))
        self.btn_update.setObjectName("btn_update")
        self.horizontalLayout_2.addWidget(self.btn_update)
        self.btn_clear = QtWidgets.QPushButton(self.bottom_widget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.btn_clear.setFont(font)
        self.btn_clear.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
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
        self.btn_cancel.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/icons/assets/icons/close.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QtCore.QSize(32, 32))
        self.btn_cancel.setObjectName("btn_cancel")
        self.horizontalLayout_2.addWidget(self.btn_cancel)
        self.verticalLayout_4.addWidget(self.bottom_widget)
        UpdateRozNamchaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(UpdateRozNamchaWindow)
        self.statusbar.setObjectName("statusbar")
        UpdateRozNamchaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(UpdateRozNamchaWindow)
        QtCore.QMetaObject.connectSlotsByName(UpdateRozNamchaWindow)

    def retranslateUi(self, UpdateRozNamchaWindow):
        _translate = QtCore.QCoreApplication.translate
        UpdateRozNamchaWindow.setWindowTitle(_translate("UpdateRozNamchaWindow", "Update Roznamcha"))
        self.label_5.setText(_translate("UpdateRozNamchaWindow", "Update RozNamcha"))
        self.lbl_date.setText(_translate("UpdateRozNamchaWindow", "Date"))
        self.lbl_cashInOut.setText(_translate("UpdateRozNamchaWindow", "Cash In / Out"))
        self.lbl_name.setText(_translate("UpdateRozNamchaWindow", "Name"))
        self.lbl_reference.setText(_translate("UpdateRozNamchaWindow", "Reference"))
        self.lbl_description.setText(_translate("UpdateRozNamchaWindow", "Description"))
        self.lbl_amount.setText(_translate("UpdateRozNamchaWindow", "Amount"))
        self.cashInOut_option.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Option"))
        self.cashInOut_option.setItemText(1, _translate("UpdateRozNamchaWindow", "Cash In"))
        self.cashInOut_option.setItemText(2, _translate("UpdateRozNamchaWindow", "Cash Out"))
        self.names_list_option.setItemText(0, _translate("UpdateRozNamchaWindow", "Select Option"))
        self.names_list_option.setItemText(1, _translate("UpdateRozNamchaWindow", "Cash In"))
        self.names_list_option.setItemText(2, _translate("UpdateRozNamchaWindow", "Cash Out"))
        self.btn_update.setText(_translate("UpdateRozNamchaWindow", "UPDATE"))
        self.btn_clear.setText(_translate("UpdateRozNamchaWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("UpdateRozNamchaWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    UpdateRozNamchaWindow = QtWidgets.QMainWindow()
    ui = Ui_UpdateRozNamchaWindow()
    ui.setupUi(UpdateRozNamchaWindow)
    UpdateRozNamchaWindow.show()
    sys.exit(app.exec_())
