from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
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
        

        self.ui.btnNext.clicked.connect(lambda: qu.loadNext(self.ui))
        self.ui.btnBack.clicked.connect(lambda: qu.loadPrevious(self.ui))
        self.ui.btnQuit.clicked.connect(lambda: quit())

        self.ui.radioButton_1.clicked.connect(lambda: qu.saveAnswer(self.ui,0))
        self.ui.radioButton_2.clicked.connect(lambda: qu.saveAnswer(self.ui,1))
        self.ui.radioButton_3.clicked.connect(lambda: qu.saveAnswer(self.ui,2))
        self.ui.radioButton_4.clicked.connect(lambda: qu.saveAnswer(self.ui,3))

        self.ui.currentQuestion = -1

def open_second(self):         # To open any other window and hide self
        self.second.show()     # Show second window
        self.hide()            # Optional

def main():
    app = QApplication(sys.argv)

    window = MainWindow()
    qu.initData(window.ui)
    window.show()

    
    

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
   