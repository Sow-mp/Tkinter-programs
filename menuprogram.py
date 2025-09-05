import tkinter as tk
top=tk.Tk()
menubar=tk.Menu(top ,bg="blue",fg="white")
file=tk.Menu(menubar,tearoff=0)#dashed line is disable tearoff=0 tearoff=false
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="Save")
file.add_command(label="Save As")
file.add_separator()
file.add_command(label="Close")
menubar.add_cascade(label="File",menu=file)
edit=tk.Menu(menubar,tearoff=0)
edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="paste")
menubar.add_cascade(label="Edit",menu=edit)
help=tk.Menu(menubar,tearoff=0)
help.add_command(label="About")
menubar.add_cascade(label="Help",menu=help)
top.config(menu=menubar)
top.mainloop()
'''menubar=tk.Menu(top)
file=tk.Menu(menubar,tearoff=0)
file.add_command(label="New")
file.add_command(label="Open")
file.add_command(label="save")
file.add_command(label="save As")
file.add_command(label="close")
file.add_separator()
file.add_command(label="Exit",command="top.quit")

menubar.add_cascade(menu=file,label="File")
edit=tk.Menu(menubar,tearoff=0)
edit.add_command(label="undo")
edit.add_separator()
edit.add_command(label="cut")
edit.add_command(label="copy")
edit.add_command(label="paste")
edit.add_command(label="delete")
edit.add_command(label="selectall")
menubar.add_cascade(menu=edit,label="Edit")

help=tk.Menu(menubar,tearoff=0)
help.add_command(label="about")
menubar.add_cascade(menu=help,label="Help")




top.config(menu=menubar)'''





top.mainloop()

# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Set the title and geometry to your app
app.title("Geeks For Geeks")
app.geometry("800x500")

# Create menubar by setting the color
menubar = Menu(app, background='blue', fg='white')

# Declare file and edit for showing in menubar
file = Menu(menubar, tearoff=False, background='yellow')
edit = Menu(menubar, tearoff=False, background='pink')

# Add commands in in file menu
file.add_command(label="New")
file.add_command(label="Exit", command=app.quit)

# Add commands in edit menu
edit.add_command(label="Cut")
edit.add_command(label="Copy")
edit.add_command(label="Paste")

# Display the file and edit declared in previous step
menubar.add_cascade(label="File", menu=file)
menubar.add_cascade(label="Edit", menu=edit)

# Displaying of menubar in the app
app.config(menu=menubar)

# Make infinite loop for displaying app on screen
app.mainloop() #explain the each line of the code


win=Tk()
menubar=tk.Menu(win)
file=Menu(menubar,label="new").pack()
win.mainloop()