import tkinter as tk
from tkinter import IntVar

# from tt import window

window=tk.Tk()
window.geometry("200x200")
b1=tk.Button(window,text="simple")
b1.pack()

b1=tk.Button(window,text="red",activebackground="red",activeforeground="white")
b1.pack(side="left")
b2=tk.Button(window,text="green")
b2.pack(side="right")
b3=tk.Button(window,text="blue")
b3.pack(side="top")
b4=tk.Button(window,text="yelllow")
b4.pack(side="bottom")

window.mainloop()
window=tk.Tk()
checkvar1=IntVar()
checkvar2=IntVar()
checkvar3=IntVar()

checkbtn1=tk.Checkbutton(window,text="C",variable=checkvar1,onvalue=1,offvalue=0,height=10,width=10)
checkbtn2=tk.Checkbutton(window,text="C++",variable=checkvar2,onvalue=1,offvalue=0,height=10,width=10)
checkbtn3=tk.Checkbutton(window,text="java",variable=checkvar3,onvalue=1,offvalue=0,height=10,width=10)
checkbtn1.pack()
checkbtn2.pack()
checkbtn3.pack()
window.mainloop()

window=tk.Tk()

name=tk.Label(window,text="Name").grid(row=0,column=0)
name=tk.Pack()
email=tk.Label(window,text="Email").grid(row=1,column=0)
email=tk.Pack()
password=tk.Label(window,text="Password").grid(row=2,column=0)
password=tk.Pack()
submitbtn=tk.Button(window,text="Submit").grid(row=3,column=0)
submitbtn=tk.Pack()
name=tk.Entry(window).grid(row=0,column=1)
email=tk.Entry(window).grid(row=1,column=1)
password=tk.Entry(window).grid(row=2,column=1)
# submitbtn=tk.Entry(window).grid(row=4,column=1)
window.mainloop()

import tkinter as tk
from functools import partial


def call_result(label_result, n1, n2):
    num1 = (n1.get())
    num2 = (n2.get())
    result = int(num1) + int(num2)
    label_result.config(text="Result = %d" % result)
    return


root = tk.Tk()
root.geometry('400x200+100+200')

root.title('Calculator')

number1 = tk.StringVar()
number2 = tk.StringVar()

labelNum1 = tk.Label(root, text="A").grid(row=1, column=0)

labelNum2 = tk.Label(root, text="B").grid(row=2, column=0)

labelResult = tk.Label(root)

labelResult.grid(row=7, column=2)

entryNum1 = tk.Entry(root, textvariable=number1).grid(row=1, column=2)

entryNum2 = tk.Entry(root, textvariable=number2).grid(row=2, column=2)

call_result = partial(call_result, labelResult, number1, number2)

buttonCal = tk.Button(root, text="Calculate", command=call_result).grid(row=3, column=0)

root.mainloop()

