import tkinter as tk
from ui.splash import show_splash
import random
import time

score = 0
risk_level = 0

# ---------------- PUZZLES ----------------

def password_cracker(answer):
    return (answer == "1234", 100 if answer == "1234" else 0)

def cipher_game(answer):
    return (answer.upper() == "CODE", 100 if answer.upper() == "CODE" else 0)

def pattern_game(answer):
    return (answer == "32", 100 if answer == "32" else 0)

def cyber_quiz(answer):
    return ("structured query language" in answer.lower(), 100 if "structured query language" in answer.lower() else 0)

def get_random_puzzle():
    return random.choice(["password", "cipher", "pattern", "quiz"])

# ---------------- TIMER ----------------

def start_timer():
    return time.time()

def check_timer(start, limit=20):
    return (time.time() - start) <= limit

# ---------------- RISK ----------------

def update_risk(correct):
    global risk_level
    if correct:
        risk_level -= 5
    else:
        risk_level += 10
    return risk_level

# ---------------- RANK ----------------

def calculate_rank(score):
    if score >= 300:
        return "Elite Investigator"
    elif score >= 200:
        return "Pro Detective"
    return "Rookie"

# ---------------- CLUES ----------------

def get_clue():
    if random.randint(1, 5) == 3:
        return "Hidden clue found! Bonus +50"
    return None

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
    # ---------------- BUTTONS ----------------
 
    def start_game():
        story_window = tk.Toplevel()
        story_window.title("Case 1")
        story_window.geometry("500x400")

        tk.Label(
            story_window,
            text="CASE: Midnight Murder",
            font=("Arial", 16, "bold")
        ).pack(pady=10)

        tk.Label(
            story_window,
            text="A businessman was found dead in his apartment at 2 AM.\nNo signs of forced entry.",
            wraplength=400
        ).pack(pady=10)

        tk.Button(
            story_window,
            text="Start Investigation",
            command=lambda: crime_scene(story_window)
        ).pack(pady=20)

    def crime_scene(prev_window):
        prev_window.destroy()

        scene = tk.Toplevel()
        scene.title("Crime Scene")

        tk.Label(scene, text="Crime Scene Evidence", font=("Arial", 14)).pack(pady=10)

        tk.Label(scene, text="• Broken Glass\n• Laptop\n• Blood Stain").pack()

        tk.Button(scene, text="Examine Laptop", command=lambda: laptop_puzzle(scene)).pack(pady=10)
    
    def laptop_puzzle(prev):
        prev.destroy()

        game = tk.Toplevel()
        game.title("Laptop Locked")

        tk.Label(game, text="Enter password to unlock laptop").pack()

        entry = tk.Entry(game)
        entry.pack()

        def check():
            ans = entry.get()

            correct, pts = password_cracker(ans)

            if correct:
                tk.Label(game, text="Laptop Unlocked!").pack()
                tk.Button(game, text="Next", command=lambda: suspects(game)).pack()
            else:
                tk.Label(game, text="Wrong password").pack()

        tk.Button(game, text="Submit", command=check).pack()

    def suspects(prev):
        prev.destroy()

        s = tk.Toplevel()
        s.title("Suspects")

        tk.Label(s, text="Choose a suspect to interrogate").pack()

        tk.Button(s, text="Wife", command=lambda: interrogation(s)).pack()
        tk.Button(s, text="Partner", command=lambda: interrogation(s)).pack()
        tk.Button(s, text="Employee", command=lambda: interrogation(s)).pack()

    def interrogation(prev):
        prev.destroy()

        i = tk.Toplevel()
        i.title("Interrogation")

        tk.Label(i, text="Decrypt message: EQFG").pack()

        entry = tk.Entry(i)
        entry.pack()

        def check():
            correct, _ = cipher_game(entry.get())

            if correct:
                tk.Label(i, text="He is lying!").pack()
                tk.Button(i, text="Final Decision", command=lambda: final_choice(i)).pack()
            else:
                tk.Label(i, text="Wrong").pack()

        tk.Button(i, text="Submit").pack()    
    
    def final_choice(prev):
        prev.destroy()

        f = tk.Toplevel()
        f.title("Final Decision")

        tk.Label(f, text="Who is the killer?").pack()

        def result(choice):
            if choice == "Partner":
                tk.Label(f, text="Correct! You solved the case").pack()
            else:
                tk.Label(f, text="Wrong!").pack()

        tk.Button(f, text="Wife", command=lambda: result("Wife")).pack()
        tk.Button(f, text="Partner", command=lambda: result("Partner")).pack()
        tk.Button(f, text="Employee", command=lambda: result("Employee")).pack()

    def submit_answer():
        global score

        user_ans = answer_entry.get()

        if not check_timer(start_time):
            tk.Label(game_window, text="⏰ Time Up!").pack()
            return

        if puzzle_type == "password":
            correct, pts = password_cracker(user_ans)
        elif puzzle_type == "cipher":
            correct, pts = cipher_game(user_ans)
        elif puzzle_type == "pattern":
            correct, pts = pattern_game(user_ans)
        else:
            correct, pts = cyber_quiz(user_ans)

        if correct:
            score += pts
            tk.Label(game_window, text=f"✅ Correct! Score: {score}").pack()
        else:
            tk.Label(game_window, text="❌ Wrong!").pack()
            
            # Risk update
            risk = update_risk(correct)
            risk_label.config(text=f"Risk Level: {risk}")
        

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
    
def open_login():
    login_window = tk.Toplevel()
    login_window.title("Login")
    login_window.geometry("400x300")

    tk.Label(login_window, text="Login", font=("Arial", 18)).pack(pady=10)

    # Username
    tk.Label(login_window, text="Username").pack()
    username_entry = tk.Entry(login_window)
    username_entry.pack()

    # Password
    tk.Label(login_window, text="Password").pack()
    password_entry = tk.Entry(login_window, show="*")
    password_entry.pack()

    def handle_login():
        username = username_entry.get().strip()
        password = password_entry.get().strip()

        print(f"Username: '{username}'")
        print(f"Password: '{password}'")

        # later: connect Soham's DB here
        if username.strip() == "admin" and password.strip() == "1234":
            print("Login successful")
            login_window.destroy()
            open_dashboard(username)
        else:
            print("Invalid credentials")

    tk.Button(login_window, text="Login", command=handle_login).pack(pady=10)

root = tk.Tk()
root.withdraw()  # hide main window

show_splash(root, open_login)

root.mainloop()

