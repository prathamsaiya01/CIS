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

    # ===== HEAT BAR =====
    heat_bar = tk.Label(root, text="🔥 HEAT: ░░░░░░░░░░",
                        fg="red", bg="black",
                        font=("Consolas", 11))
    heat_bar.pack()

    def update_heat_bar():
        bars = min(10, int(heat / 10))
        heat_bar.config(text="🔥 HEAT: " + "█"*bars + "░"*(10-bars))

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=12, width=85,
                       bg="black", fg="#00ff9f",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)

    def type_log(text):
        terminal.insert(tk.END, "\n")
        for char in text:
            terminal.insert(tk.END, char)
            terminal.update()
            terminal.after(8)

    def update(h=0, s=0):
        global heat, suspicion
        heat += h
        suspicion += s
        update_heat_bar()

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
        type_log(">>> MISSION INITIATED")
        type_log("> Target: CEO carrying encrypted drive + ₹2,00,000 cash")
        type_log("> Environment: Mall with CCTV, guards, civilians")

        tk.Label(frame, text="Choose Entry Strategy",
                 fg="#00ff9f", bg="black").pack()

        tk.Button(frame, text="Front Gate (CCTV Risk)",
                  width=35,
                  command=lambda: choose1("front")).pack(pady=5)

        tk.Button(frame, text="Service Entry (Stealth)",
                  width=35,
                  command=lambda: choose1("back")).pack(pady=5)

    def choose1(choice):
        if choice == "front":
            type_log("> Cameras captured your face ⚠️")
            update(30, 20)
        else:
            type_log("> Entered undetected ✔️")
            update(10, 5)

        if random.choice([True, False]):
            type_log("> Unexpected guard nearby 👮")
            update(15, 15)

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        type_log("> Target moving to restricted elevator")

        tk.Label(frame, text="Tracking Method",
                 fg="#00ff9f", bg="black").pack()

        tk.Button(frame, text="Follow closely",
                  width=35,
                  command=lambda: choose2("close")).pack(pady=5)

        tk.Button(frame, text="Maintain distance",
                  width=35,
                  command=lambda: choose2("far")).pack(pady=5)

    def choose2(choice):
        if choice == "close":
            type_log("> Target suspicious 👀")
            update(25, 30)
        else:
            type_log("> Tracking stable")
            update(5, 5)

        step3()

    # ===== STEP 3 (PUZZLE) =====
    def step3():
        clear()
        type_log("> Keypad locked 🔐")
        type_log("> Hint: Sum = 9 AND product = 24")

        tk.Label(frame, text="Enter 3-digit code",
                 fg="#00ff9f", bg="black").pack()

        entry = tk.Entry(frame)
        entry.pack(pady=5)

        def check():
            code = entry.get()
            if code == "342":
                type_log("> Access granted ✔️")
                update(5, 0)
            else:
                type_log("> WRONG CODE 🚨 Alarm triggered!")
                update(50, 40)

            step4()

        tk.Button(frame, text="DECRYPT", command=check).pack()

    # ===== STEP 4 =====
    def step4():
        clear()
        type_log("> Target distracted on call")

        tk.Label(frame, text="Execution Style",
                 fg="#00ff9f", bg="black").pack()

        tk.Button(frame, text="Silent Pickpocket",
                  width=35,
                  command=lambda: choose4("pick")).pack(pady=5)

        tk.Button(frame, text="Force Snatch",
                  width=35,
                  command=lambda: choose4("snatch")).pack(pady=5)

    def choose4(choice):
        if choice == "pick":
            type_log("> Clean extraction ✔️")
            update(10, 5)
        else:
            type_log("> CHAOS! Crowd alerted 🚨")
            update(60, 50)

        step5()

    # ===== STEP 5 (TIMER) =====
    def step5():
        clear()
        type_log("> 🚓 POLICE ARRIVING IN 5 SECONDS")

        def timeout():
            if not timer_running:
                return
            type_log("> You hesitated... surrounded by police 💀")
            final_result()

        start_timer(5, timeout)

        tk.Label(frame, text="ESCAPE NOW",
                 fg="#00ff9f", bg="black").pack()

        tk.Button(frame, text="Blend into crowd",
                  width=35,
                  command=lambda: result("blend")).pack(pady=5)

        tk.Button(frame, text="Run aggressively",
                  width=35,
                  command=lambda: result("run")).pack(pady=5)

    def result(choice):
        global timer_running, timer_id

        if not timer_running:
            return

        timer_running = False
        if timer_id:
            root.after_cancel(timer_id)

        timer_label.config(text="")

        if choice == "run":
            if random.choice([True, False]):
                type_log("> You escaped narrowly 🏃")
                update(20, 20)
            else:
                type_log("> Police spotted you 🚨")
                update(40, 40)
        else:
            type_log("> Disappeared in crowd like a ghost 👤")
            update(5, 5)

        final_result()

    # ===== FINAL RESULT =====
    def final_result():
        clear()
        type_log("\n>>> FINAL ANALYSIS")

        if heat > 90 or suspicion > 90:
            msg = "❌ MISSION FAILED — CAUGHT"
            color = "red"
        elif heat > 60:
            msg = "⚠️ ESCAPED — BUT IDENTIFIED"
            color = "yellow"
        else:
            msg = "😈 PERFECT HEIST — ZERO TRACE"
            color = "#00ff9f"

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Button(root, text="RETRY MISSION",
                  command=lambda: start_theft(root)).pack(pady=10)

    step1()