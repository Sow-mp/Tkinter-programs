import tkinter as tk
from tkinter import *

def selection():
    selection="you selected this option"+str(radio.get())
    label.config(text=selection)#changes or update the text,color,font of the widget
top=tk.Tk()
radio=tk.IntVar()
lbl=tk.Label(text="your favourite programming language")
lbl.pack()
rd1=tk.Radiobutton(top,variable=radio,text="c",value=1,command=selection)
rd1.pack(anchor=W)#anchor it is the option in pack ,W means west side(left)
rd2=tk.Radiobutton(top,variable=radio,text="c++",value=2,command=selection)
rd2.pack(anchor=W)
rd3=tk.Radiobutton(top,variable=radio,text="c#",value=3,command=selection)
rd3.pack(anchor=W)
#label=tk.Button(top,text="submit",activeforeground="red",bg="blue").pack(side='left')
label =tk.Label(top)
label.pack()
top.mainloop()

def selection():
    select="you selecte this option"+str(radio.get())
    label.config(text=select)


top=tk.Tk()
radio=tk.IntVar()
rd1=tk.Radiobutton(top,text="c++",variable=radio,value=1,command=selection)
rd1.pack()
rd1=tk.Radiobutton(top,text="c#",variable=radio,value=2,command=selection)
rd1.pack()
label=tk.Label(top)
label.pack()
top.mainloop()