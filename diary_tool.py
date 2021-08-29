
# TOOL FOR KEEPING A DIARY LOG BASED ON QUESTIONS SPECIFIED AND ASKED BY THE USER


# import used for os specific line seperations
from os import linesep

# import used to check wether users file already exists or needs to be specified
import sys
from os.path import exists
import os

# import used for asking user to specify file location via tkinter GUI window
import tkinter as tk
from tkinter import filedialog

import datetime



# def get_users_diary_log_path():
    
#     """open file dialog window for user to select which file they want to use
#         to store their diary log"""
#     # sets up tkinter
#     root = tk.Tk()
#     root.withdraw()
    
#     # asks for file
#     path_to_file = filedialog.askopenfilename()
#     return path_to_file



def get_datetime_as_string():

    """Function for getting todays date/time as string
        so it can be added to the users diary log"""
    
    x = datetime.datetime.now()
    time_as_string = x.strftime("%c")
    return time_as_string



def get_questions_from_user():

    """ asks user for questions they would like to ask themselves
        and adds them to a list, which is later used in function
        'ask and await answer'. Exits upon user typing QUIT """

    flag = True
    question_list = []
    
    while flag:
        users_question = (input('\n\nEnter your question here, or type QUIT \n\n'))
        if users_question == 'QUIT':
            flag = False
        else:
            question_list.append(users_question)
    
    return question_list



def ask_and_await_answer(question_list):

    """asks question, waits for answer, then takes date/time, question and answer
    and stores in a log file with appropriate line spacing for readability"""
    

    datetime = get_datetime_as_string()
    
    # TAKES ANSWER AND WRITES DATE/TIME, QUESTION AND ANSWER TO SPECIFIED FILE
    
    # opens file as file object using append parameter
    destination_file = open(log_file_path,'a')

    for i in range(0, len(question_list)): 

        
        answer = input('\n\n' + question_list[i] + '\n\n')
        
        # outputs log in correct format for user to log file
       
        destination_file.write('\n\n' + datetime + '\n\n' 
        + question_list[i] + '\n\n' + answer + '\n\n')
        
    
    destination_file.close()
    
    #add extra line space in terminal for cleanliness
    print('\n')




    
if __name__ == '__main__':


    """ sets up file paths"""

    current_file_path = os.path.realpath(__file__)
    
    # sets file path for users questions dynamically
    current_file_path.replace('diary_tool.py', 'questions')      
    
    questions_file_path = current_file_path.replace('diary_tool.py', 'questions')
    log_file_path = current_file_path.replace('diary_tool.py', 'diary_log')

    # opens file objects in either read or amend as appropriate

    questions_file_path_read = open(questions_file_path, "r")
    questions_file_path_append = open(questions_file_path, "a")
    log_file_path_append = open(log_file_path, "a")


    # adds contents of questions file lines to list of questions
    
    text_lines = questions_file_path_read.read().split('\n')

    # filters unwanted empty elements from list (streamlines ask command functionality)   
    users_question_list = list(filter(None, text_lines))
    
    
        

    """ THIS AREA takes CLI args to specify which functionality user wants, as follows:
        'input' to update questions
        'ask' to ask the questions user has stored previously
        'clearq' to clear all the users questions
        'reset' to delete all log entries and start over """

    
    if len(sys.argv) < 2:
        print('\n\nNo argument given. Please use "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch\n\n')
    
    elif len(sys.argv) > 2:
        print('Too many arguments given, only 1 is required')
    
    else:
        
        # asks user to input their questions
        
        if sys.argv[1] == 'input':

            questions = get_questions_from_user()

            # then iterates through list of questions and writes to questions file
            for i in questions:

                questions_file_path_append.write((i + '\n\n'))
            

        # asks the user the questions that they previously input and stores results in log file
        # or if no questions are present, they are given the option to store questions with y or n

        elif sys.argv[1] == 'ask':
            
            if users_question_list == []:
                
                flag = True
                while flag:
                    request = input("\n\n No questions currently stored. Run CLI arg 'input' to update questions, or would you like to update them now? y or n? \n\n")
                    
                    if request == 'y':
                        flag = False
                        questions = get_questions_from_user()
                        # iterates through list of questions and writes to questions file
                        for i in questions:
                            questions_file_path_append.write((i + '\n\n'))                      
                    elif request == 'n':
                        break
                    else:
                        print("\n\nPlease enter y or n to continue")
                    
            if users_question_list != []:
                ask_and_await_answer(users_question_list)    
            


        # clears the users question file

        elif sys.argv[1] == 'clearq':
            # resets the list that store the questions for writing
            users_question_list = []
            # deletes contents of questions file
            open(questions_file_path, "w").close()
            print('\n\nQuestions cleared\n\n')

        
        # deletes everything from the log file

        elif sys.argv[1] == 'reset':
            open(log_file_path, "w").close()
            print('\n\nDiary log reset\n\n')

        elif sys.argv[1] == 'help':
            print('\n\nuse "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch\n\n')

        else:
            print('Invalid input')
