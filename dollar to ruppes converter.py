def convert():
    c=int(e1.get())
    f=(82.71)*(float(c))
import formcreation as tk

t1.config(state='normal')
t1.delete('1.0',tk.END)
t1.insert(tk.END,f)
t1.config(state='disabled')
window=tk.Tk()
window.geometry("300x500")
window.config(bg="purple")
window.resizable(width=False,height=False)
window.title("do to ru convert")

l1=tk.Label(window,text="dollar ruppes converter",font=("arial",15),fg="white",bg="red")
l2=tk.Label(window,text="enter dollar amount",font=("arial",18,"bold"),fg="white",bg="black")
l3=tk.Label(window,text="amount in ruppes",font=("arial",13,"bold"),fg="black",bg="yellow")

empty_l1=tk.Label(window,bg="#E99674")
empty_l2=tk.Label(window,bg="#E9967A")
e1=tk.Entry(window,font=("Arial",10))
btn1=tk.Button(window,text="convert to ruppes",font=("arial",10))
t1=tk.Text(window,state="disabled",width=15,height=0)
l1.pack()
l2.pack()
e1.pack()
btn1.pack()

window.mainloop()
















import  formcreation as tk

def convert():
    # Get input from entry widget
    try:
        c = float(e1.get())  # Convert input to float for calculation
        f = 82.71 * c  # Conversion logic (Dollar to Rupee)

        # Enable the text widget, update it, then disable it again
        t1.config(state='normal')
        t1.delete('1.0', tk.END)  # Clear previous output
        t1.insert(tk.END, f"₹{f:.2f}")  # Insert converted value with formatting
        t1.config(state='disabled')  # Disable the text widget to make it read-only
    except ValueError:
        # Handle invalid input (non-numeric)
        t1.config(state='normal')
        t1.delete('1.0', tk.END)
        t1.insert(tk.END, "Invalid input")
        t1.config(state='disabled')

# Initialize the main Tkinter window
window = tk.Tk()
window.geometry("300x500")
window.config(bg="purple")
window.resizable(width=False, height=False)
window.title("Dollar to Rupees Converter")

# Labels
l1 = tk.Label(window, text="Dollar to Rupees Converter", font=("Arial", 15), fg="white", bg="red")
l2 = tk.Label(window, text="Enter Dollar Amount:", font=("Arial", 18, "bold"), fg="white", bg="black")
l3 = tk.Label(window, text="Amount in Rupees:", font=("Arial", 13, "bold"), fg="black", bg="yellow")

# Entry widget for input
e1 = tk.Entry(window, font=("Arial", 10))

# Button to trigger the conversion
btn1 = tk.Button(window, text="Convert to Rupees", font=("Arial", 10), command=convert)

# Text widget to display the output
t1 = tk.Text(window, state="disabled", width=20, height=2)

# Pack widgets into the window
l1.pack(pady=10)
l2.pack(pady=5)
e1.pack(pady=5)
btn1.pack(pady=10)
l3.pack(pady=5)
t1.pack(pady=5)

# Start the Tkinter event loop
window.mainloop()