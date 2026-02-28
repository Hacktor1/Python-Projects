import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
from collections import Counter


class ColorAnalyzer:
    def __init__(self, root):
        self.root = root
        self.root.title("Smart Image Color Analyzer & Palette Generator")
        self.root.geometry("700x600")

        tk.Button(root, text="Load Image", command=self.load_image).pack(pady=10)
        tk.Button(root, text="Analyze Colors", command=self.analyze_colors).pack(pady=10)
        tk.Button(root, text="Save Palette", command=self.save_palette).pack(pady=10)

        tk.Label(root, text="Top Colors:").pack()
        self.canvas = tk.Canvas(root, width=600, height=300, bg="white")
        self.canvas.pack(pady=10)

        self.hex_label = tk.Label(root, text="", font=("Arial", 12))
        self.hex_label.pack()

        self.image = None
        self.palette = []

    def load_image(self):
        file_path = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
        if file_path:
            self.image = Image.open(file_path)
            messagebox.showinfo("Loaded", f"Image loaded: {file_path}")

    def analyze_colors(self):
        if not self.image:
            messagebox.showwarning("No Image", "Please load an image first!")
            return

        img = self.image.copy()
        img.thumbnail((200, 200))
        pixels = list(img.getdata())
        pixels = [pixel[:3] for pixel in pixels]  # ignore alpha

        counter = Counter(pixels)
        top_colors = counter.most_common(10)
        self.palette = [color for color, _ in top_colors]

        self.canvas.delete("all")
        width = 50
        for i, color in enumerate(self.palette):
            x0 = i * width
            x1 = x0 + width
            self.canvas.create_rectangle(x0, 0, x1, 300, fill=self.rgb_to_hex(color), outline="black")

        hex_codes = [self.rgb_to_hex(c) for c in self.palette]
        self.hex_label.config(text="Hex Codes: " + ", ".join(hex_codes))

    def rgb_to_hex(self, rgb):
        return '#%02x%02x%02x' % rgb

    def save_palette(self):
        if not self.palette:
            messagebox.showwarning("No Palette", "Analyze colors first!")
            return
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text Files", "*.txt")])
        if file_path:
            with open(file_path, "w") as f:
                for color in self.palette:
                    f.write(self.rgb_to_hex(color) + "\n")
            messagebox.showinfo("Saved", f"Palette saved to {file_path}")


if __name__ == "__main__":
    root = tk.Tk()
    app = ColorAnalyzer(root)
    root.mainloop()
