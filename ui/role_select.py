import tkinter as tk
from ui.avatar_select import open_avatar_select
from ui.criminal import open_criminal

def open_role_select(root, username):

    # Clear screen instead of new window
    for widget in root.winfo_children():
        widget.destroy()

    root.title("Select Role")
    root.geometry("800x550")
    root.configure(bg="#020617")

    # Center window
    x = (root.winfo_screenwidth() // 2) - (800 // 2)
    y = (root.winfo_screenheight() // 2) - (550 // 2)
    root.geometry(f"800x550+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        root,
        text="CHOOSE YOUR PATH",
        font=("Consolas", 32, "bold"),
        fg="#38bdf8",
        bg="#020617"
    ).pack(pady=40)

    tk.Label(
        root,
        text=f"> Welcome Agent {username}",
        font=("Consolas", 12),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=10)

    # ===== BUTTON FRAME =====
    frame = tk.Frame(root, bg="#020617")
    frame.pack(pady=50)

    # ===== HOVER EFFECT =====
    def on_enter(e):
        e.widget.config(bg="#1e293b")

    def on_leave(e, color):
        e.widget.config(bg=color)

    # ===== INVESTIGATOR =====
    def choose_investigator():
        open_avatar_select(root, username)   # 🔥 GO TO AVATAR SCREEN

    inv_btn = tk.Button(
        frame,
        text="🕵️ INVESTIGATOR",
        font=("Consolas", 16, "bold"),
        bg="#22c55e",
        fg="black",
        width=22,
        height=2,
        command=choose_investigator
    )
    inv_btn.grid(row=0, column=0, padx=30)

    inv_btn.bind("<Enter>", on_enter)
    inv_btn.bind("<Leave>", lambda e: on_leave(e, "#22c55e"))

    # ===== CRIMINAL =====
    def choose_criminal():
        open_criminal(root, username)   # 🔥 GO TO CRIMINAL MODE

    crim_btn = tk.Button(
        frame,
        text="🕶️ CRIMINAL",
        font=("Consolas", 16, "bold"),
        bg="#ef4444",
        fg="white",
        width=22,
        height=2,
        command=choose_criminal
    )
    crim_btn.grid(row=0, column=1, padx=30)

    crim_btn.bind("<Enter>", on_enter)
    crim_btn.bind("<Leave>", lambda e: on_leave(e, "#ef4444"))