import tkinter as tk
from tkinter import messagebox
import random

def computer_choice():
    return random.choice(['Rock', 'Paper', 'Scissors'])

def determine_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == 'Rock' and computer == 'Scissors') or \
         (user == 'Scissors' and computer == 'Paper') or \
         (user == 'Paper' and computer == 'Rock'):
        global user_score
        user_score += 1
        return "You win! "  
    else:
        global computer_score
        computer_score += 1
        return "You lose! "  

def play(user):
    computer = computer_choice()
    result = determine_winner(user, computer)
    result_label.config(text=f"Your choice: {user}\nComputer's choice: {computer}\n{result}")
    score_label.config(text=f"Your Score: {user_score}  Computer's Score: {computer_score}")

def reset_game():
    global user_score, computer_score
    user_score, computer_score = 0, 0
    result_label.config(text="")
    score_label.config(text=f"Your Score: {user_score}  Computer's Score: {computer_score}")

def quit_game():
    if messagebox.askyesno("Quit Game", "Are you sure you want to quit?"):
        root.destroy()

user_score = 0
computer_score = 0


root = tk.Tk()
root.title("Rock-Paper-Scissors Game")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#E6E6FA")  


title_label = tk.Label(root, text="Rock-Paper-Scissors Game", font=("Helvetica", 16, "bold"), pady=10, bg="#E6E6FA", fg="#333333")  
title_label.pack()


result_label = tk.Label(root, text="", font=("Helvetica", 12), pady=10, bg="#E6E6FA", fg="#9932CC")  # Dark 
result_label.pack()

score_label = tk.Label(root, text=f"Your Score: {user_score}  Computer's Score: {computer_score}", font=("Helvetica", 12), bg="#E6E6FA", fg="#9932CC")  
score_label.pack()


button_frame = tk.Frame(root, bg="#E6E6FA")
button_frame.pack(pady=20)

button_style = {
    "font": ("Helvetica", 12),
    "width": 10,
    "relief": "raised",
    "bd": 5,
    "bg": "#D50032", 
    "fg": "white",
    "activebackground": "#B71C1C",  
    "activeforeground": "white"
}

rock_button = tk.Button(button_frame, text="\u270A Rock", command=lambda: play("Rock"), **button_style)
rock_button.grid(row=0, column=0, padx=5)

paper_button = tk.Button(button_frame, text="\u270B Paper", command=lambda: play("Paper"), **button_style)
paper_button.grid(row=0, column=1, padx=5)

scissors_button = tk.Button(button_frame, text="\u270C Scissors", command=lambda: play("Scissors"), **button_style)
scissors_button.grid(row=0, column=2, padx=5)

control_frame = tk.Frame(root, bg="#E6E6FA")
control_frame.pack(pady=10)

reset_button = tk.Button(control_frame, text="Reset", command=reset_game, **button_style)
reset_button.grid(row=0, column=0, padx=10)

quit_button = tk.Button(control_frame, text="Quit", command=quit_game, **button_style)
quit_button.grid(row=0, column=1, padx=10)

root.mainloop()
