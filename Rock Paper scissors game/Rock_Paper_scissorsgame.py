import tkinter as tk
import random

user_score = 0
computer_score = 0

def play(user_choice):
    global user_score, computer_score
    computer_choice = random.choice(["rock", "paper", "scissors"])

    result = determine_winner(user_choice, computer_choice)
    display_result(result)

    if "You win" in result:
        user_score += 1
        display_result(result, "green")
    elif "Computer wins" in result:
        computer_score += 1
        display_result(result, "red")

    update_score_label()

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "rock" and computer_choice == "scissors") or \
         (user_choice == "scissors" and computer_choice == "paper") or \
         (user_choice == "paper" and computer_choice == "rock"):
        return f"You win! {user_choice} beats {computer_choice}"
    else:
        return f"Computer wins! {computer_choice} beats {user_choice}"

def display_result(result, color=None):
    result_label.config(text=result, fg=color)

def update_score_label():
    score_label.config(text=f"Your score: {user_score}  |  Computer's score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score = 0
    computer_score = 0
    update_score_label()
    display_result("", "black")

root = tk.Tk()
root.title("Rock Paper Scissors Game")
root.configure(bg="#121212")
root.geometry("350x305")
root.minsize(350,305)

custom_font = ("Arial", 14)

title_label = tk.Label(root, text="Rock Paper Scissors", fg="white", bg="#121212", font=("Helvetica", 20))
title_label.pack(pady=10)

result_label = tk.Label(root, text="", fg="white", bg="#121212", font=custom_font)
result_label.pack()

choices_frame = tk.Frame(root, bg="#121212")
choices_frame.pack(pady=10)

rock_button = tk.Button(choices_frame, text="Rock", command=lambda: play("rock"), bg="#333333", fg="white", font=custom_font)
paper_button = tk.Button(choices_frame, text="Paper", command=lambda: play("paper"), bg="#333333", fg="white", font=custom_font)
scissors_button = tk.Button(choices_frame, text="Scissors", command=lambda: play("scissors"), bg="#333333", fg="white", font=custom_font)

rock_button.grid(row=0, column=0, padx=10)
paper_button.grid(row=0, column=1, padx=10)
scissors_button.grid(row=0, column=2, padx=10)

score_label = tk.Label(root, text=f"Your score: {user_score}  |  Computer's score: {computer_score}", fg="white", bg="#121212", font=custom_font)
score_label.pack()

reset_button = tk.Button(root, text="Reset Game", command=reset_game, bg="#333333", fg="white", font=custom_font)
reset_button.pack(pady=20)

root.mainloop()
