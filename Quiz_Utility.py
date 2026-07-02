class Question():
    def __init__(self):
        self.question = ''
        self.answer = ''
        self.answerList = []

class QuizState():
    def __init__(self):
        self.currentStudent = 0
        self.currentQuestion = -1
        self.currentAnswer = 0

class Student():
    def __init__(self):
        self.name = ''
        self.answers = []

        
questions = []
students = []
qs = QuizState()

def initData():
    quest = Question()
    quest.question = "what are you?"
    quest.answer = "A human"
    quest.answerList = ["A dog","A cat","A human","A fish"]
    questions.append(quest)

    quest = Question()
    quest.question = "how old are you?"
    quest.answer = "37"
    quest.answerList = ["21","33","76","101"]
    questions.append(quest)

    stu = Student()
    stu.name = "Billy"
    stu.answers = [len(questions)]
    students.append(stu)

    stu = Student()
    stu.name = "Emma"
    stu.answers = [len(questions)]
    students.append(stu)

def submit():
    # evealuate answers
    students[qs.currentStudent].answers[qs.currentQuestion]

def loadNext(ui):
    print("next")
    
    if qs.currentQuestion >= len(questions) - 1:
        submit(ui)
    # save answer

    qs.currentQuestion += 1


    ui.lblQuestion.setText(questions[qs.currentQuestion].question)
    ui.radioButton.setText(questions[qs.currentQuestion].answerList[0])
    ui.radioButton_2.setText(questions[qs.currentQuestion].answerList[1])
    ui.radioButton_3.setText(questions[qs.currentQuestion].answerList[2])
    ui.radioButton_4.setText(questions[qs.currentQuestion].answerList[3])

def loadPrevious(ui):
    print("back")
    
    if qs.currentQuestion == 0:
        return
    qs.currentQuestion -= 1

    ui.lblQuestion.setText(questions[qs.currentQuestion].question)
    ui.radioButton.setText(questions[qs.currentQuestion].answerList[0])
    ui.radioButton_2.setText(questions[qs.currentQuestion].answerList[1])
    ui.radioButton_3.setText(questions[qs.currentQuestion].answerList[2])
    ui.radioButton_4.setText(questions[qs.currentQuestion].answerList[3])

def saveAnswer(value):
    students[qs.currentStudent].answers[qs.currentQuestion] = value