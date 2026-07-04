import Quiz_GUI_QT6

class Question():
    '''
    List of questions and answers
    '''
    def __init__(self):
        self.question = ''
        self.answer = ""
        self.guess = -1
        self.answerList = []

questions = []
radioButtons = []  # easier to reference them

def initData(ui):  #for testing purposes
    '''
    Now hard coded
    later it will be filled with data from the AI call

    expect a list as: 
        question_list = 
        [
        ["What is the value of x in the equation x/2 + 3 = 7?", "4", ["1", "3", "5", "9"]],
        ["What is the area of a triangle with base 10 cm and height 6 cm?", "60", ["40", "60", "80", "90"]],
        ["What is the value of y in the equation y - 2 = 9?", "11", ["7", "9", "11", "13"]],
        ["What is the perimeter of a polygon with 5 sides, each with length 8 cm?", "40", ["30", "40", "50", "60"]],
        ["What is the volume of a rectangular prism with length 6 cm, width 4 cm, and height 2 cm?", "48", ["32", "48", "64", "80"]]
        ]

    Read it into the questions class with:
        for index, q in enumerate(question_list, start=1)
            quest = Question()
            quest.question = f"{index}. {q[0]}"
            quest.answer = q[1]
            quest.answerList = q[2]
            questions.append(quest)
    '''
    
    quest = Question()
    quest.question = "1. What is the value of x in the equation x/2 + 3 = 7?"
    quest.answer = "4"
    quest.answerList = ["1", "3", "5", "9"]
    questions.append(quest)

    quest = Question()
    quest.question = "2.What is the area of a triangle with base 10 cm and height 6 cm?"
    quest.answer = "60"
    quest.answerList = ["40", "60", "80", "90"]
    questions.append(quest)

    quest = Question()
    quest.question = "3. What is the value of y in the equation y - 2 = 9?"
    quest.answer = "11"
    quest.answerList =  ["7", "9", "11", "13"]
    questions.append(quest)

    quest = Question()
    quest.question = "4. What is the perimeter of a polygon with 5 sides, each with length 8 cm?"
    quest.answer = "40"
    quest.answerList = ["30", "40", "50", "60"]
    questions.append(quest)

    quest = Question()
    quest.question = "5. What is the volume of a rectangular prism with length 6 cm, width 4 cm, and height 2 cm?"
    quest.answer = "48"
    quest.answerList = ["32", "48", "64", "80"]
    questions.append(quest)

    # create list of radio button objects (indexed list is easier to use)
    radioButtons.append(ui.radioButton_1)
    radioButtons.append(ui.radioButton_2)
    radioButtons.append(ui.radioButton_3)
    radioButtons.append(ui.radioButton_4)

def submit(ui):
    '''
    user hit the end of the question set and selected 'Submit' button
    compute the user's score
    clear all the user's guesses from questions[]
    switch to results page
    '''
     # evealuate answers
    score = 0    
    for quest in questions:
       if quest.guess == quest.answer:
           score += 1

    # display score
    ui.lblResults.setText(f"Your score is: {score} / {len(questions)}")  #replace with text edit for extended review text
    ui.stackedWidget.setCurrentWidget(ui.pageResults)

    # reset question pointer
    ui.currentQuestion = 0 
    # reset all quesses 
    for quest in questions:
        quest.guess = -1
    
def loadNext(ui):
    '''
    increment question pointer if not on last question
    and call dislayQuestion()
    '''
    # increment question counter if not on last question
    
    ui.btnBack.setEnabled(True)
    ui.currentQuestion += 1
    if ui.currentQuestion >= len(questions) - 1:
        
        # evaluate score if done with last question
        ui.btnNext.setEnabled(False)
        ui.btnSubmit.setVisible(True)
        
    dislayQuestion(ui)
    

def loadPrevious(ui):
    '''
    decrement question pointer if not on first question
    and call dislayQuestion()
    '''
    ui.btnNext.setEnabled(True)
    ui.currentQuestion -= 1
    
    if ui.currentQuestion == 0:
        ui.btnBack.setEnabled(False)
    
    dislayQuestion(ui)

def dislayQuestion(ui):
    '''
    Clear radio button selections from last question
    populate question and radio button text with current question and answers
    If user has previously selected an answer, click that radio button.
    '''
    # clear all rbs to false
    ui.radioButton_1.setChecked(True)  # sets all others to false
    ui.buttonGroup_1.setExclusive(False)
    ui.radioButton_1.setChecked(False)   
    ui.buttonGroup_1.setExclusive(True)

    # display question and answers
    ui.lblQuestion.setText(questions[ui.currentQuestion].question)
    for index in range(4):
        radioButtons[index].setText(questions[ui.currentQuestion].answerList[index])
    # ui.radioButton_2.setText(questions[ui.currentQuestion].answerList[1])
    # ui.radioButton_3.setText(questions[ui.currentQuestion].answerList[2])
    # ui.radioButton_4.setText(questions[ui.currentQuestion].answerList[3])

    # reset previously selected answer if there is one
    #   I have to do it this way since there is no collection of widgets in Qt.
    if not questions[ui.currentQuestion].guess == '':
        for index, value in enumerate(questions[ui.currentQuestion].answerList):
            if  questions[ui.currentQuestion].guess == questions[ui.currentQuestion].answerList[index]:
                radioButtons[index].setChecked(True)
        
        # if questions[ui.currentQuestion].guess == 0:
        #     ui.radioButton_1.setChecked(True)
        # elif questions[ui.currentQuestion].guess == 1:
        #     ui.radioButton_2.setChecked(True)
        # elif questions[ui.currentQuestion].guess == 2:
        #     ui.radioButton_3.setChecked(True)
        # elif questions[ui.currentQuestion].guess == 3:
        #     ui.radioButton_4.setChecked(True)
    if ui.currentQuestion == 0:
        ui.btnBack.setEnabled(False)


def saveAnswer(ui, value):
    '''
    save the text of the currently selected radio button
        to later compare it to the correct answer.
    'value' is the index of the currently selected radio button 
    '''
    questions[ui.currentQuestion].guess = questions[ui.currentQuestion].answerList[value]

def clearGUI(ui):
    '''
    Set all Radio buttons to not selected
    Clear text in question label and radio buttons
    '''
        # set all rbs to false
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