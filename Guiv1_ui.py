# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Guiv1.ui'
##
## Created by: Qt User Interface Compiler version 6.5.0
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QComboBox, QDialog, QHBoxLayout,
    QHeaderView, QLabel, QLineEdit, QListWidget,
    QListWidgetItem, QPushButton, QSizePolicy, QTableWidget,
    QTableWidgetItem, QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(1027, 669)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(240, 130, 71, 31))
        font = QFont()
        font.setPointSize(11)
        self.pushButton_2.setFont(font)
        icon = QIcon()
        icon.addFile(u"res/2.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.pushButton_2.setIconSize(QSize(20, 20))
        self.listWidget = QListWidget(Dialog)
        self.listWidget.setObjectName(u"listWidget")
        self.listWidget.setGeometry(QRect(320, 30, 351, 131))
        self.comboBox_2 = QComboBox(Dialog)
        self.comboBox_2.setObjectName(u"comboBox_2")
        self.comboBox_2.setGeometry(QRect(400, 0, 181, 21))
        self.reloadingButton = QPushButton(Dialog)
        self.reloadingButton.setObjectName(u"reloadingButton")
        self.reloadingButton.setGeometry(QRect(590, 0, 81, 21))
        icon1 = QIcon()
        icon1.addFile(u"res/4.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.reloadingButton.setIcon(icon1)
        self.reloadingButton.setAutoRepeatDelay(300)
        self.label_5 = QLabel(Dialog)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(320, 0, 71, 21))
        self.layoutWidget = QWidget(Dialog)
        self.layoutWidget.setObjectName(u"layoutWidget")
        self.layoutWidget.setGeometry(QRect(20, 10, 289, 86))
        self.verticalLayout_2 = QVBoxLayout(self.layoutWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.layoutWidget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.layoutWidget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.layoutWidget)
        self.pushButton.setObjectName(u"pushButton")
        icon2 = QIcon()
        icon2.addFile(u"res/3.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon2)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.layoutWidget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.layoutWidget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.layoutWidget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.layoutWidget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)

        self.dumpfilename = QLabel(Dialog)
        self.dumpfilename.setObjectName(u"dumpfilename")
        self.dumpfilename.setGeometry(QRect(20, 100, 291, 21))
        self.dumpfilename.setLineWidth(2)
        self.pushButton_3 = QPushButton(Dialog)
        self.pushButton_3.setObjectName(u"pushButton_3")
        self.pushButton_3.setGeometry(QRect(90, 130, 141, 31))
        self.pushButton_3.setFont(font)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(20, 20))
        self.tableWidget = QTableWidget(Dialog)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setGeometry(QRect(10, 170, 1011, 491))
        self.layoutWidget1 = QWidget(Dialog)
        self.layoutWidget1.setObjectName(u"layoutWidget1")
        self.layoutWidget1.setGeometry(QRect(680, 0, 259, 172))
        self.horizontalLayout = QHBoxLayout(self.layoutWidget1)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.pushButton_4 = QPushButton(self.layoutWidget1)
        self.pushButton_4.setObjectName(u"pushButton_4")

        self.verticalLayout.addWidget(self.pushButton_4)

        self.pushButton_5 = QPushButton(self.layoutWidget1)
        self.pushButton_5.setObjectName(u"pushButton_5")

        self.verticalLayout.addWidget(self.pushButton_5)

        self.pushButton_6 = QPushButton(self.layoutWidget1)
        self.pushButton_6.setObjectName(u"pushButton_6")

        self.verticalLayout.addWidget(self.pushButton_6)

        self.pushButton_7 = QPushButton(self.layoutWidget1)
        self.pushButton_7.setObjectName(u"pushButton_7")

        self.verticalLayout.addWidget(self.pushButton_7)

        self.pushButton_8 = QPushButton(self.layoutWidget1)
        self.pushButton_8.setObjectName(u"pushButton_8")

        self.verticalLayout.addWidget(self.pushButton_8)

        self.pushButton_9 = QPushButton(self.layoutWidget1)
        self.pushButton_9.setObjectName(u"pushButton_9")

        self.verticalLayout.addWidget(self.pushButton_9)


        self.horizontalLayout.addLayout(self.verticalLayout)

        self.verticalLayout_3 = QVBoxLayout()
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.pushButton_10 = QPushButton(self.layoutWidget1)
        self.pushButton_10.setObjectName(u"pushButton_10")

        self.verticalLayout_3.addWidget(self.pushButton_10)

        self.pushButton_11 = QPushButton(self.layoutWidget1)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.verticalLayout_3.addWidget(self.pushButton_11)

        self.pushButton_12 = QPushButton(self.layoutWidget1)
        self.pushButton_12.setObjectName(u"pushButton_12")

        self.verticalLayout_3.addWidget(self.pushButton_12)

        self.pushButton_13 = QPushButton(self.layoutWidget1)
        self.pushButton_13.setObjectName(u"pushButton_13")

        self.verticalLayout_3.addWidget(self.pushButton_13)

        self.pushButton_14 = QPushButton(self.layoutWidget1)
        self.pushButton_14.setObjectName(u"pushButton_14")

        self.verticalLayout_3.addWidget(self.pushButton_14)

        self.pushButton_15 = QPushButton(self.layoutWidget1)
        self.pushButton_15.setObjectName(u"pushButton_15")

        self.verticalLayout_3.addWidget(self.pushButton_15)


        self.horizontalLayout.addLayout(self.verticalLayout_3)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.pushButton_16 = QPushButton(self.layoutWidget1)
        self.pushButton_16.setObjectName(u"pushButton_16")

        self.verticalLayout_4.addWidget(self.pushButton_16)

        self.pushButton_17 = QPushButton(self.layoutWidget1)
        self.pushButton_17.setObjectName(u"pushButton_17")

        self.verticalLayout_4.addWidget(self.pushButton_17)

        self.pushButton_18 = QPushButton(self.layoutWidget1)
        self.pushButton_18.setObjectName(u"pushButton_18")

        self.verticalLayout_4.addWidget(self.pushButton_18)

        self.pushButton_19 = QPushButton(self.layoutWidget1)
        self.pushButton_19.setObjectName(u"pushButton_19")

        self.verticalLayout_4.addWidget(self.pushButton_19)

        self.pushButton_20 = QPushButton(self.layoutWidget1)
        self.pushButton_20.setObjectName(u"pushButton_20")

        self.verticalLayout_4.addWidget(self.pushButton_20)

        self.pushButton_21 = QPushButton(self.layoutWidget1)
        self.pushButton_21.setObjectName(u"pushButton_21")

        self.verticalLayout_4.addWidget(self.pushButton_21)


        self.horizontalLayout.addLayout(self.verticalLayout_4)

        self.pushButton_22 = QPushButton(Dialog)
        self.pushButton_22.setObjectName(u"pushButton_22")
        self.pushButton_22.setGeometry(QRect(940, 0, 78, 23))

        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u6267\u884c", None))
        self.reloadingButton.setText(QCoreApplication.translate("Dialog", u"\u91cd\u65b0\u52a0\u8f7d", None))
        self.label_5.setText(QCoreApplication.translate("Dialog", u"filescan\u6587\u4ef6", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"\u955c\u50cf\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Profile(\u955c\u50cf\u7cfb\u7edf\u7248\u672c)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"dumpfiles\u5185\u5b58\u5730\u5740", None))
        self.dumpfilename.setText("")
        self.pushButton_3.setText(QCoreApplication.translate("Dialog", u"\u65e0Profile\u6267\u884c", None))
        self.pushButton_4.setText(QCoreApplication.translate("Dialog", u"pslist", None))
        self.pushButton_5.setText(QCoreApplication.translate("Dialog", u"atoms", None))
        self.pushButton_6.setText(QCoreApplication.translate("Dialog", u"atomscan", None))
        self.pushButton_7.setText(QCoreApplication.translate("Dialog", u"drivermodule", None))
        self.pushButton_8.setText(QCoreApplication.translate("Dialog", u"driverscan", None))
        self.pushButton_9.setText(QCoreApplication.translate("Dialog", u"envars", None))
        self.pushButton_10.setText(QCoreApplication.translate("Dialog", u"gditimers", None))
        self.pushButton_11.setText(QCoreApplication.translate("Dialog", u"hivelist", None))
        self.pushButton_12.setText(QCoreApplication.translate("Dialog", u"joblinks", None))
        self.pushButton_13.setText(QCoreApplication.translate("Dialog", u"ldrmodules", None))
        self.pushButton_14.setText(QCoreApplication.translate("Dialog", u"modscan", None))
        self.pushButton_15.setText(QCoreApplication.translate("Dialog", u"modules", None))
        self.pushButton_16.setText(QCoreApplication.translate("Dialog", u"netscan", None))
        self.pushButton_17.setText(QCoreApplication.translate("Dialog", u"objtypescan", None))
        self.pushButton_18.setText(QCoreApplication.translate("Dialog", u"psscan", None))
        self.pushButton_19.setText(QCoreApplication.translate("Dialog", u"psxview", None))
        self.pushButton_20.setText(QCoreApplication.translate("Dialog", u"shimcache", None))
        self.pushButton_21.setText(QCoreApplication.translate("Dialog", u"callbacks", None))
        self.pushButton_22.setText(QCoreApplication.translate("Dialog", u"cmdline", None))
    # retranslateUi

