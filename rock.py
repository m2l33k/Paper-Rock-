import tkinter as tk
from tkinter import messagebox
import random

class RockPaperScissorsApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Rock-Paper-Scissors")

        # Create GUI components
        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Rock, Paper, Scissors", font=('Arial', 20)).pack(pady=10)

        self.choice_var = tk.StringVar(value="")

        # Buttons for user choices
        tk.Button(self.root, text="Rock", command=lambda: self.user_choice("Rock")).pack(pady=5)
        tk.Button(self.root, text="Paper", command=lambda: self.user_choice("Paper")).pack(pady=5)
        tk.Button(self.root, text="Scissors", command=lambda: self.user_choice("Scissors")).pack(pady=5)

        # Result display
        self.result_label = tk.Label(self.root, text="", font=('Arial', 16))
        self.result_label.pack(pady=20)

    def user_choice(self, user_choice):
        computer_choice = random.choice(["Rock", "Paper", "Scissors"])
        result = self.determine_winner(user_choice, computer_choice)

        self.result_label.config(text=f"Computer chose: {computer_choice}\n{result}")

    def determine_winner(self, user_choice, computer_choice):
        if user_choice == computer_choice:
            return "It's a tie!"
        elif (user_choice == "Rock" and computer_choice == "Scissors") or \
             (user_choice == "Paper" and computer_choice == "Rock") or \
             (user_choice == "Scissors" and computer_choice == "Paper"):
            return "You win!"
        else:
            return "You lose!"

if __name__ == "__main__":
    root = tk.Tk()
    app = RockPaperScissorsApp(root)
    root.mainloop()
