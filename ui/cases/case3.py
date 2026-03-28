import tkinter as tk
from logic.puzzles import cyber_quiz, cipher_game

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 3")
    story.configure(bg=BG)
    story.geometry("550x320")

    label = tk.Label(
        story,
        text="",
        wraplength=500,
        font=("Consolas", 11),
        fg=GREEN,
        bg=BG,
        justify="left"
    )
    label.pack(pady=30)

    index = [0]

    def next_text():
        if index[0] < len(text_list):
            label.config(text=text_list[index[0]])
            index[0] += 1
        else:
            story.destroy()
            next_func()

    tk.Button(
        story,
        text="▶ NEXT",
        bg="#020617",
        fg=CYAN,
        activebackground=CYAN,
        activeforeground="black",
        command=next_text
    ).pack(pady=10)

    next_text()


# ---------------- ENTRY ----------------
def open_case3(prev):
    story_text = [
        "📍 01:30 AM — TechCorp Headquarters",
        "Sensitive company data leaked overnight.",
        "No external breach detected.",
        "Firewall logs show no outside intrusion...",
        "But one account accessed the server internally.",
        "Admin-level privileges were used.",
        "This wasn’t a random hack...",
        "Someone inside the system is responsible."
    ]

    show_story(prev, story_text, server_logs)


# ---------------- STEP 1: SERVER LOGS ----------------
def server_logs():
    logs = tk.Toplevel()
    logs.title("CIS // Server Logs")
    logs.configure(bg=BG)
    logs.geometry("500x300")

    tk.Label(logs, text="SERVER LOG ANALYSIS",
             font=("Consolas", 14, "bold"),
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(logs,
             text="""
• Unauthorized login (Internal Network)
• SQL Injection detected
• Encrypted file found
• Access Level: ADMIN
• Login time: 01:07 AM
""",
             fg=GREEN, bg=BG, justify="left").pack(pady=10)

    tk.Button(logs, text="▶ ANALYZE ATTACK",
              bg="#020617", fg=GREEN,
              command=lambda: quiz_stage(logs)).pack(pady=10)


# ---------------- STEP 2: CYBER QUIZ ----------------
def quiz_stage(prev):
    prev.destroy()

    quiz = tk.Toplevel()
    quiz.title("CIS // Cyber Analysis")
    quiz.configure(bg=BG)
    quiz.geometry("450x300")

    tk.Label(quiz, text="Identify the attack type",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(quiz, text="What does SQL stand for?",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(quiz, bg="black", fg=GREEN, insertbackground=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(quiz, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get().lower() in ["structured query language"]:
            result_label.config(text="✅ SQL Injection Confirmed", fg=GREEN)

            tk.Button(quiz, text="▶ DECRYPT FILE",
                      command=lambda: decrypt_stage(quiz)).pack(pady=10)
        else:
            result_label.config(text="❌ Incorrect", fg="red")

    tk.Button(quiz, text="SUBMIT", command=check).pack()


# ---------------- STEP 3: DECRYPT FILE ----------------
def decrypt_stage(prev):
    prev.destroy()

    dec = tk.Toplevel()
    dec.title("CIS // Decryption")
    dec.configure(bg=BG)
    dec.geometry("450x300")

    tk.Label(dec, text="Encrypted File: DGPLQ",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(dec, text="Hint: Caesar Cipher (+3)",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(dec, bg="black", fg=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(dec, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get().lower() == "admin":
            result_label.config(text="✅ DECRYPTED: ADMIN ACCESS USED", fg=GREEN)

            tk.Button(dec, text="▶ IDENTIFY HACKER",
                      command=lambda: final_choice(dec)).pack(pady=10)
        else:
            result_label.config(text="❌ WRONG", fg="red")

    tk.Button(dec, text="SUBMIT", command=check).pack()


# ---------------- FINAL DECISION ----------------
def final_choice(prev):
    prev.destroy()

    f = tk.Toplevel()
    f.title("CIS // Final Decision")
    f.configure(bg=BG)
    f.geometry("400x300")

    tk.Label(f, text="WHO IS THE HACKER?",
             fg=CYAN, bg=BG).pack(pady=10)

    def result(choice):
        f.destroy()

        if choice == "System Admin":
            ending = [
                "You trace admin-level access logs...",
                "Only one person had that level of control...",
                "The System Admin tried to cover tracks...",
                "But the logs expose everything.",
                "💥 INSIDER BREACH CONFIRMED",
                "🎉 CASE SOLVED"
            ]
        else:
            ending = [
                "Your assumption was incorrect...",
                "The attacker remains hidden...",
                "Critical data is lost forever...",
                "⚠ MISSION FAILED"
            ]

        show_story(f, ending, lambda: None)

    tk.Button(f, text="System Admin", command=lambda: result("System Admin")).pack(pady=5)
    tk.Button(f, text="Intern", command=lambda: result("Intern")).pack(pady=5)
    tk.Button(f, text="External Hacker", command=lambda: result("External Hacker")).pack(pady=5)