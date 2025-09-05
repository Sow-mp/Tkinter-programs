import tkinter as tk
from tkinter import LabelFrame

root = tk.Tk()
root.title("Multiple LabelFrames")
root.geometry("350x250")

# Personal Info Frame
personal_frame = LabelFrame(root, text="Personal Info", padx=10, pady=10)
personal_frame.pack(padx=10, pady=10, fill="both")

tk.Label(personal_frame, text="Name:").grid(row=0, column=0)
tk.Entry(personal_frame).grid(row=0, column=1)

tk.Label(personal_frame, text="Age:").grid(row=1, column=0)
tk.Entry(personal_frame).grid(row=1, column=1)

# Contact Info Frame
contact_frame = LabelFrame(root, text="Contact Info", padx=10, pady=10)
contact_frame.pack(padx=10, pady=10, fill="both")

tk.Label(contact_frame, text="Phone:").grid(row=0, column=0)
tk.Entry(contact_frame).grid(row=0, column=1)

tk.Label(contact_frame, text="Email:").grid(row=1, column=0)
tk.Entry(contact_frame).grid(row=1, column=1)

root.mainloop()
