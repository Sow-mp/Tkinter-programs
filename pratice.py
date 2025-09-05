import tkinter as tk

top=tk.Tk()
# top.geometry("100x200")
frame=tk.Frame(top)
frame.pack()
leftframe=tk.Frame(top)
leftframe.pack(side="left")
rightframe=tk.Frame(top)
rightframe.pack(side="right")
b1=tk.Button(frame,text="remove")
b1.pack(side="left")
b2=tk.Button(frame,text="add")
b2.pack(side="right")
b3=tk.Button(leftframe,text="delete")
b3.pack(side="right")
b4=tk.Button(rightframe,text="insert")
b4.pack(side="left")
top.mainloop
