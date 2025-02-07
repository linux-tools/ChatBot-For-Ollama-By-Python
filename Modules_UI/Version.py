# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Version.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QPlainTextEdit, QPushButton,
    QSizePolicy, QWidget)

class Ui_DialogVersion(object):
    def setupUi(self, DialogVersion):
        if not DialogVersion.objectName():
            DialogVersion.setObjectName(u"DialogVersion")
        DialogVersion.resize(531, 357)
        self.plainTextEdit = QPlainTextEdit(DialogVersion)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setEnabled(False)
        self.plainTextEdit.setGeometry(QRect(0, 0, 531, 331))
        font = QFont()
        font.setPointSize(11)
        self.plainTextEdit.setFont(font)
        self.pushButton = QPushButton(DialogVersion)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 330, 75, 24))

        self.retranslateUi(DialogVersion)

        QMetaObject.connectSlotsByName(DialogVersion)
    # setupUi

    def retranslateUi(self, DialogVersion):
        DialogVersion.setWindowTitle(QCoreApplication.translate("DialogVersion", u"版本", None))
        self.plainTextEdit.setPlainText(QCoreApplication.translate("DialogVersion", u"\u7248\u672c0.1_1.0-dev1:\n"
"\u9879\u76ee\u9996\u7248\uff0c\u652f\u6301ollama\u6a21\u578b\u8c03\u7528\u5e76\u4e14\u80fd\u8ba9\u5f53\u524d\u5bf9\u8bdd\u4e0e\u524d\u540e\u6587\u8054\u7cfb\uff0c\u652f\u6301\u5bf9ollama\u6a21\u578b\u7ba1\u7406\uff0c\u652f\u6301\u67e5\u770bollama\u7248\u672c\uff0c\u4ee5\u53ca\u5bf9ollama\u670d\u52a1\u542f\u52a8\u548c\u5173\u95ed", None))
        self.pushButton.setText(QCoreApplication.translate("DialogVersion", u"\u786e\u5b9a", None))
    # retranslateUi

