import tkinter as tk
import random
import string
from tkinter import messagebox

def generate_password():
    length = length_entry.get()
    if not length.isdigit() or int(length) <= 0:
        messagebox.showerror("Error", "Please enter a valid positive integer for the length.")
        return
    length = int(length)
    if length > 12:
        messagebox.showwarning("Warning", "Password length is too long. Maximum allowed is 12.")
        return

    characters = ""
    if use_letters.get():
        characters += string.ascii_letters
    if use_digits.get():
        characters += string.digits
    if use_punctuation.get():
        characters += string.punctuation

    if not characters:
        messagebox.showerror("Error", "Please select at least one character set.")
        return

    password = ''.join(random.choice(characters) for _ in range(length))
    result_label.config(text=password)

def copy_to_clipboard():
    password = result_label.cget("text")
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        messagebox.showinfo("Copied", "Password copied to clipboard!")
    else:
        messagebox.showwarning("Warning", "No password generated yet.")

root = tk.Tk()
root.title("Password Generator")

# Length input
length_label = tk.Label(root, text="Length:")
length_label.pack()

length_entry = tk.Entry(root)
length_entry.pack()

# Character set options
use_letters = tk.BooleanVar(value=True)
letters_check = tk.Checkbutton(root, text="Include Letters", variable=use_letters)
letters_check.pack()

use_digits = tk.BooleanVar(value=True)
digits_check = tk.Checkbutton(root, text="Include Digits", variable=use_digits)
digits_check.pack()

use_punctuation = tk.BooleanVar(value=True)
punctuation_check = tk.Checkbutton(root, text="Include Punctuation", variable=use_punctuation)
punctuation_check.pack()

# Generate button
generate_button = tk.Button(root, text="Generate Password", command=generate_password)
generate_button.pack()

# Result label
result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack()

# Copy to clipboard button
copy_button = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_button.pack()

root.mainloop()