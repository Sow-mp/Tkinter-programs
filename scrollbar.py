import tkinter as tk
from tkinter import *

top = tk.Tk()
top.geometry("200x200")
sb = tk.Scrollbar(top)
sb.pack(fill=Y,side="right")

mylist = tk.Listbox(top, yscrollcommand=sb.set)

for line in range(30):
    mylist.insert(END, "Number " + str(line))

mylist.pack(side=LEFT)
sb.config(command=mylist.yview)

top.mainloop()
