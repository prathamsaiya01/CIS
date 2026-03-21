import tkinter as tk
from logic.puzzles import cyber_quiz, cipher_game

def open_case3(prev):
    prev.destroy()

    story = tk.Toplevel()
    story.title("Case 3: Cyber Attack")

    tk.Label(story, text="CASE: Cyber Attack", font=("Arial", 16)).pack(pady=10)

    tk.Label(
        story,
        text="A company server was breached.\nSensitive data leaked overnight.",
        wraplength=300
    ).pack(pady=10)

    tk.Button(story, text="Start Investigation",
              command=lambda: server_logs(story)).pack(pady=10)

# ---------------- STEP 1: SERVER LOGS ----------------

def server_logs(prev):
    prev.destroy()

    logs = tk.Toplevel()
    logs.title("Server Logs")

    tk.Label(logs, text="Suspicious Activity Detected", font=("Arial", 14)).pack(pady=10)

    tk.Label(logs, text="""
Unauthorized login
SQL query injection detected
Encrypted file found
""").pack()

    tk.Button(logs, text="Analyze Attack",
              command=lambda: quiz_stage(logs)).pack(pady=10)

# ---------------- STEP 2: CYBER QUIZ ----------------

def quiz_stage(prev):
    prev.destroy()

    quiz = tk.Toplevel()
    quiz.title("Cyber Analysis")

    tk.Label(quiz, text="What does SQL stand for?").pack()

    entry = tk.Entry(quiz)
    entry.pack()

    result_label = tk.Label(quiz, text="")
    result_label.pack()

    def check():
        correct, _ = cyber_quiz(entry.get())

        if correct:
            result_label.config(text="✅ Correct! Attack method identified")
            tk.Button(quiz, text="Decrypt File",
                      command=lambda: decrypt_stage(quiz)).pack()
        else:
            result_label.config(text="❌ Wrong answer")

    tk.Button(quiz, text="Submit", command=check).pack(pady=10)

# ---------------- STEP 3: DECRYPT FILE ----------------

def decrypt_stage(prev):
    prev.destroy()

    dec = tk.Toplevel()
    dec.title("Decrypt Data")

    tk.Label(dec, text="Encrypted File: EQFG").pack()

    entry = tk.Entry(dec)
    entry.pack()

    result_label = tk.Label(dec, text="")
    result_label.pack()

    def check():
        correct, _ = cipher_game(entry.get())

        if correct:
            result_label.config(text="✅ File decrypted: Internal access detected")
            tk.Button(dec, text="Identify Hacker",
                      command=lambda: final_choice(dec)).pack()
        else:
            result_label.config(text="❌ Wrong decryption")

    tk.Button(dec, text="Submit", command=check).pack(pady=10)

# ---------------- FINAL DECISION ----------------

def final_choice(prev):
    prev.destroy()

    f = tk.Toplevel()
    f.title("Final Decision")

    tk.Label(f, text="Who hacked the system?", font=("Arial", 14)).pack(pady=10)

    def result(choice):
        if choice == "System Admin":
            tk.Label(f, text="✅ Correct! Insider attack confirmed").pack()
        else:
            tk.Label(f, text="❌ Wrong! Hacker not caught").pack()

    tk.Button(f, text="System Admin", command=lambda: result("System Admin")).pack(pady=5)
    tk.Button(f, text="Intern", command=lambda: result("Intern")).pack(pady=5)
    tk.Button(f, text="External Hacker", command=lambda: result("External Hacker")).pack(pady=5)