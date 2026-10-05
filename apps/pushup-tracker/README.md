# Push-Up Progress Tracker

A desktop **push-up progress tracker** built with `customtkinter`, `pandas`, and `matplotlib`. Record your push-up count and time, visualize trends with a live-updating graph, and store everything locally in a CSV file.

## Features

* **Live Graphing** — Real-time plot of push-up count over time using `matplotlib`
* **CSV Storage** — All entries are saved to a local `pushup_data.csv` file
* **Dark Theme** — Clean dark-mode interface via `customtkinter`
* **Table View** — Overview of all recorded entries in a sortable table

## Project Structure

```
pushup-tracker/
├── pushup.py             # Main application script
├── pushup_data.csv       # Local database for push-up entries (auto-created)
└── pushup.exe            # Precompiled executable (optional)
```

## Requirements & Dependencies

1. **Python**: Version 3.8 or higher
2. **Libraries**:
* `customtkinter`
* `pandas`
* `matplotlib`

Install the required libraries via terminal/CLI:

```bash
pip install customtkinter pandas matplotlib
```

## Setup and Running

1. Ensure all dependencies are installed (see above).
2. Run the script:
```bash
python pushup.py
```
