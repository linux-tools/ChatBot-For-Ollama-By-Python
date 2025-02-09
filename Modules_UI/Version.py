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
from PySide6.QtWidgets import (QApplication, QDialog, QPushButton, QSizePolicy,
    QTextBrowser, QWidget)

class Ui_DialogVersion(object):
    def setupUi(self, DialogVersion):
        if not DialogVersion.objectName():
            DialogVersion.setObjectName(u"DialogVersion")
        DialogVersion.resize(531, 365)
        self.pushButton = QPushButton(DialogVersion)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(10, 330, 75, 24))
        self.textBrowser = QTextBrowser(DialogVersion)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(10, 11, 511, 311))
        font = QFont()
        font.setFamilies([u"\u5b8b\u4f53"])
        font.setPointSize(16)
        self.textBrowser.setFont(font)

        self.retranslateUi(DialogVersion)

        QMetaObject.connectSlotsByName(DialogVersion)
    # setupUi

    def retranslateUi(self, DialogVersion):
        DialogVersion.setWindowTitle(QCoreApplication.translate("DialogVersion", u"Dialog", None))
        self.pushButton.setText(QCoreApplication.translate("DialogVersion", u"\u786e\u5b9a", None))
        self.textBrowser.setHtml(QCoreApplication.translate("DialogVersion", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><meta charset=\"utf-8\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"hr { height: 1px; border-width: 0; }\n"
"li.unchecked::marker { content: \"\\2610\"; }\n"
"li.checked::marker { content: \"\\2612\"; }\n"
"</style></head><body style=\" font-family:'\u5b8b\u4f53'; font-size:16pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u5f53\u524d\u7248\u672c\uff1av0.3_1.0-dev3:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u5bf9\u8bdd\u652f\u6301Markdown\u6587\u672c\uff0c\u5bf9\u90e8\u5206\u754c\u9762\u505a"
                        "\u5c0f\u90e8\u5206\u6539\u8fdb\uff0c\u4ee5\u89e3\u51b3\u6781\u5c11\u90e8\u5206bug(\u5c3d\u7ba1\u4e0d\u5f71\u54cd\u4f7f\u7528\uff0c\u4f46\u662f\u4f1a\u9020\u6210\u5c0f\u8bef\u4f1a)</span></p>\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u5386\u53f2\u7248\u672c\uff1a0.2_1.0-dev2:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u4fee\u590d\u6a21\u578b\u65e0\u6cd5\u9009\u62e9\u6a21\u578b\u548c\u5220\u9664\u6a21\u578b\u7684bug\uff0c\u4ee5\u53ca\u5c0f\u90e8\u5206Ui\u754c\u9762\u9519\u8bef</span></p>\n"
"<p styl"
                        "e=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-family:'Microsoft YaHei UI'; font-size:14pt;\"><br /></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u5386\u53f2\u7248\u672c\uff1a0.1_1.0-dev1:</span></p>\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-family:'Microsoft YaHei UI'; font-size:14pt;\">\u9879\u76ee\u9996\u7248\uff0c\u652f\u6301ollama\u6a21\u578b\u8c03\u7528\u5e76\u4e14\u80fd\u8ba9\u5f53\u524d\u5bf9\u8bdd\u4e0e\u524d\u540e\u6587\u8054\u7cfb\uff0c\u652f\u6301\u5bf9ollama\u6a21\u578b\u7ba1\u7406\uff0c\u652f\u6301\u67e5\u770bollama\u7248\u672c\uff0c\u4ee5\u53ca\u5bf9ollama\u670d\u52a1\u542f\u52a8\u548c\u5173\u95ed</span></p></body></html>", None))
    # retranslateUi

