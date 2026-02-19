import tkinter as tk

def update_color(event=None):
    r = scale_r.get()
    g = scale_g.get()
    b = scale_b.get()

    color = f"#{r:02x}{g:02x}{b:02x}"
    brightness = (r * 0.299 + g * 0.587 + b * 0.114)

    text_color = "black" if brightness > 186 else "white"

    display.config(bg=color, fg=text_color, text=color)

root = tk.Tk()
root.geometry("900x900")

scale_r = tk.Scale(root, from_=0, to=255, orient="horizontal", command=update_color)
scale_g = tk.Scale(root, from_=0, to=255, orient="horizontal", command=update_color)
scale_b = tk.Scale(root, from_=0, to=255, orient="horizontal", command=update_color)


scale_r.pack(fill="x")
scale_g.pack(fill="x")
scale_b.pack(fill="x")


display = tk.Label(root, font=("Arial", 32))
display.pack(fill="both", expand=True)

update_color()

root.mainloop()