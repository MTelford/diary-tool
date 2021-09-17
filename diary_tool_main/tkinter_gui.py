from tkinter import *
from tkinter import messagebox
from diary_tool import *


# sets file paths for questions and diary log

questions_path = set_questions_file_path()
log_file_path = set_log_file_path()

# initlialises/configures root window

root = Tk()

root.geometry('1920x1080')
root.minsize('600', '400')
root.maxsize('1920', '1080')
root.title("Diary Tool Application")




# adds window for showing users questions/diary log

log_box = Text(root, width=80, height=20)
log_box.place(relx=0.5, rely=0.25, anchor=CENTER)


# define functions for gui use

def add_questions():
    
    # initialize new window
    input_window = Tk()
    input_window.geometry('600x400+700+370')
    input_window.title("Question Entry Window")

    
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
    
    action = messagebox.askyesnocancel('Warning', 'Are you sure you want to clear your questions?')
    
    if action:   
        # deletes contents of questions file
        open(questions_path, "w").close()
        show_questions()


def reset_log():
    
    # resets contents of the log file to nothing
    action = messagebox.askyesnocancel('Warning', 'Are you sure you want to reset your log?')
    if action:    
        open(log_file_path, 'w').close()
        display_log()  
    

def get_questions():
    question_file = open(questions_path, 'r')
    text_lines = question_file.read().split('\n')

    # filters unwanted empty elements from list
    question_list = list(filter(None, text_lines))
    return question_list


questions_counter = 0

def ask_questions():
     
     # initialize new window
    input_window = Tk()
    input_window.geometry('600x400+700+370')
    input_window.title("My Questions")

    # get questions from file
    questions = get_questions()
        
    # warning if no question available

    if questions == []:
        error_label = Label(input_window, text="No questions")
        error_label.place(relx=0.5, rely=0.5, anchor=CENTER)
    else:
        # initializes question in box
        question_box = Text(input_window, width=40, height=5)
        question_box.place(relx=0.5, rely=0.25, anchor=CENTER)
        
        question_box.insert(END, questions[questions_counter])

        # adds entry field for user to answer questions
        answer_field = Entry(input_window, width=40)
        answer_field.place(relx=0.5, rely=0.5, anchor=CENTER)

        def write_to_log():          
            
            # global var allows us to iterate through list as 
            # this function is called repeatedly
            global questions_counter      

            questions = get_questions()
            log_file = open(log_file_path, 'a')

            log_file.write('\n\n' + get_datetime_as_string() + '\n\n' +
                            questions[questions_counter] + '\n\n' + 
                            answer_field.get() + '\n\n')
            
            log_file.close()
            
            # refreshes answer field for next answer
            answer_field.delete(0, END)            
            
            questions_counter += 1
            question_box.delete(1.0, END)
            
            # inserts new question into question box for user
            if questions_counter < len(questions): 
                question_box.insert(END, questions[questions_counter])
            else:
                messagebox.showinfo('Attention', 'Log entry complete' )
                questions_counter = 0
                input_window.destroy()
         

        # add button to add question
        add_btn = Button(input_window, text='ADD', width=30, command=write_to_log)
        add_btn.place(relx=0.5, rely=0.7, anchor=CENTER)

        input_window.mainloop()


def display_log():

    log_box = Text(root, width=80, height=20)
    log_box.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    log_file = open(log_file_path, 'r')
    log_file_contents = log_file.read()
    
    log_box.insert(END, log_file_contents)

    log_file.close()


def show_questions():
    
    log_box = Text(root, width=80, height=20)
    log_box.place(relx=0.5, rely=0.25, anchor=CENTER)
    
    questions_file = open(questions_path, 'r')
    questions_file_contents = questions_file.read()
    
    log_box.insert(END, questions_file_contents)

    questions_file.close()


# setting up control buttons

ask_questions_btn = Button(root, text="ASK MY QUESTIONS", width=22, command=ask_questions)
input_questions_btn = Button(root, text="INPUT QUESTIONS", width=22, command=add_questions)
show_questions_btn = Button(root, text="SHOW QUESTIONS", width=22, command=show_questions)
display_log_btn = Button(root, text="DISPLAY LOG", width=22, command=display_log)
clear_questions_btn = Button(root, text="CLEAR QUESTIONS", width=22, command=clear_questions)
reset_log_btn = Button(root, text="RESET LOG", width=22, command=reset_log)

# positioning buttons using rel which is relative to parent window

ask_questions_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
input_questions_btn.place(relx=0.5, rely=0.65, anchor=CENTER)
show_questions_btn.place(relx=0.5, rely=0.7, anchor=CENTER)
display_log_btn.place(relx=0.5, rely=0.75, anchor=CENTER)
clear_questions_btn.place(relx=0.5, rely=0.82, anchor=CENTER)
reset_log_btn.place(relx=0.5, rely=0.87, anchor=CENTER)


# keep the window displaying
root.mainloop()

