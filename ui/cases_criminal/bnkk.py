import tkinter as tk

def start_bank(root):

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    tk.Label(
        root,
        text="💰 BANK HEIST WORKING ✅",
        fg="#ff004f",
        bg="black",
        font=("Consolas", 20)
    ).pack(pady=50)