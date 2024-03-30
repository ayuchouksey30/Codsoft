import tkinter as tk
from tkinter import ttk, messagebox
import random
import string
import pyperclip

def generate_password():
    try:
        length = int(length_entry.get())
        if length <= 0:
            raise ValueError("Length should be a positive integer.")
        password = ''.join(random.choices(string.ascii_letters + string.digits + string.punctuation, k=length))
        password_label.config(text="Generated Password: " + password)
    except ValueError as e:
        messagebox.showerror("Error", str(e))

def copy_to_clipboard():
    generated_password = password_label.cget("text")
    if generated_password:
        generated_password = generated_password.split(": ")[1]
        pyperclip.copy(generated_password)
        messagebox.showinfo("Copied", "Password copied to clipboard.")

root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#1E1E1E")  
root.geometry("460x300")
root.minsize(460,300)

custom_font = ("Helvetica", 14)


style = ttk.Style()
style.configure('DarkFrame.TFrame', background='#1E1E1E')

# Frame
frame = ttk.Frame(root, style='DarkFrame.TFrame')  
frame.pack(padx=20, pady=20)

# Title label
title_label = ttk.Label(frame, text="Password Generator", font=("Helvetica", 18, "bold"), foreground="white", background="#1E1E1E")
title_label.grid(row=0, column=0, columnspan=3, padx=5, pady=5)

# Password Length label
length_label = ttk.Label(frame, text="Password Length:", font=custom_font, foreground="white", background="#1E1E1E")
length_label.grid(row=1, column=0, padx=5, pady=5)

# Spinbox for Password Length
length_entry = tk.Spinbox(frame, from_=1, to=100, width=5, font=custom_font)
length_entry.grid(row=1, column=1, padx=5, pady=5)

# Generate Password Button
generate_button = ttk.Button(frame, text="Generate Password", command=generate_password, style="GenerateButton.TButton")
generate_button.grid(row=2, column=0, padx=5, pady=5)

# Copy to Clipboard Button
copy_button = ttk.Button(frame, text="Copy to Clipboard", command=copy_to_clipboard, style="CopyButton.TButton")
copy_button.grid(row=2, column=1, columnspan=2, padx=5, pady=5)

# Generated Password label
password_label = ttk.Label(root, text="", font=custom_font, foreground="white", background="#1E1E1E")
password_label.pack()

# Configure style for buttons with dark grey background
style.configure('GenerateButton.TButton', foreground='black', background='#333333', font=custom_font)
style.configure('CopyButton.TButton', foreground='black', background='#333333', font=custom_font)

root.mainloop()
