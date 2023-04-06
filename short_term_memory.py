# pylint: disable=C0114, W0603, W0602, C0301
import random
from tkinter import Tk, Label, Entry, StringVar, Button

CORRECT = 0
FAIL = -1
COUNTER = NUMBER = 6
PROBLEM = 3
ANSWER_LIST = []
INPUT_LIST = []

def game_restart():
    """
    Update the text and score label
    """
    global COUNTER, FAIL, CORRECT, NUMBER, ANSWER_LIST, INPUT_LIST
    COUNTER = NUMBER
    CORRECT = 0
    FAIL = -1
    ANSWER_LIST = []
    INPUT_LIST = []
    correct_label.config(text="Correct : " + str(CORRECT))
    fail_label.config(text="Fail : " + str(FAIL + 1))
    goto_next()

def show_result():
    """
    Show the result in window
    """
    ANSWER_LIST.pop(0)
    INPUT_LIST.pop(0)
    label.config(fg="black", text= '\n'.join([f"{x[0]} - {x[1]}" for x in zip(ANSWER_LIST, INPUT_LIST)]))
    input_str.set('')
    input_entry.delete(0,'end')
    input_entry.pack_forget()
    next_btn.config(text="R E S T A R T")

def update_counter():
    """
    Set the time
    """
    global COUNTER
    if COUNTER > 0:
        COUNTER -= 1
        time_label.config(text="Time : " + str(COUNTER))
        window.after(1000, update_counter)

def reset_time():
    """
    Reset the time
    """
    global COUNTER, NUMBER
    COUNTER = NUMBER
    time_label.config(fg="black", text="Time : " + str(COUNTER))
    update_counter()

def get_random_string(str_len):
    """
    Generate random string
    """
    #letters = [chr(random.randint(97, 122)) for _ in range(str_len)]
    letters = [chr(random.randint(65, 90)) for _ in range(str_len)]
    result = ''.join(letters)
    return result

def add_score():
    """
    Validate the input and add score
    """
    global CORRECT, FAIL, ANSWER_LIST, INPUT_LIST
    ANSWER_LIST.append(label.cget('text'))
    INPUT_LIST.append(input_str.get())

    if input_str.get() == label.cget('text'):
        CORRECT += 1
        correct_label.config(text="Correct : " + str(CORRECT))
    else:
        FAIL += 1
        fail_label.config(text="Fail : " + str(FAIL))

def input_step():
    """
    Hide the label and show the input entry
    """
    label.config(fg="#7AFEC6")
    time_label.config(fg="#7AFEC6")
    input_entry.pack()
    next_btn.pack(pady='10')
    next_btn.config(text="N E X T")

def goto_next():
    """
    Go to next stage
    """
    next_btn.config(command=goto_next)
    if len(ANSWER_LIST) + 1 <= PROBLEM:
        #Into the input step and validate
        window.after(NUMBER * 1000,input_step)
        label.config(fg="black")
        add_score()

        #Clear the last round of string and reset time
        input_str.set('')
        input_entry.delete(0,'end')
        input_entry.pack_forget()
        next_btn.pack_forget()
        label.config(text=get_random_string(len(ANSWER_LIST)*2))
        reset_time()
    else:
        add_score()
        show_result()
        next_btn.config(command=game_restart)


window = Tk()
window.title("Short Term Memory")
window.configure(bg="#7AFEC6")
window.minsize(width=500, height=450)
window.resizable(width=False, height=False)

correct_label = Label(text="Correct : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
fail_label = Label(text="Fail : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
time_label = Label(text="Time : 0", font=("Arial", 10, "bold"), bg="#7AFEC6", fg="black")
label = Label(text=get_random_string(2), font=("Arial", 20, "bold"),
               padx=5, bg="#7AFEC6", fg="black")

correct_label.pack(anchor="n", side="left", padx="30")
fail_label.pack(anchor="n", side="right", padx="40")
time_label.pack(anchor="n", side="top", padx="30")
label.pack(pady="100")

input_str = StringVar()
input_entry = Entry(window, bd=2 ,font=50, relief="solid", textvariable=input_str)
input_entry.pack()

next_btn = Button(height=2, width=10, command=goto_next, text="N E X T",
                  font=("Arial", 10, "bold"), bg="black",fg="white")
next_btn.pack(pady='10')

goto_next()

window.mainloop()
