import tkinter as tk
from tkinter import *
import requests
top = Tk()

top.geometry("200x250")

menubutton = Menubutton(top, text="Language")

menubutton.grid()

menubutton.menu = Menu(menubutton)

menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label="Hindi", variable=IntVar())

menubutton.menu.add_checkbutton(label="English", variable=IntVar())

menubutton.pack()
import requests
import json
from tkinter import *

window = Tk()

# creating the Box
window.title("Covid-19")

# Determining the size of the Box
window.geometry('220x70')

# Including labels
lbl = Label(window,
            text="Total active cases:-......")
lbl1 = Label(window,
             text="Total confirmed cases:-...")

lbl.grid(column=1, row=0)
lbl1.grid(column=1, row=1)
lbl2 = Label(window, text="")
lbl2.grid(column=1, row=3)


def clicked():
    # Opening the url and loading the
    # json data using json Library
    url = "https://api.covid19india.org/ / data.json"
    page = requests.get(url)
    data = json.loads(page.text)

    lbl.configure(text="Total active cases:-"
                       + data["statewise"][0]["active"])

    lbl1.configure(text="Total Confirmed cases:-"
                        + data["statewise"][0]["confirmed"])

    lbl2.configure(text="Data refreshed")


btn = Button(window, text="Refresh", command=clicked)
btn.grid(column=2, row=0)

window.mainloop()


(top.mainloop())

top=Tk()
menubutton=Menubutton(top,text="lang")
menubutton.grid()
menubutton.menu=Menu(menubutton)
top.mainloop()



top=Tk()
english_var=IntVar()
Hindi_var=IntVar()
menubutton=Menubutton(top,text="Language",relief="flat")#relief is used for border style and apperance
menubutton.pack()

menubutton.menu=Menu(menubutton)
menubutton["menu"] = menubutton.menu

menubutton.menu.add_checkbutton(label="english",variable=english_var)
menubutton.menu.add_checkbutton(label="hindi",variable=Hindi_var)

def selection():
    print(f"hindi is selected {Hindi_var.get()}")
    print(f"english is selected {english_var.get()}")
btn=tk.Button(top,text="show",command=selection)
btn.pack(side="right")

top.mainloop()

# importing tkinter module
from tkinter import *
from tkinter.ttk import *

# creating tkinter window
root = Tk()

# getting screen's height in pixels
height = root.winfo_screenheight()

# getting screen's width in pixels
width = root.winfo_screenwidth()

print("\n width x height = %d x %d (in pixels)\n" %(width, height))
# infinite loop
mainloop()

import tkinter
from tkinter import *

root = Tk()

L = Label(root, text ="Right-click to display menu",
          width = 40, height = 20)
L.pack()

m = Menu(root, tearoff = 0)
m.add_command(label ="Cut")
m.add_command(label ="Copy")
m.add_command(label ="Paste")
m.add_command(label ="Reload")
m.add_separator()
m.add_command(label ="Rename")

def do_popup(event):
    try:
        m.tk_popup(event.x_root, event.y_root)
    finally:
        m.grab_release()

L.bind("<Button-3>", do_popup)

mainloop()