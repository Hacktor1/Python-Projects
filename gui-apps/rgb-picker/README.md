\# 🎨 RGB Picker (Tkinter)



A simple RGB color picker built with Python and Tkinter.

This application allows you to interactively adjust Red, Green, and Blue values using sliders and instantly see the resulting color along with its HEX code.



---



\## 📌 Features



\* 🎚 Three sliders for \*\*Red\*\*, \*\*Green\*\*, and \*\*Blue\*\* values (0–255)

\* 🎨 Live color preview

\* 🔢 Automatically generated HEX color code

\* 🌗 Automatic text color adjustment (black/white) based on brightness for better readability

\* 🖥 Simple and clean GUI using Tkinter



---



\## 📂 Project Structure



```

rgb-picker.py

README.md

```



---



\## ⚙️ Requirements



\* Python 3.x

\* Tkinter (usually included with standard Python installation)



To check your Python version:



```bash

python --version

```



If Tkinter is not installed:



\### On Windows



Tkinter is included by default with Python.



\### On Linux (Debian/Ubuntu)



```bash

sudo apt install python3-tk

```



\### On macOS



Tkinter is included with the official Python installer from python.org.



---



\## 🚀 Installation \& Usage



1\. Clone this repository or download the file:



```bash

git clone https://github.com/your-username/rgb-picker.git

cd rgb-picker

```



2\. Run the application:



```bash

python rgb-picker.py

```



That’s it! 🎉



---



\## 🧠 How It Works



\* Each slider controls one RGB channel (0–255).

\* The selected values are converted into a HEX color string using:



```python

color = f"#{r:02x}{g:02x}{b:02x}"

```



\* Brightness is calculated using the formula:



```

brightness = (r \* 0.299 + g \* 0.587 + b \* 0.114)

```



\* Based on brightness, the text color automatically switches to black or white for better visibility.



---



\## 🖼 Example



If you set:



\* R = 255

\* G = 0

\* B = 0



The displayed HEX color will be:



```

\#ff0000

```



---



\## 📖 License



This project is open-source and free to use for educational purposes.

