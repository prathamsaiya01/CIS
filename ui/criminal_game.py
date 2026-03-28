import tkinter as tk
from ui.cases_criminal.theft import start_theft
from ui.cases_criminal.bnkk import start_bank
from ui.cases_criminal.murder import start_murder
from ui.cases_criminal.cyber import start_cyber

def start_criminal_game():

    window = tk.Toplevel()
    window.title("CIS // Criminal Missions")
    window.geometry("500x420")
    window.configure(bg="black")

    # Center window
    x = (window.winfo_screenwidth() // 2) - 250
    y = (window.winfo_screenheight() // 2) - 210
    window.geometry(f"500x420+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        window,
        text="SELECT MISSION",
        font=("Consolas", 22, "bold"),
        fg="#ff004f",   # 🔥 red theme
        bg="black"
    ).pack(pady=20)

    tk.Label(
        window,
        text="> Choose your criminal operation",
        font=("Consolas", 11),
        fg="#ff4d4d",
        bg="black"
    ).pack()

    # ===== BUTTON STYLE =====
    def create_button(text, command):

        btn = tk.Button(
            window,
            text=text,
            font=("Consolas", 12, "bold"),
            bg="#020617",
            fg="#ff4d4d",
            activebackground="#ff004f",
            activeforeground="black",
            bd=1,
            relief="solid",
            width=30,
            pady=5,
            command=command
        )

        # Hover effect
        def on_enter(e):
            btn.config(bg="#ff004f", fg="black")

        def on_leave(e):
            btn.config(bg="#020617", fg="#ff4d4d")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        btn.pack(pady=10)

    # ===== MISSION BUTTONS =====
    create_button("▶ LEVEL 1: STREET THEFT",
                  lambda: start_theft(window))

    create_button("▶ LEVEL 2: BANK HEIST",
                  lambda: start_bank(window))

    create_button("▶ LEVEL 3: PERFECT CRIME",
                  lambda: start_murder(window))

    create_button("▶ LEVEL 4: CYBER ATTACK",
                  lambda: start_cyber(window))