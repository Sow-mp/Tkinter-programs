import tkinter as tk

top=tk.Tk()
frame=tk.Frame(top)
frame.pack()
leftframe=tk.Frame(top)
leftframe.pack()
left=tk.Button(frame,text="add 1")
left.pack(side="left")
right=tk.Button(frame,text="add 2")
right.pack(side="right")
l1=tk.Button(leftframe,text="submit")
l1.pack(side="top")
l2=tk.Button(leftframe,text="add")
l2.pack(side="bottom")

top.mainloop()