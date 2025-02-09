# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'RemoveLLMs.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QTextBrowser, QWidget)

class Ui_DialogForRemoveLLMs(object):
    def setupUi(self, DialogForRemoveLLMs):
        if not DialogForRemoveLLMs.objectName():
            DialogForRemoveLLMs.setObjectName(u"DialogForRemoveLLMs")
        DialogForRemoveLLMs.resize(761, 319)
        self.label = QLabel(DialogForRemoveLLMs)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 81, 16))
        self.label_2 = QLabel(DialogForRemoveLLMs)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(10, 240, 181, 16))
        self.lineEdit = QLineEdit(DialogForRemoveLLMs)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(10, 260, 741, 20))
        self.pushButton = QPushButton(DialogForRemoveLLMs)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 290, 75, 24))
        self.pushButton_2 = QPushButton(DialogForRemoveLLMs)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(100, 290, 75, 24))
        self.textBrowser = QTextBrowser(DialogForRemoveLLMs)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 30, 741, 211))

        self.retranslateUi(DialogForRemoveLLMs)

        QMetaObject.connectSlotsByName(DialogForRemoveLLMs)
    # setupUi

    def retranslateUi(self, DialogForRemoveLLMs):
        DialogForRemoveLLMs.setWindowTitle(QCoreApplication.translate("DialogForRemoveLLMs", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("DialogForRemoveLLMs", u"\u5df2\u6709\u7684\u6a21\u578b\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("DialogForRemoveLLMs", u"\u8bf7\u8f93\u5165\u4f60\u60f3\u8981\u5220\u9664\u7684\u5927\u8bed\u8a00\u6a21\u578b\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("DialogForRemoveLLMs", u"\u786e\u5b9a", None))
        self.pushButton_2.setText(QCoreApplication.translate("DialogForRemoveLLMs", u"\u9000\u51fa", None))
    # retranslateUi

