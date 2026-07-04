from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtCore import QTimer
from ui_mainwindow import Ui_MainWindow
import Quiz_Utility as qu

# Only needed for access to command line arguments
import sys
# use PySide6-uic xxx.ui -o xxx.py to convert ui to py
# use PySide6

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSubmit.setVisible(False)
        

        self.ui.btnNext.clicked.connect(lambda: qu.loadNext(self.ui))
        self.ui.btnBack.clicked.connect(lambda: qu.loadPrevious(self.ui))
        self.ui.btnQuit.clicked.connect(lambda: quit())

        self.ui.radioButton_1.clicked.connect(lambda: qu.saveAnswer(self.ui,0))
        self.ui.radioButton_2.clicked.connect(lambda: qu.saveAnswer(self.ui,1))
        self.ui.radioButton_3.clicked.connect(lambda: qu.saveAnswer(self.ui,2))
        self.ui.radioButton_4.clicked.connect(lambda: qu.saveAnswer(self.ui,3))

        self.ui.currentQuestion = 0

        self.ui.btnConfirm.clicked.connect(lambda: change_page(self,"pageLoading"))
        self.ui.btnSubmit.clicked.connect(lambda: qu.submit(self.ui))
        self.ui.btnTryNew.clicked.connect(lambda: change_page(self,"pageHome"))
        self.ui.btnTrySame.clicked.connect(lambda: change_page(self,"pageLoading"))

def change_page(self, pageName, caller = ''):
    qu.clearGUI(self.ui)

    if pageName == "pageLoading":
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLoading)
        QTimer.singleShot(2000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageQuiz))  #does not freeze event loop
        qu.loadGUI(self.ui)
    else:
        self.ui.stackedWidget.setCurrentWidget(getattr(self.ui, pageName))


def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    qu.initData(window.ui)
    window.show()

    
    

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
   