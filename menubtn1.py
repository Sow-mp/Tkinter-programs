import  tkinter as tk

t=tk.Tk()
menubutton=tk.Menubutton(t,text="Lang")
menubutton.pack()
menubutton.menu=tk.Menu(t)
menubutton.menu.add_checkbutton(label="c")
t.mainloop()