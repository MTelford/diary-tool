# tool for keeping a diary log based on questions specified and asked by the user


from os import linesep
import sys
from os.path import exists

import tkinter as tk
from tkinter import filedialog

import datetime



def get_file_path():
    
    """open file dialog window for text file location selection"""
    
    root = tk.Tk()
    root.withdraw()
    path_to_file = filedialog.askopenfilename()
    return path_to_file



def get_datetime_as_string():

    """Function for getting todays date/time as string"""
    
    x = datetime.datetime.now()
    time_as_string = x.strftime("%c")
    return time_as_string



def get_questions_from_user():

    """ asks user for questions they would like to ask themselves
        and adds them to a list"""

    flag = True
    question_list = []
    
    while flag:
        users_question = (input('\n\n' + 'Enter your question here, or type QUIT \n\n' + ''))
        if users_question == 'QUIT':
            flag = False
        else:
            question_list.append(users_question)
    
    return question_list



def ask_and_await_answer(question):

    """asks question, waits for answer, then takes date/time, question and answer
    and stores in a file"""
    
    if question == []:
        return 'No questions, run arg input'

    # asks question
    line_spaces = "\n\n"
    answer = input(line_spaces + question + line_spaces)
    
    
    # takes answer and writes date/time, question and answer to specified file
    
    # opens file as file object using append parameter
    destination_file = open(log_file_path,'a')
    
    # adds datetime question and answer to file
    destination_file.write(get_datetime_as_string() + line_spaces 
    + question + line_spaces + answer + line_spaces)
    
    destination_file.close()
    




def format_lines_from_file():

    text_lines = questions_file_path_read.readlines()
    # removes new lines from each element in the list before returning
    return [i.replace('\n', '') for i in text_lines]
    




questions_file_path = r"/home/michael-engineer/projects/diary_tool/questions"
log_file_path = r"/home/michael-engineer/projects/diary_tool/test_file"

questions_file_path_read = open(questions_file_path, "r")
questions_file_path_append = open(questions_file_path, "a")
log_file_path_append = open(log_file_path, "a")




# checks if file exists, if so adds contents of lines to list of questions

if exists(questions_file_path):
    users_question_list = format_lines_from_file()
    


    if len(sys.argv) < 2:
        print('No argument given. Please use "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch')
    elif len(sys.argv) > 2:
        print('Too many arguments given, only 1 is required')
    else:
        
        # asks user to input their questions
        
        if sys.argv[1] == 'input':

            questions = get_questions_from_user()

            # iterates through list of questions and writes to questions file
            for i in questions:

                questions_file_path_append.write((i + '\n\n'))
            

        # asks the user the questions that the input and stores results in log file

        elif sys.argv[1] == 'ask':

            for i in range(0, len(users_question_list)):
                ask_and_await_answer(users_question_list[i])


        # clears the users question file

        elif sys.argv[1] == 'clearq':
            users_question_list = []
            open(questions_file_path, "w").close()

        
        # deletes everything from the log file for a fresh start

        elif sys.argv[1] == 'reset':
            open(log_file_path, "w").close()

        elif sys.argv[1] == 'help':
            print('use "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch')

        else:
            print('Invalid input')
