import tkinter as tk
import random

trace = 10
access = 0
override = 0
timer_running = False
timer_id = None


def start_cyber(root):

    global trace, access, override, timer_running, timer_id
    trace = 10
    access = 0
    override = 0
    timer_running = False
    timer_id = None

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    # ===== HEADER =====
    tk.Label(root, text="💀 BLACKOUT PROTOCOL",
             font=("Consolas", 22, "bold"),
             fg="#00f5ff", bg="black").pack(pady=10)

    status = tk.Label(root,
                      text="🛰 TRACE: 10% | ⚡ ACCESS: 0% | ☠ OVERRIDE: 0%",
                      fg="#00f5ff", bg="black",
                      font=("Consolas", 11))
    status.pack()

    def update(t=0, a=0, o=0):
        global trace, access, override
        trace += t
        access += a
        override += o
        status.config(text=f"🛰 TRACE: {trace}% | ⚡ ACCESS: {access}% | ☠ OVERRIDE: {override}%")

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=14, width=90,
                       bg="black", fg="#00f5ff",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)

    def type_log(text):
        terminal.insert(tk.END, "\n")
        for c in text:
            terminal.insert(tk.END, c)
            terminal.update()
            terminal.after(6)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=20)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    # ===== TIMER =====
    timer_label = tk.Label(root, text="", fg="yellow", bg="black")
    timer_label.pack()

    def start_timer(sec, timeout):
        global timer_running, timer_id
        timer_running = True

        def count(s):
            global timer_running, timer_id
            if not timer_running:
                return
            if s <= 0:
                timer_running = False
                timeout()
                return
            timer_label.config(text=f"⏱️ TRACE LOCK IN: {s}s")
            timer_id = root.after(1000, lambda: count(s-1))

        count(sec)

    # ===== STEP 1 =====
    def step1():
        clear()
        type_log(">>> CONNECTING TO GLOBAL NETWORK")
        type_log("> Target: Government secure server")

        tk.Button(frame, text="Launch DDoS Attack 🌐",
                  width=40,
                  command=lambda: choose1("ddos")).pack(pady=5)

        tk.Button(frame, text="Phishing Backdoor 🎣",
                  width=40,
                  command=lambda: choose1("phish")).pack(pady=5)

    def choose1(c):
        if c == "ddos":
            type_log("> Massive traffic spike detected 🚨")
            update(30, 20, 0)
        else:
            type_log("> Backdoor installed ✔️")
            update(5, 15, 5)

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        type_log("> AI Firewall detected 🤖")

        tk.Button(frame, text="Bypass AI (slow) 🧠",
                  width=40,
                  command=lambda: choose2("ai")).pack(pady=5)

        tk.Button(frame, text="Exploit vulnerability ⚡",
                  width=40,
                  command=lambda: choose2("exploit")).pack(pady=5)

    def choose2(c):
        if c == "ai":
            type_log("> AI fooled ✔️")
            update(10, 20, 10)
        else:
            type_log("> System instability triggered 🚨")
            update(40, 30, 0)

        step3()

    # ===== STEP 3 (DECRYPTION GAME) =====
    def step3():
        clear()
        type_log("> ENCRYPTED FILE DETECTED 🔐")
        type_log("> MULTI-LAYER DECRYPTION REQUIRED")

        questions = [
            ("Binary of 5?", "101"),
            ("Reverse the rescue tag SAFE", "efas"),
            ("Sequence override: 2, 4, 8, 16, ?", "32"),
            ("Mirror code: reverse 1203", "3021")
        ]

        index = [0]
        correct = [0]

        q_label = tk.Label(frame, fg="#00f5ff", bg="black",
                           font=("Consolas", 11))
        q_label.pack(pady=10)

        entry = tk.Entry(frame, font=("Consolas", 11))
        entry.pack(pady=5)

        feedback = tk.Label(frame, text="", bg="black",
                            font=("Consolas", 10))
        feedback.pack()

        def ask():
            if index[0] < len(questions):
                q_label.config(text=f"QUESTION {index[0]+1}: {questions[index[0]][0]}")
                entry.delete(0, tk.END)
            else:
                if correct[0] >= 3:
                    type_log("> DECRYPTION LAYER BREACHED — CORE ACCESS UNLOCKED ✔️")
                    update(-5, 35, 15)
                else:
                    type_log("> DECRYPTION PARTIAL — TRACE LEVEL SPIKES 🔥")
                    update(25, 15, 0)
                step4()

        def check():
            q, ans = questions[index[0]]
            if entry.get().strip().lower() == ans:
                correct[0] += 1
                feedback.config(text="✔ ACCESS GRANTED", fg="#00ff41")
                type_log(f"> {q} ✓")
            else:
                feedback.config(text="❌ ACCESS DENIED", fg="red")
                type_log(f"> {q} ✗")
                update(10, 5, 0)
            index[0] += 1
            ask()

        tk.Button(frame, text="RUN DECRYPTION", width=20,
                  command=check).pack(pady=5)
        entry.bind("<Return>", lambda e: check())
        ask()

    # ===== STEP 4 =====
    def step4():
        clear()
        type_log("> NETWORK NODES AVAILABLE — CHOOSE YOUR STRIKE")

        tk.Button(frame, text="Hack 1 node",
                  width=40,
                  command=lambda: choose4(1)).pack(pady=5)

        tk.Button(frame, text="Hack 3 nodes (risky)",
                  width=40,
                  command=lambda: choose4(3)).pack(pady=5)

    def choose4(nodes):
        if nodes == 3:
            type_log("> Multi-node breach initiated 🚨")
            update(40, 40, 30)
        else:
            type_log("> Single node secured silently ✔️")
            update(10, 20, 10)

        step5()

    # ===== STEP 5 =====
    def step5():
        clear()
        type_log("> CORE OVERRIDE CHALLENGE — LOGIC GATES ACTIVE")

        questions = [
            ("Rescue code: reverse 'GHOST'", "tsohg"),
            ("Priority sequence: 3, 6, 12, 24, ?", "48"),
            ("Cipher check: 7 * 7 - 7 = ?", "42")
        ]

        index = [0]
        correct = [0]

        q_label = tk.Label(frame, fg="#00f5ff", bg="black",
                           font=("Consolas", 11))
        q_label.pack(pady=10)

        entry = tk.Entry(frame, font=("Consolas", 11))
        entry.pack(pady=5)

        feedback = tk.Label(frame, text="", bg="black",
                            font=("Consolas", 10))
        feedback.pack()

        def ask():
            if index[0] < len(questions):
                q_label.config(text=f"CORE PUZZLE {index[0]+1}: {questions[index[0]][0]}")
                entry.delete(0, tk.END)
            else:
                if correct[0] >= 2:
                    type_log("> CORE OVERRIDE AUTHORIZED — SYSTEMS ARE YOURS ✔️")
                    update(-10, 30, 30)
                else:
                    type_log("> OVERRIDE FAILED — COUNTERMEASURES ENGAGED 🚨")
                    update(35, 10, 0)
                step6()

        def check():
            q, ans = questions[index[0]]
            if entry.get().strip().lower() == ans:
                correct[0] += 1
                feedback.config(text="✔ PUZZLE SOLVED", fg="#00ff41")
                type_log(f"> {q} ✓")
            else:
                feedback.config(text="❌ PUZZLE FAILED", fg="red")
                type_log(f"> {q} ✗")
                update(15, 5, 0)
            index[0] += 1
            ask()

        tk.Button(frame, text="AUTHENTICATE", width=20,
                  command=check).pack(pady=5)
        entry.bind("<Return>", lambda e: check())
        ask()

    # ===== STEP 6 =====
    def step6():
        clear()
        type_log("> FINAL ESCAPE PROTOCOL — TRACE LOCKDOWN IMMINENT")

        def timeout():
            type_log("> TRACE COMPLETE 💀")
            final()

        start_timer(8, timeout)

        tk.Button(frame, text="Ghost out silently 🕶️",
                  width=40,
                  command=lambda: result("ghost")).pack(pady=5)

        tk.Button(frame, text="Blow the network and vanish 💣",
                  width=40,
                  command=lambda: result("blow")).pack(pady=5)

    def result(c):
        global timer_running, timer_id

        if not timer_running:
            return

        timer_running = False
        if timer_id:
            root.after_cancel(timer_id)

        if c == "blow":
            type_log("> SYSTEM BLACKOUT TRIGGERED — CHAOS UNLEASHED 💥")
            update(50, 20, 60)
        else:
            type_log("> SHADOW EXIT INITIATED — TRACE MISSED ✔️")
            update(-20, 30, 25)

        final()

    # ===== FINAL =====
    def final():
        clear()
        type_log("\n>>> FINAL OUTCOME")

        if trace > 90:
            msg = "❌ TRACE COMPLETE — ARREST WARRANT ISSUED"
            color = "red"
            subtitle = "The net closes in as your signal is burned."
        elif override > 70 and access > 60:
            msg = "💀 DOMINION ACHIEVED — YOU OWN THE GRID"
            color = "#00ff9f"
            subtitle = "Every server bends to your will. The world rewrites itself."
        elif access > 70:
            msg = "⚠️ HIGH-VALUE BREACH — DATA TAP SECURED"
            color = "yellow"
            subtitle = "Sensitive intel harvested. Ghost protocol engaged."
        elif override > 40:
            msg = "🔥 SYSTEM DISRUPTION — ESCAPE WITH SCRAP"
            color = "orange"
            subtitle = "You made it out, but the network is hunting you."
        else:
            msg = "❌ FAILED HACK"
            color = "red"
            subtitle = "Your presence was detected and the mission collapsed."

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Label(root,
                 text=subtitle,
                 fg="white", bg="black",
                 font=("Consolas", 11)).pack(pady=5)

        tk.Label(root,
                 text=f"TRACE: {trace}% | ACCESS: {access}% | OVERRIDE: {override}%",
                 fg="white", bg="black").pack(pady=5)

        tk.Label(root,
                 text="MISSION RATING: " + (
                     "CYBER GOD" if override > 70 and access > 60 and trace < 40 else
                     "GHOST HACKER" if access > 60 and trace < 50 else
                     "RISKY GHOST" if override > 40 else
                     "BURNED ASSET"
                 ),
                 fg="#00f5ff", bg="black",
                 font=("Consolas", 12, "bold")).pack(pady=5)

        tk.Button(root, text="RETRY",
                  command=lambda: start_cyber(root)).pack(pady=10)

    step1()