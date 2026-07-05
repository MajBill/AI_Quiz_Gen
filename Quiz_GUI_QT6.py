from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtCore import QFile
from PySide6.QtCore import QTimer
from ui_mainwindow import Ui_MainWindow
import Quiz_Utility as qu
from server_start import start_server

# Only needed for access to command line arguments
import sys
# use PySide6-uic xxx.ui -o xxx.py to convert ui to py

class MainWindow(QMainWindow):
    '''
    load the GUI python file, Ui_Mainwindow
    incorporate that into the PySide6 framework
    '''
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.btnSubmit.setVisible(False)
        
        self.ui.btnNext.clicked.connect(lambda: qu.loadNext(self.ui))
        self.ui.btnBack.clicked.connect(lambda: qu.loadPrevious(self.ui))
        self.ui.btnQuit.clicked.connect(lambda: quit())
        self.ui.btnQuit_2.clicked.connect(lambda: quit())

        self.ui.radioButton_1.clicked.connect(lambda: qu.saveAnswer(self.ui, 0))
        self.ui.radioButton_2.clicked.connect(lambda: qu.saveAnswer(self.ui, 1))
        self.ui.radioButton_3.clicked.connect(lambda: qu.saveAnswer(self.ui, 2))
        self.ui.radioButton_4.clicked.connect(lambda: qu.saveAnswer(self.ui, 3))

        self.ui.btnConfirm.clicked.connect(lambda: change_page(self,"pageLoading"))
        self.ui.btnSubmit.clicked.connect(lambda: qu.submit(self.ui))
        self.ui.btnClear.clicked.connect(lambda: clear(self))
        self.ui.btnTryNew.clicked.connect(lambda: tryNew(self))
        self.ui.btnTrySame.clicked.connect(lambda: trySame(self))

        self.ui.currentQuestion = 0  # initialize quesion pointer 


def change_page(self, pageName):
    '''
    change the GUI page currently displayed
    if displaying quiz page, display current question
        assume question pointer is at 0
    '''
    if pageName == "pageLoading":
        self.ui.stackedWidget.setCurrentWidget(self.ui.pageLoading)
        QApplication.processEvents() #refresh gui
        # qu.initData(self.ui)
        QTimer.singleShot(2000, lambda: self.ui.stackedWidget.setCurrentWidget(self.ui.pageQuiz))  #does not freeze event loop

        questions = qu.generate_quest(self.ui.txtTopic.toPlainText(), int(self.ui.txtMaxLength.toPlainText()))
        qu.initData(self.ui, questions)
        qu.dislayQuestion(self.ui)

        
    else:
        self.ui.stackedWidget.setCurrentWidget(getattr(self.ui, pageName))

def tryNew(self):
    '''
    Clear screens
    set display to first page
    Assume quesses have been cleared 
        and currentQuestion set to 0 in submit()
    '''
    self.ui.btnNext.setEnabled(True)
    self.ui.stackedWidget.setCurrentWidget(self.ui.pageHome)
    
def trySame(self):
    '''
    set display to quiz page
    display current question
    Assume quesses have been cleared 
        and currentQuestion set to 0 in submit()
    '''
    self.ui.stackedWidget.setCurrentWidget(self.ui.pageQuiz)
    self.ui.btnNext.setEnabled(True)
    qu.dislayQuestion(self.ui)         # display first question
 
def clear(self):
    self.ui.txtTopic.setText('')
    self.ui.txtMaxLength.setText('')

def main():
    '''
    mostly boilerplate
    but added initdata()
    '''
    app = QApplication(sys.argv)

    start_server()  # Start the FastAPI server in a subprocess

    window = MainWindow()
    
    window.show()

    sys.exit(app.exec())

if __name__ == "__main__":
    main()
   