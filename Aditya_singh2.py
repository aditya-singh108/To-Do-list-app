import tkinter as tk
from tkinter import messagebox
import json
import os

FILENAME = "tasks.json"

def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, "r") as file:
            return json.load(file)
    return []

def save_tasks():
    tasks = listbox.get(0, tk.END)
    with open(FILENAME, "w") as file:
        json.dump(tasks, file)

def add_task():
    task = task_entry.get()
    if task != "":
        listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected = listbox.curselection()[0]
        listbox.delete(selected)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

adi = tk.Tk()
adi.title("To-Do List App")
adi.geometry("400x450")
adi.config(bg="light blue")  

title_label = tk.Label(
    adi, text="My To-Do List",
    font=("Comic Sans MS", 16, "bold"),
    bg="light blue", fg="blue"
)
title_label.pack(pady=10)

task_entry = tk.Entry(
    adi, font=("Comic Sans MS", 12),
    width=30, bg="white", fg="black"
)
task_entry.pack(pady=10)

add_btn = tk.Button(
    adi, text="Add Task", width=15,
    command=add_task, bg="blue", fg="white"
)
add_btn.pack()

del_btn = tk.Button(
    adi, text="Delete Task", width=15,
    command=delete_task, bg="dark red", fg="white"
)
del_btn.pack(pady=5)

listbox = tk.Listbox(
    adi, font=("Comic Sans MS", 12),
    width=40, height=15,
    bg="white", fg="black", selectbackground="sky blue"
)
listbox.pack(pady=10)

tasks = load_tasks()
for task in tasks:
    listbox.insert(tk.END, task)

adi.mainloop()
