import tkinter as tk
from tkinter import ttk
import psutil
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from collections import deque
import time


class PCMonitorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("PC Resource Monitor")
        self.root.geometry("900x600")

        self.max_points = 60
        self.cpu_data = deque([0]*self.max_points, maxlen=self.max_points)
        self.ram_data = deque([0]*self.max_points, maxlen=self.max_points)
        self.disk_data = deque([0]*self.max_points, maxlen=self.max_points)

        self.create_widgets()
        self.update_stats()

    def create_widgets(self):
        top_frame = tk.Frame(self.root)
        top_frame.pack(pady=10)

        self.cpu_label = tk.Label(top_frame, text="CPU: 0%", font=("Arial", 14))
        self.cpu_label.grid(row=0, column=0, padx=20)

        self.ram_label = tk.Label(top_frame, text="RAM: 0%", font=("Arial", 14))
        self.ram_label.grid(row=0, column=1, padx=20)

        self.disk_label = tk.Label(top_frame, text="Disk: 0%", font=("Arial", 14))
        self.disk_label.grid(row=0, column=2, padx=20)

        self.figure, self.ax = plt.subplots(figsize=(8, 4))
        self.ax.set_ylim(0, 100)
        self.ax.set_title("System Usage (Last 60 Seconds)")
        self.ax.set_ylabel("Usage (%)")
        self.ax.set_xlabel("Time (seconds ago)")

        self.cpu_line, = self.ax.plot(self.cpu_data, label="CPU")
        self.ram_line, = self.ax.plot(self.ram_data, label="RAM")
        self.disk_line, = self.ax.plot(self.disk_data, label="Disk")

        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.figure, master=self.root)
        self.canvas.get_tk_widget().pack(pady=20)

    def update_stats(self):
        cpu = psutil.cpu_percent()
        ram = psutil.virtual_memory().percent
        disk = psutil.disk_usage('/').percent

        self.cpu_label.config(text=f"CPU: {cpu}%")
        self.ram_label.config(text=f"RAM: {ram}%")
        self.disk_label.config(text=f"Disk: {disk}%")

        self.cpu_data.append(cpu)
        self.ram_data.append(ram)
        self.disk_data.append(disk)

        self.cpu_line.set_ydata(self.cpu_data)
        self.ram_line.set_ydata(self.ram_data)
        self.disk_line.set_ydata(self.disk_data)

        self.ax.set_xlim(0, len(self.cpu_data))
        self.canvas.draw()

        self.root.after(1000, self.update_stats)


if __name__ == "__main__":
    root = tk.Tk()
    app = PCMonitorApp(root)
    root.mainloop()
