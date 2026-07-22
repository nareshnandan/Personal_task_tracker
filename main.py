import tkinter as tk
import json
from datetime import datetime

root = tk.Tk()
root.title("Personal task Tracker")
root.geometry("700x550")
root.configure(bg="white")

file_name = "tasks.json"


# Title
title_label = tk.Label(
    root,
    text = "Personal Task Tracker",
    font = ("Arial", 24, "bold"),
    bg = "white"
)
title_label.pack(pady=20)

# Date
date_label = tk.Label(
    root,
    text = datetime.now().strftime("%d-%m-%Y"),
    font = ("Arial", 12),
    bg = "white"
)
date_label.pack()

# Task Entry
task_entry = tk.Entry(
    root,
    width = 40,
    font = ('Arial', 14)
)
task_entry.pack(pady=15)


def add_task():

    task = task_entry.get().strip()

    if task:

        task_list.insert(tk.END, task)

        task_entry.delete(0, tk.END)

        save_tasks()
        update_progress()

def complete_task():

    selected_task = task_list.curselection()

    if selected_task:

        index = selected_task[0]

        task = task_list.get(index)

        if not task.startswith("✔"):

            task_list.delete(index)

            task_list.insert(
                index,
                "✔ " + task
            )

            save_tasks()
            update_progress()

def delete_task():

    selected_task = task_list.curselection()

    if selected_task:

        task_list.delete(selected_task[0])

        save_tasks()
        update_progress()

def save_tasks():

    tasks = task_list.get(0, tk.END)

    with open(file_name, "w") as file:

        json.dump(

            list(tasks),

            file,

            indent=4

        )

def load_tasks():

    try:

        with open(file_name, "r") as file:

            tasks = json.load(file)

            for task in tasks:

                task_list.insert(tk.END, task)

    except:

        pass

def update_progress():

    tasks = task_list.get(0, tk.END)

    total = len(tasks)

    completed = 0

    for task in tasks:

        if task.startswith("✔"):

            completed += 1

    if total > 0:

        progress = int((completed / total) * 100)

    else:

        progress = 0

    progress_label.config(
        text=f"Completed: {completed}/{total} | Progress: {progress}%"
    )

# Add Task button
add_button = tk.Button(
    root,
    text = "Add task",
    width = 15,
    command = add_task
)
add_button.pack()

# Task List
task_list = tk.Listbox(
    root,
    width = 50,
    height = 10,
    font = ("Arial", 12)
)
task_list.pack(pady=20)

# Task Complete button
complete_button = tk.Button(
    root,
    text = "Complete task",
    width = 15,
    command = complete_task
)
complete_button.pack()

# Delete task button
delete_button = tk.Button(
    root,
    text = "Delete task",
    width = 15,
    command = delete_task
)
delete_button.pack()

# Progress label %
progress_label = tk.Label(
    root,
    text = "Completed: 0/0 | Progress: 0%",
    font=("Arial", 12),
    bg="white"
)
progress_label.pack(pady=15)
load_tasks()
update_progress()

root.mainloop()