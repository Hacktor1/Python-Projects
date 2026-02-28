import tkinter as tk
from tkinter import ttk, messagebox, filedialog
import csv
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class FinanceDashboard:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Finance Dashboard")
        self.root.geometry("900x600")

        self.data = []

        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack(fill="x")

        tk.Label(frame_input, text="Type:").grid(row=0, column=0, sticky="w")
        self.combo_type = ttk.Combobox(frame_input, values=["Income", "Expense"], width=10)
        self.combo_type.current(0)
        self.combo_type.grid(row=0, column=1, padx=5)

        tk.Label(frame_input, text="Category:").grid(row=0, column=2, sticky="w")
        self.entry_category = tk.Entry(frame_input)
        self.entry_category.grid(row=0, column=3, padx=5)

        tk.Label(frame_input, text="Amount:").grid(row=0, column=4, sticky="w")
        self.entry_amount = tk.Entry(frame_input)
        self.entry_amount.grid(row=0, column=5, padx=5)

        tk.Label(frame_input, text="Date (YYYY-MM-DD):").grid(row=0, column=6, sticky="w")
        self.entry_date = tk.Entry(frame_input)
        self.entry_date.grid(row=0, column=7, padx=5)
        self.entry_date.insert(0, datetime.today().strftime("%Y-%m-%d"))

        tk.Button(frame_input, text="Add Record", command=self.add_record).grid(row=0, column=8, padx=5)
        tk.Button(frame_input, text="Load CSV", command=self.load_csv).grid(row=1, column=0, pady=5)
        tk.Button(frame_input, text="Save CSV", command=self.save_csv).grid(row=1, column=1, pady=5)
        tk.Button(frame_input, text="Show Charts", command=self.show_charts).grid(row=1, column=2, pady=5)

        frame_table = tk.Frame(root)
        frame_table.pack(fill="both", expand=True, pady=10)

        columns = ("type", "category", "amount", "date")
        self.tree = ttk.Treeview(frame_table, columns=columns, show="headings")
        self.tree.heading("type", text="Type")
        self.tree.heading("category", text="Category")
        self.tree.heading("amount", text="Amount")
        self.tree.heading("date", text="Date")
        self.tree.pack(fill="both", expand=True, side="left")

        scrollbar = ttk.Scrollbar(frame_table, orient="vertical", command=self.tree.yview)
        self.tree.configure(yscroll=scrollbar.set)
        scrollbar.pack(side="right", fill="y")

    def add_record(self):
        rtype = self.combo_type.get()
        category = self.entry_category.get()
        amount = self.entry_amount.get()
        date_str = self.entry_date.get()

        if not category or not amount:
            messagebox.showwarning("Input Error", "Please fill all fields")
            return
        try:
            amount = float(amount)
            datetime.strptime(date_str, "%Y-%m-%d")
        except:
            messagebox.showerror("Input Error", "Invalid amount or date format")
            return

        record = {"type": rtype, "category": category, "amount": amount, "date": date_str}
        self.data.append(record)
        self.refresh_tree()

    def refresh_tree(self):
        for i in self.tree.get_children():
            self.tree.delete(i)
        for record in self.data:
            self.tree.insert("", "end", values=(record["type"], record["category"], record["amount"], record["date"]))

    def save_csv(self):
        if not self.data:
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".csv", filetypes=[("CSV files","*.csv")])
        if file_path:
            with open(file_path, "w", newline="") as f:
                writer = csv.DictWriter(f, fieldnames=["type","category","amount","date"])
                writer.writeheader()
                writer.writerows(self.data)
            messagebox.showinfo("Saved", f"Data saved to {file_path}")

    def load_csv(self):
        file_path = filedialog.askopenfilename(filetypes=[("CSV files","*.csv")])
        if file_path:
            with open(file_path, "r") as f:
                reader = csv.DictReader(f)
                self.data = []
                for row in reader:
                    row["amount"] = float(row["amount"])
                    self.data.append(row)
            self.refresh_tree()
            messagebox.showinfo("Loaded", f"Data loaded from {file_path}")

    def show_charts(self):
        if not self.data:
            return

        income = {}
        expense = {}

        for record in self.data:
            cat = record["category"]
            if record["type"] == "Income":
                income[cat] = income.get(cat,0) + record["amount"]
            else:
                expense[cat] = expense.get(cat,0) + record["amount"]

        fig, axs = plt.subplots(1,2, figsize=(10,5))
        axs[0].pie(income.values(), labels=income.keys(), autopct="%1.1f%%")
        axs[0].set_title("Income by Category")
        axs[1].pie(expense.values(), labels=expense.keys(), autopct="%1.1f%%")
        axs[1].set_title("Expense by Category")
        plt.tight_layout()
        plt.show()

if __name__ == "__main__":
    root = tk.Tk()
    app = FinanceDashboard(root)
    root.mainloop()
