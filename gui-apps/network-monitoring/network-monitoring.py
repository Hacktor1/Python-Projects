import tkinter as tk
from tkinter import ttk, messagebox
import speedtest
from datetime import datetime
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import threading
import time

class NetworkMonitor:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Monitor & Speed Tester")
        self.root.geometry("900x600")

        self.download_history = []
        self.upload_history = []
        self.time_history = []

        # --- INPUT FRAME ---
        frame_input = tk.Frame(root, padx=10, pady=10)
        frame_input.pack(fill="x")

        tk.Label(frame_input, text="Ping Server (optional):").grid(row=0, column=0, sticky="w")
        self.entry_server = tk.Entry(frame_input, width=30)
        self.entry_server.grid(row=0, column=1, padx=5)
        self.entry_server.insert(0, "8.8.8.8")

        tk.Label(frame_input, text="Alert if Download < (Mbps):").grid(row=0, column=2, sticky="w")
        self.entry_alert = tk.Entry(frame_input, width=10)
        self.entry_alert.grid(row=0, column=3, padx=5)
        self.entry_alert.insert(0, "10")

        tk.Button(frame_input, text="Test Speed Once", command=self.test_speed_once).grid(row=0, column=4, padx=5)
        tk.Button(frame_input, text="Start Monitoring", command=self.start_monitoring).grid(row=0, column=5, padx=5)
        tk.Button(frame_input, text="Stop Monitoring", command=self.stop_monitoring).grid(row=0, column=6, padx=5)

        # --- OUTPUT FRAME ---
        frame_output = tk.Frame(root, padx=10, pady=10)
        frame_output.pack(fill="both", expand=True)

        tk.Label(frame_output, text="Latest Test:").pack()
        self.label_result = tk.Label(frame_output, text="", font=("Arial", 12))
        self.label_result.pack(pady=5)

        # --- GRAPH FRAME ---
        self.fig, self.ax = plt.subplots(figsize=(8,4))
        self.ax.set_title("Download & Upload Speed (Mbps)")
        self.ax.set_xlabel("Time")
        self.ax.set_ylabel("Mbps")
        self.line_download, = self.ax.plot([], [], label="Download")
        self.line_upload, = self.ax.plot([], [], label="Upload")
        self.ax.legend()

        self.canvas = FigureCanvasTkAgg(self.fig, master=frame_output)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # Monitoring control
        self.monitoring = False

    # --- SPEED TEST FUNCTIONS ---
    def test_speed(self):
        st = speedtest.Speedtest()
        download = st.download() / 1e6  # Convert to Mbps
        upload = st.upload() / 1e6
        return round(download,2), round(upload,2)

    def test_speed_once(self):
        try:
            download, upload = self.test_speed()
            self.update_history(download, upload)
            self.update_graph()
            self.label_result.config(text=f"Download: {download} Mbps | Upload: {upload} Mbps")
            self.check_alert(download)
        except Exception as e:
            messagebox.showerror("Error", f"Speed test failed: {e}")

    # --- HISTORY & GRAPH ---
    def update_history(self, download, upload):
        self.download_history.append(download)
        self.upload_history.append(upload)
        self.time_history.append(datetime.now().strftime("%H:%M:%S"))
        if len(self.time_history) > 20:  # keep last 20 measurements
            self.download_history.pop(0)
            self.upload_history.pop(0)
            self.time_history.pop(0)

    def update_graph(self):
        self.line_download.set_data(range(len(self.download_history)), self.download_history)
        self.line_upload.set_data(range(len(self.upload_history)), self.upload_history)
        self.ax.set_xticks(range(len(self.time_history)))
        self.ax.set_xticklabels(self.time_history, rotation=45, ha="right")
        self.ax.relim()
        self.ax.autoscale_view()
        self.canvas.draw()

    # --- ALERT ---
    def check_alert(self, download):
        try:
            alert_threshold = float(self.entry_alert.get())
            if download < alert_threshold:
                messagebox.showwarning("Speed Alert", f"Download speed dropped below {alert_threshold} Mbps!")
        except:
            pass

    # --- MONITORING THREAD ---
    def start_monitoring(self):
        if self.monitoring:
            return
        self.monitoring = True
        self.thread = threading.Thread(target=self.monitor_loop, daemon=True)
        self.thread.start()

    def stop_monitoring(self):
        self.monitoring = False

    def monitor_loop(self):
        while self.monitoring:
            self.test_speed_once()
            time.sleep(60)  # every 60 seconds

if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkMonitor(root)
    root.mainloop()
