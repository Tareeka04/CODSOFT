import tkinter as tk
from tkinter import messagebox

def add_task():
    task = task_entry.get()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Input Error", "Please enter a task.")

def delete_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        task_listbox.delete(selected_task)
    else:
        messagebox.showwarning("Selection Error", "Please select a task to delete.")

def update_task():
    selected_task = task_listbox.curselection()
    if selected_task:
        updated_task = task_entry.get()
        if updated_task:
            task_listbox.delete(selected_task)
            task_listbox.insert(selected_task, updated_task)
            task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Input Error", "Please enter the updated task.")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to update.")

def mark_completed():
    selected_task = task_listbox.curselection()
    if selected_task:
        task = task_listbox.get(selected_task)
        task_listbox.delete(selected_task)
        task_listbox.insert(tk.END, f"{task} (Completed)")
    else:
        messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("400x500")
root.configure(bg="#D32F2F")  

task_entry = tk.Entry(
    root, 
    font=("Arial", 14), 
    bd=4, 
    relief="sunken", 
    bg="#FFFFFF",  
    fg="#006400" 
)
task_entry.pack(pady=10, padx=10, fill=tk.X)

button_frame = tk.Frame(root, bg="#D32F2F")  
button_frame.pack(pady=10)

button_specs = {
    "font": ("Arial", 12, "bold"),
    "width": 12,
    "height": 1,
    "bd": 3,
    "relief": "raised",
}

add_button = tk.Button(
    button_frame, 
    text="Add Task", 
    **button_specs, 
    command=add_task, 
    bg="#228B22",  
    fg="#FFFFFF"  
)
add_button.grid(row=0, column=0, padx=5, pady=5)

complete_button = tk.Button(
    button_frame, 
    text="Mark Completed", 
    **button_specs, 
    command=mark_completed, 
    bg="#006400", 
    fg="#FFFFFF"   
)
complete_button.grid(row=0, column=1, padx=5, pady=5)

update_button = tk.Button(
    button_frame, 
    text="Update Task", 
    **button_specs, 
    command=update_task, 
    bg="#32CD32", 
    fg="#FFFFFF"   
)
update_button.grid(row=1, column=0, padx=5, pady=5)

delete_button = tk.Button(
    button_frame, 
    text="Delete Task", 
    **button_specs, 
    command=delete_task, 
    bg="#98FB98",  
    fg="#FFFFFF"   
)
delete_button.grid(row=1, column=1, padx=5, pady=5)

task_listbox = tk.Listbox(
    root,
    font=("Arial", 14),
    bd=4,
    relief="sunken",
    bg="#FFFFFF",  
    fg="#006400", 
    selectbackground="#FFEB3B",  
    selectforeground="#000000"  
)
task_listbox.pack(pady=10, padx=10, fill=tk.BOTH, expand=True)

root.mainloop()
