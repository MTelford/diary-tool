from tkinter import *
from diary_tool import *


# sets file paths for questions and diary log

questions_path = set_questions_file_path()
log_file_path = set_log_file_path()

# initlialises/configures root window

root = Tk()

root.geometry('1920x1080')
root.minsize('600', '400')
root.maxsize('1920', '1080')

# define functions for gui use

def test_func():
    myLabel = Label(root, text="hello")
    myLabel.pack()

def add_questions():
    
    # initialize new window
    input_window = Tk()
    input_window.geometry('600x400+700+370')
    
    # add input field
    input_field = Entry(input_window, width=40, justify='center')
    input_field.place(relx=0.5, rely=0.3, anchor=CENTER)
    
    # function for adding question to question file
    def add_question():
        users_question = input_field.get()
        questions_file = open(questions_path, 'a')
        questions_file.write(users_question + '\n\n')                
        input_field.delete(0, END)
        
    # add question button
    add_btn = Button(input_window, width=10, text='ADD', command=add_question)
    add_btn.place(relx=0.5, rely=0.5, anchor=CENTER)    
    
    # quit from adding questions
    quit_btn = Button(input_window, width=10, text='QUIT', command=input_window.destroy)
    quit_btn.place(relx=0.5, rely=0.6, anchor=CENTER)

    #mainloop
    input_window.mainloop()

    
def clear_questions():
    # resets the list that stores the questions for writing
    question_list = []

    # deletes contents of questions file
    open(questions_path, "w").close()


def reset_log():
    # resets contents of the log file to nothing
    open(log_file_path, 'w').close()  


def get_questions():
    question_file = open(questions_path, 'r')
    text_lines = question_file.read().split('\n')

    # filters unwanted empty elements from list
    question_list = list(filter(None, text_lines))
    return question_list






def ask_questions():
     # initialize new window
    input_window = Tk()
    input_window.geometry('600x400+700+370')
    
    # get questions from file
    questions = get_questions()
    

    if questions == []:
        error_label = Label(input_window, text="No questions")
        error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        # initializes question in box
        question_box = Text(input_window, width=40, height=5)
        question_box.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        question_box.insert(END, questions[0])

        # adds entry field for user to answer questions
        answer_field = Entry(input_window, width=40)
        answer_field.place(relx=0.5, rely=0.5, anchor=CENTER)

        def write_to_log():
            
            questions_counter = 0
            flag = True

            while flag:
                questions = get_questions()
                log_file = open(log_file_path, 'a')

                log_file.write(get_datetime_as_string() + '\n\n' +
                                questions[questions_counter] + '\n\n' + 
                                answer_field.get() + '\n\n')
                answer_field.delete(0, END)
                questions_counter += 1
            
         

        # add button to add question
        add_btn = Button(input_window, text='ADD', width=30, command=write_to_log)
        add_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        input_window.mainloop()







# setting up control buttons

ask_btn = Button(root, text="ASK MY QUESTIONS", width=22, command=ask_questions)
input_questions_btn = Button(root, text="INPUT QUESTIONS", width=22, command=add_questions)
clear_questions_btn = Button(root, text="CLEAR QUESTIONS", width=22, command=clear_questions)
reset_log_btn = Button(root, text="RESET LOG", width=22, command=reset_log)

# positioning buttons using rel which is relative to parent window

ask_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
input_questions_btn.place(relx=0.5, rely=0.65, anchor=CENTER)
clear_questions_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
reset_log_btn.place(relx=0.5, rely=0.75, anchor=CENTER)


# keep the window displaying
root.mainloop()

