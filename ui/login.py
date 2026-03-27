import tkinter as tk
from tkinter import messagebox
from Database.auth import login
from ui.role_select import open_role_select
from ui.signup import open_signup
import random
import winsound

attempts = 0


# ===== SOUND =====
def play_click():
    winsound.Beep(1000, 80)


def play_success():
    winsound.Beep(1500, 150)


# ===== TYPING EFFECT =====
def type_text(widget, text, delay=20):
    widget.delete("1.0", tk.END)

    def animate(i=0):
        if i < len(text):
            widget.insert(tk.END, text[i])
            widget.see(tk.END)
            widget.after(delay, lambda: animate(i + 1))

    animate()


# ===== GLITCH EFFECT =====
def glitch_text(label, text):
    def animate():
        temp = list(text)
        for _ in range(random.randint(1, 3)):
            i = random.randint(0, len(temp) - 1)
            temp[i] = random.choice("@#$%&*")
        label.config(text="".join(temp))
        label.after(80, lambda: label.config(text=text))
        label.after(2000, animate)

    animate()


# ===== MAIN LOGIN UI =====
def open_login(root):
    root.deiconify()
    global attempts

    for widget in root.winfo_children():
        widget.destroy()

    root.title("CIS Secure Access")
    root.geometry("700x520")
    root.configure(bg="#020617")

    # Center window
    x = (root.winfo_screenwidth() // 2) - 350
    y = (root.winfo_screenheight() // 2) - 260
    root.geometry(f"700x520+{x}+{y}")

    # ===== TITLE =====
    title = tk.Label(
        root,
        text="CIS",
        font=("Consolas", 42, "bold"),
        fg="#38bdf8",
        bg="#020617"
    )
    title.pack(pady=10)

    glitch_text(title, "CIS")

    tk.Label(
        root,
        text="> Crime Investigation System Terminal",
        font=("Consolas", 12),
        fg="#22c55e",
        bg="#020617"
    ).pack()

    # ===== TERMINAL =====
    terminal = tk.Text(
        root,
        height=10,
        width=75,
        bg="black",
        fg="#22c55e",
        font=("Consolas", 11),
        bd=0
    )
    terminal.pack(pady=20)

    type_text(
        terminal,
        "Initializing CIS System...\nLoading Secure Modules...\nSystem Ready.\n\n> Enter Agent Credentials\n"
    )

    # ===== INPUT =====
    frame = tk.Frame(root, bg="#020617")
    frame.pack()

    tk.Label(frame, text="Agent ID:", fg="white", bg="#020617").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(frame, font=("Consolas", 12), bg="#1e293b", fg="white")
    username_entry.grid(row=0, column=1)

    tk.Label(frame, text="Security Key:", fg="white", bg="#020617").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(frame, font=("Consolas", 12), show="*", bg="#1e293b", fg="white")
    password_entry.grid(row=1, column=1)

    status = tk.Label(root, text="", fg="yellow", bg="#020617", font=("Consolas", 11))
    status.pack(pady=10)

    # ===== LOGIN FUNCTION =====
    def handle_login():
        global attempts
        play_click()

        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            status.config(text="⚠ Missing credentials")
            return

        attempts += 1

        if attempts >= 3:
            status.config(text="🔒 SYSTEM LOCKED", fg="red")
            login_btn.config(state="disabled")
            return

        login_btn.config(state="disabled")

        messages = [
            "[✓] Establishing secure tunnel...",
            "[✓] Hashing credentials...",
            "[✓] Checking encrypted database...",
            "[✓] Validating agent clearance..."
        ]

        def animate(i=0):
            if i < len(messages):
                status.config(text=messages[i])
                root.after(700, lambda: animate(i + 1))
            else:
                user = login(username, password)

                if user:
                    play_success()
                    status.config(text="ACCESS GRANTED ✅", fg="#22c55e")
                    terminal.insert(tk.END, f"\n> Welcome Agent {username}\n")

                    root.after(1000, lambda: open_role_select(root, username))
                else:
                    status.config(text="ACCESS DENIED ❌", fg="red")
                    terminal.insert(tk.END, "\n> Unauthorized Access Attempt\n")
                    login_btn.config(state="normal")

        animate()

    # ===== BUTTONS =====
    btn_frame = tk.Frame(root, bg="#020617")
    btn_frame.pack(pady=20)

    login_btn = tk.Button(
        btn_frame,
        text="▶ INITIATE ACCESS",
        font=("Consolas", 12, "bold"),
        bg="#16a34a",
        fg="white",
        bd=0,
        command=handle_login
    )
    login_btn.grid(row=0, column=0, padx=10)

    def hover_on(e): e.widget.config(bg="#22c55e")
    def hover_off(e): e.widget.config(bg="#16a34a")

    login_btn.bind("<Enter>", hover_on)
    login_btn.bind("<Leave>", hover_off)

    tk.Button(
        btn_frame,
        text="NEW AGENT? SIGN UP",
        font=("Consolas", 10),
        bg="#020617",
        fg="#38bdf8",
        bd=0,
        command=lambda: open_signup(root)
    ).grid(row=0, column=1, padx=10)