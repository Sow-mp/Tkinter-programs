import tkinter as tk
import re
from tkinter import messagebox

#from loginform import validate
def validate():
    name=name_entry.get()
    email=email_entry.get()
    password=pass_entry.get()
    Confirm=confirm_entry.get()

    if not name or not email or not password or not Confirm:
        messagebox.showerror("Error","All fields are required ")
        return

    if not re.match(r"[^@]+@[^@]+\.[^@]+",email):
        messagebox.showerror("Error","invalid format")
        return

    if password != Confirm:
        messagebox.showinfo("Error","password do not match")
        return

    messagebox.showinfo("succesful "," registration succesful")

top=tk.Tk()
tk.Label(top,text="Name").pack()
name_entry=tk.Entry(top)
name_entry.pack()
tk.Label(top,text="Email").pack()
email_entry=tk.Entry(top)
email_entry.pack()
tk.Label(top,text="password").pack()
pass_entry=tk.Entry(top,show="*")
pass_entry.pack()
tk.Label(top,text="confirm").pack()
confirm_entry=tk.Entry(top,show="*")
confirm_entry.pack()
tk.Button(top,text="Register",command=validate).pack()
top.mainloop()
