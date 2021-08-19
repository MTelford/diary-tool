
# TOOL FOR KEEPING A DIARY LOG BASED ON QUESTIONS SPECIFIED AND ASKED BY THE USER


# import used for os specific line seperations
from os import linesep

# import used to check wether users file already exists or needs to be specified
import sys
from os.path import exists


# import used for asking user to specify file location
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
    line_spaces = '\n\n'
    
    while flag:
        users_question = (input(line_spaces + 'Enter your question here, or type QUIT ' + line_spaces))
        if users_question == 'QUIT':
            flag = False
        else:
            question_list.append(users_question)
    
    return question_list



def ask_and_await_answer(question):

    """asks question, waits for answer, then takes date/time, question and answer
    and stores in a log file"""
    
    if question == []:
        return 'No questions, run arg input'

    # asks question
    line_spaces = "\n\n"
    answer = input(line_spaces + question + line_spaces)    
    
    # TAKES ANSWER AND WRITES DATE/TIME, QUESTION AND ANSWER TO SPECIFIED FILE
    
    
    
    # adds datetime, question and answer to file
    destination_file.write(get_datetime_as_string() + line_spaces 
    + question + line_spaces + answer + line_spaces)
    
    destination_file.close()



def format_lines_from_file():

    """"""

    text_lines = questions_file_path_read.readlines()
    # removes new lines from each element in the list before returning
    return [i.replace('\n', '') for i in text_lines]
    




questions_file_path = r"/home/michael-engineer/projects/diary_tool/questions"
log_file_path = r"/home/michael-engineer/projects/diary_tool/test_file"

questions_file_path_read = open(questions_file_path, "r")
questions_file_path_append = open(questions_file_path, "a")
log_file_path_append = open(log_file_path, "a")




# checks if users questions file exists, if so adds contents of lines to list of questions

if exists(questions_file_path):
    users_question_list = format_lines_from_file()
    

    """ THIS AREA takes CLI args to specify which functionality user wants, as follows:
        'input' to update questions
        'ask' to ask the questions user has stored previously
        'clearq' to clear all the users questions
        'reset' to delete all log entries and start over """

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

            # opens file as file object using append parameter
            destination_file = open(log_file_path,'a')

            for i in range(0, len(users_question_list)):
                ask_and_await_answer(users_question_list[i])
            
            destination_file.close()


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
