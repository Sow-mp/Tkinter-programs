import tkinter as tk
from tkinter.constants import ANCHOR

top=tk.Tk()
top.geometry("200x200")
lbl=tk.Label(top,text="list of favorty contries")
lbl.pack()
listbox=tk.Listbox(top)
listbox.pack()
listbox.insert(1,"USA")
listbox.insert(2,"UK")
listbox.insert(3,"Germany")
btn=tk.Button(top,text="delete",command=lambda:listbox.delete(tk.ANCHOR))
btn.pack()
#lambda:listbox.delete(tk.ANCHOR)
top.mainloop()



import tkinter as tk
from tkinter import messagebox

# Create the main window
root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

# List of items to display
items = ["Python", "Java", "C++", "JavaScript", "HTML", "CSS"]

# Create a Listbox
listbox = tk.Listbox(root, selectmode=tk.SINGLE)  # use MULTIPLE for multiple selection
listbox.pack(pady=20)

# Add items to Listbox
for item in items:
    listbox.insert(tk.END, item)

# Function to display selected item
def show_selection():
    selected = listbox.curselection()
    if selected:
        item = listbox.get(selected[0])
        messagebox.showinfo("Selection", f"You selected: {item}")
    else:
        messagebox.showwarning("No Selection", "Please select an item.")

# Button to trigger selection function
button = tk.Button(root, text="Show Selected", command=show_selection)
button.pack()

# Start the GUI loop
root.mainloop()
