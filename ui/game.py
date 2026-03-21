import tkinter as tk
from logic.puzzles import password_cracker, cipher_game
from ui.cases.case1 import open_case1
from ui.cases.case2 import open_case2
from ui.cases.case3 import open_case3
from ui.cases.case4 import open_case4

    # ---------------- BUTTONS ----------------
 
def start_game():
    case_window = tk.Toplevel()
    case_window.title("Select Case")
    case_window.geometry("400x300")

    tk.Label(case_window, text="Select a Case", font=("Arial", 16)).pack(pady=20)

    tk.Button(case_window, text="Case 1: Midnight Murder",
              command=lambda: open_case1(case_window)).pack(pady=10)

    tk.Button(case_window, text="Case 2: Bank Heist",
              command=lambda: open_case2(case_window)).pack(pady=10)

    tk.Button(case_window, text="Case 3: Cyber Attack",
              command=lambda: open_case3(case_window)).pack(pady=10)

    tk.Button(case_window, text="Case 4: Kidnapping",
              command=lambda: open_case4(case_window)).pack(pady=10)

