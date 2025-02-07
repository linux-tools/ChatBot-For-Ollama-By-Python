# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Search_For_LLMs.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
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
from PySide6.QtWebEngineWidgets import QWebEngineView
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_DialogForSearchLLMs(object):
    def setupUi(self, DialogForSearchLLMs):
        if not DialogForSearchLLMs.objectName():
            DialogForSearchLLMs.setObjectName(u"DialogForSearchLLMs")
        DialogForSearchLLMs.resize(992, 448)
        self.pushButton = QPushButton(DialogForSearchLLMs)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 420, 75, 24))
        self.pushButton_2 = QPushButton(DialogForSearchLLMs)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(90, 420, 75, 24))
        self.lineEdit = QLineEdit(DialogForSearchLLMs)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 390, 971, 20))
        self.label = QLabel(DialogForSearchLLMs)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 54, 16))
        self.label_2 = QLabel(DialogForSearchLLMs)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 370, 151, 16))
        self.webEngineView = QWebEngineView(DialogForSearchLLMs)
        self.webEngineView.setObjectName(u"webEngineView")
        self.webEngineView.setGeometry(QRect(10, 30, 971, 341))
        self.webEngineView.setUrl(QUrl(u"about:blank"))
        self.label_3 = QLabel(DialogForSearchLLMs)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(420, 10, 121, 16))

        self.retranslateUi(DialogForSearchLLMs)

        QMetaObject.connectSlotsByName(DialogForSearchLLMs)
    # setupUi

    def retranslateUi(self, DialogForSearchLLMs):
        DialogForSearchLLMs.setWindowTitle(QCoreApplication.translate("DialogForSearchLLMs", u"搜索", None))
        self.pushButton.setText(QCoreApplication.translate("DialogForSearchLLMs", u"\u4e0b\u8f7d", None))
        self.pushButton_2.setText(QCoreApplication.translate("DialogForSearchLLMs", u"\u53d6\u6d88", None))
        self.label.setText(QCoreApplication.translate("DialogForSearchLLMs", u"\u4e0b\u8f7d\u72b6\u6001", None))
        self.label_2.setText(QCoreApplication.translate("DialogForSearchLLMs", u"\u8f93\u5165\u4f60\u8981\u4e0b\u8f7d\u7684\u5927\u6a21\u578b\u540d\u79f0", None))
        self.label_3.setText(QCoreApplication.translate("DialogForSearchLLMs", u"\u6d4f\u89c8\u5927\u8bed\u8a00\u6a21\u578b\u754c\u9762", None))
    # retranslateUi

