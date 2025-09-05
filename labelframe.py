# !/usr/bin/python3
import tkinter
from tkinter import *

top = Tk()
top.geometry("300x200")

labelframe1 = LabelFrame(top, text="Positive Comments")
labelframe1.pack(fill="both",expand='yes')#it fills both horizontal and vertical

toplabel = Label(labelframe1, text="Place to put the positive comments")
toplabel.pack()

labelframe2 = LabelFrame(top, text="Negative Comments")
labelframe2.pack(fill="both", expand="yes")#it will expand full withen avaliable space

bottomlabel = Label(labelframe2, text="Place to put the negative comments")
bottomlabel.pack()

top.mainloop()


top=Tk()
labelframe1=LabelFrame(top,text="positve comments")
labelframe1.pack(fill="both",expand="yes")
toplabel=Label(labelframe1,text="ffgfffffffffffffffffffff")
toplabel.pack()
labelframe2=LabelFrame(top,text="negative comments")
labelframe2.pack(fill="both",expand="yes")
bottomlabel=Label(labelframe2,text="ffgfffffffffffffffffffff")
bottomlabel.pack()
top.mainloop()

top=Tk()
labelframe1=LabelFrame(top,text="positive comments")

labelframe1.pack(fill='both',expand='yes')
toplabel=Label(labelframe1,text="hfhjfhj hjfghfg")
toplabel.pack()
labelframe2=LabelFrame(top,text="positive comments")

labelframe2.pack(fill='both',expand='yes')
bottomlabel=Label(labelframe2,text="hfh hf")
bottomlabel.pack()
top.mainloop()