from tkinter import *

top=Tk()
top.geometry("200x200")
c=Canvas(top,bg="pink",width="200 ",height="200")
arc=c.create_arc((5,10,150,200),start=0,extent=150,fill="white")
c.pack()





# top = Tk()

# top.geometry("200x200")

checkvar1 = IntVar()

checkvar2 = IntVar()

checkvar3 = IntVar()

chkbtn1 = Checkbutton(top, text="C", variable=checkvar1, onvalue=1, offvalue=0, height=2, width=10)

chkbtn2 = Checkbutton(top, text="C++", variable=checkvar2, onvalue=1, offvalue=0, height=2, width=10)

chkbtn3 = Checkbutton(top, text="Java", variable=checkvar3, onvalue=1, offvalue=0, height=2, width=10)

chkbtn1.pack()

chkbtn2.pack()

chkbtn3.pack()

top.mainloop()