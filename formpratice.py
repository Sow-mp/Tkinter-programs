import tkinter as tk

top=tk.Tk()
lb1=tk.Label(top,text="Name").grid(row=0,column=0)
lb1=tk.Entry(top).grid(row=0,column=1)
lb2=tk.Label(top,text="Age").grid(row=1,column=0)
lb2=tk.Entry(top).grid(row=1,column=1)

top.mainloop()
from tkinter import *
from tkinter import messagebox

# Root window
root = Tk()
root.title("Login & Sign Up Form")
root.geometry("400x300")
root.resizable(False, False)

# ==== Functions ====
def show_signup():
    login_frame.pack_forget()
    signup_frame.pack()

def show_login():
    signup_frame.pack_forget()
    login_frame.pack()

def login():
    username = login_username.get()
    password = login_password.get()
    if username == "admin" and password == "1234":
        messagebox.showinfo("Login", "Login Successful!")
    else:
        messagebox.showerror("Login Failed", "Invalid credentials.")

def signup():
    username = signup_username.get()
    password = signup_password.get()
    confirm = signup_confirm.get()
    if password != confirm:
        messagebox.showerror("Sign Up Failed", "Passwords do not match!")
    else:
        messagebox.showinfo("Sign Up", "Account created successfully!")
        show_login()

# ==== Login Frame ====
login_frame = Frame(root)

Label(login_frame, text="Login", font=("Arial", 16)).pack()

Label(login_frame, text="Username").pack()
login_username = Entry(login_frame)
login_username.pack()

Label(login_frame, text="Password").pack()
login_password = Entry(login_frame, show="*")
login_password.pack()

Button(login_frame, text="Login", command=login).pack(pady=10)
Button(login_frame, text="Create Account", command=show_signup).pack()

login_frame.pack()

# ==== Sign Up Frame ====
signup_frame = Frame(root)

Label(signup_frame, text="Sign Up", font=("Arial", 16)).pack(pady=10)

Label(signup_frame, text="Username").pack()
signup_username = Entry(signup_frame)
signup_username.pack()

Label(signup_frame, text="Password").pack()
signup_password = Entry(signup_frame, show="*")
signup_password.pack()

Label(signup_frame, text="Confirm Password").pack()
signup_confirm = Entry(signup_frame, show="*")
signup_confirm.pack()

Button(signup_frame, text="Sign Up", command=signup).pack(pady=10)
Button(signup_frame, text="Back to Login", command=show_login).pack()

# ==== Run App ====
root.mainloop()



def login():
    username=login_entry1.get()
    password=login_entry2.get()

    if username=="sow" and password=="1234":
        messagebox.showinfo("login","login successful")
    else:
        messagebox.showinfo("login failed","invalid")

def sign_up():
    username=signup_entry.get()
    password=signup_entry1.get()
    confirm_password=signup_entry2.get()
    if password!=confirm_passsword:
        messagebox.showerror("fail","invalid")
    else:
        messagebox.showinfo("login","successful")

root=tk.Tk()
root.title("Login-Form")
login_frame=Frame(root).pack()
login_lbl=tk.Label(login_frame,text="Login",font=("Arial",12)).pack()
login_username=tk.Label(login_frame,text="username").pack()
login_entry1=tk.Entry(login_frame)
login_entry1.pack()
login_password=tk.Label(login_frame,text="password").pack()
login_entry2=tk.Entry(login_frame)
login_entry2.pack()
btn=tk.Button(login_frame,text="login",command=login,font=("Arial",18)).pack()
btn1=tk.Button(login_frame,text="Create acc",command=sign_up).pack()

signup_frame=Frame(root)
signup_lbl=tk.Label(signup_frame,text="signup",font=("Arial",16)).pack()
signup_username=tk.Label(signup_frame,text="Name").pack()
signup_entry=tk.Entry(signup_frame)
signup_passsword=tk.Label(signup_frame,text="Password").pack()
signup_entry1=tk.Entry(signup_frame)
confirm_passsword=tk.Label(signup_frame,text=" confirm Password").pack()
signup_entry2=tk.Entry(signup_frame)

signup_entry.pack()


root.mainloop()