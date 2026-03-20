import tkinter as tk
from logic.puzzles import password_cracker, cipher_game

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