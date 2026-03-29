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
            global timer_id
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
        type_log("> Hint: Binary of 5")

        tk.Label(frame, text="Enter Binary Code",
                 fg="#00f5ff", bg="black").pack()

        entry = tk.Entry(frame)
        entry.pack()

        def check():
            if entry.get() == "101":
                type_log("> Decryption successful ✔️")
                update(5, 25, 10)
            else:
                type_log("> Decryption failed 🚨")
                update(30, 10, 0)

            step4()

        tk.Button(frame, text="DECRYPT", command=check).pack()

    # ===== STEP 4 =====
    def step4():
        clear()
        type_log("> NETWORK NODES AVAILABLE")

        tk.Button(frame, text="Hack 1 node",
                  width=40,
                  command=lambda: choose4(1)).pack(pady=5)

        tk.Button(frame, text="Hack 3 nodes (risky)",
                  width=40,
                  command=lambda: choose4(3)).pack(pady=5)

    def choose4(nodes):
        if nodes == 3:
            type_log("> Multi-node breach 🚨")
            update(40, 40, 30)
        else:
            type_log("> Single node secured ✔️")
            update(10, 20, 10)

        step5()

    # ===== STEP 5 =====
    def step5():
        clear()
        type_log("> FINAL SYSTEM OVERRIDE INITIATED ☠")

        def timeout():
            type_log("> TRACE COMPLETE 💀")
            final()

        start_timer(6, timeout)

        tk.Button(frame, text="Inject Virus 💣",
                  width=40,
                  command=lambda: result("virus")).pack(pady=5)

        tk.Button(frame, text="Stealth Shutdown 🕶️",
                  width=40,
                  command=lambda: result("stealth")).pack(pady=5)

    def result(c):
        global timer_running, timer_id

        if not timer_running:
            return

        timer_running = False
        if timer_id:
            root.after_cancel(timer_id)

        if c == "virus":
            type_log("> System collapse initiated 💥")
            update(30, 20, 50)
        else:
            type_log("> Silent takeover ✔️")
            update(-20, 10, 30)

        final()

    # ===== FINAL =====
    def final():
        clear()
        type_log("\n>>> FINAL OUTCOME")

        if trace > 90:
            msg = "❌ TRACE COMPLETE — ARREST WARRANT ISSUED"
            color = "red"
        elif override > 70:
            msg = "💀 TOTAL SYSTEM CONTROL — YOU RULE THE NETWORK"
            color = "#00ff9f"
        elif access > 50:
            msg = "⚠️ PARTIAL BREACH — DATA ACQUIRED"
            color = "yellow"
        else:
            msg = "❌ FAILED HACK"
            color = "red"

        tk.Label(root, text=msg,
                 fg=color, bg="black",
                 font=("Consolas", 16, "bold")).pack(pady=10)

        tk.Label(root,
                 text=f"TRACE: {trace}% | ACCESS: {access}% | OVERRIDE: {override}%",
                 fg="white", bg="black").pack()

        tk.Button(root, text="RETRY",
                  command=lambda: start_cyber(root)).pack(pady=10)

    step1()