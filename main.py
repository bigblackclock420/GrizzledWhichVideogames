import tkinter as tk
import math_game
import spelling_game

def math():
    math_game.run()

def spelling():
    spelling_game.run()

window = tk.Tk()
window.title("Main Menu")
window.geometry("300x300")

power = tk.Label(text="Welcome to the Game.\nSelect the game you want.")
power.pack()

button = tk.Button(text="Math", command=math)
button.pack()

butt = tk.Button(text="Spelling", command=spelling)
butt.pack()

tk.mainloop()