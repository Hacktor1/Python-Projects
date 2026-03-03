import tkinter as tk
import time
import math

root = tk.Tk()
root.title("Analogy Clocks")

WIDTH = 400
HEIGHT = 400
CENTER = WIDTH // 2
RADIUS = 180

canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT, bg="white")
canvas.pack()


def draw_clock():
    canvas.delete("all")

    canvas.create_oval(CENTER - RADIUS, CENTER - RADIUS,
                       CENTER + RADIUS, CENTER + RADIUS,
                       width=4)

    for i in range(1, 13):
        angle = math.radians(i * 30 - 90)
        x = CENTER + math.cos(angle) * (RADIUS - 30)
        y = CENTER + math.sin(angle) * (RADIUS - 30)
        canvas.create_text(x, y, text=str(i), font=("Arial", 16, "bold"))

    current_time = time.localtime()
    hour = current_time.tm_hour % 12
    minute = current_time.tm_min
    second = current_time.tm_sec

    hour_angle = math.radians((hour + minute / 60) * 30 - 90)
    minute_angle = math.radians(minute * 6 - 90)
    second_angle = math.radians(second * 6 - 90)

    canvas.create_line(CENTER, CENTER,
                       CENTER + math.cos(hour_angle) * 80,
                       CENTER + math.sin(hour_angle) * 80,
                       width=6, fill="black")

    canvas.create_line(CENTER, CENTER,
                       CENTER + math.cos(minute_angle) * 120,
                       CENTER + math.sin(minute_angle) * 120,
                       width=4, fill="blue")

    canvas.create_line(CENTER, CENTER,
                       CENTER + math.cos(second_angle) * 150,
                       CENTER + math.sin(second_angle) * 150,
                       width=2, fill="red")

    canvas.create_oval(CENTER - 5, CENTER - 5,
                       CENTER + 5, CENTER + 5,
                       fill="black")

    root.after(1000, draw_clock)


draw_clock()
root.mainloop()