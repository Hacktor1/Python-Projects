# 🔐 Random Password Generator (Tkinter)

A simple desktop **Random Password Generator** built with Python and Tkinter.
This application allows users to generate secure passwords, save them locally, and manage saved passwords through a clean graphical interface.

---

## 📸 Preview

Features a simple GUI built with Tkinter:

* Choose password length
* Select character types (letters, numbers, symbols)
* Generate random passwords
* Save passwords locally
* Delete saved passwords

---

## 🚀 Features

* ✅ Custom password length
* ✅ Include/exclude:

  * Letters (A–Z, a–z)
  * Numbers (0–9)
  * Symbols (!@#$%^&* etc.)
* ✅ Save passwords to a local JSON file
* ✅ View saved passwords
* ✅ Delete selected passwords
* ✅ Error handling and validation

---

## 🛠️ Technologies Used

* Python 3
* Tkinter (built-in GUI library)
* JSON (for local storage)
* Random & String modules

---

## 📦 Installation

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/yourusername/random-password-generator.git
cd random-password-generator
```

### 2️⃣ Make Sure Python Is Installed

Check your Python version:

```bash
python --version
```

If not installed, download it from:
[https://www.python.org/downloads/](https://www.python.org/downloads/)

---

## ▶️ How to Run

Run the script:

```bash
python main.py
```

*(Replace `main.py` with your actual filename if different.)*

The GUI window will open.

---

## 📖 How to Use (Step-by-Step Tutorial)

### 1️⃣ Set Password Length

* Enter the desired password length in the input field.
* Default is **12 characters**.

### 2️⃣ Select Character Types

Check the boxes for:

* ✔ Include Letters
* ✔ Include Numbers
* ✔ Include Symbols

⚠ At least one option must be selected.

### 3️⃣ Generate Password

Click **"Generate Password"**.

The generated password will appear in the output field.

### 4️⃣ Save Password

Click **"Save Password"** to store it locally.

Saved passwords are stored in:

```
passwords.json
```

### 5️⃣ Delete a Password

* Select a password from the list.
* Click **"Delete Selected Password"**.

---

## 💾 File Storage

Passwords are stored in:

```bash
passwords.json
```

Example structure:

```json
[
    "aB3$kL9!xQ2@",
    "T7#pLm8&zR1!"
]
```

The file is automatically created when you save your first password.

---

## ⚠️ Important Notes

* Passwords are stored locally in plain text.
* This is a basic educational project.
* For production use, consider:

  * Encryption
  * Secure storage methods
  * Master password protection

---

## 🧠 Possible Improvements

* 🔒 Add password encryption
* 📋 Add copy-to-clipboard button
* 🔑 Add master password protection
* 🎨 Improve UI styling
* 📊 Add password strength indicator

---

## 📜 License

This project is open-source and free to use.

---

## 👨‍💻 Author

Created as a Python GUI practice project.
