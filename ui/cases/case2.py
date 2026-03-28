import tkinter as tk
from logic.puzzles import cipher_game, pattern_game

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 2")
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
def open_case2(prev):
    story_text = [
        "📍 11:45 PM — National Bank Server Room",
        "₹50 Lakhs transferred without authorization.",
        "No physical break-in detected.",
        "Security logs show unusual activity at midnight.",
        "Only one system was accessed remotely...",
        "The breach came from inside the network.",
        "An insider might be involved.",
        "Time to analyze the server logs..."
    ]

    show_story(prev, story_text, logs_analysis)


# ---------------- STEP 1: LOGS ----------------
def logs_analysis():
    logs = tk.Toplevel()
    logs.title("CIS // Server Logs")
    logs.configure(bg=BG)
    logs.geometry("500x300")

    tk.Label(logs, text="SERVER LOGS",
             font=("Consolas", 14, "bold"),
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(logs,
             text="""
• Login from internal IP: 192.168.336.X
• Access time: 00:03 AM
• Encrypted file detected
• Multiple failed login attempts
• Only IT department had access at that hour
""",
             fg=GREEN, bg=BG, justify="left").pack(pady=10)

    tk.Button(logs, text="▶ DECRYPT FILE",
              bg="#020617", fg=GREEN,
              command=lambda: decrypt_file(logs)).pack(pady=10)


# ---------------- STEP 2: DECRYPT ----------------
def decrypt_file(prev):
    prev.destroy()

    dec = tk.Toplevel()
    dec.title("CIS // Decryption")
    dec.configure(bg=BG)
    dec.geometry("450x300")

    tk.Label(dec, text="Encrypted Code: LW HPSOR\\HH",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(dec, text="Hint: Caesar Cipher (+3)",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(dec, bg="black", fg=GREEN, insertbackground=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(dec, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get().lower() == "it employee":
            result_label.config(text="✅ DECRYPTED", fg=GREEN)

            tk.Button(dec, text="▶ TRACK IP",
                      command=lambda: track_ip(dec)).pack(pady=10)
        else:
            result_label.config(text="❌ WRONG", fg="red")

    tk.Button(dec, text="SUBMIT", command=check).pack()


# ---------------- STEP 3: IP TRACKING ----------------
def track_ip(prev):
    prev.destroy()

    ip = tk.Toplevel()
    ip.title("CIS // IP Tracking")
    ip.configure(bg=BG)
    ip.geometry("450x300")

    tk.Label(ip, text="TRACE THE IP",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(ip,
             text="Pattern found in logs:\n192, 168, 336, ?",
             fg=GREEN, bg=BG).pack()

    tk.Label(ip,
             text="Hint: Each number doubles from previous pair",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(ip, bg="black", fg=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(ip, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get() == "672":
            result_label.config(text="✅ IP RESOLVED: Mumbai Server", fg=GREEN)

            tk.Button(ip, text="▶ IDENTIFY HACKER",
                      command=lambda: final_choice(ip)).pack(pady=10)
        else:
            result_label.config(text="❌ WRONG PATTERN", fg="red")

    tk.Button(ip, text="SUBMIT", command=check).pack()


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

        if choice == "IT Employee":
            ending = [
                "You trace the logs back to internal access...",
                "Only one person had system privileges at that time...",
                "The IT employee tried to cover tracks...",
                "But evidence is undeniable.",
                "💥 INSIDER ATTACK CONFIRMED",
                "🎉 CASE SOLVED"
            ]
        else:
            ending = [
                "Your assumption was incorrect...",
                "The real hacker wipes remaining traces...",
                "The case remains unsolved...",
                "⚠ MISSION FAILED"
            ]

        show_story(f, ending, lambda: None)

    tk.Button(f, text="Manager", command=lambda: result("Manager")).pack(pady=5)
    tk.Button(f, text="IT Employee", command=lambda: result("IT Employee")).pack(pady=5)
    tk.Button(f, text="Customer", command=lambda: result("Customer")).pack(pady=5)