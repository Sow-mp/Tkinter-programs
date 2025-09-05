import tkinter as tk from pyplot as plt
from tkinter import Canvas
from turtledemo.penrose import start

top=tk.Tk()
label=tk.Label(text="Name").place(x=30,y=50)
label1=tk.Label(text="Email").place(x=30,y=90)
label2=tk.Label(text="Password").place(x=30,y=130)
entry1=tk.Entry(top).place(x=80,y=50)
entry2=tk.Entry(top).place(x=85,y=90)
entry3=tk.Entry(top).place(x=95,y=130)
# entry4=tk.Entry(top).place(x=105,y=150)
btn=tk.Button(top,text="Submit")
btn.pack(side="bottom")
c=Canvas(top,bg="pink",height=200,width=200)
arc=c.create_arc(5,10,150,200,start=0,extent=150,fill="white")
c.pack()





top.mainloop()