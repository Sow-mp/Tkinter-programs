import tkinter as tk
from tkinter import Label

window=tk.Tk()
window.title("tutorial")
window.geometry("600x200")
Name=tk.Label(window,text="Name").place(x=30,y=50)
Email=tk.Label(window,text="Email").place(x=30,y=90)
password=tk.Label(window,text="password").place(x=40,y=100)
e1=tk.Entry(window).place(x=80,y=50)
e2 =tk.Entry(window).place(x=80, y=90)
e3 =tk.Entry(window).place(x=80, y=130)
window.mainloop()

