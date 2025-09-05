import tkinter as tk
from tkinter import IntVar

window=tk.Tk()
chkbtn=IntVar()

chkbtn1=tk.Checkbutton(window,text="c",variable=chkbtn,onvalue=1,offvalue=0).grid(row=0,column=0)

window.mainloop()