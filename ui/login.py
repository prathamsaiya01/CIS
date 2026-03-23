import tkinter as tk
from tkinter import messagebox
from Database.auth import login
from ui.role_select import open_role_select
from ui.signup import open_signup

def open_login(root):

    # Destroy any existing windows (important fix)
    for widget in root.winfo_children():
        widget.destroy()

    root.deiconify()
    root.title("CIS Secure Access")
    root.geometry("700x520")
    root.configure(bg="#020617")

    # Center window
    x = (root.winfo_screenwidth() // 2) - (700 // 2)
    y = (root.winfo_screenheight() // 2) - (520 // 2)
    root.geometry(f"700x520+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        root,
        text="CIS",
        font=("Consolas", 42, "bold"),
        fg="#38bdf8",
        bg="#020617"
    ).pack(pady=10)

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

    terminal.insert(tk.END, "Initializing CIS System...\n")
    terminal.insert(tk.END, "Loading Secure Modules...\n")
    terminal.insert(tk.END, "System Ready.\n\n")
    terminal.insert(tk.END, "> Enter Agent Credentials\n")

    # ===== INPUT SECTION =====
    input_frame = tk.Frame(root, bg="#020617")
    input_frame.pack()

    tk.Label(input_frame, text="Agent ID:", fg="white", bg="#020617").grid(row=0, column=0, padx=10, pady=10)
    username_entry = tk.Entry(input_frame, font=("Consolas", 12), bg="#1e293b", fg="white", insertbackground="white")
    username_entry.grid(row=0, column=1, padx=10)

    tk.Label(input_frame, text="Security Key:", fg="white", bg="#020617").grid(row=1, column=0, padx=10, pady=10)
    password_entry = tk.Entry(input_frame, font=("Consolas", 12), show="*", bg="#1e293b", fg="white", insertbackground="white")
    password_entry.grid(row=1, column=1, padx=10)

    # ===== STATUS =====
    status_label = tk.Label(root, text="", fg="yellow", bg="#020617", font=("Consolas", 11))
    status_label.pack(pady=10)

    # ===== LOGIN FUNCTION =====
    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        if not username or not password:
            status_label.config(text="⚠ Missing credentials")
            return

        # Disable button during animation
        login_btn.config(state="disabled")

        messages = [
            "Scanning database...",
            "Decrypting credentials...",
            "Verifying access..."
        ]

        def animate(i=0):
            if i < len(messages):
                status_label.config(text=messages[i])
                root.after(600, lambda: animate(i+1))
            else:
                user = login(username, password)

                if user:
                    status_label.config(text="ACCESS GRANTED ✅", fg="#22c55e")
                    terminal.insert(tk.END, f"\n> Welcome Agent {username}\n")

                    # Move to role selection
                    root.after(1000, lambda: open_role_select(root, username))

                else:
                    status_label.config(text="ACCESS DENIED ❌", fg="red")
                    terminal.insert(tk.END, "\n> Unauthorized Access Attempt\n")
                    login_btn.config(state="normal")  # re-enable button

        animate()

    # ===== BUTTONS =====
    btn_frame = tk.Frame(root, bg="#020617")
    btn_frame.pack(pady=20)

    login_btn = tk.Button(
        btn_frame,
        text="INITIATE ACCESS",
        font=("Consolas", 12, "bold"),
        bg="#22c55e",
        fg="black",
        width=18,
        command=handle_login
    )
    login_btn.grid(row=0, column=0, padx=10)

    tk.Button(
        btn_frame,
        text="NEW AGENT? SIGN UP",
        font=("Consolas", 10),
        bg="#020617",
        fg="#38bdf8",
        bd=0,
        command=lambda: open_signup(root)
    ).grid(row=0, column=1, padx=10)