import tkinter as tk
from tkinter import *

top = Tk()
top.geometry("140x100")
frame = Frame(top)
frame.pack()

leftframe = Frame(top)
leftframe.pack(side=LEFT)

rightframe = Frame(top)
rightframe.pack(side=RIGHT)

btn1 = Button(frame, text="Submit", fg="red", activebackground="red")
btn1.pack(side=LEFT)

btn2 = Button(frame, text="Remove", fg="brown", activebackground="brown")
btn2.pack(side=RIGHT)

btn3 = Button(leftframe, text="Add", fg="blue", activebackground="blue")
btn3.pack(side=LEFT)

btn4 = Button(rightframe, text="Modify", fg="black", activebackground="white")
btn4.pack(side=RIGHT)

top.mainloop()

top=tk.Tk()
frame=Frame(top)
frame.pack()
leftframe=Frame(top)
leftframe.pack(side=LEFT)
rightframe=Frame(top)
rightframe.pack(side=RIGHT)
btn1=Button(frame,text="submit",fg="red",bg="yellow")
btn1.pack()
btn2=Button(leftframe,text="remove",fg='pink',bg='orange')
btn2.pack(side=LEFT)
btn3=Button(rightframe,text="delete",fg='pink',activebackground='orange')
btn3.pack(side=RIGHT)
btn4=Button(leftframe,text="insert",fg='pink',activebackground='orange')
btn4.pack(side=LEFT)

top.mainloop()


from tkinter import *

# Create the main window
root = Tk()
root.title("Frame Example")
root.geometry("300x200")

# Create a Frame
frame = Frame(root, bg="lightblue", bd=2, relief="groove")
frame.pack(padx=20, pady=20, fill=BOTH, expand=True)

# Add widgets inside the Frame
Label(frame, text="Welcome!", bg="lightblue", font=("Arial", 14)).pack(pady=5)
Button(frame, text="Click Me").pack(pady=5)
Button(frame, text="Exit", command=root.quit).pack(pady=5)

# Start the GUI event loop
root.mainloop()

from tkinter import *

# Function to show entered data
def submit_data():
    name = name_var.get()
    age = age_var.get()
    gender = gender_var.get()
    output_label.config(text=f"Name: {name}, Age: {age}, Gender: {gender}")

# Main window
root = Tk()
root.title("Advanced Frame Example")
root.geometry("400x300")

# ===== Main outer frame =====
main_frame = Frame(root, bg="lightgray", bd=3, relief=RIDGE)
main_frame.pack(padx=10, pady=10, fill=BOTH, expand=True)

# ===== Header frame =====
header = Frame(main_frame, bg="navy")
header.pack(fill=X)
Label(header, text="Student Registration", bg="navy", fg="white", font=("Arial", 16)).pack(pady=10)

# ===== Form frame =====
form = Frame(main_frame, bg="white")
form.pack(padx=20, pady=10, fill=BOTH, expand=True)

# Variables for form
name_var = StringVar()
age_var = StringVar()
gender_var = StringVar()

# Name row
Label(form, text="Name:", bg="white").grid(row=0, column=0, padx=5, pady=5, sticky=E)
Entry(form, textvariable=name_var).grid(row=0, column=1, padx=5, pady=5)

# Age row
Label(form, text="Age:", bg="white").grid(row=1, column=0, padx=5, pady=5, sticky=E)
Entry(form, textvariable=age_var).grid(row=1, column=1, padx=5, pady=5)

# Gender row
Label(form, text="Gender:", bg="white").grid(row=2, column=0, padx=5, pady=5, sticky=E)
Entry(form, textvariable=gender_var).grid(row=2, column=1, padx=5, pady=5)

# ===== Button frame =====
button_frame = Frame(main_frame, bg="lightgray")
button_frame.pack(pady=10)

Button(button_frame, text="Submit", command=submit_data, bg="green", fg="white").pack()

# ===== Output frame =====
output_frame = Frame(main_frame, bg="white")
output_frame.pack(padx=10, pady=10, fill=X)

output_label = Label(output_frame, text="", bg="white", fg="blue", font=("Arial", 10))
output_label.pack()

root.mainloop()
