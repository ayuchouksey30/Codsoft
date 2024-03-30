import tkinter as tk
from tkinter import messagebox

# Dark Mode Colors
BG_COLOR = "#202124"
FG_COLOR = "#FFFFFF"
ENTRY_BG_COLOR = "#424242"
BUTTON_BG_COLOR = "#757575"
BUTTON_FG_COLOR = "#FFFFFF"
LISTBOX_BG_COLOR = "#424242"
LISTBOX_FG_COLOR = "#FFFFFF"

def clear_placeholder(event):
    if task_entry.get() == "Enter task here":
        task_entry.delete(0, tk.END)
        task_entry.config(fg=FG_COLOR)

def add_task():
    task = task_entry.get()
    if task and task != "Enter task here":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_task_index = listbox.curselection()[0]
        listbox.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def clear_tasks():
    listbox.delete(0, tk.END)

def save_tasks():
    with open("tasks.txt", "w") as file:
        tasks = listbox.get(0, tk.END)
        for task in tasks:
            file.write(task + "\n")

def load_tasks():
    try:
        with open("tasks.txt", "r") as file:
            tasks = file.readlines()
            for task in tasks:
                listbox.insert(tk.END, task.strip())
    except FileNotFoundError:
        pass

root = tk.Tk()
root.title("To-Do List")
root.config(bg=BG_COLOR)
root.geometry("350x375")
root.minsize(350,375)

frame = tk.Frame(root, bg=BG_COLOR)
frame.pack(pady=10)

listbox = tk.Listbox(frame, width=50, bg=LISTBOX_BG_COLOR, fg=LISTBOX_FG_COLOR, selectbackground="#4CAF50")
listbox.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

task_entry = tk.Entry(root, width=52, bg=ENTRY_BG_COLOR, fg="#A9A9A9")
task_entry.insert(0, "Enter task here")
task_entry.bind("<FocusIn>", clear_placeholder)
task_entry.pack(pady=5)

add_button = tk.Button(root, text="Add Task", width=44, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=add_task)
add_button.pack()

delete_button = tk.Button(root, text="Delete Task", width=44, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=delete_task)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", width=44, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=clear_tasks)
clear_button.pack()

save_button = tk.Button(root, text="Save Tasks", width=44, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=save_tasks)
save_button.pack(pady=5)

load_button = tk.Button(root, text="Load Tasks", width=44, bg=BUTTON_BG_COLOR, fg=BUTTON_FG_COLOR, command=load_tasks)
load_button.pack()

load_tasks()

root.mainloop()
