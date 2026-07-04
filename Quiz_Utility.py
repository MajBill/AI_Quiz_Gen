import Quiz_GUI_QT6

class Question():
    def __init__(self):
        self.question = ''
        self.answer = 0
        self.guess = -1
        self.answerList = []


questions = []

def initData(ui):  #for testing purposes?
    
    quest = Question()
    quest.question = "1. what are you?"
    quest.answer = 2
    quest.answerList = ["A dog","A cat","A human","A fish"]
    questions.append(quest)

    quest = Question()
    quest.question = "2. how old are you?"
    quest.answer = 0
    quest.answerList = ["21","33","76","101"]
    questions.append(quest)

    quest = Question()
    quest.question = "3. and the third is this?"
    quest.answer = 2
    quest.answerList = ["21","37","76","101"]
    questions.append(quest)

    quest = Question()
    quest.question = "4. and the fourth is this?"
    quest.answer = 3
    quest.answerList = ["21","37","76","101"]
    questions.append(quest)


def submit(ui):
    # evealuate answers
    score = 0
    total = len(questions)
    for quest in questions:
       if quest.guess == quest.answer:
           score += 1
    ui.lblResults.setText(f"Your score is: {score}/{total}")  #replace with text edit
    ui.stackedWidget.setCurrentWidget(ui.pageResults)

    ui.currentQuestion = 0 

    for quest in questions:
        quest.guess = -1
    # clearGUI(ui)
    


def loadNext(ui):
    # increment question counter
    if ui.currentQuestion >= len(questions) - 1:
        ui.currentQuestion -= 1
        # evaluate score if done with last question
        ui.btnSubmit.setVisible(True)
        #submit(ui)
        return
    
    ui.currentQuestion += 1

    loadGUI(ui)

def loadPrevious(ui):
    
    if ui.currentQuestion == 0:
        return
    ui.currentQuestion -= 1
    loadGUI(ui)

def loadGUI(ui):
    # set all rbs to false
    ui.radioButton_1.setChecked(True)  # sets all others to false
    ui.buttonGroup_1.setExclusive(False)
    ui.radioButton_1.setChecked(False)   
    ui.buttonGroup_1.setExclusive(True)


    # display question and answers
    ui.lblQuestion.setText(questions[ui.currentQuestion].question)
    ui.radioButton_1.setText(questions[ui.currentQuestion].answerList[0])
    ui.radioButton_2.setText(questions[ui.currentQuestion].answerList[1])
    ui.radioButton_3.setText(questions[ui.currentQuestion].answerList[2])
    ui.radioButton_4.setText(questions[ui.currentQuestion].answerList[3])

    # reset previously selected answer if there is one
    #   I have to do it this way since there is no collection of widgets in Qt.
    if questions[ui.currentQuestion].guess > -1:
        if questions[ui.currentQuestion].guess == 0:
            ui.radioButton_1.setChecked(True)
        elif questions[ui.currentQuestion].guess == 1:
            ui.radioButton_2.setChecked(True)
        elif questions[ui.currentQuestion].guess == 2:
            ui.radioButton_3.setChecked(True)
        elif questions[ui.currentQuestion].guess == 3:
            ui.radioButton_4.setChecked(True)
    
    

def saveAnswer(ui, value):
    questions[ui.currentQuestion].guess = value

def clearGUI(ui):
    ui.radioButton_1.setChecked(True)  # sets all others to false
    ui.buttonGroup_1.setExclusive(False)
    ui.radioButton_1.setChecked(False)   
    ui.buttonGroup_1.setExclusive(True)
    ui.lblQuestion.setText('')
    ui.radioButton_1.setText('')
    ui.radioButton_2.setText('')
    ui.radioButton_3.setText('')
    ui.radioButton_4.setText('')


if __name__ == "__main__":
    Quiz_GUI_QT6.main()