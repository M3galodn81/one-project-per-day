# Basic Tkinter Application : Created on 2024-09-29

from tkinter import Label, Tk, Button

global number
number = 0

root = Tk()
root.title("Test") 

header_text = Label(root, text = "Welcome to Basic Tkinter App")

def increment_num():
    global number
    number += 1
    number_label.config(text=number)


increment_button = Button(root, text = "Increment" , width= 30, command=increment_num)
number_label = Label(root, text= number)

stop_button = Button(root, text = "Stop" , width= 30, command = root.destroy)

header_text.pack()
number_label.pack()
increment_button.pack()
stop_button.pack()

root.mainloop()