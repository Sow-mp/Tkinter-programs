import tkinter as tk
from tkinter import IntVar
from tkinter import messagebox
from pyexpat.errors import messages

top=tk.Tk()
top.title("Button Section")
top.geometry("100x100")

#spin.pack()
# redbutton=tk.Button(top,text="red",activebackground="black",fg="red")
# redbutton.pack(side="left")

name=tk.Label(top,text="Name").grid(row=0,column=0)
#pack(side="left")
rollno=tk.Label(top,text="rollno").grid(row=1,column=0)
sub=tk.Button(top,text="Submit").grid(row= 2,column=0)
e1=tk.Entry(top).grid(row=0,column=1)
e2=tk.Entry(top).grid(row=1,column=1)

tk.messagebox.showinfo("information","info")
tk.messagebox.showerror("Error","info")
tk.messagebox.askyesno("Error","info")
# tk.messagebox.as("Error","info")

# spin=tk.Spinbox(top,from_=0,to=25)

top.mainloop()


