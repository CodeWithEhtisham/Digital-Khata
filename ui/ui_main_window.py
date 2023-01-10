# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_window.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1242, 939)
        icon = QIcon()
        icon.addFile(u":/icons/assets/icons/logo.png", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        MainWindow.setIconSize(QSize(40, 40))
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.centralwidget.setStyleSheet(u"\n"
"#stackedWidget {\n"
"	background-color: #b2ebf2;\n"
"}\n"
"\n"
"#upper_widget {\n"
"	background-color: #80cbc4;\n"
"}\n"
"\n"
"#btn_accounts {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_home {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_roznamcha {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_settings {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_logout {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#user_frame {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#lbl_user_name {\n"
"	background-color: #fff;\n"
"}\n"
"\n"
"#khata_options {\n"
"	background-color: #eee;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#lbl_user_contact {\n"
"	background-color: #fff;\n"
"}")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setSpacing(0)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.verticalLayout.setContentsMargins(0, 0, 0, 0)
        self.upper_widget = QWidget(self.centralwidget)
        self.upper_widget.setObjectName(u"upper_widget")
        self.upper_widget.setStyleSheet(u"")
        self.horizontalLayout = QHBoxLayout(self.upper_widget)
        self.horizontalLayout.setSpacing(5)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(5, 5, 5, 5)
        self.btn_home = QPushButton(self.upper_widget)
        self.btn_home.setObjectName(u"btn_home")
        self.btn_home.setMinimumSize(QSize(150, 40))
        self.btn_home.setMaximumSize(QSize(150, 40))
        font = QFont()
        font.setFamily(u"Calibri")
        font.setPointSize(16)
        font.setBold(True)
        font.setWeight(75)
        self.btn_home.setFont(font)
        self.btn_home.setCursor(QCursor(Qt.OpenHandCursor))
        icon1 = QIcon()
        icon1.addFile(u":/icons/assets/icons/home.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_home.setIcon(icon1)
        self.btn_home.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_home)

        self.btn_accounts = QPushButton(self.upper_widget)
        self.btn_accounts.setObjectName(u"btn_accounts")
        self.btn_accounts.setMinimumSize(QSize(150, 40))
        self.btn_accounts.setMaximumSize(QSize(150, 40))
        self.btn_accounts.setFont(font)
        self.btn_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_accounts.setLayoutDirection(Qt.LeftToRight)
        icon2 = QIcon()
        icon2.addFile(u":/icons/assets/icons/customers_blue.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_accounts.setIcon(icon2)
        self.btn_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_accounts)

        self.btn_roznamcha = QPushButton(self.upper_widget)
        self.btn_roznamcha.setObjectName(u"btn_roznamcha")
        self.btn_roznamcha.setMinimumSize(QSize(200, 40))
        self.btn_roznamcha.setMaximumSize(QSize(200, 40))
        self.btn_roznamcha.setFont(font)
        self.btn_roznamcha.setCursor(QCursor(Qt.OpenHandCursor))
        icon3 = QIcon()
        icon3.addFile(u":/icons/assets/icons/sales.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_roznamcha.setIcon(icon3)
        self.btn_roznamcha.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_roznamcha)

        self.btn_settings = QPushButton(self.upper_widget)
        self.btn_settings.setObjectName(u"btn_settings")
        self.btn_settings.setMinimumSize(QSize(150, 40))
        self.btn_settings.setMaximumSize(QSize(150, 40))
        self.btn_settings.setFont(font)
        self.btn_settings.setCursor(QCursor(Qt.OpenHandCursor))
        icon4 = QIcon()
        icon4.addFile(u":/icons/assets/icons/settings.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_settings.setIcon(icon4)
        self.btn_settings.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_settings)

        self.user_frame = QFrame(self.upper_widget)
        self.user_frame.setObjectName(u"user_frame")
        self.user_frame.setMinimumSize(QSize(300, 30))
        self.user_frame.setMaximumSize(QSize(300, 40))
        self.user_frame.setFrameShape(QFrame.StyledPanel)
        self.user_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_4 = QHBoxLayout(self.user_frame)
        self.horizontalLayout_4.setSpacing(20)
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, 0)
        self.lbl_user_name = QLabel(self.user_frame)
        self.lbl_user_name.setObjectName(u"lbl_user_name")
        font1 = QFont()
        font1.setFamily(u"Calibri")
        font1.setPointSize(18)
        font1.setBold(True)
        font1.setWeight(75)
        self.lbl_user_name.setFont(font1)

        self.horizontalLayout_4.addWidget(self.lbl_user_name)

        self.khata_options = QComboBox(self.user_frame)
        self.khata_options.addItem("")
        self.khata_options.setObjectName(u"khata_options")
        self.khata_options.setMinimumSize(QSize(130, 35))
        self.khata_options.setMaximumSize(QSize(130, 35))
        font2 = QFont()
        font2.setFamily(u"Calibri")
        font2.setPointSize(14)
        self.khata_options.setFont(font2)
        self.khata_options.setCursor(QCursor(Qt.OpenHandCursor))

        self.horizontalLayout_4.addWidget(self.khata_options)

        self.lbl_user_khata = QLabel(self.user_frame)
        self.lbl_user_khata.setObjectName(u"lbl_user_khata")
        font3 = QFont()
        font3.setPointSize(18)
        self.lbl_user_khata.setFont(font3)

        self.horizontalLayout_4.addWidget(self.lbl_user_khata)


        self.horizontalLayout.addWidget(self.user_frame, 0, Qt.AlignRight)

        self.btn_logout = QPushButton(self.upper_widget)
        self.btn_logout.setObjectName(u"btn_logout")
        self.btn_logout.setMinimumSize(QSize(120, 40))
        self.btn_logout.setMaximumSize(QSize(120, 40))
        self.btn_logout.setFont(font)
        self.btn_logout.setCursor(QCursor(Qt.OpenHandCursor))
        icon5 = QIcon()
        icon5.addFile(u":/icons/assets/icons/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_logout.setIcon(icon5)
        self.btn_logout.setIconSize(QSize(32, 32))

        self.horizontalLayout.addWidget(self.btn_logout, 0, Qt.AlignRight)


        self.verticalLayout.addWidget(self.upper_widget)

        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.stackedWidget.setStyleSheet(u"* {\n"
"	background-color: #e1f5fe;\n"
"}")
        self.home_page = QWidget()
        self.home_page.setObjectName(u"home_page")
        self.home_page.setStyleSheet(u"#lbl_home {\n"
"	background-color: #bbdefb;\n"
"}")
        self.verticalLayout_6 = QVBoxLayout(self.home_page)
        self.verticalLayout_6.setSpacing(0)
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(0, 0, 0, 0)
        self.lbl_home = QLabel(self.home_page)
        self.lbl_home.setObjectName(u"lbl_home")
        self.lbl_home.setMinimumSize(QSize(0, 50))
        self.lbl_home.setMaximumSize(QSize(16777215, 50))
        font4 = QFont()
        font4.setFamily(u"Calibri")
        font4.setPointSize(20)
        font4.setBold(True)
        font4.setWeight(75)
        self.lbl_home.setFont(font4)
        self.lbl_home.setAlignment(Qt.AlignCenter)
        self.lbl_home.setMargin(10)

        self.verticalLayout_6.addWidget(self.lbl_home)

        self.business_details_widget = QWidget(self.home_page)
        self.business_details_widget.setObjectName(u"business_details_widget")
        self.verticalLayout_5 = QVBoxLayout(self.business_details_widget)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.b_details_frame = QFrame(self.business_details_widget)
        self.b_details_frame.setObjectName(u"b_details_frame")
        self.b_details_frame.setFrameShape(QFrame.StyledPanel)
        self.b_details_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.b_details_frame)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.lbl_business_name = QLabel(self.b_details_frame)
        self.lbl_business_name.setObjectName(u"lbl_business_name")
        self.lbl_business_name.setFont(font4)
        self.lbl_business_name.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_name, 0, Qt.AlignBottom)

        self.lbl_business_contact = QLabel(self.b_details_frame)
        self.lbl_business_contact.setObjectName(u"lbl_business_contact")
        self.lbl_business_contact.setFont(font1)
        self.lbl_business_contact.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_contact, 0, Qt.AlignBottom)

        self.lbl_business_address = QLabel(self.b_details_frame)
        self.lbl_business_address.setObjectName(u"lbl_business_address")
        self.lbl_business_address.setFont(font1)
        self.lbl_business_address.setAlignment(Qt.AlignCenter)

        self.verticalLayout_4.addWidget(self.lbl_business_address, 0, Qt.AlignTop)


        self.verticalLayout_5.addWidget(self.b_details_frame, 0, Qt.AlignVCenter)


        self.verticalLayout_6.addWidget(self.business_details_widget)

        self.conpany_details_frame = QFrame(self.home_page)
        self.conpany_details_frame.setObjectName(u"conpany_details_frame")
        self.conpany_details_frame.setLayoutDirection(Qt.LeftToRight)
        self.conpany_details_frame.setFrameShape(QFrame.StyledPanel)
        self.conpany_details_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.conpany_details_frame)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.lbl_contact = QLabel(self.conpany_details_frame)
        self.lbl_contact.setObjectName(u"lbl_contact")
        self.lbl_contact.setFont(font)

        self.horizontalLayout_17.addWidget(self.lbl_contact, 0, Qt.AlignLeft)

        self.lbl_description = QLabel(self.conpany_details_frame)
        self.lbl_description.setObjectName(u"lbl_description")
        font5 = QFont()
        font5.setFamily(u"Calibri")
        font5.setPointSize(16)
        self.lbl_description.setFont(font5)

        self.horizontalLayout_17.addWidget(self.lbl_description, 0, Qt.AlignRight)

        self.lbl_company = QLabel(self.conpany_details_frame)
        self.lbl_company.setObjectName(u"lbl_company")
        self.lbl_company.setFont(font)
        self.lbl_company.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_17.addWidget(self.lbl_company)


        self.verticalLayout_6.addWidget(self.conpany_details_frame, 0, Qt.AlignBottom)

        self.stackedWidget.addWidget(self.home_page)
        self.accounts_page = QWidget()
        self.accounts_page.setObjectName(u"accounts_page")
        self.accounts_page.setStyleSheet(u"*{\n"
"	background-color: #e0f2f1;\n"
"}\n"
"\n"
"#lbl_accounts {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#accounts_upper_widget {\n"
"	background-color: #80deea;\n"
"}\n"
"\n"
"#btn_add_accounts {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#select_search_option {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_search {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_search_accounts {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_refresh_accounts {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#lbl_from {\n"
"	background-color: #80deea;\n"
"}\n"
"\n"
"#lbl_to {\n"
"	background-color: #80deea;\n"
"}\n"
"\n"
"#txt_date_from {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_date_to {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_print_accounts {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"#btn_edit_accounts"
                        " {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.verticalLayout_2 = QVBoxLayout(self.accounts_page)
        self.verticalLayout_2.setSpacing(0)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.lbl_accounts = QLabel(self.accounts_page)
        self.lbl_accounts.setObjectName(u"lbl_accounts")
        self.lbl_accounts.setMinimumSize(QSize(0, 50))
        self.lbl_accounts.setMaximumSize(QSize(16777215, 50))
        self.lbl_accounts.setFont(font1)
        self.lbl_accounts.setAlignment(Qt.AlignCenter)
        self.lbl_accounts.setMargin(10)

        self.verticalLayout_2.addWidget(self.lbl_accounts)

        self.accounts_upper_widget = QWidget(self.accounts_page)
        self.accounts_upper_widget.setObjectName(u"accounts_upper_widget")
        self.horizontalLayout_2 = QHBoxLayout(self.accounts_upper_widget)
        self.horizontalLayout_2.setSpacing(5)
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(5, 5, 5, 10)
        self.btn_add_accounts = QPushButton(self.accounts_upper_widget)
        self.btn_add_accounts.setObjectName(u"btn_add_accounts")
        self.btn_add_accounts.setMinimumSize(QSize(180, 40))
        self.btn_add_accounts.setMaximumSize(QSize(180, 40))
        font6 = QFont()
        font6.setFamily(u"Calibri")
        font6.setPointSize(14)
        font6.setBold(True)
        font6.setWeight(75)
        self.btn_add_accounts.setFont(font6)
        self.btn_add_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        icon6 = QIcon()
        icon6.addFile(u":/icons/assets/icons/plus.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_add_accounts.setIcon(icon6)
        self.btn_add_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_add_accounts, 0, Qt.AlignLeft)

        self.select_search_option = QComboBox(self.accounts_upper_widget)
        self.select_search_option.addItem("")
        self.select_search_option.addItem("")
        self.select_search_option.addItem("")
        self.select_search_option.setObjectName(u"select_search_option")
        self.select_search_option.setMinimumSize(QSize(150, 40))
        self.select_search_option.setMaximumSize(QSize(150, 40))
        self.select_search_option.setFont(font2)
        self.select_search_option.setCursor(QCursor(Qt.OpenHandCursor))

        self.horizontalLayout_2.addWidget(self.select_search_option, 0, Qt.AlignLeft)

        self.txt_search = QLineEdit(self.accounts_upper_widget)
        self.txt_search.setObjectName(u"txt_search")
        self.txt_search.setMinimumSize(QSize(300, 40))
        self.txt_search.setMaximumSize(QSize(300, 40))
        self.txt_search.setFont(font2)

        self.horizontalLayout_2.addWidget(self.txt_search, 0, Qt.AlignLeft)

        self.lbl_from = QLabel(self.accounts_upper_widget)
        self.lbl_from.setObjectName(u"lbl_from")
        self.lbl_from.setMinimumSize(QSize(0, 40))
        self.lbl_from.setMaximumSize(QSize(16777215, 40))
        self.lbl_from.setFont(font2)
        self.lbl_from.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_from, 0, Qt.AlignLeft)

        self.txt_date_from = QDateEdit(self.accounts_upper_widget)
        self.txt_date_from.setObjectName(u"txt_date_from")
        self.txt_date_from.setMinimumSize(QSize(130, 40))
        self.txt_date_from.setMaximumSize(QSize(130, 40))
        self.txt_date_from.setFont(font2)
        self.txt_date_from.setCalendarPopup(True)
        self.txt_date_from.setDate(QDate(2022, 12, 15))

        self.horizontalLayout_2.addWidget(self.txt_date_from, 0, Qt.AlignLeft)

        self.lbl_to = QLabel(self.accounts_upper_widget)
        self.lbl_to.setObjectName(u"lbl_to")
        self.lbl_to.setMinimumSize(QSize(0, 40))
        self.lbl_to.setMaximumSize(QSize(16777215, 40))
        self.lbl_to.setFont(font2)
        self.lbl_to.setAlignment(Qt.AlignRight|Qt.AlignTrailing|Qt.AlignVCenter)

        self.horizontalLayout_2.addWidget(self.lbl_to, 0, Qt.AlignLeft)

        self.txt_date_to = QDateEdit(self.accounts_upper_widget)
        self.txt_date_to.setObjectName(u"txt_date_to")
        self.txt_date_to.setMinimumSize(QSize(130, 40))
        self.txt_date_to.setMaximumSize(QSize(130, 40))
        self.txt_date_to.setFont(font2)
        self.txt_date_to.setCalendarPopup(True)
        self.txt_date_to.setDate(QDate(2022, 12, 15))

        self.horizontalLayout_2.addWidget(self.txt_date_to, 0, Qt.AlignLeft)

        self.btn_search_accounts = QPushButton(self.accounts_upper_widget)
        self.btn_search_accounts.setObjectName(u"btn_search_accounts")
        self.btn_search_accounts.setMinimumSize(QSize(50, 40))
        self.btn_search_accounts.setMaximumSize(QSize(50, 40))
        self.btn_search_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        icon7 = QIcon()
        icon7.addFile(u":/icons/assets/icons/search.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_search_accounts.setIcon(icon7)
        self.btn_search_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_search_accounts, 0, Qt.AlignLeft)

        self.btn_edit_accounts = QPushButton(self.accounts_upper_widget)
        self.btn_edit_accounts.setObjectName(u"btn_edit_accounts")
        self.btn_edit_accounts.setMinimumSize(QSize(40, 40))
        self.btn_edit_accounts.setMaximumSize(QSize(40, 40))
        self.btn_edit_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        icon8 = QIcon()
        icon8.addFile(u":/icons/assets/icons/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_edit_accounts.setIcon(icon8)
        self.btn_edit_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_edit_accounts, 0, Qt.AlignRight)

        self.btn_print_accounts = QPushButton(self.accounts_upper_widget)
        self.btn_print_accounts.setObjectName(u"btn_print_accounts")
        self.btn_print_accounts.setMinimumSize(QSize(40, 40))
        self.btn_print_accounts.setMaximumSize(QSize(40, 40))
        self.btn_print_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        icon9 = QIcon()
        icon9.addFile(u":/icons/assets/icons/print.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_print_accounts.setIcon(icon9)
        self.btn_print_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_print_accounts, 0, Qt.AlignRight)

        self.btn_refresh_accounts = QPushButton(self.accounts_upper_widget)
        self.btn_refresh_accounts.setObjectName(u"btn_refresh_accounts")
        self.btn_refresh_accounts.setMinimumSize(QSize(40, 40))
        self.btn_refresh_accounts.setMaximumSize(QSize(40, 40))
        self.btn_refresh_accounts.setCursor(QCursor(Qt.OpenHandCursor))
        icon10 = QIcon()
        icon10.addFile(u":/icons/assets/icons/refresh.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btn_refresh_accounts.setIcon(icon10)
        self.btn_refresh_accounts.setIconSize(QSize(32, 32))

        self.horizontalLayout_2.addWidget(self.btn_refresh_accounts, 0, Qt.AlignRight)


        self.verticalLayout_2.addWidget(self.accounts_upper_widget)

        self.accounts_table = QTableWidget(self.accounts_page)
        if (self.accounts_table.columnCount() < 5):
            self.accounts_table.setColumnCount(5)
        __qtablewidgetitem = QTableWidgetItem()
        __qtablewidgetitem.setFont(font6);
        self.accounts_table.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        __qtablewidgetitem1.setFont(font6);
        self.accounts_table.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        __qtablewidgetitem2.setFont(font6);
        self.accounts_table.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        __qtablewidgetitem3.setFont(font6);
        self.accounts_table.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        __qtablewidgetitem4.setFont(font6);
        self.accounts_table.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        if (self.accounts_table.rowCount() < 20):
            self.accounts_table.setRowCount(20)
        self.accounts_table.setObjectName(u"accounts_table")
        self.accounts_table.setFont(font2)
        self.accounts_table.setFrameShape(QFrame.NoFrame)
        self.accounts_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.accounts_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.accounts_table.setDragDropOverwriteMode(True)
        self.accounts_table.setAlternatingRowColors(False)
        self.accounts_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.accounts_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.accounts_table.setTextElideMode(Qt.ElideRight)
        self.accounts_table.setShowGrid(True)
        self.accounts_table.setGridStyle(Qt.SolidLine)
        self.accounts_table.setSortingEnabled(True)
        self.accounts_table.setCornerButtonEnabled(True)
        self.accounts_table.setRowCount(20)
        self.accounts_table.horizontalHeader().setVisible(True)
        self.accounts_table.horizontalHeader().setCascadingSectionResizes(False)
        self.accounts_table.horizontalHeader().setDefaultSectionSize(150)
        self.accounts_table.horizontalHeader().setHighlightSections(False)
        self.accounts_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.accounts_table.horizontalHeader().setStretchLastSection(False)
        self.accounts_table.verticalHeader().setVisible(True)
        self.accounts_table.verticalHeader().setMinimumSectionSize(30)
        self.accounts_table.verticalHeader().setHighlightSections(True)
        self.accounts_table.verticalHeader().setProperty("showSortIndicator", False)

        self.verticalLayout_2.addWidget(self.accounts_table)

        self.bottom_widget_accounts = QWidget(self.accounts_page)
        self.bottom_widget_accounts.setObjectName(u"bottom_widget_accounts")
        self.verticalLayout_13 = QVBoxLayout(self.bottom_widget_accounts)
        self.verticalLayout_13.setSpacing(1)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_13.setContentsMargins(0, 0, 0, 0)
        self.totals_frame_accounts = QFrame(self.bottom_widget_accounts)
        self.totals_frame_accounts.setObjectName(u"totals_frame_accounts")
        self.totals_frame_accounts.setFrameShape(QFrame.StyledPanel)
        self.totals_frame_accounts.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_10 = QHBoxLayout(self.totals_frame_accounts)
        self.horizontalLayout_10.setSpacing(20)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_2 = QLabel(self.totals_frame_accounts)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)

        self.horizontalLayout_10.addWidget(self.label_2)

        self.label_7 = QLabel(self.totals_frame_accounts)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setPointSize(14)
        self.label_7.setFont(font7)

        self.horizontalLayout_10.addWidget(self.label_7, 0, Qt.AlignRight)

        self.lbl_total_opening = QLabel(self.totals_frame_accounts)
        self.lbl_total_opening.setObjectName(u"lbl_total_opening")
        self.lbl_total_opening.setFont(font)
        self.lbl_total_opening.setFrameShape(QFrame.Box)
        self.lbl_total_opening.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_10.addWidget(self.lbl_total_opening)


        self.verticalLayout_13.addWidget(self.totals_frame_accounts)


        self.verticalLayout_2.addWidget(self.bottom_widget_accounts)

        self.stackedWidget.addWidget(self.accounts_page)
        self.roznamcha_page = QWidget()
        self.roznamcha_page.setObjectName(u"roznamcha_page")
        self.roznamcha_page.setStyleSheet(u"\n"
"*{\n"
"	background-color: #e0f2f1;\n"
"}\n"
"\n"
"#lbl_roznamcha {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"#roznamcha_upper_widget {\n"
"	background-color: #80deea;\n"
"}\n"
"\n"
"#lbl_from_RN {\n"
"	background-color: #80deea;\n"
"}\n"
"#lbl_to_RN {\n"
"	background-color: #80deea;\n"
"}\n"
"\n"
"#btn_add_roznamcha {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#select_search_option_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_search_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_date_from_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#txt_date_to_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"\n"
"#btn_search_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_refresh_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"#btn_print_RN {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"")
        self.verticalLayout_12 = QVBoxLayout(self.roznamcha_page)
        self.verticalLayout_12.setSpacing(0)
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.verticalLayout_12.setContentsMargins(0, 0, 0, 0)
        self.lbl_roznamcha = QLabel(self.roznamcha_page)
        self.lbl_roznamcha.setObjectName(u"lbl_roznamcha")
        self.lbl_roznamcha.setMinimumSize(QSize(0, 50))
        self.lbl_roznamcha.setMaximumSize(QSize(16777215, 50))
        self.lbl_roznamcha.setFont(font1)
        self.lbl_roznamcha.setAlignment(Qt.AlignCenter)
        self.lbl_roznamcha.setMargin(10)

        self.verticalLayout_12.addWidget(self.lbl_roznamcha)

        self.roznamcha_upper_widget = QWidget(self.roznamcha_page)
        self.roznamcha_upper_widget.setObjectName(u"roznamcha_upper_widget")
        self.horizontalLayout_3 = QHBoxLayout(self.roznamcha_upper_widget)
        self.horizontalLayout_3.setSpacing(5)
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.horizontalLayout_3.setContentsMargins(5, 5, 5, 10)
        self.btn_add_roznamcha = QPushButton(self.roznamcha_upper_widget)
        self.btn_add_roznamcha.setObjectName(u"btn_add_roznamcha")
        self.btn_add_roznamcha.setMinimumSize(QSize(180, 40))
        self.btn_add_roznamcha.setMaximumSize(QSize(180, 40))
        self.btn_add_roznamcha.setFont(font6)
        self.btn_add_roznamcha.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_add_roznamcha.setIcon(icon6)
        self.btn_add_roznamcha.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_add_roznamcha, 0, Qt.AlignLeft)

        self.select_search_option_RN = QComboBox(self.roznamcha_upper_widget)
        self.select_search_option_RN.addItem("")
        self.select_search_option_RN.addItem("")
        self.select_search_option_RN.addItem("")
        self.select_search_option_RN.setObjectName(u"select_search_option_RN")
        self.select_search_option_RN.setMinimumSize(QSize(150, 40))
        self.select_search_option_RN.setMaximumSize(QSize(150, 40))
        self.select_search_option_RN.setFont(font2)
        self.select_search_option_RN.setCursor(QCursor(Qt.OpenHandCursor))

        self.horizontalLayout_3.addWidget(self.select_search_option_RN, 0, Qt.AlignLeft)

        self.txt_search_RN = QLineEdit(self.roznamcha_upper_widget)
        self.txt_search_RN.setObjectName(u"txt_search_RN")
        self.txt_search_RN.setMinimumSize(QSize(300, 40))
        self.txt_search_RN.setMaximumSize(QSize(300, 40))
        self.txt_search_RN.setFont(font2)

        self.horizontalLayout_3.addWidget(self.txt_search_RN, 0, Qt.AlignLeft)

        self.lbl_from_RN = QLabel(self.roznamcha_upper_widget)
        self.lbl_from_RN.setObjectName(u"lbl_from_RN")
        self.lbl_from_RN.setMaximumSize(QSize(16777215, 40))
        self.lbl_from_RN.setFont(font2)

        self.horizontalLayout_3.addWidget(self.lbl_from_RN, 0, Qt.AlignLeft)

        self.txt_date_from_RN = QDateEdit(self.roznamcha_upper_widget)
        self.txt_date_from_RN.setObjectName(u"txt_date_from_RN")
        self.txt_date_from_RN.setMinimumSize(QSize(130, 40))
        self.txt_date_from_RN.setMaximumSize(QSize(130, 40))
        font8 = QFont()
        font8.setFamily(u"Calibri")
        font8.setPointSize(14)
        font8.setBold(False)
        font8.setWeight(50)
        self.txt_date_from_RN.setFont(font8)
        self.txt_date_from_RN.setDateTime(QDateTime(QDate(2022, 1, 1), QTime(0, 0, 0)))
        self.txt_date_from_RN.setCurrentSection(QDateTimeEdit.DaySection)
        self.txt_date_from_RN.setCalendarPopup(True)

        self.horizontalLayout_3.addWidget(self.txt_date_from_RN, 0, Qt.AlignLeft)

        self.lbl_to_RN = QLabel(self.roznamcha_upper_widget)
        self.lbl_to_RN.setObjectName(u"lbl_to_RN")
        self.lbl_to_RN.setMaximumSize(QSize(16777215, 40))
        self.lbl_to_RN.setFont(font2)

        self.horizontalLayout_3.addWidget(self.lbl_to_RN, 0, Qt.AlignLeft)

        self.txt_date_to_RN = QDateEdit(self.roznamcha_upper_widget)
        self.txt_date_to_RN.setObjectName(u"txt_date_to_RN")
        self.txt_date_to_RN.setMinimumSize(QSize(130, 40))
        self.txt_date_to_RN.setMaximumSize(QSize(130, 40))
        self.txt_date_to_RN.setFont(font2)
        self.txt_date_to_RN.setCalendarPopup(True)
        self.txt_date_to_RN.setDate(QDate(2022, 12, 15))

        self.horizontalLayout_3.addWidget(self.txt_date_to_RN, 0, Qt.AlignLeft)

        self.btn_search_RN = QPushButton(self.roznamcha_upper_widget)
        self.btn_search_RN.setObjectName(u"btn_search_RN")
        self.btn_search_RN.setMinimumSize(QSize(50, 40))
        self.btn_search_RN.setMaximumSize(QSize(50, 40))
        self.btn_search_RN.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_search_RN.setIcon(icon7)
        self.btn_search_RN.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_search_RN, 0, Qt.AlignLeft)

        self.btn_print_RN = QPushButton(self.roznamcha_upper_widget)
        self.btn_print_RN.setObjectName(u"btn_print_RN")
        self.btn_print_RN.setMinimumSize(QSize(40, 40))
        self.btn_print_RN.setMaximumSize(QSize(40, 40))
        self.btn_print_RN.setIcon(icon9)
        self.btn_print_RN.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_print_RN, 0, Qt.AlignRight)

        self.btn_refresh_RN = QPushButton(self.roznamcha_upper_widget)
        self.btn_refresh_RN.setObjectName(u"btn_refresh_RN")
        self.btn_refresh_RN.setMinimumSize(QSize(50, 40))
        self.btn_refresh_RN.setMaximumSize(QSize(50, 40))
        self.btn_refresh_RN.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_refresh_RN.setIcon(icon10)
        self.btn_refresh_RN.setIconSize(QSize(32, 32))

        self.horizontalLayout_3.addWidget(self.btn_refresh_RN, 0, Qt.AlignRight)


        self.verticalLayout_12.addWidget(self.roznamcha_upper_widget)

        self.roznamcha_table = QTableWidget(self.roznamcha_page)
        if (self.roznamcha_table.columnCount() < 9):
            self.roznamcha_table.setColumnCount(9)
        __qtablewidgetitem5 = QTableWidgetItem()
        __qtablewidgetitem5.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(0, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        __qtablewidgetitem6.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(1, __qtablewidgetitem6)
        __qtablewidgetitem7 = QTableWidgetItem()
        __qtablewidgetitem7.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(2, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        __qtablewidgetitem8.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(3, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        __qtablewidgetitem9.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(4, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        __qtablewidgetitem10.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(5, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        __qtablewidgetitem11.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(6, __qtablewidgetitem11)
        brush = QBrush(QColor(0, 0, 0, 255))
        brush.setStyle(Qt.SolidPattern)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setFont(font6);
        __qtablewidgetitem12.setForeground(brush);
        self.roznamcha_table.setHorizontalHeaderItem(7, __qtablewidgetitem12)
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setFont(font6);
        self.roznamcha_table.setHorizontalHeaderItem(8, __qtablewidgetitem13)
        if (self.roznamcha_table.rowCount() < 19):
            self.roznamcha_table.setRowCount(19)
        __qtablewidgetitem14 = QTableWidgetItem()
        __qtablewidgetitem14.setFlags(Qt.ItemIsSelectable|Qt.ItemIsEnabled);
        self.roznamcha_table.setItem(0, 2, __qtablewidgetitem14)
        self.roznamcha_table.setObjectName(u"roznamcha_table")
        self.roznamcha_table.setMinimumSize(QSize(0, 0))
        self.roznamcha_table.setFont(font2)
        self.roznamcha_table.viewport().setProperty("cursor", QCursor(Qt.OpenHandCursor))
        self.roznamcha_table.setLayoutDirection(Qt.LeftToRight)
        self.roznamcha_table.setAutoFillBackground(False)
        self.roznamcha_table.setFrameShape(QFrame.NoFrame)
        self.roznamcha_table.setMidLineWidth(0)
        self.roznamcha_table.setSizeAdjustPolicy(QAbstractScrollArea.AdjustToContents)
        self.roznamcha_table.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.roznamcha_table.setAlternatingRowColors(False)
        self.roznamcha_table.setSelectionMode(QAbstractItemView.SingleSelection)
        self.roznamcha_table.setSelectionBehavior(QAbstractItemView.SelectRows)
        self.roznamcha_table.setTextElideMode(Qt.ElideLeft)
        self.roznamcha_table.setShowGrid(True)
        self.roznamcha_table.setSortingEnabled(True)
        self.roznamcha_table.setCornerButtonEnabled(True)
        self.roznamcha_table.setRowCount(15)
        self.roznamcha_table.horizontalHeader().setVisible(True)
        self.roznamcha_table.horizontalHeader().setCascadingSectionResizes(False)
        self.roznamcha_table.horizontalHeader().setMinimumSectionSize(30)
        self.roznamcha_table.horizontalHeader().setDefaultSectionSize(138)
        self.roznamcha_table.horizontalHeader().setHighlightSections(False)
        self.roznamcha_table.horizontalHeader().setProperty("showSortIndicator", False)
        self.roznamcha_table.horizontalHeader().setStretchLastSection(False)
        self.roznamcha_table.verticalHeader().setVisible(True)
        self.roznamcha_table.verticalHeader().setCascadingSectionResizes(True)
        self.roznamcha_table.verticalHeader().setMinimumSectionSize(30)
        self.roznamcha_table.verticalHeader().setDefaultSectionSize(30)
        self.roznamcha_table.verticalHeader().setProperty("showSortIndicator", True)
        self.roznamcha_table.verticalHeader().setStretchLastSection(False)

        self.verticalLayout_12.addWidget(self.roznamcha_table)

        self.bottom_widget_RN = QWidget(self.roznamcha_page)
        self.bottom_widget_RN.setObjectName(u"bottom_widget_RN")
        self.verticalLayout_3 = QVBoxLayout(self.bottom_widget_RN)
        self.verticalLayout_3.setSpacing(1)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.totals_frame_RN = QFrame(self.bottom_widget_RN)
        self.totals_frame_RN.setObjectName(u"totals_frame_RN")
        self.totals_frame_RN.setFrameShape(QFrame.StyledPanel)
        self.totals_frame_RN.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_9 = QHBoxLayout(self.totals_frame_RN)
        self.horizontalLayout_9.setSpacing(20)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.label = QLabel(self.totals_frame_RN)
        self.label.setObjectName(u"label")
        self.label.setFont(font)

        self.horizontalLayout_9.addWidget(self.label)

        self.label_6 = QLabel(self.totals_frame_RN)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_6, 0, Qt.AlignRight)

        self.lbl_total_cash_In = QLabel(self.totals_frame_RN)
        self.lbl_total_cash_In.setObjectName(u"lbl_total_cash_In")
        self.lbl_total_cash_In.setFont(font)
        self.lbl_total_cash_In.setFrameShape(QFrame.Box)
        self.lbl_total_cash_In.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.lbl_total_cash_In)

        self.label_5 = QLabel(self.totals_frame_RN)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font7)

        self.horizontalLayout_9.addWidget(self.label_5, 0, Qt.AlignRight)

        self.lbl_total_cash_out = QLabel(self.totals_frame_RN)
        self.lbl_total_cash_out.setObjectName(u"lbl_total_cash_out")
        self.lbl_total_cash_out.setFont(font)
        self.lbl_total_cash_out.setFrameShape(QFrame.Box)
        self.lbl_total_cash_out.setFrameShadow(QFrame.Raised)

        self.horizontalLayout_9.addWidget(self.lbl_total_cash_out)


        self.verticalLayout_3.addWidget(self.totals_frame_RN)


        self.verticalLayout_12.addWidget(self.bottom_widget_RN)

        self.stackedWidget.addWidget(self.roznamcha_page)
        self.settings_page = QWidget()
        self.settings_page.setObjectName(u"settings_page")
        self.settings_page.setStyleSheet(u"\n"
"#lbl_settings {\n"
"	background-color: #bbdefb;\n"
"}\n"
"\n"
"QPushButton {\n"
"	background-color: #fff;\n"
"	border-radius: 5px;\n"
"}\n"
"\n"
"QFrame {\n"
"	background-color: #eceff1;\n"
"}\n"
"\n"
"#create_widget {\n"
"	background-color: #80deea;\n"
"}")
        self.verticalLayout_11 = QVBoxLayout(self.settings_page)
        self.verticalLayout_11.setSpacing(0)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_11.setContentsMargins(0, 0, 0, 0)
        self.lbl_settings = QLabel(self.settings_page)
        self.lbl_settings.setObjectName(u"lbl_settings")
        self.lbl_settings.setMinimumSize(QSize(0, 50))
        self.lbl_settings.setMaximumSize(QSize(16777215, 50))
        self.lbl_settings.setFont(font1)
        self.lbl_settings.setAlignment(Qt.AlignCenter)
        self.lbl_settings.setMargin(0)

        self.verticalLayout_11.addWidget(self.lbl_settings)

        self.create_widget = QWidget(self.settings_page)
        self.create_widget.setObjectName(u"create_widget")
        self.create_widget.setMinimumSize(QSize(0, 0))
        self.create_widget.setMaximumSize(QSize(16777215, 60))
        self.horizontalLayout_8 = QHBoxLayout(self.create_widget)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.btn_business_details = QPushButton(self.create_widget)
        self.btn_business_details.setObjectName(u"btn_business_details")
        self.btn_business_details.setMinimumSize(QSize(300, 40))
        self.btn_business_details.setMaximumSize(QSize(300, 40))
        self.btn_business_details.setFont(font1)
        self.btn_business_details.setIcon(icon6)
        self.btn_business_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_business_details, 0, Qt.AlignLeft)

        self.btn_add_khata = QPushButton(self.create_widget)
        self.btn_add_khata.setObjectName(u"btn_add_khata")
        self.btn_add_khata.setMinimumSize(QSize(150, 40))
        self.btn_add_khata.setMaximumSize(QSize(150, 40))
        self.btn_add_khata.setFont(font6)
        self.btn_add_khata.setIcon(icon6)
        self.btn_add_khata.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_add_khata, 0, Qt.AlignLeft)

        self.btn_change_business_details = QPushButton(self.create_widget)
        self.btn_change_business_details.setObjectName(u"btn_change_business_details")
        self.btn_change_business_details.setMinimumSize(QSize(300, 40))
        self.btn_change_business_details.setMaximumSize(QSize(300, 40))
        self.btn_change_business_details.setFont(font6)
        self.btn_change_business_details.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_business_details.setIcon(icon8)
        self.btn_change_business_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_business_details)

        self.btn_change_user_details = QPushButton(self.create_widget)
        self.btn_change_user_details.setObjectName(u"btn_change_user_details")
        self.btn_change_user_details.setMinimumSize(QSize(250, 40))
        self.btn_change_user_details.setMaximumSize(QSize(250, 40))
        self.btn_change_user_details.setFont(font6)
        self.btn_change_user_details.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_user_details.setIcon(icon8)
        self.btn_change_user_details.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_user_details)

        self.btn_change_pwd = QPushButton(self.create_widget)
        self.btn_change_pwd.setObjectName(u"btn_change_pwd")
        self.btn_change_pwd.setMinimumSize(QSize(200, 40))
        self.btn_change_pwd.setMaximumSize(QSize(200, 40))
        self.btn_change_pwd.setFont(font6)
        self.btn_change_pwd.setCursor(QCursor(Qt.OpenHandCursor))
        self.btn_change_pwd.setIcon(icon8)
        self.btn_change_pwd.setIconSize(QSize(32, 32))

        self.horizontalLayout_8.addWidget(self.btn_change_pwd)


        self.verticalLayout_11.addWidget(self.create_widget)

        self.details_widget = QWidget(self.settings_page)
        self.details_widget.setObjectName(u"details_widget")
        self.details_widget.setMinimumSize(QSize(0, 0))
        self.details_widget.setMaximumSize(QSize(16777215, 200))
        self.horizontalLayout_7 = QHBoxLayout(self.details_widget)
        self.horizontalLayout_7.setSpacing(70)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.business_frame = QFrame(self.details_widget)
        self.business_frame.setObjectName(u"business_frame")
        self.business_frame.setCursor(QCursor(Qt.OpenHandCursor))
        self.business_frame.setFrameShape(QFrame.StyledPanel)
        self.business_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_6 = QHBoxLayout(self.business_frame)
        self.horizontalLayout_6.setSpacing(0)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.b_lbl_frame = QFrame(self.business_frame)
        self.b_lbl_frame.setObjectName(u"b_lbl_frame")
        self.b_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.b_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.b_lbl_frame)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.lbl_b_name = QLabel(self.b_lbl_frame)
        self.lbl_b_name.setObjectName(u"lbl_b_name")
        self.lbl_b_name.setFont(font2)

        self.verticalLayout_9.addWidget(self.lbl_b_name)

        self.lbl_b_email = QLabel(self.b_lbl_frame)
        self.lbl_b_email.setObjectName(u"lbl_b_email")
        self.lbl_b_email.setFont(font2)

        self.verticalLayout_9.addWidget(self.lbl_b_email)

        self.lbl_b_contact = QLabel(self.b_lbl_frame)
        self.lbl_b_contact.setObjectName(u"lbl_b_contact")
        self.lbl_b_contact.setFont(font2)

        self.verticalLayout_9.addWidget(self.lbl_b_contact)

        self.lbl_b_address = QLabel(self.b_lbl_frame)
        self.lbl_b_address.setObjectName(u"lbl_b_address")
        self.lbl_b_address.setFont(font2)

        self.verticalLayout_9.addWidget(self.lbl_b_address)

        self.lbl_b_owner = QLabel(self.b_lbl_frame)
        self.lbl_b_owner.setObjectName(u"lbl_b_owner")
        self.lbl_b_owner.setFont(font2)

        self.verticalLayout_9.addWidget(self.lbl_b_owner)


        self.horizontalLayout_6.addWidget(self.b_lbl_frame)

        self.b_inputs_frame = QFrame(self.business_frame)
        self.b_inputs_frame.setObjectName(u"b_inputs_frame")
        self.b_inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.b_inputs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_10 = QVBoxLayout(self.b_inputs_frame)
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.txt_business_name = QLabel(self.b_inputs_frame)
        self.txt_business_name.setObjectName(u"txt_business_name")
        self.txt_business_name.setFont(font6)

        self.verticalLayout_10.addWidget(self.txt_business_name)

        self.txt_business_email = QLabel(self.b_inputs_frame)
        self.txt_business_email.setObjectName(u"txt_business_email")
        self.txt_business_email.setFont(font6)

        self.verticalLayout_10.addWidget(self.txt_business_email)

        self.txt_business_contact = QLabel(self.b_inputs_frame)
        self.txt_business_contact.setObjectName(u"txt_business_contact")
        self.txt_business_contact.setFont(font6)

        self.verticalLayout_10.addWidget(self.txt_business_contact)

        self.txt_business_address = QLabel(self.b_inputs_frame)
        self.txt_business_address.setObjectName(u"txt_business_address")
        self.txt_business_address.setFont(font6)

        self.verticalLayout_10.addWidget(self.txt_business_address)

        self.txt_business_owner = QLabel(self.b_inputs_frame)
        self.txt_business_owner.setObjectName(u"txt_business_owner")
        self.txt_business_owner.setFont(font6)

        self.verticalLayout_10.addWidget(self.txt_business_owner)


        self.horizontalLayout_6.addWidget(self.b_inputs_frame)


        self.horizontalLayout_7.addWidget(self.business_frame)

        self.user_detail_frame = QFrame(self.details_widget)
        self.user_detail_frame.setObjectName(u"user_detail_frame")
        self.user_detail_frame.setFrameShape(QFrame.StyledPanel)
        self.user_detail_frame.setFrameShadow(QFrame.Raised)
        self.horizontalLayout_5 = QHBoxLayout(self.user_detail_frame)
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.u_lbl_frame = QFrame(self.user_detail_frame)
        self.u_lbl_frame.setObjectName(u"u_lbl_frame")
        self.u_lbl_frame.setFrameShape(QFrame.StyledPanel)
        self.u_lbl_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.u_lbl_frame)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.lbl_u_name = QLabel(self.u_lbl_frame)
        self.lbl_u_name.setObjectName(u"lbl_u_name")
        self.lbl_u_name.setFont(font2)

        self.verticalLayout_8.addWidget(self.lbl_u_name)

        self.lbl_u_email = QLabel(self.u_lbl_frame)
        self.lbl_u_email.setObjectName(u"lbl_u_email")
        self.lbl_u_email.setFont(font2)

        self.verticalLayout_8.addWidget(self.lbl_u_email)

        self.lbl_u_contact = QLabel(self.u_lbl_frame)
        self.lbl_u_contact.setObjectName(u"lbl_u_contact")
        self.lbl_u_contact.setFont(font2)

        self.verticalLayout_8.addWidget(self.lbl_u_contact)

        self.lbl_u_username = QLabel(self.u_lbl_frame)
        self.lbl_u_username.setObjectName(u"lbl_u_username")
        self.lbl_u_username.setFont(font2)

        self.verticalLayout_8.addWidget(self.lbl_u_username)


        self.horizontalLayout_5.addWidget(self.u_lbl_frame)

        self.u_inputs_frame = QFrame(self.user_detail_frame)
        self.u_inputs_frame.setObjectName(u"u_inputs_frame")
        self.u_inputs_frame.setFrameShape(QFrame.StyledPanel)
        self.u_inputs_frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_7 = QVBoxLayout(self.u_inputs_frame)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.txt_user_name = QLabel(self.u_inputs_frame)
        self.txt_user_name.setObjectName(u"txt_user_name")
        self.txt_user_name.setFont(font6)

        self.verticalLayout_7.addWidget(self.txt_user_name)

        self.txt_user_email = QLabel(self.u_inputs_frame)
        self.txt_user_email.setObjectName(u"txt_user_email")
        self.txt_user_email.setFont(font6)

        self.verticalLayout_7.addWidget(self.txt_user_email)

        self.txt_user_contact = QLabel(self.u_inputs_frame)
        self.txt_user_contact.setObjectName(u"txt_user_contact")
        self.txt_user_contact.setFont(font6)

        self.verticalLayout_7.addWidget(self.txt_user_contact)

        self.txt_user_username = QLabel(self.u_inputs_frame)
        self.txt_user_username.setObjectName(u"txt_user_username")
        self.txt_user_username.setFont(font6)

        self.verticalLayout_7.addWidget(self.txt_user_username)


        self.horizontalLayout_5.addWidget(self.u_inputs_frame)


        self.horizontalLayout_7.addWidget(self.user_detail_frame)


        self.verticalLayout_11.addWidget(self.details_widget)

        self.widget_2 = QWidget(self.settings_page)
        self.widget_2.setObjectName(u"widget_2")

        self.verticalLayout_11.addWidget(self.widget_2)

        self.stackedWidget.addWidget(self.settings_page)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"SAM Digital Khata", None))
        self.btn_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.btn_accounts.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.btn_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Roz Namcha", None))
        self.btn_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.lbl_user_name.setText(QCoreApplication.translate("MainWindow", u"User", None))
        self.khata_options.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Khata", None))

        self.lbl_user_khata.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.btn_logout.setText(QCoreApplication.translate("MainWindow", u"Logout", None))
        self.lbl_home.setText(QCoreApplication.translate("MainWindow", u"Home", None))
        self.lbl_business_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.lbl_business_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.lbl_business_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.lbl_contact.setText(QCoreApplication.translate("MainWindow", u"+92 335 2321360", None))
        self.lbl_description.setText(QCoreApplication.translate("MainWindow", u"Software Developed By:", None))
        self.lbl_company.setText(QCoreApplication.translate("MainWindow", u"SAM and SHAMI Coding Hub", None))
        self.lbl_accounts.setText(QCoreApplication.translate("MainWindow", u"Accounts", None))
        self.btn_add_accounts.setText(QCoreApplication.translate("MainWindow", u"Add Accounts", None))
        self.select_search_option.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Option", None))
        self.select_search_option.setItemText(1, QCoreApplication.translate("MainWindow", u"By Name", None))
        self.select_search_option.setItemText(2, QCoreApplication.translate("MainWindow", u"By Contact", None))

        self.lbl_from.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lbl_to.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_search_accounts.setText("")
        self.btn_edit_accounts.setText("")
        self.btn_print_accounts.setText("")
        self.btn_refresh_accounts.setText("")
        ___qtablewidgetitem = self.accounts_table.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"S No.", None));
        ___qtablewidgetitem1 = self.accounts_table.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem2 = self.accounts_table.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Mobile", None));
        ___qtablewidgetitem3 = self.accounts_table.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Address", None));
        ___qtablewidgetitem4 = self.accounts_table.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Opening Balance", None));
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Opening Balance", None))
        self.lbl_total_opening.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Roz Namcha", None))
        self.btn_add_roznamcha.setText(QCoreApplication.translate("MainWindow", u"Add RozNamcha", None))
        self.select_search_option_RN.setItemText(0, QCoreApplication.translate("MainWindow", u"Select Option", None))
        self.select_search_option_RN.setItemText(1, QCoreApplication.translate("MainWindow", u"By Name", None))
        self.select_search_option_RN.setItemText(2, QCoreApplication.translate("MainWindow", u"By Contact", None))

        self.lbl_from_RN.setText(QCoreApplication.translate("MainWindow", u"From", None))
        self.lbl_to_RN.setText(QCoreApplication.translate("MainWindow", u"To", None))
        self.btn_search_RN.setText("")
        self.btn_print_RN.setText("")
        self.btn_refresh_RN.setText("")
        ___qtablewidgetitem5 = self.roznamcha_table.horizontalHeaderItem(0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"S No.", None));
        ___qtablewidgetitem6 = self.roznamcha_table.horizontalHeaderItem(1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Date", None));
        ___qtablewidgetitem7 = self.roznamcha_table.horizontalHeaderItem(2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"Cash In / Out", None));
        ___qtablewidgetitem8 = self.roznamcha_table.horizontalHeaderItem(3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"Name", None));
        ___qtablewidgetitem9 = self.roznamcha_table.horizontalHeaderItem(4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"Reference", None));
        ___qtablewidgetitem10 = self.roznamcha_table.horizontalHeaderItem(5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Description", None));
        ___qtablewidgetitem11 = self.roznamcha_table.horizontalHeaderItem(6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Cash In Amount", None));
        ___qtablewidgetitem12 = self.roznamcha_table.horizontalHeaderItem(7)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"Cash Out Amount", None));
        ___qtablewidgetitem13 = self.roznamcha_table.horizontalHeaderItem(8)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Remaining", None));

        __sortingEnabled = self.roznamcha_table.isSortingEnabled()
        self.roznamcha_table.setSortingEnabled(False)
        self.roznamcha_table.setSortingEnabled(__sortingEnabled)

        self.label.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Cash In Amount", None))
        self.lbl_total_cash_In.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Cash Out Amount", None))
        self.lbl_total_cash_out.setText(QCoreApplication.translate("MainWindow", u"00", None))
        self.lbl_settings.setText(QCoreApplication.translate("MainWindow", u"Settings", None))
        self.btn_business_details.setText(QCoreApplication.translate("MainWindow", u"Business Details", None))
        self.btn_add_khata.setText(QCoreApplication.translate("MainWindow", u"Add Khata", None))
        self.btn_change_business_details.setText(QCoreApplication.translate("MainWindow", u"Change Business Details", None))
        self.btn_change_user_details.setText(QCoreApplication.translate("MainWindow", u"Change User Deatils", None))
        self.btn_change_pwd.setText(QCoreApplication.translate("MainWindow", u"Change Password", None))
        self.lbl_b_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.lbl_b_email.setText(QCoreApplication.translate("MainWindow", u"Business Email", None))
        self.lbl_b_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.lbl_b_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.lbl_b_owner.setText(QCoreApplication.translate("MainWindow", u"Business Owner", None))
        self.txt_business_name.setText(QCoreApplication.translate("MainWindow", u"Business Name", None))
        self.txt_business_email.setText(QCoreApplication.translate("MainWindow", u"Business Email", None))
        self.txt_business_contact.setText(QCoreApplication.translate("MainWindow", u"Business Contact", None))
        self.txt_business_address.setText(QCoreApplication.translate("MainWindow", u"Business Address", None))
        self.txt_business_owner.setText(QCoreApplication.translate("MainWindow", u"Business Owner", None))
        self.lbl_u_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.lbl_u_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.lbl_u_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.lbl_u_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
        self.txt_user_name.setText(QCoreApplication.translate("MainWindow", u"Name", None))
        self.txt_user_email.setText(QCoreApplication.translate("MainWindow", u"Email", None))
        self.txt_user_contact.setText(QCoreApplication.translate("MainWindow", u"Contact", None))
        self.txt_user_username.setText(QCoreApplication.translate("MainWindow", u"Username", None))
    # retranslateUi

