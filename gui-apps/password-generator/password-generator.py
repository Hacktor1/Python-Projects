import tkinter as tk
from tkinter import messagebox
import random
import string
import json
import os

FILE_NAME = "passwords.json"


class PasswordGenerator:
    def __init__(self, root):
        self.root = root
        self.root.title("Random Password Generator")
        self.root.geometry("500x600")

        self.passwords = []
        self.load_passwords()

        tk.Label(root, text="Password Generator", font=("Arial", 16)).pack(pady=10)

        tk.Label(root, text="Password Length:").pack()
        self.length_entry = tk.Entry(root)
        self.length_entry.insert(0, "12")
        self.length_entry.pack(pady=5)

        self.use_letters = tk.BooleanVar(value=True)
        self.use_numbers = tk.BooleanVar(value=True)
        self.use_symbols = tk.BooleanVar(value=True)

        tk.Checkbutton(root, text="Include Letters", variable=self.use_letters).pack()
        tk.Checkbutton(root, text="Include Numbers", variable=self.use_numbers).pack()
        tk.Checkbutton(root, text="Include Symbols", variable=self.use_symbols).pack()

        tk.Button(root, text="Generate Password", command=self.generate_password).pack(pady=10)

        self.password_output = tk.Entry(root, width=30)
        self.password_output.pack(pady=5)

        tk.Button(root, text="Save Password", command=self.save_password).pack(pady=5)

        tk.Label(root, text="Saved Passwords:").pack(pady=5)

        self.password_listbox = tk.Listbox(root, width=40, height=8)
        self.password_listbox.pack(pady=5)

        tk.Button(root, text="Delete Selected Password", command=self.delete_password).pack(pady=5)

        self.refresh_listbox()

    def generate_password(self):
        try:
            length = int(self.length_entry.get())
            characters = ""

            if self.use_letters.get():
                characters += string.ascii_letters
            if self.use_numbers.get():
                characters += string.digits
            if self.use_symbols.get():
                characters += string.punctuation

            if not characters:
                messagebox.showwarning("Warning", "Select at least one character type.")
                return

            password = "".join(random.choice(characters) for _ in range(length))
            self.password_output.delete(0, tk.END)
            self.password_output.insert(0, password)

        except ValueError:
            messagebox.showwarning("Warning", "Please enter a valid number.")

    def save_password(self):
        password = self.password_output.get()
        if password:
            self.passwords.append(password)
            self.save_to_file()
            self.refresh_listbox()
            self.password_output.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "No password to save.")

    def delete_password(self):
        try:
            selected_index = self.password_listbox.curselection()[0]
            removed_password = self.passwords.pop(selected_index)
            self.save_to_file()
            self.refresh_listbox()
            messagebox.showinfo("Deleted", f"Password '{removed_password}' deleted.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a password to delete.")

    def refresh_listbox(self):
        self.password_listbox.delete(0, tk.END)
        for pwd in self.passwords:
            self.password_listbox.insert(tk.END, pwd)

    def save_to_file(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.passwords, file, indent=4)

    def load_passwords(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.passwords = json.load(file)


if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGenerator(root)
    root.mainloop()
