import tkinter
from tkinter import *

from PIL._tkinter_finder import tk

# from Frames import leftframe

top=Tk()
top.geometry("200x200")


chkvar1 = IntVar()

chkvar2 = IntVar()

chkvar3 = IntVar()

chkbtn1 = Checkbutton(top, text="C",variable=chkvar1,  onvalue=1, offvalue=0)

chkbtn2 = Checkbutton(top, text="C++", variable= chkvar2,onvalue=1, offvalue=0)

chkbtn3 = Checkbutton(top, text="Java",variable=chkvar3, onvalue=1, offvalue=0)
chkbtn1.pack()

chkbtn2.pack()

chkbtn3.pack()
def show():
     print(f"c:{chkvar1.get()},c++:{chkvar2.get()},java:{chkvar3.get()}")
btn=Button(top,text="show",command=show).pack()

top.mainloop()


top=tk.Tk()
chvar=IntVar()
chbtn=tk.CheckButton(top,text="c",variable=chvar,onvalue=1,offvalue=0)
chbtn.pack()

top.mainloop()