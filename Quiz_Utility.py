import Quiz_GUI_QT6
import requests
import json

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

def initData(ui, newQuestions): 
    '''
    Load the questions list with new questions from an AI model
    newQuestions comes from the AI call
    '''
    questions.clear()     # this may be a 'new' set
    for question in newQuestions:
    
        quest = Question()
        quest.question = question['question']
        quest.answer = question['answer']
        quest.answerList = question['options']
        questions.append(quest)

    # create list of radio button objects (indexed list is easier to use)
    radioButtons.clear()
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
    review_text = 'You missed the following questions:\n'
    score = 0    
    for index,quest in enumerate(questions, start=1):
        if quest.guess == quest.answer:
           score += 1
        else:
            review_text += f"{index}. {quest.question}\nYour answer: {quest.guess}  Correct answer: {quest.answer}\n\n"

    result_text = f"Your score is: {score} / {len(questions)}\n" 
    if score < len(questions):
        result_text = result_text + review_text
    else:
        result_text = result_text + "You answered all questions correctly."
    # display score
    ui.txtResults.setPlainText(result_text)  #replace with text edit for extended review text
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
        ui.btnNext.setEnabled(False)
        # evaluate score if done with last question
        
        ui.btnSubmit.setVisible(True)
        
    dislayQuestion(ui)
    

def loadPrevious(ui):
    '''
    decrement question pointer if not on first question
    and call dislayQuestion()
    '''
    ui.btnNext.setEnabled(True)

    if not ui.currentQuestion == 0:
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
    ui.txtQuestion.setPlainText(questions[ui.currentQuestion].question)
    for index in range(4):
        radioButtons[index].setText(questions[ui.currentQuestion].answerList[index])


    # reset previously selected answer if there is one
    if not questions[ui.currentQuestion].guess == '':
        for index, value in enumerate(questions[ui.currentQuestion].answerList):
            if  questions[ui.currentQuestion].guess == questions[ui.currentQuestion].answerList[index]:
                radioButtons[index].setChecked(True)

    # show progress
    ui.lblProgress.setText(f'Question {ui.currentQuestion + 1} of {len(questions)} questions')

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

def generate_quest(topic, num_questions):
    '''
    Send a request to the FastAPI server to generate quiz questions based on the provided topic and number of questions.
    '''
    url = "http://localhost:8000/chat"
    prompt = f"Generate a list of {num_questions} multiple choice quiz questions on the topic '{topic}'"
    
    payload = {
        "prompt": prompt,
        "max_tokens": 5000
    }
    
    response = requests.post(url, json=payload)  #calls the FastAPI server /chat
    if response.status_code != 200:
        return f"Error: {response.status_code} - {response.text}"
    
    try:
        json_response = json.loads(response.content.decode("utf-8"))
    except json.JSONDecodeError:
        return 'jsonError'
    temp = json_response['response']
    json_response = json.loads(temp)    
    return json_response
    # print(json_response[0])
def generate_quest_bill(topic, num_questions):
    '''
    Send a request to the FastAPI server to generate quiz questions based on the provided topic and number of questions.
    '''
    url = "http://localhost:8000/chat"
    prompt = f"Generate a list of {num_questions} multiple choice quiz questions on the topic '{topic}' "
    # prompt = f"You are a quiz generator. Your task is to Generate a list of {num_questions} multiple choice {topic} quiz questions and format them as follows: [['question','correct_answer','Choices'[]]] without a newline character"
#     prompt = '''You are a quiz generator.
# Return ONLY valid JSON.
# [
#   {
#     "question": "...",
#     "answer": "...",
#     "choices": ["...", "...", "...", "..."]
#   }
# ]
# '''
# # have to break it here because of the curly braces above fucks with the 'f' string
#     prompt = prompt + f'''
# Generate exactly {num_questions} multiple-choice {topic} questions.

# Do not include Markdown.
# Do not include explanations.
# Do not include any text before or after the JSON.'''
    
    payload = {
        "prompt": prompt,
        "max_tokens": 5000
    }
    
    response = requests.post(url, json=payload) #calls the FastAPI server /chat
    if response.status_code != 200:  #check if the request was successful
        return f"Error: {response.status_code} - {response.text}"
    
    # response = response.json() #convert the response to a JSON object
   
    try:
        # json_response = json.loads(response["response"])   #gives back list of dictionaries with question, options, and answer
        outer = response.json()     
        questions=json.loads(outer["response"])
    except json.JSONDecodeError:
        return 'jsonError'
    
    return questions  # returns a list of questions in dictionary form       #return the list of questions dic's to the caller
   
    ''' 
len(questions)
4

questions[0]
{'question': 'What is 2 + 2?', 'answer': '4', 'choices': ['1', '3', '4', '5']}

questions[0]['question']
'What is 2 + 2?'
questions[0]['answer']
'4'
questions[0]['choices']
['1', '3', '4', '5']
'''
   
    # temp = json.loads(json_response)
    print("hello")
    # print(temp)

if __name__ == "__main__":
    Quiz_GUI_QT6.main()