import tkinter as tk
from tkinter import messagebox

def submit_form():
    name = name_entry.get()
    dob = dob_entry.get()
    aadhar = aadhar_entry.get()
    uan = uan_entry.get()
    reason = reason_entry.get()

    if not name or not dob or not aadhar or not uan or not reason:
        messagebox.showerror("Error", "All fields are required")
        return
    else:

       messagebox.showinfo("Success", "Form Submitted Successfully!")

# GUI Setup
root = tk.Tk()
root.title("EPFO Form - Withdrawal")
root.geometry("350x400")

tk.Label(root, text="EPFO Form - Withdrawal", font=("Arial", 14)).pack(pady=10)

tk.Label(root, text="Full Name").pack()
name_entry = tk.Entry(root)
name_entry.pack()

tk.Label(root, text="Date of Birth (DD-MM-YYYY)").pack()
dob_entry = tk.Entry(root)
dob_entry.pack()

tk.Label(root, text="Aadhar Number").pack()
aadhar_entry = tk.Entry(root)
aadhar_entry.pack()

tk.Label(root, text="UAN (Universal Account Number)").pack()
uan_entry = tk.Entry(root)
uan_entry.pack()

tk.Label(root, text="Reason for Withdrawal").pack()
reason_entry = tk.Entry(root)
reason_entry.pack()

tk.Button(root, text="Submit", command=submit_form).pack(pady=20)

root.mainloop()
