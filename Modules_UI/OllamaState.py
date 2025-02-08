# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'OllamaState.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextEdit, QWidget)

class Ui_DialogForStateOllama(object):
    def setupUi(self, DialogForStateOllama):
        if not DialogForStateOllama.objectName():
            DialogForStateOllama.setObjectName(u"DialogForStateOllama")
        DialogForStateOllama.resize(400, 92)
        self.textEdit = QTextEdit(DialogForStateOllama)
        self.textEdit.setObjectName(u"textEdit")
        self.textEdit.setEnabled(False)
        self.textEdit.setGeometry(QRect(20, 13, 351, 41))
        self.pushButton = QPushButton(DialogForStateOllama)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(120, 60, 75, 24))
        self.pushButton_2 = QPushButton(DialogForStateOllama)
        self.pushButton_2.setObjectName(u"pushButton_2")
        self.pushButton_2.setGeometry(QRect(210, 60, 75, 24))

        self.retranslateUi(DialogForStateOllama)

        QMetaObject.connectSlotsByName(DialogForStateOllama)
    # setupUi

    def retranslateUi(self, DialogForStateOllama):
        DialogForStateOllama.setWindowTitle(QCoreApplication.translate("DialogForStateOllama", u"选择开关Ollama", None))
        self.pushButton.setText(QCoreApplication.translate("DialogForStateOllama", u"\u5f00", None))
        self.pushButton_2.setText(QCoreApplication.translate("DialogForStateOllama", u"\u5173", None))
    # retranslateUi

