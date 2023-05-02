from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import (QApplication, QWidget, QHBoxLayout, QVBoxLayout, QGroupBox, QButtonGroup, QRadioButton, QPushButton, QLabel, QGroupBox)
from random import shuffle

class Question():
    def __init__(self, question, right_answer, wrong1, wrong2, wrong3):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3

question_list = list()  
question_list.append(Question('Сколько месецов в году', '12', '4', '55', '3'))
question_list.append(Question('Какой язык в Беларуси ?', 'Беларуский', 'Русский', 'Английский', 'Китайский'))
question_list.append(Question('Ты учишь Китайский ?', 'Да', 'нет', 'незнаю', 'конечно нет'))
question_list.append(Question('Какой сейчас год ?', '2023', '3333', '6666', '1111'))
app = QApplication([])

window = QWidget()
window.setWindowTitle('Memory Card')
window.move(800, 400)
window.resize(400, 200)
btn_OK = QPushButton('Ответить')
lb_Question = QLabel('Какой национальности не существует?')
eror = QLabel('Надо ответить на вопрос')

RadioGroupBox = QGroupBox("Варианты ответов") 
rbtn_1 = QRadioButton('Энцы')
rbtn_2 = QRadioButton('Чулымцы')
rbtn_3 = QRadioButton('Смурфы')
rbtn_4 = QRadioButton('Алеуты')

RadioGroup = QButtonGroup()
RadioGroup.addButton(rbtn_1)
RadioGroup.addButton(rbtn_2)
RadioGroup.addButton(rbtn_3)
RadioGroup.addButton(rbtn_4)
layout_ans1 = QHBoxLayout()   
layout_ans2 = QVBoxLayout() 
layout_ans3 = QVBoxLayout()
layout_ans2.addWidget(rbtn_1)
layout_ans2.addWidget(rbtn_2)
layout_ans3.addWidget(rbtn_3) 
layout_ans3.addWidget(rbtn_4)

layout_ans1.addLayout(layout_ans2)
layout_ans1.addLayout(layout_ans3)

RadioGroupBox.setLayout(layout_ans1)

AnsGroupBox = QGroupBox('Результат теста')
lb_Result = QLabel('прав ты или нет?')
lb_Correct = QLabel('ответ будет тут!')

Statys = QGroupBox('')

layout_line1 = QVBoxLayout()
layout_line1.addWidget(lb_Result, alignment=Qt.AlignLeft)
layout_line1.addWidget(lb_Correct, alignment=Qt.AlignCenter)

AnsGroupBox.setLayout(layout_line1)

layout_line1 = QHBoxLayout()
layout_line2 = QHBoxLayout()
layout_line3 = QHBoxLayout()
layout_line4 = QVBoxLayout()
layout_line5 = QVBoxLayout

layout_line1.addWidget(lb_Question, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
layout_line2.addWidget(RadioGroupBox)   
layout_line2.addWidget(AnsGroupBox)  
AnsGroupBox.hide() 

def show_result():
    layout_line4.setHidden()
    RadioGroupBox.hide()
    AnsGroupBox.show()
    btn_OK.setText('Следующий вопрос')


def show_question():
    RadioGroupBox.show()
    AnsGroupBox.hide()
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)

answers = [rbtn_1, rbtn_2, rbtn_3, rbtn_4]

def ask(q):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    lb_Question.setText(q.question)
    lb_Correct.setText(q.right_answer)
    btn_OK.setText('Ответить')
    RadioGroup.setExclusive(False)
    rbtn_1.setChecked(False)
    rbtn_2.setChecked(False)
    rbtn_3.setChecked(False)
    rbtn_4.setChecked(False)
    RadioGroup.setExclusive(True)
    AnsGroupBox.hide()
    RadioGroupBox.show()

def show_correct(res):
    eror.setText('')
    RadioGroupBox.hide()
    AnsGroupBox.show()
    lb_Correct.setText(res) 
    btn_OK.setText('Следующий вопрос')

window.vyes = 0
def check_answer():
    if answers[0].isChecked() == True:
        show_correct('Правильно')
        window.vyes += 1
    else:
        show_correct('Неправильно')
def next_question():
    window.question += 1
    if window.question == len(question_list):
        window.question = 0
    print('Статистика')
    print('-Всего вопросов:',window.question + 1)
    print('-Правильных ответов:', window.vyes)
    print('Рейтинг:', (window.vyes / len(question_list)) * 100, '%')
    q = question_list[window.question]
    ask(q)


def click_ok():
    if btn_OK.text() == 'Ответить':
        if rbtn_1.isChecked() == True or rbtn_2.isChecked() == True or rbtn_3.isChecked() == True or rbtn_4.isChecked() == True:
            check_answer()
        else:
            eror.setText('Надо ответить на вопрос')
            layout_line4.addWidget(eror, alignment=(Qt.AlignHCenter | Qt.AlignVCenter))
    else:
        next_question()
window.question = -1

layout_line3.addStretch(1)
layout_line3.addWidget(btn_OK, stretch=2) 
layout_line3.addStretch(1)

layout_card = QVBoxLayout()

layout_card.addLayout(layout_line1, stretch=2)
layout_card.addLayout(layout_line2, stretch=8)
layout_card.addStretch(1)
layout_card.addLayout(layout_line3, stretch=1)
layout_card.addStretch(1)
layout_card.setSpacing(5)
layout_card.addLayout(layout_line4, stretch=3)

window.setLayout(layout_card)

q = Question('Какой национальности не существует?','Энцы', 'Чулымцы','Смурфы','Алеуты'  )
ask(q)

btn_OK.clicked.connect(click_ok)

window.show()
app.exec_()