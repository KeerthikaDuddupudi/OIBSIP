import tkinter as tk
from tkinter import messagebox
import random

LOWER_CASE = 'abcdefghijklmnopqrstuvwxyz'
UPPER_CASE = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
NUMBERS = '0123456789'
SYMBOLS = '!@#$%^&*()_+-=[]{}|;:,.<>?'

def generate_password(length, use_uppercase, use_numbers, use_symbols):
    characters = LOWER_CASE
    if use_uppercase:
        characters += UPPER_CASE
    if use_numbers:
        characters += NUMBERS
    if use_symbols:
        characters += SYMBOLS

    if not characters:
        raise ValueError("At least one character type must be selected")

    password = []
    if use_uppercase:
        password.append(random.choice(UPPER_CASE))
    if use_numbers:
        password.append(random.choice(NUMBERS))
    if use_symbols:
        password.append(random.choice(SYMBOLS))

    remaining_length = length - len(password)
    if remaining_length > 0:
        password.extend(random.choice(characters) for _ in range(remaining_length))

    random.shuffle(password)
    return ''.join(password)

def on_generate():
    try:
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_numbers = numbers_var.get()
        use_symbols = symbols_var.get()

        if length <= 0:
            raise ValueError("Password length must be greater than 0")

        password = generate_password(length, use_uppercase, use_numbers, use_symbols)
        password_var.set(password)
    except ValueError as e:
        messagebox.showerror("Input Error", str(e))

def copy_to_clipboard():
    password = password_var.get()
    if password:
        root.clipboard_clear()
        root.clipboard_append(password)
        root.update()  
        messagebox.showinfo("Copied", "Password copied to clipboard!")

root = tk.Tk()
root.title("Password Generator")
root.geometry("700x700") 
root.configure(bg='#e3e3db')  

tk.Label(root, text="PASSWORD GENERATOR", font=("bold", 32), bg='white',fg='#5250ed').pack(pady=20)

input_frame = tk.Frame(root, bg='#e1e1e1')
input_frame.pack(pady=20)

tk.Label(input_frame, text="Password Length:", font=("Arial", 16), bg='#e1e1e1').pack(anchor='w', padx=20)
length_entry = tk.Entry(input_frame, width=15, font=("Arial", 16))
length_entry.pack(padx=20)

uppercase_var = tk.BooleanVar(value=True)
numbers_var = tk.BooleanVar(value=True)
symbols_var = tk.BooleanVar(value=True)

tk.Checkbutton(input_frame, text="Include Uppercase Letters", variable=uppercase_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)
tk.Checkbutton(input_frame, text="Include Numbers", variable=numbers_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)
tk.Checkbutton(input_frame, text="Include Symbols", variable=symbols_var, bg='#e1e1e1', font=("Arial", 14)).pack(anchor='w', padx=20, pady=5)

tk.Button(root, text="Generate Password", command=on_generate, bg='#4a90e2', fg='white', font=("Arial", 16)).pack(pady=20)

tk.Label(root, text="Generated Password:", font=("Arial", 18), bg='#f0f0f0').pack(pady=10)
password_var = tk.StringVar()
password_entry = tk.Entry(root, textvariable=password_var, width=50, font=("Arial", 16), state='readonly')
password_entry.pack(pady=10)

tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard, bg='#4a90e2', fg='white', font=("Arial", 16)).pack(pady=20)

root.mainloop()
