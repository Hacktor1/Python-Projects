# Network Monitor & Speed Tester

A **network monitoring** GUI built with `tkinter`, `speedtest`, and `matplotlib`. Test your internet speed once or start continuous monitoring with threshold-based alerts.

## Features

* **Speed Testing** — Measure download and upload speeds via `speedtest`
* **Continuous Monitoring** — Automatically runs tests at set intervals
* **Threshold Alerts** — Warns when download speed drops below a configurable limit
* **Real-time Graphs** — Live plotting of download and upload speeds over time

## Project Structure

```
network-monitoring/
└── network-monitoring.py   # Main script containing GUI and monitoring logic
```

## Requirements & Dependencies

1. **Python**: Version 3.x
2. **Libraries**:
* `tkinter`
* `speedtest-cli`
* `matplotlib`

Install the required libraries via terminal/CLI:

```bash
pip install speedtest-cli matplotlib
```

## Setup and Running

1. Ensure all dependencies are installed (see above).
2. Run the script:
```bash
python network-monitoring.py
```
