import tkinter as tk
def on_click(event):
    text = event.widget.cget("text")
    if text == "=":
        try:
            result = eval(screen.get())
            screen.delete(0, tk.END)
            screen.insert(tk.END, str(result))
        except Exception as e:
            screen.delete(0, tk.END)
            screen.insert(tk.END, "Error")
    elif text == "C":
        screen.delete(0, tk.END)
    else:
        screen.insert(tk.END, text)
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")  
root.configure(bg="#2c3e50")  
screen = tk.Entry(root, font=("Arial", 18), bd=5, relief="sunken", justify="right", bg="#ecf0f1", fg="#2c3e50")
screen.pack(fill=tk.X, ipadx=8, pady=10, padx=10)
button_frame = tk.Frame(root, bg="#2c3e50")
button_frame.pack()
buttons = [
    "7", "8", "9", "/",
    "4", "5", "6", "*",
    "1", "2", "3", "-",
    "C", "0", "=", "+"
]
row = 0
col = 0
for button in buttons:
    btn = tk.Button(
        button_frame, 
        text=button, 
        font=("Arial", 12),  
        width=5,  
        height=2,  
        bg="#3498db", 
        fg="#ffffff",  
        bd=4, 
        relief="raised" 
    )
    btn.grid(row=row, column=col, padx=5, pady=5)
    btn.bind("<Button-1>", on_click)
    col += 1
    if col > 3:
        col = 0
        row += 1
root.mainloop()
