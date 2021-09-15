from tkinter import *

root = Tk()

# change root window h, w and border

root.geometry('1920x1080')
root.minsize('600', '400')
root.maxsize('1920', '1080')


# setting up control buttons

ask_btn = Button(root, text="ASK MY QUESTIONS", width=22)

input_btn2 = Button(root, text="INPUT QUESTIONS", width=22)
input_btn3 = Button(root, text="CLEAR QUESTIONS", width=22)
input_btn4 = Button(root, text="RESET LOG", width=22)

# positioning buttons using rel which is relative to parent window

ask_btn.place(relx=0.5, rely=0.6, anchor=CENTER)
input_btn2.place(relx=0.5, rely=0.65, anchor=CENTER)
input_btn3.place(relx=0.5, rely=0.7, anchor=CENTER)
input_btn4.place(relx=0.5, rely=0.75, anchor=CENTER)


# keep the window displaying
root.mainloop()

