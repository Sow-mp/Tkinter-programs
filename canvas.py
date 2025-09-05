from tkinter import *

root = Tk()
canvas = Canvas(root, width=300, height=300, bg='skyblue')
canvas.pack()

# Draw shapes
canvas.create_line(50, 50, 250, 50, fill="blue", width=10)  # Line
canvas.create_rectangle(50, 100, 200, 200, outline="red")  # Rectangle
canvas.create_oval(100, 100, 150, 150, fill="green")  # Circle (Oval)
canvas.create_text(100,150,text="Tkinter Canvas" ,font=('Arial', 12))
#canvas.create_line(50,50,100,100,fill="blue",width=6)
#root.mainloop()

root.mainloop()


