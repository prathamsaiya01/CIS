import tkinter as tk
from logic.puzzles import cipher_game, pattern_game

def open_case2(prev):
    prev.destroy()

    story = tk.Toplevel()
    story.title("Case 2: Bank Heist")

    tk.Label(story, text="CASE: Silent Bank Heist", font=("Arial", 16)).pack(pady=10)

    tk.Label(
        story,
        text="₹50 Lakhs were transferred illegally.\nNo physical break-in detected.",
        wraplength=300
    ).pack(pady=10)

    tk.Button(story, text="Start Investigation",
              command=lambda: logs_analysis(story)).pack(pady=10)


# ---------------- STEP 1: LOGS ----------------

def logs_analysis(prev):
    prev.destroy()

    logs = tk.Toplevel()
    logs.title("Server Logs")

    tk.Label(logs, text="Suspicious Logs Found:", font=("Arial", 14)).pack(pady=10)

    tk.Label(logs, text="""
Login from unknown IP
Encrypted file detected
Multiple failed attempts
""").pack()

    tk.Button(logs, text="Decrypt File",
              command=lambda: decrypt_file(logs)).pack(pady=10)


# ---------------- STEP 2: DECRYPT ----------------

def decrypt_file(prev):
    prev.destroy()

    dec = tk.Toplevel()
    dec.title("Decrypt File")

    tk.Label(dec, text="Encrypted Code: EQFG").pack()

    entry = tk.Entry(dec)
    entry.pack()

    def check():
        correct, _ = cipher_game(entry.get())

        if correct:
            tk.Label(dec, text="File Decrypted!").pack()
            tk.Button(dec, text="Track IP",
                      command=lambda: track_ip(dec)).pack()
        else:
            tk.Label(dec, text="Wrong Decryption").pack()

    tk.Button(dec, text="Submit", command=check).pack(pady=10)


# ---------------- STEP 3: IP TRACKING ----------------

def track_ip(prev):
    prev.destroy()

    ip = tk.Toplevel()
    ip.title("IP Tracking")

    tk.Label(ip, text="Find next number in IP pattern:", font=("Arial", 12)).pack(pady=10)
    tk.Label(ip, text="192, 168, 336, ?").pack()

    entry = tk.Entry(ip)
    entry.pack()

    def check():
        correct, _ = pattern_game(entry.get())

        if correct:
            tk.Label(ip, text="IP Located: Mumbai").pack()
            tk.Button(ip, text="Identify Hacker",
                      command=lambda: final_choice(ip)).pack()
        else:
            tk.Label(ip, text="Wrong Pattern").pack()

    tk.Button(ip, text="Submit", command=check).pack(pady=10)


# ---------------- FINAL DECISION ----------------

def final_choice(prev):
    prev.destroy()

    f = tk.Toplevel()
    f.title("Final Decision")

    tk.Label(f, text="Who is the hacker?", font=("Arial", 14)).pack(pady=10)

    def result(choice):
        if choice == "IT Employee":
            tk.Label(f, text="✅ Correct! Insider attack detected").pack()
        else:
            tk.Label(f, text="❌ Wrong! Hacker escaped").pack()

    tk.Button(f, text="Manager", command=lambda: result("Manager")).pack(pady=5)
    tk.Button(f, text="IT Employee", command=lambda: result("IT Employee")).pack(pady=5)
    tk.Button(f, text="Customer", command=lambda: result("Customer")).pack(pady=5)