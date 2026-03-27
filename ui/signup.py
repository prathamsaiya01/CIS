import tkinter as tk
from tkinter import messagebox
from Database.auth import signup
import winsound


def play_click():
    winsound.Beep(900, 80)


def open_signup(root):
    for widget in root.winfo_children():
        widget.destroy()

    root.title("CIS Registration")
    root.geometry("700x500")
    root.configure(bg="#020617")

    x = (root.winfo_screenwidth() // 2) - 350
    y = (root.winfo_screenheight() // 2) - 250
    root.geometry(f"700x500+{x}+{y}")

    # TITLE
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
    ).pack()

    # CARD
    card = tk.Frame(root, bg="#0f172a")
    card.pack(pady=40, padx=50)

    tk.Label(card, text="Agent ID", fg="white", bg="#0f172a").pack(pady=10)
    username_entry = tk.Entry(card, font=("Consolas", 12), bg="#1e293b", fg="white")
    username_entry.pack(ipady=5)

    tk.Label(card, text="Security Key", fg="white", bg="#0f172a").pack(pady=10)
    password_entry = tk.Entry(card, font=("Consolas", 12), show="*", bg="#1e293b", fg="white")
    password_entry.pack(ipady=5)

    status = tk.Label(card, text="", bg="#0f172a", fg="yellow")
    status.pack(pady=10)

    def handle_signup():
        play_click()

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            status.config(text="⚠ All fields required", fg="yellow")
            return

        if signup(username, password, None):
            status.config(text="✅ Account Created", fg="#22c55e")
            messagebox.showinfo("Success", "Agent Registered Successfully")

            def redirect():
                from ui.login import open_login
                open_login(root)

            root.after(1000, redirect)
        else:
            status.config(text="❌ Username exists", fg="red")

    btn_frame = tk.Frame(card, bg="#0f172a")
    btn_frame.pack(pady=20)

    register_btn = tk.Button(
        btn_frame,
        text="REGISTER",
        font=("Consolas", 12, "bold"),
        bg="#16a34a",
        fg="white",
        bd=0,
        command=handle_signup
    )
    register_btn.grid(row=0, column=0, padx=10)

    def hover_on(e): e.widget.config(bg="#22c55e")
    def hover_off(e): e.widget.config(bg="#16a34a")

    register_btn.bind("<Enter>", hover_on)
    register_btn.bind("<Leave>", hover_off)

    def go_back():
        from ui.login import open_login
        open_login(root)

    tk.Button(
        btn_frame,
        text="BACK TO LOGIN",
        font=("Consolas", 10),
        bg="#020617",
        fg="#38bdf8",
        bd=0,
        command=go_back
    ).grid(row=0, column=1, padx=10)