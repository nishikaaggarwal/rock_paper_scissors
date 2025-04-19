import tkinter as tk
from tkinter import ttk
import random
from typing import Literal
import os
from pathlib import Path

class RockPaperScissorsGame:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Rock Paper Scissors")
        self.window.geometry("600x800")
        self.window.configure(bg="#f0f4f8")

        # Initialize scores
        self.user_score = 0
        self.computer_score = 0
        
        # Game choices
        self.choices = ["Rock", "Paper", "Scissors"]
        
        self.setup_styles()
        self.create_widgets()
        
    def setup_styles(self):
        # Configure styles
        style = ttk.Style()
        style.configure("Game.TFrame", background="#f0f4f8")
        style.configure("Choice.TButton", 
                       padding=20, 
                       font=("Helvetica", 12, "bold"))
        style.configure("Score.TLabel", 
                       background="#ffffff",
                       font=("Helvetica", 14))
        style.configure("Result.TLabel",
                       background="#ffffff",
                       font=("Helvetica", 16, "bold"))
        style.configure("Title.TLabel",
                       background="#ffffff",
                       font=("Helvetica", 24, "bold"))
        
    def create_widgets(self):
        # Main container
        self.main_frame = ttk.Frame(self.window, style="Game.TFrame")
        self.main_frame.pack(expand=True, fill="both", padx=20, pady=20)

        # Title
        title_frame = ttk.Frame(self.main_frame)
        title_frame.pack(fill="x", pady=(0, 20))
        ttk.Label(
            title_frame,
            text="Rock Paper Scissors",
            style="Title.TLabel"
        ).pack(anchor="center")

        # Score display
        self.score_frame = ttk.Frame(self.main_frame)
        self.score_frame.pack(fill="x", pady=(0, 20))
        
        # Player score
        self.player_score_label = ttk.Label(
            self.score_frame,
            text=f"You: {self.user_score}",
            style="Score.TLabel"
        )
        self.player_score_label.pack(side="left", padx=20)
        
        # Computer score
        self.computer_score_label = ttk.Label(
            self.score_frame,
            text=f"Computer: {self.computer_score}",
            style="Score.TLabel"
        )
        self.computer_score_label.pack(side="right", padx=20)

        # Choices frame
        self.choices_frame = ttk.Frame(self.main_frame)
        self.choices_frame.pack(fill="x", pady=20)
        
        # Create choice buttons
        for choice in self.choices:
            btn = ttk.Button(
                self.choices_frame,
                text=choice,
                style="Choice.TButton",
                command=lambda c=choice: self.play_game(c)
            )
            btn.pack(side="left", expand=True, padx=10)

        # Result display
        self.result_frame = ttk.Frame(self.main_frame)
        self.result_frame.pack(fill="x", pady=20)
        
        self.player_choice_label = ttk.Label(
            self.result_frame,
            text="",
            style="Score.TLabel"
        )
        self.player_choice_label.pack(pady=5)
        
        self.computer_choice_label = ttk.Label(
            self.result_frame,
            text="",
            style="Score.TLabel"
        )
        self.computer_choice_label.pack(pady=5)
        
        self.result_label = ttk.Label(
            self.result_frame,
            text="",
            style="Result.TLabel"
        )
        self.result_label.pack(pady=10)

        # Play Again button
        self.play_again_btn = ttk.Button(
            self.main_frame,
            text="Play Again",
            style="Choice.TButton",
            command=self.reset_game
        )
        self.play_again_btn.pack(pady=20)

    def play_game(self, user_choice: str):
        computer_choice = random.choice(self.choices)
        
        # Update choice labels
        self.player_choice_label.config(
            text=f"Your choice: {user_choice}"
        )
        self.computer_choice_label.config(
            text=f"Computer's choice: {computer_choice}"
        )
        
        # Determine winner
        if user_choice == computer_choice:
            result = "It's a tie!"
            self.result_label.config(text=result, foreground="#ffd700")
        elif (
            (user_choice == "Rock" and computer_choice == "Scissors") or
            (user_choice == "Paper" and computer_choice == "Rock") or
            (user_choice == "Scissors" and computer_choice == "Paper")
        ):
            result = "You win!"
            self.user_score += 1
            self.result_label.config(text=result, foreground="#008000")
        else:
            result = "Computer wins!"
            self.computer_score += 1
            self.result_label.config(text=result, foreground="#ff0000")
        
        # Update score labels
        self.player_score_label.config(text=f"You: {self.user_score}")
        self.computer_score_label.config(text=f"Computer: {self.computer_score}")

    def reset_game(self):
        self.player_choice_label.config(text="")
        self.computer_choice_label.config(text="")
        self.result_label.config(text="")

    def run(self):
        self.window.mainloop()

if __name__ == "__main__":
    game = RockPaperScissorsGame()
    game.run()
