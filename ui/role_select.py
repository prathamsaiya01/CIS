import tkinter as tk
from ui.game import start_game
def open_role_select(root, username):

    role_window = tk.Toplevel(root)
    role_window.title("Select Role")
    role_window.geometry("700x500")
    role_window.configure(bg="#020617")

    # Center window
    x = (role_window.winfo_screenwidth() // 2) - (700 // 2)
    y = (role_window.winfo_screenheight() // 2) - (500 // 2)
    role_window.geometry(f"700x500+{x}+{y}")

    tk.Label(
        role_window,
        text="CHOOSE YOUR PATH",
        font=("Arial", 28, "bold"),
        fg="#38bdf8",
        bg="#020617"
    ).pack(pady=40)

    tk.Label(
        role_window,
        text=f"Welcome Agent {username}",
        fg="white",
        bg="#020617"
    ).pack(pady=10)

    # Buttons Frame
    frame = tk.Frame(role_window, bg="#020617")
    frame.pack(pady=40)

    def choose_investigator():
        print("Investigator Selected")
        role_window.destroy()
        start_game()
        
    def choose_criminal():
        print("Criminal Selected")
        role_window.destroy()

    # Investigator Button
    tk.Button(
        frame,
        text="🕵️ INVESTIGATOR",
        font=("Arial", 16, "bold"),
        bg="#22c55e",
        fg="black",
        width=20,
        height=2,
        command=choose_investigator
    ).grid(row=0, column=0, padx=20)

    # Criminal Button
    tk.Button(
        frame,
        text="🕶️ CRIMINAL",
        font=("Arial", 16, "bold"),
        bg="#ef4444",
        fg="white",
        width=20,
        height=2,
        command=choose_criminal
    ).grid(row=0, column=1, padx=20)