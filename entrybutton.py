from tkinter import *

top = Tk()

top.geometry("400x250")

name = Label(top, text="Name").place(x=30, y=50)

email = Label(top, text="Email").place(x=30, y=90)

password = Label(top, text="Password").place(x=30, y=130)

sbmitbtn = Button(top, text="Submit", activebackground="pink", activeforeground="blue").place(x=30, y=170)

e1 = Entry(top).place(x=80, y=50)

e2 = Entry(top).place(x=80, y=90)

e3 = Entry(top).place(x=95, y=130)

top.mainloop()


top=Tk()
Name=Label(top,text="Name").grid(row=0,column=0)
Password=Label(top,text='Password').grid(row=1,column=0)
Age=Label(top,text='Age').grid(row=2,column=0)
btn=Button(top,text="Submit",bg='red',fg='blue').grid(row= 3,column=0)
e1=Entry(top).grid(row=0,column=1)
e2=Entry(top).grid(row=1,column=1)
e3=Entry(top).grid(row= 2,column= 1)
top.mainloop()






















