import tkinter as tk

top=tk.Tk()
#top.geometry("100x100")

frame=tk.Frame(top,bg="lightgray",bd=2)
frame.pack(padx=50,pady=100,fill="both",expand=True)
lbl=tk.Label(frame,text="welcome")
lbl.pack()
btn=tk.Button(frame,text="click me").pack()
btn=tk.Button(frame,text="Exit",command=top.quit).pack()
top.mainloop()