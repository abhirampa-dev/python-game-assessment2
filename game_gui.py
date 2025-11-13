# I acknowledge the use of ChatGPT (GPT-5, OpenAI, https://chat.openai.com/)
# to assist in creating this code.

import random
import tkinter as tk
from tkinter import messagebox

number = random.randint(1, 10)

def check_guess():
    try:
        guess = int(entry.get())
        if guess < number:
            messagebox.showinfo("Hint", "Too low!")
        elif guess > number:
            messagebox.showinfo("Hint", "Too high!")
        else:
            messagebox.showinfo("Winner", "You guessed it!")
    except ValueError:
        messagebox.showwarning("Error", "Please enter a valid number!")

root = tk.Tk()
root.title("Number Guessing Game")

tk.Label(root, text="Guess a number between 1 and 10:").pack()
entry = tk.Entry(root)
entry.pack()
tk.Button(root, text="Submit", command=check_guess).pack()

root.mainloop()
