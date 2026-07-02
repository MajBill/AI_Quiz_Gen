from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from ui_mainwindow import Ui_MainWindow
import Quiz_Utility as qu

# Only needed for access to command line arguments
import sys

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.ui.btnNext.clicked.connect(lambda: qu.loadNext(self.ui))
        self.ui.btnBack.clicked.connect(lambda: qu.loadPrevious(self.ui))
        self.ui.radioButton.clicked.connect(lambda: qu.saveAnswer(1))
        self.ui.radioButton_2.clicked.connect(lambda: qu.saveAnswer(2))
        self.ui.radioButton_3.clicked.connect(lambda: qu.saveAnswer(3))
        self.ui.radioButton_4.clicked.connect(lambda: qu.saveAnswer(4))


    
    # def setAnswer(self, value):
    #     qu.saveAnswer(value)

if __name__ == "__main__":
    qu.initData()

    app = QApplication(sys.argv)

    window = MainWindow()
    window.show()

    sys.exit(app.exec())