import tkinter as tk
from tkinter import messagebox
import json
import os

FILE_NAME = "tasks.json"


class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List Application")
        self.root.geometry("400x500")
        self.root.configure(background="#1e1e1e")

        self.tasks = []
        self.load_tasks()

        self.title_label = tk.Label(root, text="My To-Do List", fg="white", bg="#1e1e1e", font=("Arial", 16, "bold", "underline"))
        self.title_label.pack(pady=10)

        self.task_entry = tk.Entry(root, width=30, bg="#3e3e3e", fg="white", font=("Arial", 12))
        self.task_entry.pack(pady=5)

        self.add_button = tk.Button(root, text="Add Task", bg="#3e3e3e", fg="white", width=20, command=self.add_task)
        self.add_button.pack(pady=5)

        self.task_listbox = tk.Listbox(root, width=40, height=15, bg="#3e3e3e", fg="white", font=("Arial", 12))
        self.task_listbox.pack(pady=10)

        self.button_frame = tk.Frame(root)
        self.button_frame.pack(pady=5)

        self.complete_button = tk.Button(
            self.button_frame,
            fg="white",
            bg="#3e3e3e",
            text="Mark as Completed",
            command=self.complete_task
        )
        self.complete_button.grid(row=0, column=0, padx=0)

        self.delete_button = tk.Button(
            self.button_frame,
            fg="white",
            bg="#3e3e3e",
            text="Delete Task",
            command=self.delete_task
        )
        self.delete_button.grid(row=0, column=10, padx=0)

        self.refresh_listbox()

    def load_tasks(self):
        if os.path.exists(FILE_NAME):
            with open(FILE_NAME, "r") as file:
                self.tasks = json.load(file)

    def save_tasks(self):
        with open(FILE_NAME, "w") as file:
            json.dump(self.tasks, file, indent=4)

    def refresh_listbox(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "✓" if task["completed"] else "✗"
            self.task_listbox.insert(tk.END, f"{status} {task['title']}")

    def add_task(self):
        task_title = self.task_entry.get().strip()
        if task_title == "":
            messagebox.showwarning("Warning", "Task cannot be empty.")
            return

        new_task = {
            "title": task_title,
            "completed": False
        }

        self.tasks.append(new_task)
        self.save_tasks()
        self.refresh_listbox()
        self.task_entry.delete(0, tk.END)

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def complete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks[selected_index]["completed"] = True
            self.save_tasks()
            self.refresh_listbox()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to complete.")


if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
