import tkinter as tk


top=tk.Tk()
top.geometry("100x100")
top.title("GeeksForGeeks")
chk1=tk.IntVar()
chk2=tk.IntVar()
def submit():
 print(f"c+:{chk1.get()},c:{chk2.get()}")


lbl=tk.Label(top,text="programming lang").pack()
chbtn1=tk.Checkbutton(top,text="c+",variable=chk1,onvalue=1,offvalue=0)
chbtn1.pack()
chbtn2=tk.Checkbutton(top,text="c",variable=chk2,onvalue=1,offvalue=0)
chbtn2.pack()
btn1=tk.Button(top,text="submit",command=submit)
btn1.pack()
top.mainloop()

# Importing Tkinter module
from tkinter import *
# from tkinter.ttk import *

# Creating master Tkinter window
master = Tk()
master.geometry("175x175")

# Tkinter string variable
# able to store any string value
v = StringVar(master, "1")

# Dictionary to create multiple buttons
values = {"RadioButton 1" : "1",
          "RadioButton 2" : "2",
          "RadioButton 3" : "3",
          "RadioButton 4" : "4",
          "RadioButton 5" : "5"}

# Loop is used to create multiple Radiobuttons
# rather than creating each button separately
for (text, value) in values.items():
    Radiobutton(master, text = text, variable = v,
                value = value, indicator = 0,
                background = "light blue").pack(fill = X, ipady = 5)

# Infinite loop can be terminated by
# keyboard or mouse interrupt
# or by any predefined function (destroy())
mainloop()