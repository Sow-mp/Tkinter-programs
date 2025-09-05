import tkinter as tk


window=tk.Tk()
window.geometry("100x100")
chvar1=tk.IntVar()
chvar2=tk.IntVar()
chvar3=tk.IntVar()
lbl=tk.Checkbutton(window,text="c",variable=chvar1,onvalue=1,offvalue=0).grid(row=0,column=0)
def show():
    print(f"c:{chvar1.get()},c++:{chvar2.get()},java:{chvar3.get()}")
btn=tk.Button(window,text="show",command=show).grid(row=2,column=2)
window.mainloop()