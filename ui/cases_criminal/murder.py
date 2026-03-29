import tkinter as tk
import random

suspicion = 30
evidence = 50
alibi = 0


def start_murder(root):

    global suspicion, evidence, alibi
    suspicion = 30
    evidence = 50
    alibi = 0

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    # ===== HEADER =====
    tk.Label(root, text="💀 MASTER MANIPULATION",
             font=("Consolas", 22, "bold"),
             fg="#ff004f", bg="black").pack(pady=10)

    # ===== STATUS BAR =====
    status = tk.Label(root,
                      text="👁️ 30%  | 📂 50% | 🧾 0%",
                      fg="red", bg="black",
                      font=("Consolas", 11))
    status.pack()

    def update(s=0, e=0, a=0):
        global suspicion, evidence, alibi
        suspicion += s
        evidence += e
        alibi += a
        status.config(text=f"👁️ {suspicion}% | 📂 {evidence}% | 🧾 {alibi}%")

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=12, width=85,
                       bg="black", fg="#ff4d4d",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)

    def type_log(text):
        terminal.insert(tk.END, "\n")
        for c in text:
            terminal.insert(tk.END, c)
            terminal.update()
            terminal.after(8)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=20)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    # ===== STEP 1 =====
    def step1():
        clear()
        type_log(">>> CRIME EXECUTED SUCCESSFULLY")
        type_log("> Victim eliminated. Timeline begins.")

        # RANDOM TWIST
        if random.choice([True, False]):
            type_log("> ⚠️ CCTV footage detected")
            update(20, 20, 0)

        tk.Button(frame, text="🔥 Destroy Evidence",
                  width=35,
                  command=lambda: choose1("destroy")).pack(pady=5)

        tk.Button(frame, text="🧩 Plant Fake Suspect",
                  width=35,
                  command=lambda: choose1("plant")).pack(pady=5)

    def choose1(c):
        if c == "destroy":
            type_log("> Evidence wiped ✔️")
            update(-10, -30, 0)
        else:
            type_log("> Fake trail created 👤")
            update(-5, -10, 0)

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        type_log("> Constructing alibi...")

        tk.Button(frame, text="📞 Call friend (weak)",
                  width=35,
                  command=lambda: choose2("call")).pack(pady=5)

        tk.Button(frame, text="📍 Fake GPS (strong)",
                  width=35,
                  command=lambda: choose2("gps")).pack(pady=5)

    def choose2(c):
        if c == "call":
            type_log("> Friend seems nervous ⚠️")
            update(10, 0, 15)
        else:
            type_log("> Digital alibi created ✔️")
            update(-10, 0, 30)

        # RANDOM TWIST
        if random.choice([True, False]):
            type_log("> Witness spotted you 👀")
            update(20, 20, 0)

        step3()

    # ===== STEP 3 =====
    def step3():
        clear()
        type_log("> Investigation intensifying...")

        tk.Button(frame, text="🤐 Stay Silent",
                  width=35,
                  command=lambda: choose3("silent")).pack(pady=5)

        tk.Button(frame, text="🕵️ Misdirect Police",
                  width=35,
                  command=lambda: choose3("mislead")).pack(pady=5)

    def choose3(c):
        if c == "silent":
            type_log("> Silence increased suspicion ⚠️")
            update(25, 0, 0)
        else:
            type_log("> Police misled ✔️")
            update(-20, -10, 15)

        step4()

    # ===== STEP 4 (INTERROGATION PRESSURE) =====
    def step4():
        clear()
        type_log("> 🔴 INTERROGATION ROOM")

        tk.Label(frame, text="Where were you at 9 PM?",
                 fg="#ff4d4d", bg="black").pack()

        entry = tk.Entry(frame)
        entry.pack(pady=5)

        def check():
            ans = entry.get().lower()

            if "home" in ans or "house" in ans:
                type_log("> Statement consistent ✔️")
                update(-15, -10, 20)
            else:
                type_log("> Inconsistency detected 🚨")
                update(35, 30, 0)

            final()

        tk.Button(frame, text="ANSWER", command=check).pack()

    # ===== FINAL =====
    def final():
        clear()
        type_log("\n>>> FINAL VERDICT")

        if suspicion > 80 or evidence > 80:
            msg = "❌ ARRESTED — GAME OVER"
            color = "red"
        elif alibi > 40 and suspicion < 50:
            msg = "😈 PERFECT CRIME — YOU OUTSMARTED THE SYSTEM"
            color = "#00ff9f"
        else:
            msg = "⚠️ UNDER SURVEILLANCE — NOT SAFE"
            color = "yellow"

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Label(root,
                 text=f"FINAL STATS → Suspicion: {suspicion} | Evidence: {evidence} | Alibi: {alibi}",
                 fg="white", bg="black").pack()

        tk.Button(root, text="RETRY",
                  command=lambda: start_murder(root)).pack(pady=10)

    step1()