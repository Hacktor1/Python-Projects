# Smart Color Analyzer & Palette Generator

An **image color analyzer** GUI built with `tkinter` and `PIL`. Load an image, analyze its dominant colors, generate a palette, and export the hex codes to a text file.

## Features

* **Image Loading** — Load PNG/JPG/JPEG images from your computer
* **Color Analysis** — Identifies the top 10 dominant colors using `PIL` and `Counter`
* **Palette Display** — Visual color palette shown as colored blocks on a canvas
* **Hex Export** — Saves the color palette hex codes to a `.txt` file

## Project Structure

```
smart-color-analyzer/
└── smart-color-analyzer.py   # Main script containing GUI and analysis logic
```

## Requirements & Dependencies

1. **Python**: Version 3.x
2. **Libraries**:
* `tkinter`
* `Pillow` (PIL)

Install the required library via terminal/CLI:

```bash
pip install pillow
```

## Setup and Running

1. Ensure the dependency is installed (see above).
2. Run the script:
```bash
python smart-color-analyzer.py
```
