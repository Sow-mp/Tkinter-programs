import tkinter as tk
from tkinter import messagebox

# Function to handle form submission
def submit_form():
    uan = entry_uan.get()
    name = entry_name.get()
    reason = reason_var.get()
    account = entry_account.get()
    ifsc = entry_ifsc.get()

    # Simple validation
    if not (uan and name and reason and account and ifsc):
        messagebox.showerror("Error", "All fields are required!")
        return

    # Simulate saving the data
    messagebox.showinfo("Success", "Claim Form Submitted Successfully!")

# Main window
root = tk.Tk()
root.title("EPFO Online Claim Form")
root.geometry("400x400")

tk.Label(root, text="EPFO Claim Form", font=("Arial", 16)).pack(pady=10)

# UAN
tk.Label(root, text="UAN (Universal Account Number)").pack()
entry_uan = tk.Entry(root)
entry_uan.pack(pady=5)

# Name
tk.Label(root, text="Member Name").pack()
entry_name = tk.Entry(root)
entry_name.pack(pady=5)

# Reason for Claim
tk.Label(root, text="Reason for Claim").pack()
reason_var = tk.StringVar()
reason_dropdown = tk.OptionMenu(root, reason_var,  "Withdrawal", "Pension", "Transfer", "Others")
reason_dropdown.pack(pady=5)

# Bank Account Number
tk.Label(root, text="Bank Account Number").pack()
entry_account = tk.Entry(root)
entry_account.pack(pady=5)

# IFSC Code
tk.Label(root, text="IFSC Code").pack()
entry_ifsc = tk.Entry(root)
entry_ifsc.pack(pady=5)

# Submit Button
tk.Button(root, text="Submit Claim", command=submit_form,
          bg="green", fg="white").pack(pady=15)

root.mainloop()


