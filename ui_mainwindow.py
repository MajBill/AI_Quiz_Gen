# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'quiz_gui_qt.ui'
##
## Created by: Qt User Interface Compiler version 6.11.1
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
from PySide6.QtWidgets import (QApplication, QButtonGroup, QLabel, QMainWindow,
    QMenuBar, QPushButton, QRadioButton, QSizePolicy,
    QStatusBar, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(467, 388)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.lblQuestion = QLabel(self.centralwidget)
        self.lblQuestion.setObjectName(u"lblQuestion")
        self.lblQuestion.setGeometry(QRect(30, 20, 401, 61))
        self.lblQuestion.setTextFormat(Qt.TextFormat.RichText)
        self.lblQuestion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(30, 230, 81, 26))
        self.btnNext = QPushButton(self.centralwidget)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(140, 230, 81, 26))
        self.btnQuit = QPushButton(self.centralwidget)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setGeometry(QRect(30, 290, 81, 26))
        self.radioButton_2 = QRadioButton(self.centralwidget)
        self.buttonGroup_1 = QButtonGroup(MainWindow)
        self.buttonGroup_1.setObjectName(u"buttonGroup_1")
        self.buttonGroup_1.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(30, 110, 98, 24))
        self.radioButton_4 = QRadioButton(self.centralwidget)
        self.buttonGroup_1.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(30, 170, 98, 24))
        self.radioButton_1 = QRadioButton(self.centralwidget)
        self.buttonGroup_1.addButton(self.radioButton_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setGeometry(QRect(30, 80, 98, 24))
        self.radioButton_3 = QRadioButton(self.centralwidget)
        self.buttonGroup_1.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(30, 140, 98, 24))
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 467, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.lblQuestion.setText("")
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.radioButton_2.setText("")
        self.radioButton_4.setText("")
        self.radioButton_1.setText("")
        self.radioButton_3.setText("")
    # retranslateUi

