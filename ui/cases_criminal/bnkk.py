import tkinter as tk
import random

heat = 0
alarm = 0
loot = 0
progress = 0
timer_running = False
timer_id = None


def start_bank(root):
    global heat, alarm, loot, progress, timer_running, timer_id
    heat = 0
    alarm = 0
    loot = 0
    progress = 0
    timer_running = False
    timer_id = None

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="#0a0a0a")

    # ===== HEADER =====
    header_frame = tk.Frame(root, bg="#0a0a0a")
    header_frame.pack(pady=15)

    tk.Label(header_frame, text="▓▓▓ OPERATION: BLACK VAULT ▓▓▓",
             font=("Consolas", 24, "bold"),
             fg="#00ff41", bg="#0a0a0a").pack()

    tk.Label(header_frame, text="[ AUTHORIZED PERSONNEL ONLY ]",
             font=("Consolas", 10),
             fg="#008f11", bg="#0a0a0a").pack()

    # ===== STATUS PANEL =====
    status_frame = tk.Frame(root, bg="#0a0a0a", highlightbackground="#00ff41", highlightthickness=1)
    status_frame.pack(pady=10, padx=20, fill="x")

    status = tk.Label(status_frame, 
                      text=" HEAT: 0% | ALERT LEVEL: 0% | FUNDS EXTRACTED: $0 ",
                      fg="#00ff41", bg="#001100",
                      font=("Consolas", 12, "bold"))
    status.pack(pady=8)

    def update(h=0, a=0, l=0):
        global heat, alarm, loot
        heat = max(0, min(100, heat + h))
        alarm = max(0, min(100, alarm + a))
        loot += l
        status.config(text=f" HEAT: {heat}% | ALERT LEVEL: {alarm}% | FUNDS EXTRACTED: ${loot:,} ")
        
        # Color coding based on danger level
        if heat > 70 or alarm > 70:
            status.config(fg="#ff0040", bg="#330000")
        elif heat > 40 or alarm > 40:
            status.config(fg="#ffaa00", bg="#331100")
        else:
            status.config(fg="#00ff41", bg="#001100")

    # ===== TERMINAL =====
    terminal_frame = tk.Frame(root, bg="#0a0a0a", highlightbackground="#00ff41", highlightthickness=1)
    terminal_frame.pack(pady=10, padx=20)

    terminal = tk.Text(terminal_frame, height=14, width=90,
                       bg="#000000", fg="#00ff41",
                       font=("Consolas", 11), bd=0,
                       insertbackground="#00ff41",
                       selectbackground="#003300",
                       selectforeground="#00ff41")
    terminal.pack(padx=10, pady=10)
    terminal.insert(tk.END, ">>> INITIALIZING SECURE CONNECTION...\n")
    terminal.insert(tk.END, ">>> ENCRYPTING TRAFFIC THROUGH 7 PROXIES...\n")
    terminal.insert(tk.END, ">>> CONNECTION ESTABLISHED. WELCOME, OPERATIVE.\n")
    terminal.insert(tk.END, ">>> TARGET: FIRST NATIONAL BANK - VAULT SECTOR\n")
    terminal.insert(tk.END, "-" * 50 + "\n")
    terminal.config(state=tk.DISABLED)

    def type_log(text, color="#00ff41"):
        terminal.config(state=tk.NORMAL)
        terminal.insert(tk.END, f">>> {text}\n", color)
        terminal.see(tk.END)
        terminal.config(state=tk.DISABLED)
        root.update()

    # ===== PROGRESS BAR =====
    progress_frame = tk.Frame(root, bg="#0a0a0a")
    progress_frame.pack(pady=10)

    tk.Label(progress_frame, text="VAULT BREACH PROGRESS", 
             fg="#008f11", bg="#0a0a0a", font=("Consolas", 10)).pack()

    progress_label = tk.Label(progress_frame, 
                              text="[░░░░░░░░░░] 0%",
                              fg="#00ff41", bg="#0a0a0a",
                              font=("Consolas", 14, "bold"))
    progress_label.pack()

    def update_progress(val):
        global progress
        progress = min(100, progress + val)
        filled = int(progress / 10)
        bar = "█" * filled + "░" * (10 - filled)
        progress_label.config(text=f"[{bar}] {progress}%")

    # ===== ACTION FRAME =====
    action_frame = tk.Frame(root, bg="#0a0a0a", highlightbackground="#00ff41", highlightthickness=1)
    action_frame.pack(pady=15, padx=20, fill="both", expand=True)

    frame = tk.Frame(action_frame, bg="#0a0a0a")
    frame.pack(pady=20, padx=20)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    # ===== TIMER =====
    timer_label = tk.Label(root, text="", fg="#ff0040", bg="#0a0a0a", font=("Consolas", 16, "bold"))
    timer_label.pack()

    def start_timer(sec, timeout):
        global timer_running, timer_id
        timer_running = True

        def count(s):
            global timer_id
            if not timer_running:
                return
            if s <= 0:
                timer_running = False
                timer_label.config(text="TIME EXPIRED")
                timeout()
                return
            timer_label.config(text=f"⏱️ T-MINUS {s}s")
            timer_id = root.after(1000, lambda: count(s-1))

        count(sec)

    # ===== STEP 1: INFILTRATION =====
    def step1():
        clear()
        type_log("PHASE 1: FACILITY INFILTRATION INITIATED", "#00ffff")
        type_log("Recon complete. Two entry vectors identified.", "#00ff41")
        type_log("Choose your approach, operative...")

        tk.Label(frame, text="◄ SELECT INFILTRATION METHOD ►",
                 fg="#00ff41", bg="#0a0a0a", font=("Consolas", 12, "bold")).pack(pady=10)

        btn_frame = tk.Frame(frame, bg="#0a0a0a")
        btn_frame.pack()

        tk.Button(btn_frame, text="[ SOCIAL ENGINEERING ]\nPose as armored transport guard",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose1("front")).pack(pady=8)

        tk.Button(btn_frame, text="[ PHYSICAL BREACH ]\nHVAC ventilation system",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose1("vent")).pack(pady=8)

    def choose1(c):
        if c == "front":
            type_log("WARNING: Facial recognition flagged anomaly", "#ffaa00")
            type_log("Heat signatures rising...", "#ffaa00")
            update(20, 15)
        else:
            type_log("SUCCESS: Ventilation shaft accessed", "#00ff41")
            type_log("Motion sensors bypassed. Undetected.", "#00ff41")
            update(5, 0)

        step2()

    # ===== STEP 2: SECURITY SYSTEM =====
    def step2():
        clear()
        type_log("PHASE 2: SECURITY INFRASTRUCTURE", "#00ffff")
        type_log("Main security node detected ahead.", "#00ff41")
        type_log("Time to show me your skills, hacker...")

        tk.Label(frame, text="◄ SECURITY NODE ACCESS ►",
                 fg="#00ff41", bg="#0a0a0a", font=("Consolas", 12, "bold")).pack(pady=10)

        btn_frame = tk.Frame(frame, bg="#0a0a0a")
        btn_frame.pack()

        tk.Button(btn_frame, text="[ CYBER INTRUSION ]\nExploit firmware vulnerability",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose2("hack")).pack(pady=8)

        tk.Button(btn_frame, text="[ PHYSICAL OVERRIDE ]\nSabotage control panel",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose2("destroy")).pack(pady=8)

    def choose2(c):
        if c == "hack":
            type_log("SUCCESS: Root access obtained", "#00ff41")
            type_log("Security protocols disabled remotely", "#00ff41")
            update(5, 5)
            update_progress(20)
        else:
            type_log("CRITICAL: Circuit disruption detected", "#ff0040")
            type_log("Backup generators activated. Guards mobilizing.", "#ff0040")
            update(30, 40)
            update_progress(10)

        step3()

    # ===== STEP 3: FIREWALL CHALLENGES =====
    def step3():
        clear()
        type_log("PHASE 3: VAULT AI FIREWALL", "#00ffff")
        type_log("Neural network defense system active.", "#00ff41")
        type_log("Answer correctly to inject exploit code...")

        # Cybersecurity questions (kept 1 & 2 as requested)
        questions = [
            ("Binary representation of decimal 6?", "110"),
            ("Next in sequence: 2, 6, 12, 20, ?", "30"),
            ("What port does HTTPS use by default?", "443"),
            ("What does SQL stand for?", "structured query language"),
            ("What is the loopback IP address?", "127.0.0.1"),
            ("What does '404' HTTP status mean?", "not found"),
            ("Common password hashing algo (3 letters)?", "md5"),
        ]

        random.shuffle(questions)
        questions = questions[:5]  # Pick 5 random ones
        index = [0]
        correct_count = [0]

        tk.Label(frame, text="◄ FIREWALL BYPASS PROTOCOL ►",
                 fg="#00ff41", bg="#0a0a0a", font=("Consolas", 12, "bold")).pack(pady=5)

        challenge_frame = tk.Frame(frame, bg="#0a0a0a", highlightbackground="#00ff41", highlightthickness=1)
        challenge_frame.pack(pady=10, padx=20, fill="x")

        counter_label = tk.Label(challenge_frame, 
                                text=f"CHALLENGE 1/{len(questions)}",
                                fg="#008f11", bg="#0a0a0a", font=("Consolas", 9))
        counter_label.pack(pady=5)

        question_label = tk.Label(challenge_frame, 
                                 text="", 
                                 fg="#00ff41", bg="#0a0a0a",
                                 font=("Consolas", 12, "bold"),
                                 wraplength=400)
        question_label.pack(pady=10)

        entry = tk.Entry(challenge_frame, width=40,
                        bg="#001100", fg="#00ff41",
                        insertbackground="#00ff41",
                        font=("Consolas", 11),
                        justify="center")
        entry.pack(pady=10)
        entry.focus()

        result_label = tk.Label(challenge_frame, text="", 
                               bg="#0a0a0a", font=("Consolas", 10))
        result_label.pack(pady=5)

        def ask():
            if index[0] < len(questions):
                q, _ = questions[index[0]]
                question_label.config(text=f"Q: {q}")
                counter_label.config(text=f"CHALLENGE {index[0]+1}/{len(questions)}")
                entry.delete(0, tk.END)
                entry.focus()
                result_label.config(text="", fg="#0a0a0a")
            else:
                if correct_count[0] >= 3:
                    type_log(f"FIREWALL BREACHED: {correct_count[0]}/{len(questions)} correct", "#00ff41")
                    type_log("Vault encryption keys acquired", "#00ff41")
                    update_progress(50)
                    step4()
                else:
                    type_log(f"ACCESS DENIED: Only {correct_count[0]}/{len(questions)} correct", "#ff0040")
                    type_log("AI has locked the vault. Abort mission.", "#ff0040")
                    final()

        def check(event=None):
            q, ans = questions[index[0]]
            user_ans = entry.get().lower().strip()
            
            if user_ans == ans.lower():
                correct_count[0] += 1
                result_label.config(text="✓ PACKET INJECTED", fg="#00ff41")
                type_log(f"EXPLOIT SUCCESS: {q}", "#00ff41")
                update(5, 5)
                update_progress(10)
            else:
                result_label.config(text=f"✗ ACCESS DENIED (Answer: {ans})", fg="#ff0040")
                type_log(f"FIREWALL BLOCKED: {q}", "#ff0040")
                update(15, 20)

                if alarm > 80:
                    type_log("SYSTEM LOCKDOWN IMMINENT", "#ff0040")
                    final()
                    return

            index[0] += 1
            frame.after(800, ask)

        entry.bind("<Return>", check)

        submit_btn = tk.Button(challenge_frame, text="[ EXECUTE EXPLOIT ]",
                              bg="#003300", fg="#00ff41",
                              activebackground="#005500", activeforeground="#00ff41",
                              font=("Consolas", 10, "bold"),
                              command=check)
        submit_btn.pack(pady=10)

        ask()

    # ===== STEP 4: THE VAULT =====
    def step4():
        clear()
        type_log("PHASE 4: VAULT INTERIOR", "#00ffff")
        type_log("The vault door slides open. Gold gleams in the darkness.", "#00ff41")
        type_log("What are you taking, operative?")

        tk.Label(frame, text="◄ ASSET EXTRACTION ►",
                 fg="#00ff41", bg="#0a0a0a", font=("Consolas", 12, "bold")).pack(pady=10)

        btn_frame = tk.Frame(frame, bg="#0a0a0a")
        btn_frame.pack()

        tk.Button(btn_frame, text="[ CASH RESERVES ]\n$100,000 - Lightweight, traceable",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose4("cash")).pack(pady=8)

        tk.Button(btn_frame, text="[ DIAMOND CERTIFICATES ]\n$300,000 - High value, marked",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: choose4("diamond")).pack(pady=8)

    def choose4(c):
        if c == "cash":
            type_log("CASH ACQUIRED: Bearer bonds secured", "#00ff41")
            type_log("Low profile extraction possible", "#00ff41")
            update(5, 5, 100000)
        else:
            type_log("DIAMONDS ACQUIRED: Certificates in hand", "#00ffff")
            type_log("WARNING: RFID trackers detected on assets", "#ffaa00")
            update(30, 30, 300000)

        step5()

    # ===== STEP 5: EXTRACTION =====
    def step5():
        clear()
        type_log("PHASE 5: EMERGENCY EXTRACTION", "#ff0040")
        type_log("Security breach detected in Sector 7", "#ffaa00")
        type_log("You have 5 seconds to exfiltrate...")

        def timeout():
            type_log("EXTRACTION FAILED: Perimeter sealed", "#ff0040")
            type_log("Hostile forces surrounding building", "#ff0040")
            final()

        start_timer(5, timeout)

        tk.Label(frame, text="◄ SELECT EXTRACTION VECTOR ►",
                 fg="#ff0040", bg="#0a0a0a", font=("Consolas", 12, "bold")).pack(pady=10)

        btn_frame = tk.Frame(frame, bg="#0a0a0a")
        btn_frame.pack()

        tk.Button(btn_frame, text="[ VEHICLE EXTRACTION ]\nStolen security van",
                  width=40, height=2,
                  bg="#330000", fg="#ff0040",
                  activebackground="#550000", activeforeground="#ff0040",
                  font=("Consolas", 10),
                  command=lambda: result("car")).pack(pady=8)

        tk.Button(btn_frame, text="[ SUBTERRANEAN ESCAPE ]\nMaintenance tunnel",
                  width=40, height=2,
                  bg="#001100", fg="#00ff41",
                  activebackground="#003300", activeforeground="#00ff41",
                  font=("Consolas", 10),
                  command=lambda: result("tunnel")).pack(pady=8)

    def result(c):
        global timer_running, timer_id

        if not timer_running:
            return

        timer_running = False
        if timer_id:
            root.after_cancel(timer_id)

        if c == "car":
            if random.choice([True, False]):
                type_log("EXTRACTION SUCCESSFUL: Van cleared checkpoint", "#00ff41")
                type_log("Switching vehicles at safehouse...", "#00ff41")
                update(20, 20)
            else:
                type_log("EXTRACTION COMPROMISED: Roadblock encountered", "#ff0040")
                type_log("Vehicle disabled. Foot pursuit initiated.", "#ff0040")
                update(50, 50)
        else:
            type_log("EXTRACTION SUCCESSFUL: Tunnel exit confirmed", "#00ff41")
            type_log("No pursuit detected. Mission clean.", "#00ff41")
            update(5, 5)

        final()

    # ===== FINAL =====
    def final():
        clear()
        timer_label.config(text="")
        type_log("-" * 50, "#008f11")
        type_log("MISSION REPORT - OPERATION BLACK VAULT", "#00ffff")
        type_log("-" * 50, "#008f11")

        if heat > 100 or alarm > 100:
            msg = "[ MISSION FAILED - OPERATIVE CAPTURED ]"
            color = "#ff0040"
            sub_msg = "You left too many traces. The feds have your face."
        elif loot > 200000:
            msg = "[ ELITE OPERATIVE - MISSION ACCOMPLISHED ]"
            color = "#00ff41"
            sub_msg = "Perfect execution. The syndicate will be pleased."
        elif loot > 0:
            msg = "[ PARTIAL SUCCESS - SURVIVED TO HACK AGAIN ]"
            color = "#ffaa00"
            sub_msg = "You got out, but left money on the table."
        else:
            msg = "[ MISSION ABORTED - NO ASSETS RECOVERED ]"
            color = "#ff0040"
            sub_msg = "All that risk for nothing. Disappointing."

        result_frame = tk.Frame(frame, bg="#0a0a0a", highlightbackground=color, highlightthickness=2)
        result_frame.pack(pady=20, padx=20, fill="x")

        tk.Label(result_frame, text=msg,
                 fg=color, bg="#0a0a0a",
                 font=("Consolas", 14, "bold")).pack(pady=10)

        tk.Label(result_frame, text=sub_msg,
                 fg="#aaaaaa", bg="#0a0a0a",
                 font=("Consolas", 10)).pack()

        stats_frame = tk.Frame(result_frame, bg="#0a0a0a")
        stats_frame.pack(pady=10)

        tk.Label(stats_frame, text=f"HEAT LEVEL: {heat}%",
                fg="#ff0040" if heat > 50 else "#00ff41", 
                bg="#0a0a0a", font=("Consolas", 10)).pack()
        
        tk.Label(stats_frame, text=f"ALERT STATUS: {alarm}%",
                fg="#ff0040" if alarm > 50 else "#00ff41", 
                bg="#0a0a0a", font=("Consolas", 10)).pack()
        
        tk.Label(stats_frame, text=f"TOTAL ACQUIRED: ${loot:,}",
                fg="#00ff41", bg="#0a0a0a", 
                font=("Consolas", 12, "bold")).pack(pady=5)

        tk.Button(frame, text="[ REBOOT SYSTEM - NEW OPERATION ]",
                 bg="#003300", fg="#00ff41",
                 activebackground="#005500", activeforeground="#00ff41",
                 font=("Consolas", 11, "bold"),
                 command=lambda: start_bank(root)).pack(pady=20)

    step1()


# Initialize main window
if __name__ == "__main__":
    root = tk.Tk()
    root.title("OPERATION: BLACK VAULT")
    root.geometry("900x700")
    root.configure(bg="#0a0a0a")
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    start_bank(root)
    root.mainloop()
