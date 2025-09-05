import tkinter as tk
from tkinter import LEFT, RIGHT

top = tk.Tk()
top.geometry("140x100")
frame = tk.Frame(top)
frame.pack()

leftframe = tk.Frame(top)
leftframe.pack(side=LEFT)

rightframe = tk.Frame(top)
rightframe.pack(side=RIGHT)


btn1 = tk.Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = tk.Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = tk.Button(rightframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = tk.Button(leftframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

top.mainloop()


top=tk.Tk()
frame=tk.Frame(top)
frame.pack()
leftframe=tk.Frame(top)
leftframe.pack(side="left")
rightframe=tk.Frame(top)
rightframe.pack(side="right")
btn1=tk.Button(frame,text="remove",fg='blue')
btn1.pack(side="left")
btn2=tk.Button(leftframe,text="delete",fg='blue',activebackground='red')
btn2.pack(side="left")
btn3=tk.Button(rightframe,text="insert",activeforeground='yellow')
btn3.pack(side="right")
top.mainloop()