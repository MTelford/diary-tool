
# TOOL FOR KEEPING A DIARY LOG BASED ON QUESTIONS SPECIFIED AND ASKED BY THE USER


# import used for os specific line seperations
from os import linesep

# import used to check wether users file already exists or needs to be specified
import sys
from os.path import exists


# import used for asking user to specify file location via tkinter GUI window
import tkinter as tk
from tkinter import filedialog

import datetime



def get_users_diary_log_path():
    
    """open file dialog window for user to select which file they want to use
        to store their diary log"""
    # sets up tkinter
    root = tk.Tk()
    root.withdraw()
    
    # asks for file
    path_to_file = filedialog.askopenfilename()
    return path_to_file



def get_datetime_as_string():

    """Function for getting todays date/time as string
        so it can be added to the users diary log"""
    
    x = datetime.datetime.now()
    time_as_string = x.strftime("%c")
    return time_as_string



def get_questions_from_user():

    """ asks user for questions they would like to ask themselves
        and adds them to a list """

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



def ask_and_await_answer(question_list):

    """asks question, waits for answer, then takes date/time, question and answer
    and stores in a log file with appropriate line spacing for readability"""
    

    line_spaces = "\n\n"
    datetime = get_datetime_as_string()
    
    # TAKES ANSWER AND WRITES DATE/TIME, QUESTION AND ANSWER TO SPECIFIED FILE
    
    # opens file as file object using append parameter
    destination_file = open(log_file_path,'a')

    for i in range(0, len(question_list)): 

        
        answer = input(line_spaces + question_list[i] + line_spaces)
        
        # outputs log in correct format for user to log file
       
        destination_file.write(line_spaces + datetime + line_spaces 
        + question_list[i] + line_spaces + answer + line_spaces)
        
    
    destination_file.close()
    
    #add extra line space in terminal for cleanliness
    print('\n')



def format_lines_from_file():

    """formatting used for questions list"""
    
    text_lines = questions_file_path_read.read().split('\n')

    # filters unwanted empty elements from list (streamlines ask command functionality)   
    res = list(filter(None, text_lines))
    return res
    

    
if __name__ == '__main__':


    questions_file_path = r"/home/michael-engineer/projects/diary_tool/questions"
    log_file_path = r"/home/michael-engineer/projects/diary_tool/diary_log"

    # opens file objects as required

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
            print('\n\nNo argument given. Please use "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch\n\n')
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
                # user error message
                if users_question_list == []:
                    
                    flag = True
                    while flag:
                        request = input("\n\n No questions currently stored. Run CLI arg 'input' to update questions, or would you like to update them now? y or n? ")
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
                users_question_list = []
                open(questions_file_path, "w").close()

            
            # deletes everything from the log file

            elif sys.argv[1] == 'reset':
                open(log_file_path, "w").close()

            elif sys.argv[1] == 'help':
                print('\n\nuse "input" to update questions, "ask" to ask your questions, "clearq" to clear your questions, or "reset" to delete all log entries and start from scratch\n\n')

            else:
                print('Invalid input')
