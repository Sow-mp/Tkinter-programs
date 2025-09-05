from tkinter import *

top = Tk()
text = Text(top)
text.insert(INSERT, "Name.....")
text.insert(END, "Salary.....")

text.pack()

text.tag_add("Write Here", "1.0", "1.4")#line no.column no
text.tag_add("Click Here", "1.8", "1.13")#line no.column no #start index and end index

text.tag_config("Write Here", background="yellow", foreground="black")#(tag name)
text.tag_config("Click Here", background="black", foreground="white")
top.mainloop()

text=Text(top)
text.insert(INSERT,"hi")
text.insert(END,"hello")

text.tag_add("write here"," ","")