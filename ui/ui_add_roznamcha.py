# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'add_roznamcha.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_RozNamchaWindow(object):
    def setupUi(self, RozNamchaWindow):
        if not RozNamchaWindow.objectName():
            RozNamchaWindow.setObjectName(u"RozNamchaWindow")
        RozNamchaWindow.resize(500, 500)
        RozNamchaWindow.setMinimumSize(QSize(500, 500))
        RozNamchaWindow.setMaximumSize(QSize(500, 500))
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        RozNamchaWindow.setWindowIcon(icon)
        RozNamchaWindow.setIconSize(QSize(32, 32))
        self.centralwidget = QWidget(RozNamchaWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"#label_widget {\n"
"	background-color: #80cbc4;\n"
"}\n"
"\n"
"#label_5 {\n"
"	color: #fff;\n"
"}\n"
"\n"
"#btn_save {\n"
"	background-color: #26a69a;\n"
"	border-radius: 5px;\n"
"	padding: 5px 0px;\n"
"	color: white;\n"
"}\n"
"\n"
"#btn_clear {\n"
"	background-color: #81d4fa;\n"
"	border-radius: 5px;\n"
"	padding: 5px 0px;\n"
"	color: white;\n"
"}\n"
"\n"
"#btn_cancel {\n"
"	background-color: #b0bec5;\n"
"	border-radius: 5px;\n"
"	padding: 5px 0px;\n"
"	color: white;\n"
"}\n"
"\n"
"QLineEdit {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QDateEdit {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QComboBox {\n"
"	border-radius: 5px;\n"
"	padding: 5px 5px;\n"
"}\n"
"\n"
"QTextEdit {\n"
"	border-radius: 10px;\n"
"	padding: 0px 0px;\n"
"}")
        self.verticalLayout_4 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_4.setSpacing(1)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.label_widget = QWidget(self.centralwidget)
        self.label_widget.setObjectName(u"label_widget")
        self.verticalLayout = QVBoxLayout(self.label_widget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_5 = QLabel(self.label_widget)
        self.label_5.setObjectName(u"label_5")
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.label_5.setFont(font)
        self.label_5.setAlignment(Qt.AlignCenter)

        self.verticalLayout.addWidget(self.label_5)


        self.verticalLayout_4.addWidget(self.label_widget)

        self.details_widget = QWidget(self.centralwidget)
        self.details_widget.setObjectName(u"details_widget")
        self.horizontalLayout = QHBoxLayout(self.details_widget)
        self.horizontalLayout.setSpacing(10)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(20, 20, 20, 20)
        self.lbl_frame = QFrame(self.details_widget)
        self.lbl_frame.setObjectName(u"lbl_frame")
        self.lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_2 = QVBoxLayout(self.lbl_frame)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(-1, 9, -1, 9)
        self.lbl_date = QLabel(self.lbl_frame)
        self.lbl_date.setObjectName(u"lbl_date")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(14)
        self.lbl_date.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_date)

        self.lbl_cashInOut = QLabel(self.lbl_frame)
        self.lbl_cashInOut.setObjectName(u"lbl_cashInOut")
        self.lbl_cashInOut.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_cashInOut)

        self.lbl_name = QLabel(self.lbl_frame)
        self.lbl_name.setObjectName(u"lbl_name")
        self.lbl_name.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_name)

        self.lbl_reference = QLabel(self.lbl_frame)
        self.lbl_reference.setObjectName(u"lbl_reference")
        self.lbl_reference.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_reference)

        self.lbl_description = QLabel(self.lbl_frame)
        self.lbl_description.setObjectName(u"lbl_description")
        self.lbl_description.setFont(font1)
        self.lbl_description.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.verticalLayout_2.addWidget(self.lbl_description)

        self.lbl_amount = QLabel(self.lbl_frame)
        self.lbl_amount.setObjectName(u"lbl_amount")
        self.lbl_amount.setFont(font1)

        self.verticalLayout_2.addWidget(self.lbl_amount)


        self.horizontalLayout.addWidget(self.lbl_frame)

        self.lbl_inputs = QFrame(self.details_widget)
        self.lbl_inputs.setObjectName(u"lbl_inputs")
        self.lbl_inputs.setFrameShape(QFrame.StyledPanel)
        self.lbl_inputs.setFrameShadow(QFrame.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.lbl_inputs)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.txt_date = QDateEdit(self.lbl_inputs)
        self.txt_date.setObjectName(u"txt_date")
        self.txt_date.setMinimumSize(QSize(0, 0))
        self.txt_date.setMaximumSize(QSize(1000, 40))
        self.txt_date.setFont(font1)
        self.txt_date.setMinimumDate(QDate(2000, 9, 14))
        self.txt_date.setCurrentSection(QDateTimeEdit.DaySection)
        self.txt_date.setCalendarPopup(True)
        self.txt_date.setTimeSpec(Qt.LocalTime)

        self.verticalLayout_3.addWidget(self.txt_date)

        self.cashInOut_option = QComboBox(self.lbl_inputs)
        self.cashInOut_option.addItem("")
        self.cashInOut_option.addItem("")
        self.cashInOut_option.addItem("")
        self.cashInOut_option.setObjectName(u"cashInOut_option")
        self.cashInOut_option.setMinimumSize(QSize(0, 0))
        self.cashInOut_option.setMaximumSize(QSize(1000, 40))
        self.cashInOut_option.setFont(font1)

        self.verticalLayout_3.addWidget(self.cashInOut_option)

        self.names_list_option = QComboBox(self.lbl_inputs)
        self.names_list_option.addItem("")
        self.names_list_option.addItem("")
        self.names_list_option.addItem("")
        self.names_list_option.setObjectName(u"names_list_option")
        self.names_list_option.setMinimumSize(QSize(0, 0))
        self.names_list_option.setMaximumSize(QSize(1000, 40))
        self.names_list_option.setFont(font1)

        self.verticalLayout_3.addWidget(self.names_list_option)

        self.txt_reference = QLineEdit(self.lbl_inputs)
        self.txt_reference.setObjectName(u"txt_reference")
        self.txt_reference.setMinimumSize(QSize(0, 0))
        self.txt_reference.setMaximumSize(QSize(1000, 40))
        self.txt_reference.setFont(font1)

        self.verticalLayout_3.addWidget(self.txt_reference)

        self.txt_description = QTextEdit(self.lbl_inputs)
        self.txt_description.setObjectName(u"txt_description")
        self.txt_description.setMinimumSize(QSize(0, 0))
        self.txt_description.setMaximumSize(QSize(1000, 40))
        self.txt_description.setFont(font1)

        self.verticalLayout_3.addWidget(self.txt_description)

        self.txt_amount = QLineEdit(self.lbl_inputs)
        self.txt_amount.setObjectName(u"txt_amount")
        self.txt_amount.setMinimumSize(QSize(0, 0))
        self.txt_amount.setMaximumSize(QSize(1000, 40))
        self.txt_amount.setFont(font1)

        self.verticalLayout_3.addWidget(self.txt_amount)


        self.horizontalLayout.addWidget(self.lbl_inputs)


        self.verticalLayout_4.addWidget(self.details_widget)

        self.bottom_widget = QWidget(self.centralwidget)
        self.bottom_widget.setObjectName(u"bottom_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.bottom_widget)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.btn_save = QPushButton(self.bottom_widget)
        self.btn_save.setObjectName(u"btn_save")
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setWeight(75)
        self.btn_save.setFont(font2)
        self.btn_save.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/save.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_save.setIcon(icon1)
        self.btn_save.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_save)

        self.btn_clear = QPushButton(self.bottom_widget)
        self.btn_clear.setObjectName(u"btn_clear")
        self.btn_clear.setFont(font2)
        self.btn_clear.setCursor(QCursor(Qt.OpenHandCursor))
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/clear.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_clear.setIcon(icon2)
        self.btn_clear.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_clear)

        self.btn_cancel = QPushButton(self.bottom_widget)
        self.btn_cancel.setObjectName(u"btn_cancel")
        self.btn_cancel.setFont(font2)
        self.btn_cancel.setCursor(QCursor(Qt.OpenHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/close.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_cancel.setIcon(icon3)
        self.btn_cancel.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_cancel)


        self.verticalLayout_4.addWidget(self.bottom_widget)

        RozNamchaWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(RozNamchaWindow)
        self.statusbar.setObjectName(u"statusbar")
        RozNamchaWindow.setStatusBar(self.statusbar)

        self.retranslateUi(RozNamchaWindow)

        QMetaObject.connectSlotsByName(RozNamchaWindow)
    # setupUi

    def retranslateUi(self, RozNamchaWindow):
        RozNamchaWindow.setWindowTitle(QCoreApplication.translate("RozNamchaWindow", u"Roz Namcha", None))
        self.label_5.setText(QCoreApplication.translate("RozNamchaWindow", u"Add New RozNamcha", None))
        self.lbl_date.setText(QCoreApplication.translate("RozNamchaWindow", u"Date", None))
        self.lbl_cashInOut.setText(QCoreApplication.translate("RozNamchaWindow", u"Cash In / Out", None))
        self.lbl_name.setText(QCoreApplication.translate("RozNamchaWindow", u"Name", None))
        self.lbl_reference.setText(QCoreApplication.translate("RozNamchaWindow", u"Reference", None))
        self.lbl_description.setText(QCoreApplication.translate("RozNamchaWindow", u"Description", None))
        self.lbl_amount.setText(QCoreApplication.translate("RozNamchaWindow", u"Amount", None))
        self.cashInOut_option.setItemText(0, QCoreApplication.translate("RozNamchaWindow", u"Select Option", None))
        self.cashInOut_option.setItemText(1, QCoreApplication.translate("RozNamchaWindow", u"Cash In", None))
        self.cashInOut_option.setItemText(2, QCoreApplication.translate("RozNamchaWindow", u"Cash Out", None))

        self.names_list_option.setItemText(0, QCoreApplication.translate("RozNamchaWindow", u"Select Option", None))
        self.names_list_option.setItemText(1, QCoreApplication.translate("RozNamchaWindow", u"Cash In", None))
        self.names_list_option.setItemText(2, QCoreApplication.translate("RozNamchaWindow", u"Cash Out", None))

        self.btn_save.setText(QCoreApplication.translate("RozNamchaWindow", u"SAVE", None))
        self.btn_clear.setText(QCoreApplication.translate("RozNamchaWindow", u"CLEAR", None))
        self.btn_cancel.setText(QCoreApplication.translate("RozNamchaWindow", u"CANCEL", None))
    # retranslateUi

