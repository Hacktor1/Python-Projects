import customtkinter as ctk
import tkinter as tk
from tkinter import ttk
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from datetime import datetime
import os

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("dark-blue")

FILE_NAME = "pushup_data.csv"

def load_data():
    if os.path.exists(FILE_NAME):
        return pd.read_csv(FILE_NAME)
    else:
        df = pd.DataFrame(columns=["Date", "Pushups", "Time_seconds"])
        df.to_csv(FILE_NAME, index=False)
        return df

def save_data(df):
    df.to_csv(FILE_NAME, index=False)

data = load_data()

app = ctk.CTk()
app.title("Push-Up Progress Tracker")
app.geometry("1000x700")

left_frame = ctk.CTkFrame(app, width=300)
left_frame.pack(side="left", fill="y", padx=20, pady=20)

title_label = ctk.CTkLabel(left_frame, text="💪 Push-Up Tracker", font=("Arial", 24, "bold"))
title_label.pack(pady=20)

pushup_entry = ctk.CTkEntry(left_frame, placeholder_text="Number of Push-ups")
pushup_entry.pack(pady=10)

time_entry = ctk.CTkEntry(left_frame, placeholder_text="Time in seconds")
time_entry.pack(pady=10)

def add_entry():
    global data
    try:
        pushups = int(pushup_entry.get())
        time_sec = float(time_entry.get())
    except:
        return
    
    today = datetime.now().strftime("%Y-%m-%d")
    
    new_row = {"Date": today, "Pushups": pushups, "Time_seconds": time_sec}
    data = pd.concat([data, pd.DataFrame([new_row])], ignore_index=True)
    save_data(data)
    
    update_table()
    update_graph()
    
    pushup_entry.delete(0, tk.END)
    time_entry.delete(0, tk.END)

add_button = ctk.CTkButton(left_frame, text="Add Entry", command=add_entry)
add_button.pack(pady=20)

right_frame = ctk.CTkFrame(app)
right_frame.pack(side="right", expand=True, fill="both", padx=20, pady=20)

table = ttk.Treeview(right_frame, columns=("Date", "Pushups", "Time"), show="headings")
table.heading("Date", text="Date")
table.heading("Pushups", text="Push-ups")
table.heading("Time", text="Time (sec)")
table.pack(fill="x", pady=20)

def update_table():
    for row in table.get_children():
        table.delete(row)
    for _, row in data.iterrows():
        table.insert("", "end", values=(row["Date"], row["Pushups"], row["Time_seconds"]))

update_table()

fig, ax = plt.subplots(figsize=(6,4), facecolor="#1e1e1e")
canvas = FigureCanvasTkAgg(fig, master=right_frame)
canvas.get_tk_widget().pack(fill="both", expand=True)

def update_graph():
    ax.clear()
    fig.patch.set_facecolor("#1e1e1e")
    ax.set_facecolor("#1e1e1e")
    
    if len(data) > 0:
        ax.plot(data["Date"], data["Pushups"], marker="o", label="Push-ups")
        ax.set_xlabel("Date", color="white")
        ax.set_ylabel("Push-ups", color="white")
        ax.tick_params(colors='white')
        ax.legend()
    
    canvas.draw()

update_graph()

app.mainloop()