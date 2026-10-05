# Random Password Generator

A **password generator** GUI built with `tkinter`. Generate secure random passwords with customizable length and character sets, and store them locally in a JSON file.

## Features

* **Customizable Length** — Set the desired password length
* **Character Options** — Toggle inclusion of letters, numbers, and symbols
* **Local Storage** — Save generated passwords to `passwords.json`
* **Password Management** — Delete saved passwords individually

## Project Structure

```
password-generator/
├── password-generator.py   # Main script containing GUI and logic
└── passwords.json          # Local database for saved passwords (auto-created)
```

## Requirements & Dependencies

1. **Python**: Version 3.x
2. **Library**:
* `tkinter` (usually pre-installed with standard Python installations)

## Setup and Running

1. Run the script:
```bash
python password-generator.py
```
