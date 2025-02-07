# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ask.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
    QPushButton, QSizePolicy, QTextEdit, QWidget)

class Ui_DialogUseModels(object):
    def setupUi(self, DialogUseModels):
        if not DialogUseModels.objectName():
            DialogUseModels.setObjectName(u"DialogUseModels")
        DialogUseModels.resize(871, 556)
        self.textEdit = QTextEdit(DialogUseModels)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QRect(0, 0, 871, 481))
        font = QFont()
        font.setFamilies([u"Consolas"])
        font.setPointSize(11)
        self.textEdit.setFont(font)
        self.label = QLabel(DialogUseModels)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 480, 121, 16))
        self.lineEdit = QLineEdit(DialogUseModels)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setGeometry(QRect(0, 500, 911, 20))
        self.pushButton = QPushButton(DialogUseModels)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 520, 171, 24))

        self.retranslateUi(DialogUseModels)

        QMetaObject.connectSlotsByName(DialogUseModels)
    # setupUi

    def retranslateUi(self, DialogUseModels):
        DialogUseModels.setWindowTitle(QCoreApplication.translate("DialogUseModels", u"选择要使用的模型", None))
        self.label.setText(QCoreApplication.translate("DialogUseModels", u"\u9009\u62e9\u4f60\u60f3\u8981\u7684\u6a21\u578b\u540d\u79f0\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("DialogUseModels", u"\u786e\u5b9a", None))
    # retranslateUi

