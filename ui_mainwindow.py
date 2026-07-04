# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Quiz_GUI_QT.ui'
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
    QStackedWidget, QStatusBar, QTextEdit, QVBoxLayout,
    QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(618, 457)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout = QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.stackedWidget = QStackedWidget(self.centralwidget)
        self.stackedWidget.setObjectName(u"stackedWidget")
        self.pageHome = QWidget()
        self.pageHome.setObjectName(u"pageHome")
        self.label = QLabel(self.pageHome)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(30, 10, 521, 61))
        self.lblTopic = QTextEdit(self.pageHome)
        self.lblTopic.setObjectName(u"lblTopic")
        self.lblTopic.setGeometry(QRect(110, 90, 301, 64))
        self.label_2 = QLabel(self.pageHome)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(40, 100, 61, 41))
        self.label_3 = QLabel(self.pageHome)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(40, 170, 61, 41))
        self.lblMaxLength = QTextEdit(self.pageHome)
        self.lblMaxLength.setObjectName(u"lblMaxLength")
        self.lblMaxLength.setGeometry(QRect(110, 160, 301, 64))
        self.btnConfirm = QPushButton(self.pageHome)
        self.btnConfirm.setObjectName(u"btnConfirm")
        self.btnConfirm.setGeometry(QRect(300, 270, 81, 26))
        self.btnClear = QPushButton(self.pageHome)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(140, 270, 81, 26))
        self.stackedWidget.addWidget(self.pageHome)
        self.pageLoading = QWidget()
        self.pageLoading.setObjectName(u"pageLoading")
        self.stackedWidget.addWidget(self.pageLoading)
        self.pageQuiz = QWidget()
        self.pageQuiz.setObjectName(u"pageQuiz")
        self.lblQuestion = QLabel(self.pageQuiz)
        self.lblQuestion.setObjectName(u"lblQuestion")
        self.lblQuestion.setGeometry(QRect(10, 10, 501, 81))
        self.lblQuestion.setTextFormat(Qt.TextFormat.RichText)
        self.lblQuestion.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)
        self.btnQuit = QPushButton(self.pageQuiz)
        self.btnQuit.setObjectName(u"btnQuit")
        self.btnQuit.setGeometry(QRect(60, 350, 81, 26))
        self.btnNext = QPushButton(self.pageQuiz)
        self.btnNext.setObjectName(u"btnNext")
        self.btnNext.setGeometry(QRect(250, 310, 81, 26))
        self.btnBack = QPushButton(self.pageQuiz)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(60, 310, 81, 26))
        self.radioButton_3 = QRadioButton(self.pageQuiz)
        self.buttonGroup_1 = QButtonGroup(MainWindow)
        self.buttonGroup_1.setObjectName(u"buttonGroup_1")
        self.buttonGroup_1.addButton(self.radioButton_3)
        self.radioButton_3.setObjectName(u"radioButton_3")
        self.radioButton_3.setGeometry(QRect(60, 230, 171, 24))
        self.radioButton_4 = QRadioButton(self.pageQuiz)
        self.buttonGroup_1.addButton(self.radioButton_4)
        self.radioButton_4.setObjectName(u"radioButton_4")
        self.radioButton_4.setGeometry(QRect(60, 260, 161, 24))
        self.radioButton_1 = QRadioButton(self.pageQuiz)
        self.buttonGroup_1.addButton(self.radioButton_1)
        self.radioButton_1.setObjectName(u"radioButton_1")
        self.radioButton_1.setGeometry(QRect(60, 170, 190, 24))
        self.radioButton_2 = QRadioButton(self.pageQuiz)
        self.buttonGroup_1.addButton(self.radioButton_2)
        self.radioButton_2.setObjectName(u"radioButton_2")
        self.radioButton_2.setGeometry(QRect(60, 200, 201, 24))
        self.btnSubmit = QPushButton(self.pageQuiz)
        self.btnSubmit.setObjectName(u"btnSubmit")
        self.btnSubmit.setGeometry(QRect(250, 350, 81, 26))
        self.stackedWidget.addWidget(self.pageQuiz)
        self.pageResults = QWidget()
        self.pageResults.setObjectName(u"pageResults")
        self.btnTryNew = QPushButton(self.pageResults)
        self.btnTryNew.setObjectName(u"btnTryNew")
        self.btnTryNew.setGeometry(QRect(120, 310, 81, 26))
        self.btnTrySame = QPushButton(self.pageResults)
        self.btnTrySame.setObjectName(u"btnTrySame")
        self.btnTrySame.setGeometry(QRect(40, 310, 81, 26))
        self.label_4 = QLabel(self.pageResults)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(48, 280, 241, 20))
        self.lblResults = QLabel(self.pageResults)
        self.lblResults.setObjectName(u"lblResults")
        self.lblResults.setGeometry(QRect(50, 50, 441, 181))
        self.stackedWidget.addWidget(self.pageResults)

        self.verticalLayout.addWidget(self.stackedWidget)

        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QMenuBar(MainWindow)
        self.menubar.setObjectName(u"menubar")
        self.menubar.setGeometry(QRect(0, 0, 618, 33))
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QStatusBar(MainWindow)
        self.statusbar.setObjectName(u"statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)

        self.stackedWidget.setCurrentIndex(0)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Please enter the topic for this quiz:", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Topic:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Max Length:", None))
        self.btnConfirm.setText(QCoreApplication.translate("MainWindow", u"Confirm", None))
        self.btnClear.setText(QCoreApplication.translate("MainWindow", u"Clear", None))
        self.lblQuestion.setText("")
        self.btnQuit.setText(QCoreApplication.translate("MainWindow", u"Quit", None))
        self.btnNext.setText(QCoreApplication.translate("MainWindow", u"Next", None))
        self.btnBack.setText(QCoreApplication.translate("MainWindow", u"Back", None))
        self.radioButton_3.setText("")
        self.radioButton_4.setText("")
        self.radioButton_1.setText("")
        self.radioButton_2.setText("")
        self.btnSubmit.setText(QCoreApplication.translate("MainWindow", u"Submit", None))
        self.btnTryNew.setText(QCoreApplication.translate("MainWindow", u"New set", None))
        self.btnTrySame.setText(QCoreApplication.translate("MainWindow", u"Same set", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Try again?", None))
        self.lblResults.setText(QCoreApplication.translate("MainWindow", u"TextLabel", None))
    # retranslateUi

