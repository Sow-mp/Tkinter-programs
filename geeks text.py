import tkinter as tk


root = tk.Tk()

# specify size of window.
root.geometry("250x170")

# Create text widget and specify size.
T = tk.Text(root, height = 5, width = 52)

# Create label
l =tk.Label(root, text = "Fact of the Day")
l.config(font =("Courier", 14))

Fact = """A man can be arrested in
Italy for wearing a skirt in public."""

# Create button for next text.
b1 = tk.Button(root, text = "Next", )

# Create an Exit button.
b2 = tk.Button(root, text = "Exit",
            command = root.destroy)

l.pack()
T.pack()
b1.pack()
b2.pack()

# Insert The Fact. tk.END
T.insert(tk.END,Fact)

tk.mainloop()

from tkinter import *

# create a root window.
top = Tk()

# create listbox object
listbox = Listbox(top, height = 10,
                  width = 15,
                  bg = "grey",
                  activestyle = 'dotbox',
                  font = "Helvetica",
                  fg = "yellow")

# Define the size of the window.
top.geometry("300x250")

# Define a label for the list.
label = Label(top, text = " FOOD ITEMS")

# insert elements by their
# index and names.
listbox.insert(1, "Nachos")
listbox.insert(2, "Sandwich")
listbox.insert(3, "Burger")
listbox.insert(4, "Pizza")
listbox.insert(5, "Burrito")

# pack the widgets
label.pack()
listbox.pack()


# Display until User
# exits themselves.
top.mainloop()
