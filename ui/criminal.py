import tkinter as tk

def open_criminal(root, username):
    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    tk.Label(root, text="CRIMINAL MODE", fg="red", bg="black").pack(pady=50)