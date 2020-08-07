# Quiz Maker Project
# Goal of this project is to create an application which randomly takes questions
# from a file and compiles it into a quiz.
# For the purpose of making this simple the quizzes will be multiple choice,
# quiz length and subject of quiz can be whatever.

# Import required modules
import PySimpleGUI as sg
import re
import random
from frozendict import frozendict

# Change some gui element colors
sg.theme_input_background_color('black')
sg.theme_input_text_color('green')

# Browse for the questions file to be used to make the quiz
questions_file = sg.popup_get_file('Choose the questions file you wish to generate a quiz from.')

# Create the quiz window
layout = [[(sg.Text('Please type a, b, c, or d for your answers!', size=(40, 1)))],
          [sg.Output(size=(80, 20))],
          [sg.Multiline(size=(70, 0), enter_submits=True),
           sg.Button('SUBMIT', button_color=(sg.YELLOWS[0], sg.BLUES[0])),
           sg.Button('EXIT', button_color=(sg.YELLOWS[0], sg.GREENS[0]))]]

window = sg.Window('Quiz', layout, default_element_size=(30, 2))

# Lists that will contain questions and answers
questions_list = []
answers_list = []

# Opens the questions from the questions folder and appends each question to a list and answer to a separate list
with open(questions_file) as questions:
    if len((questions.readlines())) % 2 != 0:  # Check if the file contains the correct amount of lines
        print(len(questions.readlines()))
        print('Cannot continue')
    else:
        questions.seek(0)  # Reset iterator
        # Store odd num lines in questions and even into answers list
        for position, line in enumerate(questions, 1):
            if position % 2 != 0:
                questions_list.append(line.strip())
            else:
                answers_list.append(line.strip())

# Create a list containing a lists of the answers of each question
answers_to_swap = []
for answer_set in answers_list:
    answer_set = answer_set.replace(' ', '')
    answers_to_swap.append(re.compile('\\D\\)').split(answer_set))

# Dictionaries for holding key-value pairs used later to generate the quiz and calculate score
correct_answers = {}  # Dict mapping the correct answer to the question
answer_dict = {}  # Dict mapping the multiple choice letters to each possible answer
questions_dict = {}  # Dict mapping the questions with the answer dict for that question

# Store the correct answer for the question and shuffle the answer set and store the questions and shuffled answer sets
for answer_set, question in zip(answers_to_swap, questions_list):
    answer_set.pop(0)  # The first value of each list is empty space no idea why just remove it
    correct_answers.update({f'{question}': answer_set[0]})
    random.shuffle(answer_set)
    answer_dict.update(A=answer_set[0])
    answer_dict.update(B=answer_set[1])
    answer_dict.update(C=answer_set[2])
    answer_dict.update(D=answer_set[3])
    questions_dict.update({f'{question}': frozendict(answer_dict)})

# Create the quiz from the questions dict, quiz is randomized each time
# noinspection PyTypeChecker
quiz = dict(random.sample(questions_dict.items(), 5))
quiz_questions = [question for question in quiz.keys()]
quiz_answers = [str(dict(answer)).replace('{', '').replace('}', '').replace("'", '').replace(',', '') for answer in
                quiz.values()]
# Generate the quiz and allow user to answer the quiz questions
input_answers = []  # Store users answers to be compared to later
question_num = 0  # Used to check which question number we are on
check_question_num = 0  # Used to check which question number im comparing the answer key against
num_correct = 0  # Used to store how many answers the user got correct
first_print = 100  # This is the speed at which the information is printed to the gui
printed = False  # Checks to see if the question has been printed
while True:
    # Start reading events and values from the window gui and allow ability to exit
    event, value = window.read(first_print)
    if event == sg.WIN_CLOSED or event == 'EXIT':
        break

    # Generate quiz and take user input
    if question_num < len(quiz):
        first_print = None
        if not printed:
            print(quiz_questions[question_num] + '\n' + quiz_answers[question_num])
            printed = True
        elif event == 'SUBMIT':
            input_answers.append(value[0].strip())
            print(value[0].strip() + '\n')
            question_num += 1
            first_print = 100
            printed = False
    # Calculate the score and print it out
    else:
        answers = [answer for answer in input_answers]
        if check_question_num < len(quiz) and quiz[quiz_questions[check_question_num]][
           answers[check_question_num].upper()] == correct_answers[quiz_questions[check_question_num]]:
            check_question_num += 1
            num_correct += 1
        else:
            first_print = None
            print(f'You got {num_correct} out of {len(quiz)}')

window.close()
