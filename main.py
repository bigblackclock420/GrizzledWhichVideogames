import tkinter as tk
import math_game
def math():
    if not username:
        show_error("Please enter a username.")
    else:
        math_game.run(username)

def show_error(message):
    error_label.config(text=message)

def set_username():
    global username
    username = username_entry.get()
    username_entry.delete(0, tk.END)  # Clear the username entry field
    welcome_label.config(text=f"Welcome, {username}!")

window = tk.Tk()
window.title("Main Menu")
window.geometry("300x350")

# Label for the welcome message
power = tk.Label(text="Welcome to the Game.\nSelect the game you want.")
power.pack()

# Entry field for entering a username
username_label = tk.Label(text="Enter Username:")
username_label.pack()
username_entry = tk.Entry()
username_entry.pack()

# Button to set the username
set_username_button = tk.Button(text="Set Username", command=set_username)
set_username_button.pack()

# Error label for displaying validation messages
error_label = tk.Label(text="", fg="red")
error_label.pack()

# Label to display the welcome message with the username
welcome_label = tk.Label(text="")
welcome_label.pack()

# Button to start the math game
button_math = tk.Button(text="Math Game", command=math)
button_math.pack()

tk.mainloop()
