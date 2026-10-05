# Python Projects

A collection of small, self-contained Python applications built for automation, GUI tools, and learning experiments. Each project lives in its own folder with its own README.

## Overview

Projects are grouped by category:

- **apps/** — Standalone productivity applications (e.g. workout tracker)
- **discord-bots/** — Discord bots built with `discord.py`
- **gui-apps/** — Desktop GUI applications using `tkinter`, `customtkinter`, `matplotlib`, and `PIL`
- **mini-projects/** — Quick, experimental games and utilities

## Shared Dependencies

Most projects rely on standard or commonly-installed libraries:

* `tkinter` — GUI (usually bundled with Python)
* `matplotlib` — Plotting and charts
* `pandas` — Data handling
* `customtkinter` — Themed GUI widgets
* `PIL` (Pillow) — Image processing
* `psutil` — System monitoring
* `speedtest` — Network speed testing
* `discord.py` — Discord bot framework

Install any missing libraries via pip:

```bash
pip install matplotlib pandas customtkinter pillow psutil speedtest-cli discord.py
```

## Project Index

| Category | Project | Description |
| --- | --- | --- |
| apps | pushup-tracker | Desktop push-up progress tracker with CSV logging and live graphs |
| discord-bots | python-discord-welcomer | Discord bot with slash commands for configurable welcome messages |
| gui-apps | analogy-clock | Analog clock GUI with live updating hands |
| gui-apps | network-monitoring | Network speed monitor with real-time graphs and alerts |
| gui-apps | password-generator | Random password generator with local storage |
| gui-apps | pc-resource-monitor | Real-time PC resource monitor (CPU, RAM, disk) |
| gui-apps | personal-finance-dashboard | Personal finance tracker with CSV import/export and charts |
| gui-apps | rgb-picker | RGB color picker with live preview |
| gui-apps | smart-color-analyzer | Image color palette analyzer |
| gui-apps | todo-list | Desktop to-do list with JSON persistence |
| mini-projects | roulette | Mini roulette betting game |

## Running a Project

Each project can be run from its own directory:

```bash
cd <project-folder>
python <script-name>.py
```

See individual README files for setup details and dependencies.