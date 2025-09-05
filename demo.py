import tkinter as tk

window=tk.Tk()
window.title("Demo")
window.geometry("600x200")
l1=tk.Label(window,text="edureka",font=("Arial Bold",50))
l1.grid(column=0,row=0)
b1=tk.Button(window,text="enter",bg="black",fg="red",command="clicked")
b1.grid(column=1,row=0)

# Create the main window
window = tk.Tk()
window.title("Demo")
window.geometry("400x200")

# Create an Entry widget
t1 = tk.Entry(window, width=10)
t1.grid(column=1, row=0)

# Create a Label widget
l1 = tk.Label(window, text="Enter your name:")
l1.grid(column=0, row=0)

# Function to update the label when the button is clicked
def clicked():
    res = "Welcome to " + t1.get()  # Get user input and concatenate
    l1.configure(text=res)  # Update the label text

# Create a Button widget
bt = tk.Button(window, text="Enter", command=clicked)
bt.grid(column=1, row=1)

# Run the main loop

window.mainloop()




''' import tkinter as tk
window=tk.Tk()
window.title("demo program ")
window.geometry("600x200")
l1 = tk.Label(window, text="Enter your name:")
l1.grid(column=0, row=0)

t1=tk.Entry(window,width=10)
t1.grid(column=1,row=0)
def clicked():
     res="welcome to "+t1.get()
     l1.configure(text=res)

bt=tk.Button(window,text="enter",command=clicked)
bt.grid(column=1, row=1)
window.mainloop()'''
















