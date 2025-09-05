import formcreation as tk

# def hello():

#   label=tk.Label(text="hi learners",width=25,heigh=5,fg="white",bg="black").pack()



window=tk.Tk()
window.title("tkinter tutorials")
window.geometry("600x200")
# greeting=tk.Label(text="hello learners,welcome to tkinter tutorial")
# greeting.place(x=190,y=210)

# label=tk.Label(text=" hello learners,welcome to tkinter tutorial",fg="white",bg="red",width=40,height=10)
# label.place(x=190,y=210)
#button=tk.Button(text="click me to say hi ",width=25,height=2,bg="white",fg="purple",command=hello)
# button.pack(side="left")#default of pack()-> top & center
'''label=tk.Label(text="name")
entry=tk.Entry()
label.pack()
entry.pack()'''
name=tk.Label(window,text="name").place(x=30,y=50)
email=tk.Label(window,text="email").place(x=30,y=90)
password=tk.Label(window,text="password").place(x=20,y=130)
e1 = tk.Entry(window).place(x=80, y=50)
e2 = tk.Entry(window).place(x=80, y=90)
e3 = tk.Entry(window).place(x=80, y=130)

window.mainloop()




















