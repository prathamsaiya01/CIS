import tkinter as tk
from ui.game import start_game

def open_terminal():
        term = tk.Toplevel()
        term.title("Cyber Terminal")
        term.geometry("500x400")

        output = tk.Text(term, height=15)
        output.pack()

        entry = tk.Entry(term)
        entry.pack()
        
def run_command():
        cmd = entry.get()

        if cmd == "scan":
            output.insert(tk.END, "Scanning... Threat detected\n")
        elif cmd == "trace":
            output.insert(tk.END, "Tracking IP... Mumbai\n")
        elif cmd == "logs":
            output.insert(tk.END, "Access logs found\n")
        else:
            output.insert(tk.END, "Unknown command\n")

        entry.delete(0, tk.END)
        tk.Button(term, text="Run", command=run_command).pack()
        
def open_dashboard(username):
    dashboard = tk.Toplevel()
    dashboard.title("CIS - Main Menu")
    dashboard.geometry("500x400")
    dashboard.configure(bg="#0f172a")  # dark theme
    
    # Title
    tk.Label(
        dashboard,
        text="CRIME INVESTIGATION SYSTEM",
        font=("Arial", 16, "bold"),
        fg="white",
        bg="#0f172a"
    ).pack(pady=20)

    # Welcome text
    tk.Label(
        dashboard,
        text=f"Welcome, {username}",
        font=("Arial", 12),
        fg="lightgreen",
        bg="#0f172a"
    ).pack(pady=10)
    
    tk.Button(dashboard, text="Cyber Terminal", command=open_terminal).pack(pady=10)

    def select_avatar():
        print("Avatar Selection")

    def resume_game():
        print("Resume Game")

    def exit_game():
        dashboard.destroy()

    tk.Button(dashboard, text="Start Game", width=20, command=start_game).pack(pady=10)
    tk.Button(dashboard, text="Select Avatar", width=20, command=select_avatar).pack(pady=10)
    tk.Button(dashboard, text="Resume Game", width=20, command=resume_game).pack(pady=10)
    tk.Button(dashboard, text="Exit", width=20, command=exit_game).pack(pady=10)