import tkinter as tk
from ui.cases.case1 import open_case1
from ui.cases.case2 import open_case2
from ui.cases.case3 import open_case3
from ui.cases.case4 import open_case4


def start_game():
    case_window = tk.Toplevel()
    case_window.title("CIS // Select Case")
    case_window.geometry("500x400")
    case_window.configure(bg="black")

    # Center window
    x = (case_window.winfo_screenwidth() // 2) - 250
    y = (case_window.winfo_screenheight() // 2) - 200
    case_window.geometry(f"500x400+{x}+{y}")

    # ===== TITLE =====
    tk.Label(
        case_window,
        text="SELECT MISSION",
        font=("Consolas", 22, "bold"),
        fg="#00f5ff",
        bg="black"
    ).pack(pady=20)

    tk.Label(
        case_window,
        text="> Choose your investigation case",
        font=("Consolas", 11),
        fg="#00ff9f",
        bg="black"
    ).pack()

    # ===== BUTTON STYLE =====
    def create_button(text, command):
        btn = tk.Button(
            case_window,
            text=text,
            font=("Consolas", 12, "bold"),
            bg="#020617",
            fg="#00ff9f",
            activebackground="#00f5ff",
            activeforeground="black",
            bd=1,
            relief="solid",
            width=28,
            pady=5,
            command=command
        )

        # Hover effect
        def on_enter(e):
            btn.config(bg="#00ff9f", fg="black")

        def on_leave(e):
            btn.config(bg="#020617", fg="#00ff9f")

        btn.bind("<Enter>", on_enter)
        btn.bind("<Leave>", on_leave)

        btn.pack(pady=10)

    # ===== CASE BUTTONS =====
    create_button("▶ CASE 1: MIDNIGHT MURDER",
                  lambda: open_case1(case_window))

    create_button("▶ CASE 2: BANK HEIST",
                  lambda: open_case2(case_window))

    create_button("▶ CASE 3: CYBER ATTACK",
                  lambda: open_case3(case_window))

    create_button("▶ CASE 4: KIDNAPPING",
                  lambda: open_case4(case_window))