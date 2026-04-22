import tkinter as tk
import random

heat = 0
suspicion = 0
timer_running = False
timer_id = None


def start_theft(root):

    global heat, suspicion, timer_running, timer_id
    heat = 0
    suspicion = 0
    timer_running = False
    timer_id = None

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg="black")

    # ===== HEADER =====
    tk.Label(root, text="🟢 ELITE THEFT OPERATION",
             font=("Consolas", 22, "bold"),
             fg="#00ff9f", bg="black").pack(pady=10)

    # ===== STATUS PANEL =====
    status_frame = tk.Frame(root, bg="black")
    status_frame.pack(pady=5)

    heat_bar = tk.Label(status_frame, text="🔥 HEAT: ░░░░░░░░░░",
                        fg="red", bg="black",
                        font=("Consolas", 11))
    heat_bar.pack(side="left", padx=10)

    suspicion_label = tk.Label(status_frame,
                                text="👁️ SUSPICION: 0%",
                                fg="#00ff9f", bg="black",
                                font=("Consolas", 11))
    suspicion_label.pack(side="left", padx=10)

    timer_label = tk.Label(status_frame, text="⏱️ TIME PRESSURE: -",
                            fg="yellow", bg="black",
                            font=("Consolas", 11))
    timer_label.pack(side="left", padx=10)

    def update_heat_bar():
        bars = min(10, int(heat / 10))
        heat_bar.config(text="🔥 HEAT: " + "█"*bars + "░"*(10-bars))

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=12, width=85,
                       bg="black", fg="#00ff9f",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)
    terminal.tag_configure("warning", foreground="#ffcc00")
    terminal.tag_configure("success", foreground="#00ff9f")
    terminal.tag_configure("danger", foreground="#ff3333")
    terminal.tag_configure("info", foreground="#cccccc")

    def type_log(text, tag="info"):
        terminal.insert(tk.END, "\n")
        for char in text:
            terminal.insert(tk.END, char, tag)
            terminal.update()
            terminal.after(6)
        terminal.see(tk.END)

    def update(h=0, s=0):
        global heat, suspicion
        heat = max(0, min(100, heat + h))
        suspicion = max(0, min(100, suspicion + s))
        update_heat_bar()
        suspicion_label.config(text=f"👁️ SUSPICION: {suspicion}%")
        if suspicion > 70 or heat > 70:
            suspicion_label.config(fg="#ff3333")
        elif suspicion > 40 or heat > 40:
            suspicion_label.config(fg="#ffcc00")
        else:
            suspicion_label.config(fg="#00ff9f")

    def cancel_timer():
        global timer_running, timer_id
        timer_running = False
        if timer_id is not None:
            root.after_cancel(timer_id)
            timer_id = None
        timer_label.config(text="⏱️ TIME PRESSURE: -", fg="yellow")

    def start_timer(seconds, timeout_func, urgent=False):
        global timer_running, timer_id
        cancel_timer()
        timer_running = True

        def count(sec):
            global timer_running, timer_id
            if not timer_running:
                return
            if sec <= 0:
                timer_running = False
                timer_id = None
                timer_label.config(text="⏱️ TIME PRESSURE: 0s", fg="#ff3333")
                timeout_func()
                return
            color = "#ff3333" if urgent or sec < 6 else "#ffff66"
            timer_label.config(text=f"⏱️ TIME PRESSURE: {sec}s", fg=color)
            timer_id = root.after(1000, lambda: count(sec - 1))

        count(seconds)

    frame = tk.Frame(root, bg="black")
    frame.pack(pady=20)

    def clear():
        for w in frame.winfo_children():
            w.destroy()

    # ===== TIMER =====
    timer_label = tk.Label(root, text="", fg="yellow", bg="black")
    timer_label.pack()

    def start_timer(seconds, timeout_func):
        global timer_running, timer_id
        timer_running = True

        def count(sec):
            global timer_id

            if not timer_running:
                return

            if sec <= 0:
                timer_running = False
                timer_label.config(text="")
                timeout_func()
                return

            timer_label.config(text=f"⏱️ TIME LEFT: {sec}s")
            timer_id = root.after(1000, lambda: count(sec - 1))

        count(seconds)

    # ===== STEP 1 =====
    def step1():
        clear()
        cancel_timer()
        type_log(">>> MISSION INITIATED", "success")
        type_log("> Target: CEO carrying encrypted drive + ₹2,00,000 cash", "info")
        type_log("> Environment: Upscale mall with CCTV, guards, civilians, and a concierge.", "info")

        tk.Label(frame, text="Choose Entry Strategy",
                 fg="#00ff9f", bg="black").pack(pady=8)

        tk.Button(frame, text="Front Gate (CCTV Risk)",
                  width=35,
                  command=lambda: choose1("front")).pack(pady=5)

        tk.Button(frame, text="Service Entrance (Staff Badge)",
                  width=35,
                  command=lambda: choose1("service")).pack(pady=5)

        tk.Button(frame, text="Luxury Shopper Disguise",
                  width=35,
                  command=lambda: choose1("disguise")).pack(pady=5)

    def choose1(choice):
        if choice == "front":
            type_log("> Security cameras are already trained on you. Move fast.", "danger")
            update(30, 25)
        elif choice == "service":
            type_log("> Staff badge gets you past the first guard quietly.", "success")
            update(15, 10)
        else:
            type_log("> You blend with the crowd of high rollers and enter unnoticed.", "success")
            update(10, 8)

        if random.choice([True, False]):
            type_log("> A mall cop glances your way. Keep moving.", "warning")
            update(10, 10)

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        type_log("> The CEO heads toward the premium elevator. Security protocols are active.", "info")

        tk.Label(frame, text="Choose your distraction",
                 fg="#00ff9f", bg="black").pack(pady=8)

        tk.Button(frame, text="Create false alarm at food court",
                  width=35,
                  command=lambda: choose2("alarm")).pack(pady=5)

        tk.Button(frame, text="Hack the CCTV feed",
                  width=35,
                  command=lambda: choose2("hack")).pack(pady=5)

        tk.Button(frame, text="Slip through service door",
                  width=35,
                  command=lambda: choose2("slip")).pack(pady=5)

    def choose2(choice):
        if choice == "alarm":
            type_log("> Confusion spreads. Security rushes the food court.", "success")
            update(25, 20)
            step3()
        elif choice == "hack":
            type_log("> You access the maintenance terminal for a quick camera loop.", "info")
            update(20, 15)
            step2_hack()
        else:
            type_log("> You slip through the service corridor with a cart.", "success")
            update(10, 5)
            step3()

    def step2_hack():
        clear()
        type_log("> CCTV override in progress. Solve the security riddle before the guard returns.", "warning")
        type_log("> Puzzle: The code is 3 digits. The first two are 2 and 5, the last is the first plus the second.", "info")

        tk.Label(frame, text="Enter override code",
                 fg="#00ff9f", bg="black").pack(pady=8)
        entry = tk.Entry(frame)
        entry.pack(pady=5)

        def check_hack():
            code = entry.get().strip()
            if code == "257":
                cancel_timer()
                type_log("> CCTV loop achieved! Cameras now show an empty hallway.", "success")
                update(-5, 5)
            else:
                cancel_timer()
                type_log("> WRONG CODE! Security probes the terminal. Heat skyrockets.", "danger")
                update(40, 35)
            step3()

        tk.Button(frame, text="EXECUTE", command=check_hack).pack(pady=5)
        start_timer(10, lambda: [type_log("> TIME EXPIRED! Security catches the glitch.", "danger"), update(40, 35), step3()], urgent=True)

    # ===== STEP 3 =====
    def step3():
        clear()
        type_log("> The CEO pauses at the concierge desk. The bag is close enough to grab.", "info")
        type_log("> A hidden safe requires a code. You need perfect logic now.", "warning")

        tk.Label(frame, text="Enter safe code",
                 fg="#00ff9f", bg="black").pack(pady=8)
        entry = tk.Entry(frame)
        entry.pack(pady=5)

        type_log("> Clue 1: The sum of the digits is 12.", "info")
        type_log("> Clue 2: The first digit is double the last.", "info")
        type_log("> Clue 3: The middle digit is 3 more than the last.", "info")

        def check_safe():
            code = entry.get().strip()
            if code == "642":
                cancel_timer()
                type_log("> Safe opens with a whisper. You now control the loot path.", "success")
                update(5, -5)
            else:
                cancel_timer()
                type_log("> The lock screams. Guards are alerted to tampering.", "danger")
                update(45, 30)
            step4()

        tk.Button(frame, text="CRACK SAFE", command=check_safe).pack(pady=5)
        start_timer(12, lambda: [type_log("> TIME'S UP! Lock generates a security alert.", "danger"), update(45, 30), step4()], urgent=True)

    # ===== STEP 4 =====
    def step4():
        clear()
        type_log("> You secure the cash and encrypted drive. Now decide your exit.", "info")

        tk.Label(frame, text="Choose your extraction style",
                 fg="#00ff9f", bg="black").pack(pady=8)

        tk.Button(frame, text="Crowd diversion and slip away",
                  width=35,
                  command=lambda: choose4("diversion")).pack(pady=5)

        tk.Button(frame, text="Take the stairs in the shadows",
                  width=35,
                  command=lambda: choose4("stairs")).pack(pady=5)

        tk.Button(frame, text="Blend with staff pushing a cart",
                  width=35,
                  command=lambda: choose4("cart")).pack(pady=5)

    def choose4(choice):
        if choice == "diversion":
            type_log("> You start a commotion. Security focuses on the noise.", "success")
            update(20, 15)
        elif choice == "stairs":
            type_log("> Shadows cover your descent. Only one guard patrols the stairwell.", "success")
            update(10, 10)
        else:
            type_log("> The staff cart blends in with delivery traffic.", "success")
            update(5, 5)

        step5()

    # ===== STEP 5 =====
    def step5():
        clear()
        type_log("> Final escape begins. The mall sirens are wailing.", "warning")

        def timeout():
            type_log("> You froze. The police swarm the exits.", "danger")
            update(40, 40)
            final_result()

        start_timer(8, timeout, urgent=True)

        tk.Label(frame, text="Choose your escape route",
                 fg="#00ff9f", bg="black").pack(pady=8)

        tk.Button(frame, text="Emergency exit through kitchen",
                  width=35,
                  command=lambda: result("kitchen")).pack(pady=5)

        tk.Button(frame, text="Rooftop zipline getaway",
                  width=35,
                  command=lambda: result("roof")).pack(pady=5)

        tk.Button(frame, text="Meld into the valet line",
                  width=35,
                  command=lambda: result("valet")).pack(pady=5)

    def result(choice):
        global timer_running, timer_id
        if not timer_running:
            return
        cancel_timer()

        if choice == "kitchen":
            if random.choice([True, False, False]):
                type_log("> The kitchen door is locked. Security closes in.", "danger")
                update(35, 30)
            else:
                type_log("> You slip through the kitchen and vanish in service alleys.", "success")
                update(15, 10)
        elif choice == "roof":
            if random.choice([True, False]):
                type_log("> The zipline is rigged! You escape with a bloody sprint.", "warning")
                update(20, 15)
            else:
                type_log("> The zipline snaps. You crash but still disappear in smoke.", "danger")
                update(45, 35)
        else:
            type_log("> Valet attendants believe your story. You vanish in a car.", "success")
            update(10, 5)

        final_result()

    # ===== FINAL RESULT =====
    def final_result():
        clear()
        cancel_timer()
        type_log("\n>>> FINAL ANALYSIS", "info")

        if heat > 90 or suspicion > 90:
            msg = "❌ MISSION FAILED — CAUGHT"
            color = "red"
            subtitle = "Your face is on every security screen. The operation ends here."
        elif heat > 70 or suspicion > 70:
            msg = "⚠️ ESCAPED — IDENTIFIED"
            color = "yellow"
            subtitle = "You got away, but the agency already has your profile."
        elif heat > 50 or suspicion > 50:
            msg = "🔥 WANTED — SURVIVED THE RAID"
            color = "orange"
            subtitle = "You escaped with loot, but the hunt has only begun."
        else:
            msg = "😈 MASTER THIEF — CLEAN GETAWAY"
            color = "#00ff9f"
            subtitle = "Zero trace. No cameras, no witnesses, no regrets."

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Label(root, text=subtitle,
                 fg="#cccccc", bg="black",
                 font=("Consolas", 11)).pack(pady=5)

        tk.Label(root,
                 text=f"HEAT: {heat}%  |  SUSPICION: {suspicion}%",
                 fg="#00ff9f", bg="black",
                 font=("Consolas", 11)).pack(pady=5)

        score = max(0, 100 - heat - suspicion)
        rating = "ROGUE LEGEND" if score > 70 else "SHADOW RUNNER" if score > 50 else "EDGE WALKER" if score > 30 else "BURNED ASSET"

        tk.Label(root,
                 text=f"FINAL RATING: {rating}",
                 fg="#00ff9f", bg="black",
                 font=("Consolas", 12, "bold")).pack(pady=5)

        tk.Button(root, text="RETRY MISSION",
                  width=25,
                  bg="#00ff9f", fg="black",
                  font=("Consolas", 11, "bold"),
                  command=lambda: start_theft(root)).pack(pady=15)

    step1()
    