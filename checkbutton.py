import tkinter as tk
from tkinter import Checkbutton, IntVar

# from checkbox import chbtn1

top=tk.Tk()
top.geometry("100x200")
chkvar1=tk.IntVar()
chvar2=tk.IntVar()
chvar3=tk.IntVar()
chbtn1=tk.Checkbutton(top,text='c',variable=chkvar1,onvalue=1,offvalue=0)
chbtn2=tk.Checkbutton(top,text='c++',variable=chvar2,onvalue=1,offvalue=0)
chbtn3=tk.Checkbutton(top,text='Java',variable=chvar3,onvalue=1,offvalue=0)
chbtn1.pack()
chbtn2.pack()
chbtn3.pack()
def show():
    print(f"c:{chkvar1.get()},c++:{chvar2.get()},java:{chvar3.get()}")
btn=tk.Button(top,text="showtext",command=show)
btn.pack()
top.mainloop()


top=tk.Tk()
top.geometry("100x200")
chvar1=tk.IntVar()
chvar2=tk.IntVar()
chvar3=tk.IntVar()

chbtn1=tk.Checkbutton(top,text="c",variable=chvar1,onvalue=1,offvalue=0)
chbtn2=tk.Checkbutton(top,text="c+",variable=chvar2,onvalue=1,offvalue=0)
chbtn3=tk.Checkbutton(top,text="c#",variable=chvar3,onvalue=1,offvalue=0)
chbtn1.pack()
chbtn2.pack()
chbtn3.pack()
def show():
    print(f"c:{chvar1.get()},c+{chvar2.get()},c#:{chvar3.get()}")
btn=tk.Button(top,text="show",command=show)
btn.pack()



top.mainloop()

