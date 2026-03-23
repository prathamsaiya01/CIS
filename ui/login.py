import tkinter as tk
from tkinter import messagebox
from Database.auth import login   # connect DB

def open_login(root, open_dashboard):

    login_window = tk.Toplevel(root)
    login_window.title("CIS Login")
    login_window.geometry("600x500")
    login_window.configure(bg="#020617")

    # Center window
    x = (login_window.winfo_screenwidth() // 2) - (600 // 2)
    y = (login_window.winfo_screenheight() // 2) - (500 // 2)
    login_window.geometry(f"600x500+{x}+{y}")

    # TITLE (CIS STYLE)
    tk.Label(
        login_window,
        text="CIS",
        font=("Orbitron", 40, "bold"),
        fg="#38bdf8",
        bg="#020617"
    ).pack(pady=20)

    tk.Label(
        login_window,
        text="Crime Investigation System",
        font=("Arial", 14),
        fg="white",
        bg="#020617"
    ).pack()

    # FRAME (glass feel)
    frame = tk.Frame(login_window, bg="#0f172a", bd=2)
    frame.pack(pady=40, padx=40, fill="both", expand=True)

    # Username
    tk.Label(frame, text="Username", fg="white", bg="#0f172a").pack(pady=5)
    username_entry = tk.Entry(frame, font=("Arial", 14), bg="#1e293b", fg="white", insertbackground="white")
    username_entry.pack(pady=10, ipadx=10, ipady=5)

    # Password
    tk.Label(frame, text="Password", fg="white", bg="#0f172a").pack(pady=5)
    password_entry = tk.Entry(frame, font=("Arial", 14), show="*", bg="#1e293b", fg="white", insertbackground="white")
    password_entry.pack(pady=10, ipadx=10, ipady=5)

    # STATUS LABEL (cool feature)
    status_label = tk.Label(frame, text="", fg="red", bg="#0f172a")
    status_label.pack()

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        user = login(username, password)   # DB call

        if user:
            status_label.config(text="ACCESS GRANTED ✅", fg="#22c55e")
            login_window.after(1000, lambda: [login_window.destroy(), open_dashboard(username)])
        else:
            status_label.config(text="ACCESS DENIED ❌", fg="red")

    # LOGIN BUTTON
    tk.Button(
        frame,
        text="LOGIN",
        font=("Arial", 14, "bold"),
        bg="#22c55e",
        fg="black",
        width=15,
        command=handle_login
    ).pack(pady=20)

    # SIGNUP BUTTON
    tk.Button(
        frame,
        text="New Agent? Register",
        bg="#020617",
        fg="#38bdf8",
        bd=0
    ).pack()