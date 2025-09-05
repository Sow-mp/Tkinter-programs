import tkinter as tk
import re
from tkinter import messagebox

def validate():
    name=lbl_entry.get()
    Email=lbl1_entry.get()
    Password=lbl2_entry.get()
    confirm=lbl3_entry.get()

    if not name or not Email or not Password or not confirm:
       messagebox.showerror("ERRor","All fields are requirds")
       return

    if Password != confirm:
       messagebox.showerror("Error","password do not match")
       return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
         messagebox.showerror("Error", "Invalid email format")
         return
#if not re.match (r"[^@]+@[^@]+\.[^@]+",Email):
    messagebox.showinfo("successful","Registeration Succesful")

top=tk.Tk()
tk.Label(top,text="Name").pack()
lbl_entry=tk.Entry(top)
lbl_entry.pack()
tk.Label(top,text="Email").pack()
lbl1_entry=tk.Entry(top)
lbl1_entry.pack()
tk.Label(top,text="Password").pack()
lbl2_entry=tk.Entry(top,show="*")
lbl2_entry.pack()
tk.Label(top,text="confirm password").pack()
lbl3_entry=tk.Entry(top,show="*")
lbl3_entry.pack()
tk.Button(top,text="Register",command=validate).pack()
top.mainloop()







