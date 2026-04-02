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

    root.configure(bg="black")

    # ===== HEADER =====
    tk.Label(root, text="💀 OPERATION: BLACK VAULT",
             font=("Consolas", 22, "bold"),
             fg="#ff004f", bg="black").pack(pady=10)

    status = tk.Label(root, text="🔥 HEAT: 0 | 🚨 ALARM: 0 | 💰 LOOT: 0",
                      fg="red", bg="black",
                      font=("Consolas", 11))
    status.pack()

    def update(h=0, a=0, l=0):
        global heat, alarm, loot
        heat += h
        alarm += a
        loot += l
        status.config(text=f"🔥 HEAT: {heat} | 🚨 ALARM: {alarm} | 💰 LOOT: ₹{loot}")

    # ===== TERMINAL =====
    terminal = tk.Text(root, height=12, width=85,
                       bg="black", fg="#ff4d4d",
                       font=("Consolas", 10), bd=0)
    terminal.pack(pady=10)

    def type_log(text):
        terminal.insert(tk.END, "\n")
        for char in text:
            terminal.insert(tk.END, char)
            terminal.update()
            terminal.after(8)

    # ===== PROGRESS BAR =====
    progress_label = tk.Label(root, text="VAULT BREACH: ░░░░░░░░░░",
                              fg="#ff4d4d", bg="black",
                              font=("Consolas", 11))
    progress_label.pack()

    def update_progress(val):
        global progress
        progress += val
        bars = min(10, int(progress / 10))
        progress_label.config(text="VAULT BREACH: " + "█"*bars + "░"*(10-bars))

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
            global timer_id
            if not timer_running:
                return
            if s <= 0:
                timer_running = False
                timeout()
                return
            timer_label.config(text=f"⏱️ {s}s")
            timer_id = root.after(1000, lambda: count(s-1))

        count(sec)

    # ===== STEP 1 =====
    def step1():
        clear()
        type_log(">>> INFILTRATION STARTED")
        type_log("> Elite vault detected")

        tk.Button(frame, text="Enter via disguise 🎭",
                  width=35,
                  command=lambda: choose1("front")).pack(pady=5)

        tk.Button(frame, text="Ventilation stealth 🕳️",
                  width=35,
                  command=lambda: choose1("vent")).pack(pady=5)

    def choose1(c):
        if c == "front":
            type_log("> Suspicion raised ⚠️")
            update(20, 15)
        else:
            type_log("> Silent entry ✔️")
            update(5, 0)

        step2()

    # ===== STEP 2 =====
    def step2():
        clear()
        type_log("> Security system ahead")

        tk.Button(frame, text="Hack system 💻",
                  width=35,
                  command=lambda: choose2("hack")).pack(pady=5)

        tk.Button(frame, text="Destroy panel 🔧",
                  width=35,
                  command=lambda: choose2("destroy")).pack(pady=5)

    def choose2(c):
        if c == "hack":
            type_log("> Access granted ✔️")
            update(5, 5)
            update_progress(20)
        else:
            type_log("> Alarm triggered 🚨")
            update(30, 40)
            update_progress(10)

        step3()

    # ===== STEP 3 =====
    def step3():
        clear()
        type_log("> Vault Firewall Detected 🔐")
        type_log("> Decrypt the admin password hash")

        tk.Label(frame, text="MD5: 5f4dcc3b5aa765d61d8327deb882cf99",
                 fg="#ff4d4d", bg="black", font=("Consolas", 10)).pack()

        tk.Label(frame, text="Hint: Most common default password",
                 fg="#888888", bg="black", font=("Consolas", 9)).pack(pady=2)

        entry = tk.Entry(frame, show="*", font=("Consolas", 10))
        entry.pack(pady=5)

        def check():
            if entry.get().lower() == "password":
                type_log("> Firewall bypassed ✔️")
                update_progress(30)
            else:
                type_log("> Security breach detected 🚨")
                update(40, 40)

            step4()

        tk.Button(frame, text="DECRYPT", command=check).pack()

    # ===== STEP 4 =====
    def step4():
        clear()
        type_log("> Vault opening...")

        tk.Button(frame, text="Take CASH 💵 (+₹1L)",
                  width=35,
                  command=lambda: choose4("cash")).pack(pady=5)

        tk.Button(frame, text="Take DIAMONDS 💎 (+₹3L, risky)",
                  width=35,
                  command=lambda: choose4("diamond")).pack(pady=5)

    def choose4(c):
        if c == "cash":
            update(5, 5, 100000)
        else:
            update(30, 30, 300000)

        update_progress(50)
        step5()

    # ===== STEP 5 =====
    def step5():
        clear()
        type_log("> 🚓 FINAL ESCAPE WINDOW: 5s")

        def timeout():
            type_log("> 💀 SURROUNDED")
            final()

        start_timer(5, timeout)

        tk.Button(frame, text="Escape via car 🚗",
                  width=35,
                  command=lambda: result("car")).pack(pady=5)

        tk.Button(frame, text="Escape via tunnel 🕳️",
                  width=35,
                  command=lambda: result("tunnel")).pack(pady=5)

    def result(c):
        global timer_running, timer_id

        if not timer_running:
            return

        timer_running = False
        if timer_id:
            root.after_cancel(timer_id)

        if c == "car":
            if random.choice([True, False]):
                type_log("> High-speed escape ✔️")
                update(20, 20)
            else:
                type_log("> Caught in chase 🚨")
                update(50, 50)
        else:
            type_log("> Disappeared underground ✔️")
            update(5, 5)

        final()

    # ===== FINAL =====
    def final():
        clear()
        type_log("\n>>> HEIST COMPLETE")

        if heat > 100 or alarm > 100:
            msg = "❌ YOU WERE CAUGHT"
            color = "red"
        elif loot > 200000:
            msg = "💎 LEGENDARY HEIST SUCCESS"
            color = "#00ff9f"
        else:
            msg = "⚠️ PARTIAL SUCCESS"
            color = "yellow"

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Label(root, text=f"💰 TOTAL LOOT: ₹{loot}",
                 fg="white", bg="black").pack()

        tk.Button(root, text="RETRY",
                  command=lambda: start_bank(root)).pack(pady=10)

    step1()