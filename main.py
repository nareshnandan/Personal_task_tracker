import tkinter as tk
from datetime import datetime

root = tk.Tk()
root.title("Personal task Tracker")
root.geometry("700x550")
root.configure(bg="white")

title_label = tk.Label(
    root,
    text = "Personal Task Tracker",
    font = ("Arial", 24, "bold"),
    bg = "white"
)
title_label.pack(pady=20)

date_label = tk.Label(
    root,
    text = datetime.now().strftime("%d-%m-%Y"),
    font = ("Arial", 12),
    bg = "white"
)
date_label.pack()

task_entry = tk.Entry(
    root,
    width = 40,
    font = ('Arial', 14)
)
task_entry.pack(pady=15)

add_button = tk.Button(
    root,
    text = "Add task",
    width = 15
)
add_button.pack()

task_list = tk.Listbox(
    root,
    width = 50,
    height = 10,
    font = ("Arial", 12)
)
task_list.pack(pady=20)

complete_button = tk.Button(
    root,
    text = "Complete task",
    width = 15
)
complete_button.pack()

delete_button = tk.Button(
    root,
    text = "Delete task",
    width = 15
)
delete_button.pack()

progress_label = tk.Label(
    root,
    text = "Completed: 0/0 | Progress: 0%",
    font=("Arial", 12),
    bg="white"
)
progress_label.pack(pady=15)

root.mainloop()