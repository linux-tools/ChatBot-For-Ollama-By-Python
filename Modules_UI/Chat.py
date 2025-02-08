# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Chat.ui'
##
## Created by: Qt User Interface Compiler version 6.8.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QAction, QBrush, QColor, QConicalGradient,
    QCursor, QFont, QFontDatabase, QGradient,
    QIcon, QImage, QKeySequence, QLinearGradient,
    QPainter, QPalette, QPixmap, QRadialGradient,
    QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QMenu,
    QMenuBar, QPlainTextEdit, QPushButton, QSizePolicy,
    QStatusBar, QTextBrowser, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1176, 919)
        self.actionChoose_Language_Models = QAction(MainWindow)
        self.actionChoose_Language_Models.setObjectName(u"actionChoose_Language_Models")
        self.actionAbout = QAction(MainWindow)
        self.actionAbout.setObjectName(u"actionAbout")
        self.actionExit = QAction(MainWindow)
        self.actionExit.setObjectName(u"actionExit")
        self.actionCurrent_LLM = QAction(MainWindow)
        self.actionCurrent_LLM.setObjectName(u"actionCurrent_LLM")
        self.action_Open_or_close_ollama = QAction(MainWindow)
        self.action_Open_or_close_ollama.setObjectName(u"action_Open_or_close_ollama")
        self.actionDownload_LLMs = QAction(MainWindow)
        self.actionDownload_LLMs.setObjectName(u"actionDownload_LLMs")
        self.actionCheck_Ollama_Version = QAction(MainWindow)
        self.actionCheck_Ollama_Version.setObjectName(u"actionCheck_Ollama_Version")
        self.actionRemove_LLMs = QAction(MainWindow)
        self.actionRemove_LLMs.setObjectName(u"actionRemove_LLMs")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 10, 61, 16))
        self.textBrowser = QTextBrowser(self.centralwidget)
        self.textBrowser.setObjectName(u"textBrowser")
        self.textBrowser.setGeometry(QRect(0, 30, 1181, 451))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 490, 71, 16))
        self.plainTextEdit = QPlainTextEdit(self.centralwidget)
        self.plainTextEdit.setObjectName(u"plainTextEdit")
        self.plainTextEdit.setGeometry(QRect(0, 510, 1181, 301))
        self.pushButton = QPushButton(self.centralwidget)
        self.pushButton.setObjectName(u"pushButton")
        self.pushButton.setGeometry(QRect(0, 810, 75, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 1176, 33))
        self.menu = QMenu(self.menubar)
        self.menu.setObjectName(u"menu")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.menubar.addAction(self.menu.menuAction())
        self.menu.addAction(self.actionChoose_Language_Models)
        self.menu.addAction(self.actionCurrent_LLM)
        self.menu.addAction(self.actionDownload_LLMs)
        self.menu.addAction(self.actionRemove_LLMs)
        self.menu.addSeparator()
        self.menu.addAction(self.action_Open_or_close_ollama)
        self.menu.addAction(self.actionCheck_Ollama_Version)
        self.menu.addSeparator()
        self.menu.addAction(self.actionAbout)
        self.menu.addAction(self.actionExit)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"ChatBot For Ollama", None))
        self.actionChoose_Language_Models.setText(QCoreApplication.translate("MainWindow", u"\u9009\u62e9\u5927\u8bed\u8a00\u6a21\u578b", None))
        self.actionAbout.setText(QCoreApplication.translate("MainWindow", u"\u5173\u4e8e\u8f6f\u4ef6", None))
        self.actionExit.setText(QCoreApplication.translate("MainWindow", u"\u9000\u51fa", None))
        self.actionCurrent_LLM.setText(QCoreApplication.translate("MainWindow", u"\u5f53\u524d\u4f7f\u7528\u7684\u5927\u8bed\u8a00\u6a21\u578b", None))
        self.action_Open_or_close_ollama.setText(QCoreApplication.translate("MainWindow", u"\u6253\u5f00\u6216\u5173\u95edOllama", None))
        self.actionDownload_LLMs.setText(QCoreApplication.translate("MainWindow", u"\u4e0b\u8f7d\u5927\u8bed\u8a00\u6a21\u578b", None))
        self.actionCheck_Ollama_Version.setText(QCoreApplication.translate("MainWindow", u"\u67e5\u770bOllama\u7248\u672c", None))
        self.actionRemove_LLMs.setText(QCoreApplication.translate("MainWindow", u"\u79fb\u9664\u5927\u8bed\u8a00\u6a21\u578b", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"AI\u6d88\u606f\u6846\uff1a", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"\u7528\u6237\u5bf9\u8bdd\u6846\uff1a", None))
        self.pushButton.setText(QCoreApplication.translate("MainWindow", u"\u53d1\u9001", None))
        self.menu.setTitle(QCoreApplication.translate("MainWindow", u"\u9009\u9879", None))
    # retranslateUi

