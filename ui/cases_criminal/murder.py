import tkinter as tk

def start_murder(root):
    for w in root.winfo_children():
        w.destroy()

    root.configure(bg='black')

    tk.Label(
        root,
        text='🔪 PERFECT CRIME WORKING ✅',
        fg='#ff9966',
        bg='black',
        font=('Consolas', 20)
    ).pack(pady=50)
