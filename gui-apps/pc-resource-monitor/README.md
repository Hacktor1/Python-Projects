# PC Resource Monitor

A **real-time PC resource monitor** built with `tkinter`, `psutil`, and `matplotlib`. Tracks CPU, RAM, and disk usage with a live-updating graph.

## Features

* **Live Monitoring** — Real-time display of CPU, RAM, and disk usage percentages
* **Historical Graph** — Scrolling graph showing usage trends over the last 60 seconds
* **System Stats** — Uses `psutil` for accurate system resource reporting

## Project Structure

```
pc-resource-monitor/
└── pc-resource-monitor.py   # Main script containing GUI and monitoring logic
```

## Requirements & Dependencies

1. **Python**: Version 3.x
2. **Libraries**:
* `tkinter`
* `psutil`
* `matplotlib`

Install the required libraries via terminal/CLI:

```bash
pip install psutil matplotlib
```

## Setup and Running

1. Ensure all dependencies are installed (see above).
2. Run the script:
```bash
python pc-resource-monitor.py
```
