# Importing tkinter module
# and all functions
from tkinter import *
from tkinter.ttk import *

# creating master window
master = Tk()

# This method is used to get
# the name of the widget
# which currently has the focus
# by clicking Mouse Button-1
def focus(event):
    widget = master.focus_get()
    print(widget, "has focus")

# Entry widget
e1 = Entry(master)
e1.pack(expand = 1, fill = BOTH)

# Button Widget
e2 = Button(master, text ="Button")
e2.pack(pady = 5)

# Radiobutton widget
e3 = Radiobutton(master, text ="Hello")
e3.pack(pady = 5)

# Here function focus() is binded with Mouse Button-1
# so every time you click mouse, it will call the
# focus method, defined above
master.bind_all("<Button-1>", lambda e: focus(e))

# infinite loop
mainloop()

from tkinter import *
from tkinter import messagebox

# object of TK()
main = Tk()


# function to use the
# askquestion() function
def Submit():
    messagebox.askquestion("Form",
                           "Do you want to Submit")


# setting geometry of window
# instance
main.geometry("100x100")

# creating Window
B1 = Button(main, text="Submit", command=Submit)

# Button positioning
B1.pack()

# infinite loop till close
main.mainloop()

# Imports tkinter and ttk module
from tkinter import *
from tkinter.ttk import *
import time

# toplevel window
root = Tk()


def forget(widget):
    widget.forget()
    print("After Forget method called. Is widget mapped? = ",
          bool(widget.winfo_ismapped()))


def retrieve(widget):
    widget.pack()
    print("After retrieval of widget. Is widget mapped? = ",
          bool(widget.winfo_ismapped()))


# Button widgets
b1 = Button(root, text="Btn 1")
b1.pack()

# This is used to make widget invisible
b2 = Button(root, text="Btn 2", command=lambda: forget(b1))
b2.pack()

# This will retrieve widget
b3 = Button(root, text="Btn 3", command=lambda: retrieve(b1))
b3.pack()

# infinite loop, interrupted by keyboard or mouse
mainloop()