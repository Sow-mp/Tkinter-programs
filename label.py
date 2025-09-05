import tkinter as tk
from tkinter import *

from entrybutton import password, name

top=tk.Tk()
top.geometry("200x200")
lbl=tk.Label(top,text="name",bg="red",justify="center",underline=0).pack()
top.mainloop()

import tkinter as tk

def button_clicked():
    print("Button clicked!")

root = tk.Tk()
btn1=tk.Button(root,text="click me ",bg="red",activebackground="green",font=("arial",12,"bold"),activeforeground="white",fg="gray").pack()

root.mainloop()

import tkinter as tk

top=tk.Tk()
top.geometry("100x100")

name_var=tk.StringVar()

password_var=tk.StringVar()

def submit():
    name=name_var.get()
    password=password_var.get()


    print("name:", name)
    print("password:", password)

    name_var.set("")
    password_var.set("")
name_lbl=tk.Label(top,text="Name").pack()
name_entry=tk.Entry(top,textvariable=name_var).pack()
password_lbl=tk.Label(top,text="pass").pack()
password_entry=tk.Entry(top,textvariable=password_var,show='*').pack()
sub_btn=tk.Button(top,text="submit",command=submit).pack()
top.mainloop()

# Program to make a simple
# login screen


import tkinter as tk

root = tk.Tk()

# setting the windows size
root.geometry("600x400")

# declaring string variable
# for storing name and password
name_var = tk.StringVar()
passw_var = tk.StringVar()


# defining a function that will
# get the name and password and
# print them on the screen
def submit():
    name = name_var.get()
    password = passw_var.get()

    print("The name is : " + name)
    print("The password is : " + password)

    name_var.set("")
    passw_var.set("")


# creating a label for
# name using widget Label
name_label = tk.Label(root, text='Username', font=('calibre', 10, 'bold'))

# creating a entry for input
# name using widget Entry
name_entry = tk.Entry(root, textvariable=name_var, font=('calibre', 10, 'normal'))

# creating a label for password
passw_label = tk.Label(root, text='Password', font=('calibre', 10, 'bold'))

# creating a entry for password
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'),
                       show='*')

# creating a button using the widget
# Button that will call the submit function
sub_btn = tk.Button(root, text='Submit', command=submit)

# placing the label and entry in
# the required position using grid
# method
name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
passw_label.grid(row=1, column=0)
passw_entry.grid(row=1, column=1)
sub_btn.grid(row=2, column=1)

# performing an infinite loop
# for the window to display
root.mainloop()

# This will import tkinter and ttk
from tkinter import *
from tkinter import ttk

root = Tk()

# This will set the geometry to 200x100
root.geometry('200x100')

text1 = StringVar()
text2 = StringVar()

# These text are used to set initial
# values of Checkbutton to off
text1.set('OFF')
text2.set('OFF')

chkbtn1 = ttk.Checkbutton(root, textvariable = text1, variable = text1,
                          offvalue = 'GFG Not Selected',
                          onvalue = 'GFG Selected')

chkbtn1.pack(side = TOP, pady = 10)
chkbtn2 = ttk.Checkbutton(root, textvariable = text2, variable = text2,
                          offvalue = 'GFG Average',
                          onvalue = 'GFG Good')
chkbtn2.pack(side = TOP, pady = 10)

root.mainloop()

# Python Program to search string in text using Tkinter

from tkinter import *

# to create a window
root = Tk()

# root window is the parent window
fram = Frame(root)

# adding label to search box
Label(fram, text='Text to find:').pack(side=LEFT)

# adding of single line text box
edit = Entry(fram)

# positioning of text box
edit.pack(side=LEFT, fill=BOTH, expand=1)

# setting focus
edit.focus_set()

# adding of search button
butt = Button(fram, text='Find')
butt.pack(side=RIGHT)
fram.pack(side=TOP)

# text box in root window
text = Text(root)

# text input area at index 1 in text window
text.insert('1.0', '''Type your text here''')
text.pack(side=BOTTOM)


# function to search string in text
def find():
    # remove tag 'found' from index 1 to END
    text.tag_remove('found', '1.0', END)

    # returns to widget currently in focus
    s = edit.get()
    if s:
        idx = '1.0'
        while 1:
            # searches for desired string from index 1
            idx = text.search(s, idx, nocase=1,
                              stopindex=END)
            if not idx: break

            # last index sum of current index and
            # length of text
            lastidx = '%s+%dc' % (idx, len(s))

            # overwrite 'Found' at idx
            text.tag_add('found', idx, lastidx)
            idx = lastidx

        # mark located string as red
        text.tag_config('found', foreground='red')
    edit.focus_set()


butt.config(command=find)

# mainloop function calls the endless loop of the window,
# so the window will wait for any
# user interaction till we close it
root.mainloop()

import tkinter
from tkinter import *


def callback(input):
    if input.isdigit():
        print(input)
        return True

    elif input is "":
        print(input)
        return True

    else:
        print(input)
        return False


root = Tk()

e = Entry(root)
e.place(x=50, y=50)
reg = root.register(callback)

e.config(validate="key",
         validatecommand=(reg, '% P'))

root.mainloop()