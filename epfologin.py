import tkinter as tk
from tkinter import messagebox
# Function to handle login
def login():
    uan = uan_entry.get()
    password = password_entry.get()

    # Dummy credentials for demo
    if uan == "123456789012" and password == "epfo@123":
        messagebox.showinfo("Login Success", "Welcome to EPFO Portal!")
    else:
        messagebox.showerror("Login Failed", "Invalid UAN or Password")

# GUI Setup
root = tk.Tk()
root.title("EPFO Login")
root.geometry("350x250")

tk.Label(root, text="EPFO Member Login", font=("Arial", 16)).pack(pady=10)

tk.Label(root, text="UAN (Universal Account Number)").pack()
uan_entry = tk.Entry(root)
uan_entry.pack(pady=5)

tk.Label(root, text="Password").pack()
password_entry = tk.Entry(root, show="*")
password_entry.pack(pady=5)

tk.Button(root, text="Login", command=login, bg="blue", fg="white").pack(pady=15)

root.mainloop()

# import package
import turtle


# set direction at 0
# angle using seth
turtle.seth(0)

# motion
turtle.forward(80)
turtle.write("East")

# back to home
turtle.home()

# set direction at 90
# angle using sethading
turtle.setheading(90)

# motion
turtle.forward(80)
turtle.write("North")

# back to home
turtle.home()

# set direction at 180
# angle using seth
turtle.seth(180)

# motion
turtle.forward(80)
turtle.write("West",align="right")

# back to home
turtle.home()

# set direction at 270
# angle using setheading
turtle.setheading(270)

# motion
turtle.forward(80)
turtle.write("South")

# hide the turtle
turtle.ht()