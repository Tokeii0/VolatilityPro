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
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QVBoxLayout, QWidget)

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(314, 159)
        self.pushButton_2 = QPushButton(Dialog)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(220, 120, 71, 21))
        icon = QIcon()
        icon.addFile(u"res/2.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton_2.setIcon(icon)
        self.label_4 = QLabel(Dialog)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 10, 61, 16))
        self.runpath = QLabel(Dialog)
        self.runpath.setObjectName(u"runpath")
        self.runpath.setGeometry(QRect(80, 10, 211, 16))
        self.widget = QWidget(Dialog)
        self.widget.setObjectName(u"widget")
        self.widget.setGeometry(QRect(20, 30, 272, 86))
        self.verticalLayout_2 = QVBoxLayout(self.widget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label = QLabel(self.widget)
        self.label.setObjectName(u"label")

        self.horizontalLayout_4.addWidget(self.label)

        self.lineEdit = QLineEdit(self.widget)
        self.lineEdit.setObjectName(u"lineEdit")

        self.horizontalLayout_4.addWidget(self.lineEdit)

        self.pushButton = QPushButton(self.widget)
        self.pushButton.setObjectName(u"pushButton")
        icon1 = QIcon()
        icon1.addFile(u"res/3.gif", QSize(), QIcon.Normal, QIcon.Off)
        self.pushButton.setIcon(icon1)

        self.horizontalLayout_4.addWidget(self.pushButton)


        self.verticalLayout_2.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.label_2 = QLabel(self.widget)
        self.label_2.setObjectName(u"label_2")

        self.horizontalLayout_2.addWidget(self.label_2)

        self.comboBox = QComboBox(self.widget)
        self.comboBox.setObjectName(u"comboBox")

        self.horizontalLayout_2.addWidget(self.comboBox)


        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_3 = QLabel(self.widget)
        self.label_3.setObjectName(u"label_3")

        self.horizontalLayout_3.addWidget(self.label_3)

        self.lineEdit_2 = QLineEdit(self.widget)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setEnabled(True)

        self.horizontalLayout_3.addWidget(self.lineEdit_2)


        self.verticalLayout_2.addLayout(self.horizontalLayout_3)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.pushButton_2.setText(QCoreApplication.translate("Dialog", u"\u6267\u884c", None))
        self.label_4.setText(QCoreApplication.translate("Dialog", u"\u5de5\u4f5c\u76ee\u5f55", None))
        self.runpath.setText("")
        self.label.setText(QCoreApplication.translate("Dialog", u"\u955c\u50cf\u6587\u4ef6", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"\u6d4f\u89c8", None))
        self.label_2.setText(QCoreApplication.translate("Dialog", u"Profile(\u955c\u50cf\u7cfb\u7edf\u7248\u672c)", None))
        self.label_3.setText(QCoreApplication.translate("Dialog", u"dumpfiles\u5185\u5b58\u5730\u5740", None))
    # retranslateUi

