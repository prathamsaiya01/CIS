
import tkinter as tk
from tkinter import messagebox
import random

# Game state variables
suspicion = 0
evidence = 0
alibi = 0
risk_level = 0
current_phase = 0

# Color scheme - Blood & Darkness
BG_DARK = "#0d0d0d"
BG_PANEL = "#1a0505"
BLOOD_RED = "#8a0303"
BLOOD_BRIGHT = "#ff0000"
BLOOD_DIM = "#4a0000"
TEXT_GRAY = "#8a8a8a"
WARNING_ORANGE = "#ff4500"

def start_murder(root):
    global suspicion, evidence, alibi, risk_level, current_phase
    suspicion = 15
    evidence = 25
    alibi = 0
    risk_level = 0
    current_phase = 0

    for w in root.winfo_children():
        w.destroy()

    root.configure(bg=BG_DARK)

    # Create blood drip effect canvas at top
    blood_canvas = tk.Canvas(root, height=60, bg=BG_DARK, highlightthickness=0)
    blood_canvas.pack(fill="x")
    
    # Draw blood drips
    for i in range(0, 900, 40):
        height = random.randint(10, 50)
        blood_canvas.create_line(i, 0, i, height, fill=BLOOD_RED, width=3)
        blood_canvas.create_oval(i-3, height-3, i+3, height+3, fill=BLOOD_RED, outline="")

    # ===== HEADER WITH BLOOD STAIN EFFECT =====
    header_frame = tk.Frame(root, bg=BG_DARK)
    header_frame.pack(pady=10)

    title = tk.Label(header_frame, text="◄ THE PERFECT MURDER ►",
             font=("Courier New", 26, "bold"),
             fg=BLOOD_BRIGHT, bg=BG_DARK)
    title.pack()
    
    subtitle = tk.Label(header_frame, text="Every choice leaves a trace...",
             font=("Courier New", 10, "italic"),
             fg=BLOOD_DIM, bg=BG_DARK)
    subtitle.pack()

    # ===== RISK METER PANEL =====
    risk_frame = tk.Frame(root, bg=BG_PANEL, highlightbackground=BLOOD_RED, highlightthickness=2)
    risk_frame.pack(pady=10, padx=30, fill="x")

    tk.Label(risk_frame, text="⚠ RISK ASSESSMENT SYSTEM ⚠",
             font=("Courier New", 11, "bold"),
             fg=WARNING_ORANGE, bg=BG_PANEL).pack(pady=5)

    meter_frame = tk.Frame(risk_frame, bg=BG_PANEL)
    meter_frame.pack(pady=5)

    # Risk bar
    risk_bar_bg = tk.Frame(meter_frame, width=400, height=25, bg=BLOOD_DIM)
    risk_bar_bg.pack()
    risk_bar_bg.pack_propagate(False)
    
    global risk_fill
    risk_fill = tk.Frame(risk_bar_bg, width=50, height=25, bg=BLOOD_BRIGHT)
    risk_fill.place(x=0, y=0)
    
    global risk_text
    risk_text = tk.Label(risk_bar_bg, text="LOW RISK", font=("Courier New", 10, "bold"),
                        fg="white", bg=BLOOD_BRIGHT)
    risk_text.place(relx=0.5, rely=0.5, anchor="center")

    # ===== STATUS PANEL =====
    status_frame = tk.Frame(root, bg=BG_PANEL, highlightbackground=BLOOD_RED, highlightthickness=1)
    status_frame.pack(pady=5, padx=30, fill="x")

    global status_label
    status_label = tk.Label(status_frame,
                      text="🩸 SUSPICION: 15%  |  📁 EVIDENCE: 25%  |  🎭 ALIBI: 0%",
                      fg=BLOOD_BRIGHT, bg=BG_PANEL,
                      font=("Courier New", 11, "bold"))
    status_label.pack(pady=8)

    def update_stats(s=0, e=0, a=0, r=0):
        global suspicion, evidence, alibi, risk_level
        suspicion = max(0, min(100, suspicion + s))
        evidence = max(0, min(100, evidence + e))
        alibi = max(0, min(100, alibi + a))
        risk_level = max(0, min(100, risk_level + r))
        
        # Update status
        status_label.config(text=f"🩸 SUSPICION: {suspicion}%  |  📁 EVIDENCE: {evidence}%  |  🎭 ALIBI: {alibi}%")
        
        # Color code based on danger
        if suspicion > 70 or evidence > 70:
            status_label.config(fg=BLOOD_BRIGHT)
        elif suspicion > 40 or evidence > 40:
            status_label.config(fg=WARNING_ORANGE)
        else:
            status_label.config(fg="#00ff41")
        
        # Update risk meter
        bar_width = int(4 * risk_level)
        risk_fill.config(width=max(50, bar_width))
        
        if risk_level < 30:
            risk_fill.config(bg="#00aa00")
            risk_text.config(text="LOW RISK", bg="#00aa00")
        elif risk_level < 60:
            risk_fill.config(bg=WARNING_ORANGE)
            risk_text.config(text="MODERATE RISK", bg=WARNING_ORANGE)
        else:
            risk_fill.config(bg=BLOOD_BRIGHT)
            risk_text.config(text="HIGH RISK - LIKELY CAUGHT", bg=BLOOD_BRIGHT)

    # ===== STORY TERMINAL =====
    terminal_frame = tk.Frame(root, bg=BG_DARK, highlightbackground=BLOOD_DIM, highlightthickness=1)
    terminal_frame.pack(pady=10, padx=30)

    global terminal
    terminal = tk.Text(terminal_frame, height=16, width=90,
                       bg=BG_DARK, fg=BLOOD_BRIGHT,
                       font=("Courier New", 11), bd=0,
                       insertbackground=BLOOD_BRIGHT,
                       selectbackground=BLOOD_DIM,
                       padx=10, pady=10)
    terminal.pack()
    terminal.config(state=tk.DISABLED)

    def type_log(text, color=BLOOD_BRIGHT, delay=True):
        terminal.config(state=tk.NORMAL)
        if delay:
            for char in text:
                terminal.insert(tk.END, char, color)
                terminal.update()
                terminal.after(15)
            terminal.insert(tk.END, "\n")
        else:
            terminal.insert(tk.END, text + "\n", color)
        terminal.see(tk.END)
        terminal.config(state=tk.DISABLED)

    # ===== ACTION AREA =====
    global action_frame
    action_frame = tk.Frame(root, bg=BG_DARK, highlightbackground=BLOOD_RED, highlightthickness=1)
    action_frame.pack(pady=15, padx=30, fill="both", expand=True)

    global content_frame
    content_frame = tk.Frame(action_frame, bg=BG_DARK)
    content_frame.pack(pady=20, padx=20, fill="both", expand=True)

    def clear_content():
        for w in content_frame.winfo_children():
            w.destroy()

    # ===== PHASE 1: THE SETUP =====
    def phase1():
        clear_content()
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║  PROLOGUE: THE SERVANT'S RESENTMENT      ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        type_log("You are Marcus Cole, a servant in the Whitmore Estate.")
        type_log("For three years, you've served Lord Whitmore, watching him")
        type_log("squander his wealth while treating you like dirt beneath his boots.")
        type_log("")
        type_log("Tonight, he hosts a dinner party. The staff is busy.")
        type_log("His Lordship will retire to his study at 11 PM, alone.")
        type_log("The safe behind his portrait contains $2 million in bearer bonds.")
        type_log("")
        type_log("But first... you must choose your moment.", WARNING_ORANGE)
        
        tk.Label(content_frame, text="◄ SELECT MURDER TIME ►",
                 font=("Courier New", 12, "bold"),
                 fg=BLOOD_BRIGHT, bg=BG_DARK).pack(pady=15)

        choices_frame = tk.Frame(content_frame, bg=BG_DARK)
        choices_frame.pack()

        # Option 1
        btn1 = tk.Button(choices_frame, 
                        text="[ 9:00 PM - During Dinner Party ]\n"
                             "Risk: HIGH | Guests present, but chaos provides cover",
                        width=50, height=3,
                        bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                        activebackground=BLOOD_RED, activeforeground="white",
                        font=("Courier New", 10),
                        command=lambda: choose_time("9pm"))
        btn1.pack(pady=8)

        # Option 2
        btn2 = tk.Button(choices_frame, 
                        text="[ 11:30 PM - After Study Retreat ]\n"
                             "Risk: MEDIUM | He's alone, but staff still awake",
                        width=50, height=3,
                        bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                        activebackground=BLOOD_RED, activeforeground="white",
                        font=("Courier New", 10),
                        command=lambda: choose_time("1130pm"))
        btn2.pack(pady=8)

        # Option 3
        btn3 = tk.Button(choices_frame, 
                        text="[ 2:00 AM - Deep Night ]\n"
                             "Risk: LOW | House asleep, but prolonged absence suspicious",
                        width=50, height=3,
                        bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                        activebackground=BLOOD_RED, activeforeground="white",
                        font=("Courier New", 10),
                        command=lambda: choose_time("2am"))
        btn3.pack(pady=8)

    def choose_time(time_choice):
        global selected_time
        selected_time = time_choice
        
        if time_choice == "9pm":
            type_log("")
            type_log("You slip away during the soup course...", BLOOD_BRIGHT)
            update_stats(s=25, e=15, a=0, r=30)
            type_log("RISK: Guests might notice your absence. Blood could splash on attire.", WARNING_ORANGE)
        elif time_choice == "1130pm":
            type_log("")
            type_log("You wait until the study lamp turns on...", BLOOD_BRIGHT)
            update_stats(s=10, e=10, a=0, r=15)
            type_log("RISK: Balanced approach. Butler checks on Lord at midnight.", "#00ff41")
        else:
            type_log("")
            type_log("The grandfather clock strikes two...", BLOOD_BRIGHT)
            update_stats(s=5, e=5, a=0, r=10)
            type_log("RISK: Safest timing, but your bed was empty all night.", "#00ff41")
        
        phase2()

    # ===== PHASE 2: THE WEAPON =====
    def phase2():
        clear_content()
        type_log("")
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║  CHAPTER 1: THE INSTRUMENT OF DEATH     ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        type_log("The study door is before you. Lord Whitmore sits with his back")
        type_log("to the door, reading financial reports, sipping brandy.")
        type_log("")
        type_log("Your weapon determines everything: noise, blood, evidence, trace.", WARNING_ORANGE)
        
        tk.Label(content_frame, text="◄ SELECT MURDER WEAPON ►",
                 font=("Courier New", 12, "bold"),
                 fg=BLOOD_BRIGHT, bg=BG_DARK).pack(pady=15)

        choices_frame = tk.Frame(content_frame, bg=BG_DARK)
        choices_frame.pack()

        # Weapon 1
        tk.Button(choices_frame, 
                 text="[ CEREMONIAL DAGGER ]\n"
                      "Risk: MEDIUM | Silent, but DNA on blade, blood spray likely",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_weapon("dagger")).pack(pady=8)

        # Weapon 2
        tk.Button(choices_frame, 
                 text="[ SILK GARROTE ]\n"
                      "Risk: LOW | Silent, no blood, requires physical strength",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_weapon("garrote")).pack(pady=8)

        # Weapon 3
        tk.Button(choices_frame, 
                 text="[ HEAVY BRONZE STATUE ]\n"
                      "Risk: HIGH | Blunt trauma, blood minimal, but fingerprints/dents",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_weapon("statue")).pack(pady=8)

        # Weapon 4
        tk.Button(choices_frame, 
                 text="[ POISON - ARSENIC IN BRANDY ]\n"
                      "Risk: MEDIUM-HIGH | Natural death suspected initially, but toxicology...",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_weapon("poison")).pack(pady=8)

    def choose_weapon(weapon):
        global selected_weapon
        selected_weapon = weapon
        
        type_log("")
        if weapon == "dagger":
            type_log("You grip the cold steel. The blade is sharp, serrated near the hilt.", BLOOD_BRIGHT)
            update_stats(s=15, e=25, a=0, r=20)
            type_log("ANALYSIS: Blood will spray. Fibers may stick to hilt.", WARNING_ORANGE)
        elif weapon == "garrote":
            type_log("The silk cord is soft but unbreakable. You practiced on fence posts.", BLOOD_BRIGHT)
            update_stats(s=5, e=10, a=0, r=10)
            type_log("ANALYSIS: Clean kill. Strangulation marks distinctive, though.", "#00ff41")
        elif weapon == "statue":
            type_log("The bronze eagle is heavy. One blow should suffice.", BLOOD_BRIGHT)
            update_stats(s=20, e=30, a=0, r=25)
            type_log("ANALYSIS: Dent in statue. Bone fragments possible. Very messy.", WARNING_ORANGE)
        else:
            type_log("You prepared the arsenic weeks ago, waiting for the right moment.", BLOOD_BRIGHT)
            update_stats(s=10, e=35, a=0, r=30)
            type_log("ANALYSIS: Delayed death. You must be seen elsewhere when he dies.", WARNING_ORANGE)
        
        phase3()

    # ===== PHASE 3: LOGICAL CHALLENGES =====
    def phase3():
        clear_content()
        type_log("")
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║  CHAPTER 2: THE SCENE                  ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        type_log("It is done. Lord Whitmore lies still.")
        type_log("Now the real work begins. Every detail matters.")
        type_log("")
        type_log("Answer correctly to minimize evidence and suspicion.", WARNING_ORANGE)
        
        # Challenge questions based on murder logic
        challenges = [
            {
                "q": "The study door has a keyhole but no key inside.\nHow do you lock it from outside?",
                "options": [
                    ("Use the master key from housekeeping", 15, 10),
                    ("Pick the lock with a hairpin", 5, 5),
                    ("Leave it unlocked - looks like natural entry", 25, 20),
                    ("Thread string under door to pull key through", 0, 0)
                ],
                "correct": 3,
                "correct_text": "Clever. The string trick leaves no trace.",
                "wrong_text": "Risky. Keys can be traced. Unlocked doors invite suspicion."
            },
            {
                "q": "Blood has soaked into the Turkish rug.\nWhat is your move?",
                "options": [
                    ("Roll up the entire rug and hide it", 20, 25),
                    ("Blot with towels, then burn them", 10, 15),
                    ("Flip the rug over, stain side down", 30, 30),
                    ("Cut out the stained section precisely", 5, 10)
                ],
                "correct": 1,
                "correct_text": "Smart. Small fires in fireplaces raise no eyebrows.",
                "wrong_text": "Problematic. Missing rugs and cut fibers are obvious."
            },
            {
                "q": "You need an alibi for the time of death.\nWho do you approach?",
                "options": [
                    ("The scullery maid - she'll say anything for coin", 20, 10),
                    ("The butler - his word carries weight", 5, 5),
                    ("A fellow servant doing laundry - mundane, believable", 0, 0),
                    ("No one - solitary alibi is suspicious but unbreakable", 30, 20)
                ],
                "correct": 2,
                "correct_text": "Perfect. Mundane tasks with witnesses are gold.",
                "wrong_text": "Dangerous. Bribed witnesses crack. Solitude screams guilt."
            },
            {
                "q": "Lord Whitmore's safe is behind the portrait.\nHow do you open it?",
                "options": [
                    ("Brute force - crowbar and hope", 35, 40),
                    ("Guess his birthday combination", 15, 20),
                    ("You watched him enter it yesterday: 17-42-09", 0, 5),
                    ("Leave it - too risky, walk away empty", 5, 0)
                ],
                "correct": 2,
                "correct_text": "Excellent observation. Clean entry, no damage.",
                "wrong_text": "Mistake. Damage shows intent. Guessing wastes time."
            }
        ]

        current_challenge = [0]
        
        challenge_frame = tk.Frame(content_frame, bg=BG_DARK)
        challenge_frame.pack(fill="both", expand=True)

        def show_challenge():
            for w in challenge_frame.winfo_children():
                w.destroy()
            
            if current_challenge[0] >= len(challenges):
                phase4()
                return
            
            ch = challenges[current_challenge[0]]
            
            tk.Label(challenge_frame, 
                    text=f"◄ EVIDENCE MANAGEMENT: SCENARIO {current_challenge[0]+1}/4 ►",
                    font=("Courier New", 11, "bold"),
                    fg=WARNING_ORANGE, bg=BG_DARK).pack(pady=10)
            
            q_frame = tk.Frame(challenge_frame, bg=BG_PANEL, highlightbackground=BLOOD_DIM, highlightthickness=1)
            q_frame.pack(pady=10, padx=20, fill="x")
            
            tk.Label(q_frame, text=ch["q"],
                    font=("Courier New", 11),
                    fg=BLOOD_BRIGHT, bg=BG_PANEL,
                    wraplength=500, justify="left").pack(pady=15, padx=15)
            
            options_frame = tk.Frame(challenge_frame, bg=BG_DARK)
            options_frame.pack(pady=10)
            
            for idx, (opt_text, susp, evid) in enumerate(ch["options"]):
                btn = tk.Button(options_frame,
                              text=opt_text,
                              width=60, height=2,
                              bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                              activebackground=BLOOD_RED, activeforeground="white",
                              font=("Courier New", 9),
                              command=lambda i=idx, s=susp, e=evid: check_answer(i, s, e))
                btn.pack(pady=5)

        def check_answer(choice_idx, susp_penalty, evid_penalty):
            ch = challenges[current_challenge[0]]
            
            type_log("")
            if choice_idx == ch["correct"]:
                type_log(f"✓ {ch['correct_text']}", "#00ff41")
                update_stats(s=0, e=0, a=10, r=-5)
            else:
                type_log(f"✗ {ch['wrong_text']}", BLOOD_BRIGHT)
                update_stats(s=susp_penalty, e=evid_penalty, a=0, r=10)
            
            current_challenge[0] += 1
            challenge_frame.after(1000, show_challenge)
        
        show_challenge()

    # ===== PHASE 4: DISPOSAL =====
    def phase4():
        clear_content()
        type_log("")
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║  CHAPTER 3: THE BODY                   ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        type_log("Four hours remain until dawn. The body grows cold.")
        type_log("Disposal method determines discovery timeline.")
        
        tk.Label(content_frame, text="◄ BODY DISPOSAL METHOD ►",
                 font=("Courier New", 12, "bold"),
                 fg=BLOOD_BRIGHT, bg=BG_DARK).pack(pady=15)

        choices_frame = tk.Frame(content_frame, bg=BG_DARK)
        choices_frame.pack()

        tk.Button(choices_frame, 
                 text="[ HIDE IN WINE CELLAR ]\n"
                      "Risk: HIGH | Found eventually, but buys time to flee",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_disposal("cellar")).pack(pady=8)

        tk.Button(choices_frame, 
                 text="[ WEIGHTS & ESTATE POND ]\n"
                      "Risk: MEDIUM | Water destroys evidence, but bloating reveals",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_disposal("pond")).pack(pady=8)

        tk.Button(choices_frame, 
                 text="[ FIRE - STUDY ACCIDENT ]\n"
                      "Risk: MEDIUM-HIGH | Destroys all evidence, but arson detected",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_disposal("fire")).pack(pady=8)

        tk.Button(choices_frame, 
                 text="[ LEAVE AS IS - STAGED ROBBERY ]\n"
                      "Risk: MEDIUM | No disposal risk, but crime scene evidence abundant",
                 width=55, height=3,
                 bg=BLOOD_DIM, fg=BLOOD_BRIGHT,
                 activebackground=BLOOD_RED, activeforeground="white",
                 font=("Courier New", 10),
                 command=lambda: choose_disposal("staged")).pack(pady=8)

    def choose_disposal(method):
        type_log("")
        if method == "cellar":
            type_log("You drag the body to the cellar. The cool darkness preserves... and betrays.", BLOOD_BRIGHT)
            update_stats(s=20, e=15, a=0, r=25)
            type_log("The smell will surface in 48 hours. You must be gone by then.", WARNING_ORANGE)
        elif method == "pond":
            type_log("The water accepts its offering silently. Bubbles rise, then stop.", BLOOD_BRIGHT)
            update_stats(s=10, e=20, a=0, r=15)
            type_log("Water destroys DNA, but the body will float in 5-7 days.", "#00ff41")
        elif method == "fire":
            type_log("The match strikes. You have 3 minutes to vacate before smoke rises.", BLOOD_BRIGHT)
            update_stats(s=15, e=5, a=0, r=20)
            type_log("Accelerant traces remain. Arson investigators are thorough.", WARNING_ORANGE)
        else:
            type_log("You smash the window, overturn furniture, take the wallet.", BLOOD_BRIGHT)
            update_stats(s=5, e=30, a=0, r=15)
            type_log("Simple narrative, but your skin cells are everywhere.", WARNING_ORANGE)
        
        phase5()

    # ===== PHASE 5: INVESTIGATION =====
    def phase5():
        clear_content()
        type_log("")
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║  FINAL CHAPTER: THE INTERROGATION       ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        type_log("Three days later. Scotland Yard has questions.")
        type_log("Detective Inspector Graves stares across the metal table.")
        type_log("")
        type_log("\"Where were you between 11 PM and 3 AM on the night in question?\"")
        
        tk.Label(content_frame, text="◄ PROVIDE YOUR ALIBI ►",
                 font=("Courier New", 12, "bold"),
                 fg=BLOOD_BRIGHT, bg=BG_DARK).pack(pady=15)

        input_frame = tk.Frame(content_frame, bg=BG_PANEL, highlightbackground=BLOOD_DIM, highlightthickness=1)
        input_frame.pack(pady=10, padx=20, fill="x")
        
        tk.Label(input_frame, 
                text="Type your alibi carefully. Inconsistencies will be noted.",
                fg=TEXT_GRAY, bg=BG_PANEL, font=("Courier New", 10)).pack(pady=10)
        
        entry = tk.Entry(input_frame, width=50,
                        bg=BG_DARK, fg=BLOOD_BRIGHT,
                        insertbackground=BLOOD_BRIGHT,
                        font=("Courier New", 11),
                        justify="center")
        entry.pack(pady=10)
        entry.focus()
        
        result_label = tk.Label(input_frame, text="", 
                               bg=BG_PANEL, font=("Courier New", 10))
        result_label.pack(pady=10)

        def check_alibi():
            ans = entry.get().lower().strip()
            
            good_keywords = ["servant", "cleaning", "kitchen", "laundry", "other servant", 
                           "witness", "chores", "working", "duty", "maid", "butler"]
            bad_keywords = ["alone", "sleeping", "bed", "room", "nowhere", "home", "nobody"]
            
            good_count = sum(1 for k in good_keywords if k in ans)
            bad_count = sum(1 for k in bad_keywords if k in ans)
            
            if good_count > bad_count and len(ans) > 20:
                result_label.config(text="✓ ALIBI ACCEPTED - WITNESSES CORROBORATE", fg="#00ff41")
                type_log("")
                type_log("Your alibi holds. The laundry maid remembers your presence.", "#00ff41")
                update_stats(s=-20, e=0, a=30, r=-15)
            else:
                result_label.config(text="✗ ALIBI SUSPECT - INCONSISTENCIES DETECTED", fg=BLOOD_BRIGHT)
                type_log("")
                type_log("Graves frowns. Your story has gaps. He makes notes.", BLOOD_BRIGHT)
                update_stats(s=30, e=20, a=0, r=25)
            
            entry.config(state=tk.DISABLED)
            content_frame.after(2000, final_verdict)

        tk.Button(input_frame, text="[ SUBMIT STATEMENT ]",
                 bg=BLOOD_RED, fg="white",
                 activebackground=BLOOD_BRIGHT, activeforeground="white",
                 font=("Courier New", 10, "bold"),
                 command=check_alibi).pack(pady=10)

    # ===== FINAL VERDICT =====
    def final_verdict():
        clear_content()
        type_log("")
        type_log("╔══════════════════════════════════════════╗", TEXT_GRAY)
        type_log("║           FINAL VERDICT                  ║", TEXT_GRAY)
        type_log("╚══════════════════════════════════════════╝", TEXT_GRAY)
        type_log("")
        
        # Calculate outcome
        total_risk = suspicion + evidence - alibi
        
        if total_risk > 120 or suspicion > 80 or evidence > 80:
            outcome = "caught"
        elif total_risk < 60 and alibi > 40:
            outcome = "perfect"
        elif total_risk < 100:
            outcome = "suspected"
        else:
            outcome = "caught"
        
        result_frame = tk.Frame(content_frame, bg=BG_PANEL, 
                             highlightbackground=BLOOD_RED if outcome == "caught" else "#00ff41",
                             highlightthickness=3)
        result_frame.pack(pady=20, padx=20, fill="x")
        
        if outcome == "caught":
            tk.Label(result_frame, 
                    text="⚠ YOU HAVE BEEN ARRESTED ⚠",
                    font=("Courier New", 18, "bold"),
                    fg=BLOOD_BRIGHT, bg=BG_PANEL).pack(pady=15)
            
            tk.Label(result_frame,
                    text="The evidence was overwhelming.\n"
                         "Your alibi collapsed under scrutiny.\n"
                         "You will hang by the neck until dead.",
                    font=("Courier New", 11),
                    fg=TEXT_GRAY, bg=BG_PANEL).pack(pady=10)
            
            type_log("ARREST WARRANT EXECUTED. EVIDENCE IRREFUTABLE.", BLOOD_BRIGHT)
            
        elif outcome == "perfect":
            tk.Label(result_frame, 
                    text="✓ THE PERFECT MURDER ✓",
                    font=("Courier New", 18, "bold"),
                    fg="#00ff41", bg=BG_PANEL).pack(pady=15)
            
            tk.Label(result_frame,
                    text="The case goes cold. You inherit through a loophole.\n"
                         "You live as a free man, the secret burning in your chest.\n"
                         "But perfect crimes demand perfect silence... forever.",
                    font=("Courier New", 11),
                    fg=TEXT_GRAY, bg=BG_PANEL).pack(pady=10)
            
            type_log("CASE CLOSED - UNSOLVED. YOU ARE FREE.", "#00ff41")
            
        else:
            tk.Label(result_frame, 
                    text="⚠ UNDER PERMANENT SUSPICION ⚠",
                    font=("Courier New", 18, "bold"),
                    fg=WARNING_ORANGE, bg=BG_PANEL).pack(pady=15)
            
            tk.Label(result_frame,
                    text="They know you did it. They cannot prove it.\n"
                         "You are watched. Followed. Your freedom is a cage.\n"
                         "One mistake, and they will have you.",
                    font=("Courier New", 11),
                    fg=TEXT_GRAY, bg=BG_PANEL).pack(pady=10)
            
            type_log("SURVEILLANCE ACTIVE. YOU ARE NOT FREE.", WARNING_ORANGE)
        
        # Stats display
        stats_frame = tk.Frame(result_frame, bg=BG_PANEL)
        stats_frame.pack(pady=15)
        
        tk.Label(stats_frame, 
                text=f"FINAL METRICS",
                font=("Courier New", 10, "bold"),
                fg=BLOOD_BRIGHT, bg=BG_PANEL).pack()
        
        tk.Label(stats_frame,
                text=f"Suspicion: {suspicion}% | Evidence: {evidence}% | Alibi Strength: {alibi}%",
                font=("Courier New", 10),
                fg=TEXT_GRAY, bg=BG_PANEL).pack(pady=5)
        
        tk.Label(stats_frame,
                text=f"Total Risk Score: {total_risk}/200",
                font=("Courier New", 10, "bold"),
                fg=BLOOD_BRIGHT if total_risk > 100 else "#00ff41",
                bg=BG_PANEL).pack()
        
        # Retry button
        tk.Button(content_frame, text="[ COMMIT ANOTHER MURDER ]",
                 bg=BLOOD_RED, fg="white",
                 activebackground=BLOOD_BRIGHT, activeforeground="white",
                 font=("Courier New", 12, "bold"),
                 command=lambda: start_murder(root)).pack(pady=30)

    # Start the game
    phase1()


# Main initialization
if __name__ == "__main__":
    root = tk.Tk()
    root.title("THE PERFECT MURDER")
    root.geometry("950x800")
    root.configure(bg=BG_DARK)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    start_murder(root)
    root.mainloop()
