from PyQt5 import QtCore, QtGui, QtWidgets
from PySide2 import QtCore, QtGui, QtWidgets
from PySide2.QtCore import (QCoreApplication, QPropertyAnimation, QDate, QDateTime,
                            QMetaObject, QObject, QPoint, QRect, QSize, QTime, QUrl, Qt, QEvent)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont, QFontDatabase,
                           QIcon, QKeySequence, QLinearGradient, QPalette, QPainter, QPixmap, QRadialGradient)
from PySide2.QtWidgets import *


class Ui_KhataWindow(object):
    def setupUi(self, KhataWindow):
        KhataWindow.setObjectName("KhataWindow")
        KhataWindow.resize(500, 300)
        KhataWindow.setMinimumSize(QtCore.QSize(500, 300))
        KhataWindow.setMaximumSize(QtCore.QSize(500, 300))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/icons/assets/icons/logo.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        KhataWindow.setWindowIcon(icon)
        KhataWindow.setIconSize(QtCore.QSize(32, 32))
        self.centralwidget = QtWidgets.QWidget(KhataWindow)
        self.centralwidget.setStyleSheet("\n"
"\n"
"#label {\n"
"    background-color: #80cbc4;\n"
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
"#btn_create_business {\n"
"    background-color: #4dd0e1;\n"
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
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setSpacing(0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.label = QtWidgets.QLabel(self.centralwidget)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(18)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.verticalLayout_3.addWidget(self.label, 0, QtCore.Qt.AlignTop)
        self.widget = QtWidgets.QWidget(self.centralwidget)
        self.widget.setObjectName("widget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.frame = QtWidgets.QFrame(self.widget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.lbl_username = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.lbl_username.setFont(font)
        self.lbl_username.setObjectName("lbl_username")
        self.verticalLayout_2.addWidget(self.lbl_username)
        self.horizontalLayout.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.widget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.frame_2)
        self.verticalLayout.setObjectName("verticalLayout")
        self.txt_username = QtWidgets.QLineEdit(self.frame_2)
        self.txt_username.setMinimumSize(QtCore.QSize(0, 35))
        self.txt_username.setMaximumSize(QtCore.QSize(16777215, 35))
        font = QtGui.QFont()
        font.setFamily("Calibri")
        font.setPointSize(14)
        self.txt_username.setFont(font)
        self.txt_username.setObjectName("txt_username")
        self.verticalLayout.addWidget(self.txt_username)
        self.horizontalLayout.addWidget(self.frame_2)
        self.verticalLayout_3.addWidget(self.widget)
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
        self.btn_save.setCursor(QtGui.QCursor(QtCore.Qt.OpenHandCursor))
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
        self.verticalLayout_3.addWidget(self.bottom_widget)
        KhataWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(KhataWindow)
        self.statusbar.setObjectName("statusbar")
        KhataWindow.setStatusBar(self.statusbar)

        self.retranslateUi(KhataWindow)
        QtCore.QMetaObject.connectSlotsByName(KhataWindow)

    def retranslateUi(self, KhataWindow):
        _translate = QtCore.QCoreApplication.translate
        KhataWindow.setWindowTitle(_translate("KhataWindow", "Khata"))
        self.label.setText(_translate("KhataWindow", "Khata"))
        self.lbl_username.setText(_translate("KhataWindow", "Khata Name"))
        self.btn_save.setText(_translate("KhataWindow", "Save"))
        self.btn_clear.setText(_translate("KhataWindow", "CLEAR"))
        self.btn_cancel.setText(_translate("KhataWindow", "CANCEL"))
import resources_rc


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    KhataWindow = QtWidgets.QMainWindow()
    ui = Ui_KhataWindow()
    ui.setupUi(KhataWindow)
    KhataWindow.show()
    sys.exit(app.exec_())
