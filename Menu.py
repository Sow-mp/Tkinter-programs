from tkinter import *
from turtledemo.penrose import start

top = Tk()
def hello():
    print("hello")

menubar=Menu(top)
menubar.add_command(label="hello",command=hello)
menubar.add_command(label='quit',command=top.quit)
top.config(menu=menubar)
top.mainloop()

