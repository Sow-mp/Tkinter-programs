import tkinter as tk
from tkinter import messagebox


window=tk.Tk()


def fun():
    tk.messagebox.showinfo("hello","hi how r u")


btn1=tk.Button(window,text="Submit",bg="red",fg="green")
btn1.pack(side="left")
btn2=tk.Button(window,text="insert",command=fun,bg="red",fg="green")
btn2.pack(side="right")


window.mainloop()