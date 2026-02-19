import tkinter as tk
import random

points = 100


def spin(color_choice):
    global points

    try:
        bet = int(entry_bet.get())
    except ValueError:
        result_label.config(text="Enter bet")
        return

    if bet <= 0:
        result_label.config(text="Bet must be bigger than 0!")
        return

    if bet > points:
        result_label.config(text="You got no points!")
        return

    colors = ["red"] * 7 + ["black"] * 7 + ["green"]
    result = random.choice(colors)

    if result == color_choice:
        if result == "green":
            win = bet * 14
        else:
            win = bet * 2
        points += win - bet
        result_label.config(text=f"Result {result}! You win {win} points!")
    else:
        points -= bet
        result_label.config(text=f"Result {result}! You lose {bet} points...")

    points_label.config(text=f"Points: {points}")


root = tk.Tk()
root.title("Mini Roulette")
root.geometry("300x300")

points_label = tk.Label(root, text=f"Body: {points}", font=("Arial", 14))
points_label.pack(pady=10)

entry_bet = tk.Entry(root)
entry_bet.pack(pady=5)
entry_bet.insert(0, "10")

btn_red = tk.Button(root, text="Red", bg="red", fg="white",
                    command=lambda: spin("red"))
btn_red.pack(pady=5)

btn_black = tk.Button(root, text="Black", bg="black", fg="white",
                      command=lambda: spin("black"))
btn_black.pack(pady=5)

btn_green = tk.Button(root, text="Green", bg="green", fg="white",
                      command=lambda: spin("green"))
btn_green.pack(pady=5)

result_label = tk.Label(root, text="", font=("Arial", 12))
result_label.pack(pady=10)

root.mainloop()