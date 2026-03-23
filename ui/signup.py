import tkinter as tk
from tkinter import messagebox
from Database.auth import signup


def open_signup(root):

    # Clear screen
    for widget in root.winfo_children():
        widget.destroy()

    root.title("CIS Registration")
    root.geometry("700x500")
    root.configure(bg="#020617")

    # Center window
    x = (root.winfo_screenwidth() // 2) - (700 // 2)
    y = (root.winfo_screenheight() // 2) - (500 // 2)
    root.geometry(f"700x500+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        root,
        text="CIS",
        font=("Consolas", 40, "bold"),
        fg="#38bdf8",
        bg="#020617"
    ).pack(pady=10)

    tk.Label(
        root,
        text="> Register New Agent",
        font=("Consolas", 12),
        fg="#22c55e",
        bg="#020617"
    ).pack(pady=5)

    # ===== CARD FRAME =====
    card = tk.Frame(root, bg="#0f172a", bd=2)
    card.pack(pady=40, padx=50, fill="both", expand=False)

    # ===== USERNAME =====
    tk.Label(card, text="Agent ID", fg="white", bg="#0f172a").pack(pady=10)

    username_entry = tk.Entry(
        card,
        font=("Consolas", 12),
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        width=25
    )
    username_entry.pack(ipady=5)

    # ===== PASSWORD =====
    tk.Label(card, text="Security Key", fg="white", bg="#0f172a").pack(pady=10)

    password_entry = tk.Entry(
        card,
        font=("Consolas", 12),
        show="*",
        bg="#1e293b",
        fg="white",
        insertbackground="white",
        width=25
    )
    password_entry.pack(ipady=5)

    # ===== STATUS =====
    status_label = tk.Label(card, text="", fg="yellow", bg="#0f172a")
    status_label.pack(pady=10)

    # ===== SIGNUP FUNCTION =====
    def handle_signup():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            status_label.config(text="⚠ All fields required", fg="yellow")
            return

        if signup(username, password, None):
            status_label.config(text="✅ Account Created", fg="#22c55e")
            messagebox.showinfo("Success", "Agent Registered Successfully")

            # Go back to login
            root.after(1000, lambda: open_login(root))

        else:
            status_label.config(text="❌ Username already exists", fg="red")

    # ===== BUTTONS =====
    btn_frame = tk.Frame(card, bg="#0f172a")
    btn_frame.pack(pady=20)

    tk.Button(
        btn_frame,
        text="REGISTER",
        font=("Consolas", 12, "bold"),
        bg="#22c55e",
        fg="black",
        width=15,
        command=handle_signup
    ).grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="BACK TO LOGIN",
        font=("Consolas", 10),
        bg="#020617",
        fg="#38bdf8",
        bd=0,
        command=lambda: __import__('ui.login').login.open_login(root)
    ).grid(row=0, column=1, padx=10)