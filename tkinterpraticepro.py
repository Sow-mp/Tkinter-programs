import tkinter as tk

top=tk.Tk()
lbl=tk.Label(top,text="Name").pack()
e1=tk.Entry(top).pack()
lbl2=tk.Label(top,text="age").pack()
e2=tk.Entry(top).pack()
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
passw_entry = tk.Entry(root, textvariable=passw_var, font=('calibre', 10, 'normal'), show='*')

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
from tkinter import *

root = Tk()
root.geometry("150x200")

w = Label(root, text='GeeksForGeeks',
          font="50")

w.pack()

scroll_bar = Scrollbar(root)

scroll_bar.pack(side=RIGHT,
                fill=Y)

mylist = Listbox(root,
                 yscrollcommand=scroll_bar.set)

for line in range(1, 26):
    mylist.insert("end","Geeks " + str(line))

mylist.pack(side=LEFT, fill=BOTH)

scroll_bar.config(command=mylist.yview)

root.mainloop()
# Python program to illustrate the usage
# of hierarchical treeview in python GUI
# application using tkinter

# Importing tkinter
from tkinter import *

# Importing ttk from tkinter
from tkinter import ttk

# Creating app window
app = Tk()

# Defining title of the app
app.title("GUI Application of Python")

# Defining label of the app and calling a geometry
# management method i.e, pack in order to organize
# widgets in form of blocks before locating them
# in the parent widget
ttk.Label(app, text ="Treeview(hierarchical)").pack()

# Creating treeview window
treeview = ttk.Treeview(app)

# Calling pack method on the treeview
treeview.pack()

# Inserting items to the treeview
# Inserting parent
treeview.insert('', '0', 'item1',
                text ='GeeksforGeeks')

# Inserting child
treeview.insert('', '1', 'item2',
                text ='Computer Science')
treeview.insert('', '2', 'item3',
                text ='GATE papers')
treeview.insert('', 'end', 'item4',
                text ='Programming Languages')

# Inserting more than one attribute of an item
treeview.insert('item2', 'end', 'Algorithm',
                text ='Algorithm')
treeview.insert('item2', 'end', 'Data structure',
                text ='Data structure')
treeview.insert('item3', 'end', '2018 paper',
                text ='2018 paper')
treeview.insert('item3', 'end', '2019 paper',
                text ='2019 paper')
treeview.insert('item4', 'end', 'Python',
                text ='Python')
treeview.insert('item4', 'end', 'Java',
                text ='Java')

# Placing each child items in parent widget
treeview.move('item2', 'item1', 'end')
treeview.move('item3', 'item1', 'end')
treeview.move('item4', 'item1', 'end')

# Calling main()
app.mainloop()

from tkinter import *
from tkinter import messagebox

root = Tk()
root.geometry("300x200")

w = Label(root, text ='GeeksForGeeks', font = "50")
w.pack()

messagebox.showinfo("showinfo", "Information")

messagebox.showwarning("showwarning", "Warning")

messagebox.showerror("showerror", "Error")

messagebox.askquestion("askquestion", "Are you sure?")

messagebox.askokcancel("askokcancel", "Want to continue?")

messagebox.askyesno("askyesno", "Find the value?")


messagebox.askretrycancel("askretrycancel", "Try again?")

root.mainloop()

import tkinter as tk

def on_button_toggle():
    if var.get() == 1:
        print("Checkbutton is selected")
    else:
        print("Checkbutton is deselected")

root = tk.Tk()

# Creating a Checkbutton
var = tk.IntVar()
checkbutton = tk.Checkbutton(root, text="Enable Feature", variable=var,
                             onvalue=1, offvalue=0, command=on_button_toggle)

# Setting options for the Checkbutton
checkbutton.config(bg="lightgrey", fg="blue", font=("Arial", 12),
                   selectcolor="green", relief="raised", padx=10, pady=5)

# Adding a bitmap to the Checkbutton
checkbutton.config(bitmap="info", width=20, height=2)

# Placing the Checkbutton in the window
checkbutton.pack(padx=40, pady=40)

# Calling methods on the Checkbutton
checkbutton.flash()

root.mainloop()