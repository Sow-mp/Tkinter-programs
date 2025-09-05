import tkinter as tk
from tkinter import *
def select():
    sel="your selected option"+str(v.get())
    label.config(text=sel)

top=tk.Tk()
v=DoubleVar()
scale=Scale(top,variable=v,from_=1,to=50,orient="horizontal")
scale.pack()
btn=Button(top,text="Value",command=select)
btn.pack()
label=Label(top)
label.pack()








'''def select():
    sel = "Value = " + str(v.get())
    label.config(text=sel)


top = Tk()
top.geometry("200x100")
v = DoubleVar()
scale = Scale(top, variable=v, from_=1, to=50, orient=HORIZONTAL)
scale.pack(anchor=CENTER)

btn = Button(top, text="Value", command=select)
btn.pack(anchor=CENTER)

label = Label(top)
label.pack()'''

top.mainloop()
