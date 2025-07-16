import tkinter as tk
from tkinter import ttk, messagebox
import random, string
import pyperclip

class PasswordGenerator:
    def __init__(self, root):
        root.title("Random Password Generator")
        root.geometry("350x250")
        root.resizable(False, False)

        ttk.Label(root, text="Password Length:").pack(pady=(20, 5))
        self.length_var = tk.IntVar(value=12)
        self.spin = ttk.Spinbox(root, from_=4, to_=64, textvariable=self.length_var, width=5)
        self.spin.pack()

        ttk.Label(root, text="Complexity:").pack(pady=(10, 5))
        self.complexity = tk.StringVar(value="medium")
        for lvl in ('low','medium','high'):
            ttk.Radiobutton(root, text=lvl.title(), value=lvl, variable=self.complexity).pack(anchor='w', padx=50)

        ttk.Button(root, text="Generate", command=self.generate_password).pack(pady=15)
        self.result_var = tk.StringVar()
        ttk.Entry(root, textvariable=self.result_var, font=('Courier', 12), width=30).pack()

        ttk.Button(root, text="Copy to Clipboard", command=self.copy_password).pack(pady=5)

    def generate_password(self):
        length = self.length_var.get()
        lvl = self.complexity.get()
        if length < 4:
            messagebox.showerror("Error", "Password length must be at least 4.")
            return

        if lvl == 'low':
            chars = string.ascii_lowercase
        elif lvl == 'medium':
            chars = string.ascii_letters + string.digits
        else:  # high
            chars = string.ascii_letters + string.digits + string.punctuation

        password = ''.join(random.choice(chars) for _ in range(length))
        self.result_var.set(password)

    def copy_password(self):
        pwd = self.result_var.get()
        if pwd:
            pyperclip.copy(pwd)
            messagebox.showinfo("Copied", "Password copied to clipboard.")
        else:
            messagebox.showwarning("Warning", "No password to copy.")

if __name__ == "__main__":
    root = tk.Tk()
    PasswordGenerator(root)
    root.mainloop()
