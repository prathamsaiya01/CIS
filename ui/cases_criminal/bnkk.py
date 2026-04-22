import tkinter as tk
import random
import winsound  # 🔥 SOUND

heat = 0
alarm = 0
loot = 0
progress = 0


def start_bank(root):

    global heat, alarm, loot, progress
    heat = 0
    alarm = 0
    loot = 0
    progress = 0

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="#0a0a0a")

    # ===== HEADER =====
    tk.Label(root, text="💀 OPERATION BLACK VAULT",
             font=("Consolas", 26, "bold"),
             fg="#00ff41", bg="#0a0a0a").pack(pady=10)

    # ===== STATUS =====
    status = tk.Label(root,
                      text="HEAT: 0% | ALERT: 0% | LOOT: $0",
                      fg="#00ff41", bg="#001100",
                      font=("Consolas", 12, "bold"))
    status.pack(pady=5)

    def update(h=0, a=0, l=0):
        global heat, alarm, loot
        heat = max(0, min(100, heat + h))
        alarm = max(0, min(100, alarm + a))
        loot += l
        status.config(text=f"HEAT: {heat}% | ALERT: {alarm}% | LOOT: ${loot:,}")

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=12, width=90,
                       bg="black", fg="#00ff41",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)

    def log(msg):
        terminal.insert(tk.END, msg + "\n")
        terminal.see(tk.END)

    # ===== PROGRESS =====
    progress_label = tk.Label(root,
                              text="[░░░░░░░░░░] 0%",
                              fg="#00ff41", bg="#0a0a0a",
                              font=("Consolas", 11))
    progress_label.pack()

    def update_progress(val):
        global progress
        progress += val
        bars = min(10, progress // 10)
        progress_label.config(text="[" + "█"*bars + "░"*(10-bars) + f"] {progress}%")

    # ===== ACTION FRAME =====
    frame = tk.Frame(root, bg="#0a0a0a")
    frame.pack(pady=20)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    # ===== STEP 1 =====
    def step1():
        clear()
        log(">>> INFILTRATION STARTED")

        tk.Button(frame, text="Disguise Entry", width=30,
                  command=lambda: choose1("front")).pack(pady=5)

        tk.Button(frame, text="Vent Entry", width=30,
                  command=lambda: choose1("vent")).pack(pady=5)

    def choose1(c):
        if c == "front":
            update(20, 15)
            log("⚠ Cameras detected movement")
        else:
            update(5, 0)
            log("✔ Silent entry")

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        log(">>> SECURITY NODE")

        tk.Button(frame, text="Hack System", width=30,
                  command=lambda: choose2("hack")).pack(pady=5)

        tk.Button(frame, text="Disable Power", width=30,
                  command=lambda: choose2("destroy")).pack(pady=5)

    def choose2(c):
        if c == "hack":
            update(5, 5)
            update_progress(20)
            log("✔ Access granted")
        else:
            update(30, 40)
            update_progress(10)
            log("🚨 Alarm triggered")

        step3()

    # ===== STEP 3 (ADVANCED + SOUND) =====
    def step3():
        clear()
        log(">>> FIREWALL ACTIVATED")

        questions = [
            ("Vault lock pattern: 3, 5, 9, 17, ?", "33"),
            ("Rescue code: reverse the word SAFE", "efas"),
            ("Emergency timer: 2^3, 3^2, 4^2, next = ?", "25"),
            ("Laser grid shift: move 1 digit of 3142 to the end -> ?", "1423"),
            ("Guard cipher: RED -> DER, BLUE -> ?", "eulb"),
            ("Secret asset: reverse 2048", "8402")
        ]

        index = [0]
        correct = [0]

        q_label = tk.Label(frame, fg="white", bg="#0a0a0a",
                           font=("Consolas", 11))
        q_label.pack(pady=10)

        entry = tk.Entry(frame, font=("Consolas", 11))
        entry.pack(pady=5)

        feedback = tk.Label(frame, text="", bg="#0a0a0a",
                            font=("Consolas", 10))
        feedback.pack()

        def ask():
            if index[0] < len(questions):
                q_label.config(text=questions[index[0]][0])
                entry.delete(0, tk.END)
            else:
                if correct[0] >= 4:
                    log("🔥 FIREWALL BREACHED")
                    update_progress(50)
                    step4()
                else:
                    log("💀 FAILED")
                    final()

        def check():
            q, ans = questions[index[0]]
            user = entry.get().strip().lower()

            if user == ans:
                correct[0] += 1
                feedback.config(text="✔ ACCESS GRANTED", fg="#00ff41")
                winsound.Beep(1000, 200)  # 🔊 correct sound
                update_progress(10)
            else:
                feedback.config(text="❌ ACCESS DENIED", fg="red")
                winsound.Beep(300, 400)  # 🔊 wrong sound
                update(15, 20)

                if alarm > 80:
                    winsound.Beep(200, 600)
                    log("💀 LOCKDOWN INITIATED")
                    final()
                    return

            index[0] += 1
            ask()

        tk.Button(frame, text="EXECUTE", width=20,
                  command=check).pack(pady=5)

        entry.bind("<Return>", lambda e: check())

        ask()

    # ===== STEP 4 =====
    def step4():
        clear()
        log(">>> VAULT OPENED")

        tk.Button(frame, text="Take Cash ($100K)",
                  command=lambda: choose4("cash")).pack(pady=5)

        tk.Button(frame, text="Take Diamonds ($300K)",
                  command=lambda: choose4("diamond")).pack(pady=5)

    def choose4(c):
        if c == "cash":
            update(5, 5, 100000)
        else:
            update(30, 30, 300000)

        step5()

    # ===== STEP 5 =====
    def step5():
        clear()
        log(">>> ESCAPE")

        tk.Button(frame, text="Car Escape",
                  command=lambda: result("car")).pack(pady=5)

        tk.Button(frame, text="Tunnel Escape",
                  command=lambda: result("tunnel")).pack(pady=5)

    def result(c):
        if c == "car":
            if random.choice([True, False]):
                log("✔ Escaped successfully")
            else:
                update(50, 50)
                log("🚨 Caught in chase")
        else:
            log("✔ Clean silent escape")

        final()

    # ===== FINAL =====
    def final():
        clear()

        if heat > 90 or alarm > 90:
            msg = "💀 CAPTURED"
            winsound.Beep(200, 800)
        elif loot > 250000 and heat < 40:
            msg = "🧠 MASTER HEIST"
            winsound.Beep(1200, 300)
        elif loot > 0:
            msg = "😈 SUCCESSFUL ESCAPE"
        else:
            msg = "❌ FAILED"

        tk.Label(frame, text=msg,
                 fg="white", bg="#0a0a0a",
                 font=("Consolas", 18, "bold")).pack(pady=10)

        tk.Label(frame,
                 text=f"HEAT: {heat} | ALERT: {alarm} | LOOT: ${loot:,}",
                 fg="white", bg="#0a0a0a").pack()

        tk.Button(frame, text="PLAY AGAIN",
                  command=lambda: start_bank(root)).pack(pady=10)

    step1()