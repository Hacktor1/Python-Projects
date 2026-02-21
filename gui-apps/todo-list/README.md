# 📝 To-Do List Application (Tkinter + JSON)

A simple desktop To-Do List application built with Python and Tkinter.

The application allows you to:

* Add tasks
* Mark tasks as completed
* Delete tasks
* Automatically save tasks to a JSON file
* Reload tasks when reopening the program

---

## 📁 Project Structure

```
todo-list.py
tasks.json
README.md
```

### File Description

* **todo-list.py** → Main application file (GUI program)
* **tasks.json** → Stores all tasks permanently
* **README.md** → Project documentation

---

## ⚙️ Requirements

* Python 3.8 or newer
* Tkinter (included in standard Python installation)

To check your Python version:

```bash
python --version
```

---

## ▶️ How to Run the Application

1. Make sure both files are in the same folder:

   * `todo-list.py`
   * `tasks.json` (can be empty at first)

2. Open terminal or command prompt in that folder.

3. Run:

```bash
python todo-list.py
```

4. The application window will open.

---

## 🧠 How to Use the Application

### ➕ Add a Task

1. Type a task into the input field.
2. Click **"Add Task"**.
3. The task will appear in the list.

---

### ✅ Mark Task as Completed

1. Select a task from the list.
2. Click **"Mark as Completed"**.
3. The task will show a ✓ symbol.

---

### ❌ Delete a Task

1. Select a task from the list.
2. Click **"Delete Task"**.
3. The task will be removed permanently.

---

## 💾 How Data Storage Works

All tasks are saved inside `tasks.json`.

Example structure:

```json
[
    {
        "title": "Finish homework",
        "completed": false
    },
    {
        "title": "Go to the gym",
        "completed": true
    }
]
```

Each task contains:

* `title` → Task description
* `completed` → Boolean value (true or false)

The file updates automatically whenever:

* You add a task
* You mark a task as completed
* You delete a task

---

## 🛠 Troubleshooting

### Tkinter not working?

On Linux, install it manually:

```bash
sudo apt install python3-tk
```

### JSON file missing?

The application will create `tasks.json` automatically if it does not exist.

---

## 🚀 Possible Improvements

You can extend this project by adding:

* Dark mode
* Task deadlines
* Priority levels
* SQLite database
* Drag & drop reordering
* Task editing feature

---

## 📜 License


This project is free to use for learning and personal development.
