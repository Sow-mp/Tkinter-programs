 # import tkinter as tk

import tkinter as tk
from tkinter import messagebox
import re  # for email validation,regular expression

from entrybutton import Password, password


 # Function to validate form
def validate():
    name = name_entry.get()
    email = email_entry.get()
    password = password_entry.get()
    confirm = confirm_entry.get()

    # Check if all fields are filled
    if not name or not email or not password or not confirm:
        messagebox.showerror("Error", "All fields are required")
        return

    # Email validation (basic)
    if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
        messagebox.showerror("Error", "Invalid email format")
        return

    # Password match check
    if password != confirm:
        messagebox.showerror("Error", "Passwords do not match")
        return

    # If all validations pass
    messagebox.showinfo("Success", "Registration Successful")

# GUI setup
root = tk.Tk()
root.title("Registration Form")
root.geometry("300x300")

# Labels and Entries
tk.Label(root, text="Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Email").pack()
email_entry = tk.Entry(root)
email_entry.pack()

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack()

tk.Label(root, text="Confirm Password").pack()
confirm_entry = tk.Entry(root, show="*")
confirm_entry.pack()

# Submit Button
tk.Button(root, text="Register", command=validate).pack(pady=10)

root.mainloop()

import tkinter as tk
import re

def validate():
    name=lbl_entry.get()
    Email=lbl1_entry.get()
    Password=lbl2_entry.get()
    confirm=lbl3_entry.get()

    if not name or not Email or not Password or confirm:
       messagebox.showerror("ERRor","All fields are requirds")
       return

    if Password != confirm:
       messagebox.showerror("Error","password do not match")
       return

    if not re.match(r"[^@]+@[^@]+\.[^@]+", Email):
         messagebox.showerror("Error", "Invalid email format")
         return

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