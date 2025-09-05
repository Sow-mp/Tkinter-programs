import tkinter as tk
from tkinter import Listbox
from tkinter.constants import ANCHOR
from tkinter.ttk import Label

top=tk.Tk()
top.title("listbox")
lbl=tk.Label(top,text="list of favourity contries")
lbl.pack()
listbox=tk.Listbox(top)
listbox.insert(1,"USA")
listbox.insert(2,"germany")
listbox.insert(3,"Russia")
listbox.pack()
btn=tk.Button(top,text="delete",command = lambda:listbox.delete(tk.ANCHOR))
btn.pack()
top.mainloop()


top=tk.Tk()
lbl=Label(top,text="fvfn")
lbl.pack()
l1=Listbox(top)
l1.pack()
l1.insert(1,'java')
l1.insert(2,"xyz")
l1.insert(3,"abc")
btn=tk.Button(top,text="delete",command=lambda l1=l1:l1.delete(tk.ANCHOR))
btn.pack()
top.mainloop()