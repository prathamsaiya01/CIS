import tkinter as tk

heat = 0

def start_theft(root):

    global heat
    heat = 0

    # Clear screen
    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    tk.Label(root, text="THEFT LEVEL WORKING ✅",
             fg="#00ff9f", bg="black",
             font=("Consolas", 20)).pack(pady=50)