import tkinter as tk

def start_cyber(root):
    for w in root.winfo_children():
        w.destroy()

    root.configure(bg='black')

    tk.Label(
        root,
        text='💻 CYBER ATTACK WORKING ✅',
        fg='#66ccff',
        bg='black',
        font=('Consolas', 20)
    ).pack(pady=50)
