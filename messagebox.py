import tkinter as tk
from tkinter import messagebox
from tkinter.messagebox import askquestion

top=tk.Tk()
messagebox.showinfo("info","info")
messagebox.askyesno("maritalstatus",message="are u married")
messagebox.askokcancel("info","info")
messagebox.askquestion("hello",'how r u')
messagebox.askretrycancel()
messagebox.askquestion("how old r u")
messagebox.showinfo("info")

top.mainloop()


top=tk.Tk()
messagebox.showinfo("info","information")
messagebox.askquestion("info","information")
messagebox.askyesno("info","information")
messagebox.askokcancel()
messagebox.askretrycancel()
top.mainloop()

messagebox.askyesno('info','info')

