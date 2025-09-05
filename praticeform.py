import tkinter as tk
from tkinter import messagebox
from tkinter.ttk import Label
from tkinter import LabelFrame



def submit_form():
    name=e1.get()
    dob=e2.get()
    uan=e3.get()
    adar=e4.get()
    if not name or not dob or not uan or not adar:
        messagebox.showinfo("error","all fields are requird")
    else:
        messagebox.showinfo("Submit","submitted successfully")

root=tk.Tk()
root.geometry("200x300")
root.title("EPFO form withdrawal")
lbl1=tk.Label(root,text="Fullname")
lbl1.pack()
e1=tk.Entry(root)
e1.pack()
lbl2=tk.Label(root,text="Date-of-birth")
lbl2.pack()
e2=tk.Entry(root)
e2.pack()
lbl3=tk.Label(root,text="UAN number")
lbl3.pack()
e3=tk.Entry(root)
e3.pack()
lbl4=tk.Label(root,text="Adar number")
lbl4.pack()
e4=tk.Entry(root)
e4.pack()
btn=tk.Button(root,text="Submit",command=submit_form).pack()

root.mainloop()

def submit():
    uan=e1.get()
    password=e2.get()



    if uan=="123456789" or password=="epf@123":
        messagebox.showinfo("Login","login successful")
    else:
        messagebox.showerror("Error","invalid login creditials")

root=tk.Tk()
tk.Label(root,text="uan").pack()
e1=tk.Entry(root)
e1.pack()
tk.Label(root,text="Password").pack()
e2=tk.Entry(root)
e2.pack()
tk.Button(root,text="Submit",command=submit).pack()
root.mainloop()

root=tk.Tk()
lblframe1=tk.LabelFrame(root,text="Personal info",padx=10,pady=10)
lblframe1.pack(fill="both",padx=10,pady=10)
Label(lblframe1,text="Name:").grid(row=0,column=0)
e1=tk.Entry(lblframe1)
e1.grid(row=0,column=1)
Label(lblframe1,text="Age:").grid(row=1,column=0)
e2=tk.Entry(lblframe1)
e2.grid(row=1,column=1)
root.mainloop()

















