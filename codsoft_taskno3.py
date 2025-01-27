import tkinter as tk
import random
import string


def generate_password(length):
    
    all_characters = string.ascii_letters + string.digits + string.punctuation
    
    
    password = ''.join(random.choice(all_characters) for _ in range(length))
    
    return password


def generate():
    try:
        
        length = int(length_entry.get())
        
        
        if length <= 0:
            password_label.config(text="Password length must be a positive integer!", fg="#F08080")
            return
        
        
        password = generate_password(length)
        
        
        password_label.config(text=f"Generated Password: {password}", fg="#FF00FF")
    
    except ValueError:
        password_label.config(text="Please enter a valid number!", fg="#F08080")
root = tk.Tk()
root.title("Password Generator")
root.configure(bg="#E6E6FA")
title_label = tk.Label(root, text="Password Generator", font=("Helvetica", 16, "bold"), bg="#E6E6FA", fg="#800080")
title_label.pack(pady=10)
length_label = tk.Label(root, text="Enter desired password length:", font=("Helvetica", 12), bg="#E6E6FA", fg="#006B6B")
length_label.pack(pady=5)
length_entry = tk.Entry(root, font=("Helvetica", 12), bd=3, relief="solid", highlightthickness=2, highlightbackground="#00BFFF", highlightcolor="#00BFFF")
length_entry.pack(pady=5)
generate_button = tk.Button(root, text="Generate Password", font=("Helvetica", 12, "bold"), bg="#D2042D", fg="white", command=generate, 
                            relief="raised", bd=4, highlightthickness=2, highlightbackground="#00BFFF", highlightcolor="#00BFFF")
generate_button.pack(pady=10)
password_label = tk.Label(root, text="", font=("Helvetica", 12), bg="#E6E6FA", fg="#FF00FF", width=50, height=2, relief="solid", bd=3)
password_label.pack(pady=10)

root.mainloop()
