import tkinter as tk
#from Pillow import ImageTk, Image
from PIL import ImageTk, Image  # ✅ CORRECT

top=tk.Tk()
top.geometry("100x100")
top.config(bg="green")
lbl=tk.Label(top,text="hi welcome \nto\ngeeks",bg="red",font=("arial",10,"bold"),
             justify="center",cursor="Plus",relief="flat")

lbl.pack()
image = Image.open("C:/Users/sachi/PycharmProjects/tkinterTutorial/PNG/new.png.jpg")

#img = ImageTk.PhotoImage(Image.open
               #          ("C:/Users/sachi/PycharmProjects/tkinterTutorial/PNG/new.png.jpg"))

resized_image = image.resize((400, 150))  # ✅ Resize PIL Image

# Convert to PhotoImage
tk_image = ImageTk.PhotoImage(resized_image)


# Convert to Tkinter-compatible image
#tk_image = ImageTk.PhotoImage(resized_image)
label = tk.Label(top, image=tk_image)
label.pack()
#img = ImageTk.PhotoImage(Image.open("C:/Users/sachi/PycharmProjects/tkinterTutorial/img.png"))

#img = ImageTk.PhotoImage(Image.open("C:/Users/sachi/PycharmProjects/tkinterTutorial/PNG/new.png.jpg"))

#img=tk.PhotoImage(file=r"C:\Users\sachi\PycharmProjects\tkinterTutorial\img.png")
top.mainloop()

