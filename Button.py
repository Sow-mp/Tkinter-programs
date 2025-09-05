import tkinter as tk

window=tk.Tk()
window.title("main program")
label1=tk.Label(window,text="Name").grid(row=0,column=0)
label2=tk.Label(window,text="Email").grid(row=1,column=0)
label3=tk.Label(window,text="Password").grid(row=2,column=0)
submitbut=(tk.Button(window,text="Submit",activebackground="red",activeforeground="white")
           .grid(row=3,column=0))
e1=tk.Entry(window).grid(row=0,column=1)
e2=tk.Entry(window).grid(row=1,column=1)
e3=tk.Entry(window).grid(row=2,column=1)
window.mainloop()

window=tk.Tk()
window.title("")
lbl1=tk.Label(window,text="name").grid(row=0,column=0)
e1=tk.Entry(window).grid(row=0,column=1)
window.mainloop()


window=tk.Tk()
window.title("table info")
lbl1=tk.Label(window,text="Name").grid(row=0,column=0)
e1=tk.Entry(window).grid(row=0,column=1)
lbl2=tk.Label(window,text="Email").grid(row=1,column=0)
e2=tk.Entry(window).grid(row=1,column=1)
sub=tk.Button(window,text="submit").grid(row=3,column=1)
window.mainloop()