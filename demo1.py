import tkinter as tk
from tkinter import messagebox

window=tk.Tk()
window.title("Demo")
window.geometry("600x200")
'''l1=tk.Label(window,text="enter the name")
l1.grid(column=0,row=0)
t1=tk.Entry(window)
t1.grid(column=1,row=0)
def clicked():
     res="welcome to"+t1.get()
     l1.configure(text=res)

bt=tk.Button(window,text="Enter",command=clicked)
bt.grid(column=1,row=1)'''
def fun():
     messagebox.showinfo("hi ","red button is clicked")

b1=tk.Button(window,text="red",command=fun,activeforeground="red",activebackground="pink",pady=10)
b2=tk.Button(window,text="yellow",activeforeground="red",activebackground="pink",pady=10)

b1.pack(side=tk.LEFT)
b2.pack(side=tk.RIGHT)




window.mainloop()
