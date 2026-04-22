import tkinter as tk

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"
MAGENTA = "#ff5fe3"
WARNING = "#ff9f00"

notes = []
evidence_count = 0


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Story")
    story.configure(bg=BG)
    story.geometry("580x320")

    label = tk.Label(
        story,
        text="",
        wraplength=520,
        font=("Consolas", 12),
        fg=GREEN,
        bg=BG,
        justify="left"
    )
    label.pack(pady=30)

    index = [0]

    def next_text():
        if index[0] < len(text_list):
            label.config(text=text_list[index[0]])
            index[0] += 1
        else:
            story.destroy()
            next_func()

    tk.Button(
        story,
        text="▶ NEXT",
        bg="#020617",
        fg=CYAN,
        activebackground=CYAN,
        activeforeground="black",
        font=("Consolas", 11, "bold"),
        command=next_text
    ).pack(pady=10)

    next_text()


# ---------------- ENTRY ----------------
def open_case1(prev):
    story_text = [
        "📍 02:13 AM — Penthouse Apartment",
        "Rain hammers the glass as you enter the crime scene.",
        "Victim: Raj Malhotra, 42, real estate magnate.",
        "No forced entry. The door was locked from the inside.",
        "A family portrait sits intact. A small smear of mud stains the window sill.",
        "His laptop is shut, and the screen reads: 'ENTER CODE'.",
        "The caseboard is ready. Every clue you gather must fit the timeline.",
        "Your job is not just to accuse. You must think like an investigator."
    ]

    show_story(prev, story_text, crime_scene)


# ---------------- CRIME SCENE ----------------
def crime_scene():
    global notes, evidence_count
    notes = []
    evidence_count = 0

    scene = tk.Toplevel()
    scene.title("CIS // Crime Scene")
    scene.configure(bg=BG)
    scene.geometry("780x520")

    tk.Label(scene, text="CRIME SCENE INVESTIGATION",
             font=("Consolas", 18, "bold"),
             fg=CYAN, bg=BG).pack(pady=12)

    container = tk.Frame(scene, bg=BG)
    container.pack(fill="both", expand=True, padx=12, pady=5)

    left = tk.Frame(container, bg="#081327", bd=2, relief="sunken")
    left.pack(side="left", fill="both", expand=True, padx=8, pady=8)
    right = tk.Frame(container, bg="#081327", bd=2, relief="sunken")
    right.pack(side="left", fill="both", expand=True, padx=8, pady=8)

    tk.Label(left, text="EVIDENCE BOARD",
             font=("Consolas", 14, "bold"),
             bg="#081327", fg=GREEN).pack(pady=10)

    notes_box = tk.Text(left, bg="#020617", fg=CYAN,
                        font=("Consolas", 11), bd=0,
                        wrap="word", padx=10, pady=10)
    notes_box.pack(fill="both", expand=True, padx=10, pady=10)
    notes_box.config(state=tk.DISABLED)

    tracker = tk.Label(left, text="CLUES COLLECTED: 0/4",
                       fg=CYAN, bg="#081327",
                       font=("Consolas", 10, "bold"))
    tracker.pack(pady=(0, 12))

    def add_note(text, color=GREEN):
        notes_box.config(state=tk.NORMAL)
        notes_box.insert(tk.END, f"• {text}\n")
        notes_box.tag_add(str(len(notes)), f"{len(notes)+1}.0", f"{len(notes)+1}.end")
        notes_box.tag_config(str(len(notes)), foreground=color)
        notes_box.config(state=tk.DISABLED)
        notes_box.see(tk.END)
        notes.append(text)

    def update_tracking():
        tracker.config(text=f"CLUES COLLECTED: {evidence_count}/4")
        if evidence_count >= 3:
            analyze_button.config(state=tk.NORMAL)

    tk.Label(right, text="SCENE OPTIONS",
             font=("Consolas", 14, "bold"),
             bg="#081327", fg=MAGENTA).pack(pady=10)

    action_frame = tk.Frame(right, bg="#081327")
    action_frame.pack(fill="both", expand=True, padx=10, pady=5)

    option_buttons = {}

    def disable_button(name):
        if name in option_buttons:
            option_buttons[name].config(state=tk.DISABLED, bg="#03212e")

    def examine_body():
        global evidence_count
        if "body" in notes:
            return
        add_note("No blunt trauma. A tiny puncture wound is hidden behind the right collarbone.")
        add_note("The victim's fingertips are clean — he did not fight.", WARNING)
        add_note("A faint scent of burnt metal lingers, like a tampered power cable.", MAGENTA)
        evidence_count += 1
        disable_button("body")
        update_tracking()

    def inspect_laptop():
        global evidence_count
        if "laptop" in notes:
            return
        add_note("The laptop is locked with a numeric keypad.")
        add_note("A sticky note reads: 'DOB is key, but the first code is an answer.'", WARNING)
        add_note("The victim's date of birth is 17/08/1983.", CYAN)
        evidence_count += 1
        disable_button("laptop")
        update_tracking()

    def check_photo():
        global evidence_count
        if "photo" in notes:
            return
        add_note("The family portrait is pristine. The frame is shifted 3 cm to the left.")
        add_note("A receipt behind the frame shows a 22:00 dinner reservation.")
        add_note("A stray mud print on the balcony sill is size 42.", WARNING)
        evidence_count += 1
        disable_button("photo")
        update_tracking()

    def analyze_window():
        global evidence_count
        if "window" in notes:
            return
        add_note("The balcony window was opened from the inside and latched afterwards.")
        add_note("Wet mud stains suggest footsteps after 2:00 AM.")
        add_note("The lock has a burn mark consistent with a shorted cable.", MAGENTA)
        evidence_count += 1
        disable_button("window")
        update_tracking()

    option_buttons["body"] = tk.Button(action_frame, text="Examine Body",
                                        width=30, height=3,
                                        bg="#020617", fg=GREEN,
                                        activebackground=MAGENTA,
                                        command=examine_body)
    option_buttons["body"].pack(pady=6)

    option_buttons["laptop"] = tk.Button(action_frame, text="Inspect Laptop",
                                          width=30, height=3,
                                          bg="#020617", fg=GREEN,
                                          activebackground=MAGENTA,
                                          command=inspect_laptop)
    option_buttons["laptop"].pack(pady=6)

    option_buttons["photo"] = tk.Button(action_frame, text="Check Photo & Receipt",
                                         width=30, height=3,
                                         bg="#020617", fg=GREEN,
                                         activebackground=MAGENTA,
                                         command=check_photo)
    option_buttons["photo"].pack(pady=6)

    option_buttons["window"] = tk.Button(action_frame, text="Analyze Window",
                                          width=30, height=3,
                                          bg="#020617", fg=GREEN,
                                          activebackground=MAGENTA,
                                          command=analyze_window)
    option_buttons["window"].pack(pady=6)

    analyze_button = tk.Button(right, text="▶ ANALYZE EVIDENCE",
                               width=32, height=2,
                               bg="#020617", fg=CYAN,
                               state=tk.DISABLED,
                               command=lambda: show_story(scene, [
                                   "You have enough evidence to build a caseboard.",
                                   "The laptop hint points to a hidden code pattern.",
                                   "The balcony window and burn marks suggest sabotage.",
                                   "Now you must deduce the password and the guilty party."
                               ], evidence_analysis))
    analyze_button.pack(pady=16)

    tk.Label(right, text="Tip: Collect at least 3 clues before analysis.",
             fg=GREEN, bg="#081327",
             font=("Consolas", 10, "italic")).pack(pady=6)


# ---------------- EVIDENCE ANALYSIS ----------------
def evidence_analysis():
    analysis = tk.Toplevel()
    analysis.title("CIS // Evidence Analysis")
    analysis.configure(bg=BG)
    analysis.geometry("520x360")

    tk.Label(analysis, text="EVIDENCE ANALYSIS BOARD",
             fg=CYAN, bg=BG,
             font=("Consolas", 16, "bold")).pack(pady=12)

    tk.Label(analysis, text="The victim's DOB is 17/08/1983.",
             fg=GREEN, bg=BG, font=("Consolas", 11)).pack(pady=3)
    tk.Label(analysis, text="The sticky note says: 'DOB is key, but the first code is an answer.'",
             fg=WARNING, bg=BG, wraplength=480, justify="left").pack(pady=3)

    tk.Label(analysis, text="Investigator puzzle: Decode the laptop password.",
             fg=CYAN, bg=BG, font=("Consolas", 12, "bold")).pack(pady=12)

    tk.Label(analysis, text="Use this rule:", fg=GREEN, bg=BG, justify="left").pack()
    tk.Label(analysis, text="1. First two digits = day minus month.\n"
                             "2. Middle two digits = month.\n"
                             "3. Last two digits = last two digits of year.",
             fg=GREEN, bg=BG, wraplength=480, justify="left").pack(pady=6)

    entry = tk.Entry(analysis, bg="#020617", fg=GREEN, insertbackground=GREEN)
    entry.pack(pady=10)

    feedback = tk.Label(analysis, text="", bg=BG)
    feedback.pack()

    def attempt():
        code = entry.get().strip()
        if code == "090883":
            feedback.config(text="✅ PASSWORD CRACKED", fg=GREEN)
            tk.Button(analysis, text="▶ PROCEED TO SUSPECTS",
                      bg="#020617", fg=CYAN,
                      command=lambda: show_story(analysis, [
                          "Access granted. The victim's messages expose key relationships.",
                          "One suspect lies about their whereabouts.",
                          "It is time to interrogate with logic, not guesswork."
                      ], suspect_board)).pack(pady=12)
        else:
            feedback.config(text="❌ INCORRECT. Re-check the clue logic.", fg="red")

    tk.Button(analysis, text="SUBMIT CODE", bg="#020617", fg=GREEN,
              command=attempt).pack(pady=6)


# ---------------- SUSPECT BOARD ----------------
def suspect_board():
    board = tk.Toplevel()
    board.title("CIS // Suspect Board")
    board.configure(bg=BG)
    board.geometry("620x520")

    tk.Label(board, text="SUSPECT BOARD",
             fg=CYAN, bg=BG,
             font=("Consolas", 18, "bold")).pack(pady=12)

    instruction = tk.Label(board,
                           text="Review the alibis and contradictions. Then choose the suspect who cannot be telling the truth.",
                           fg=GREEN, bg=BG, wraplength=580, justify="left")
    instruction.pack(pady=10)

    clues_text = ("Clue 1: The driver returned at 2:05 AM and the elevator log shows the victim on the 24th floor at 2:08 AM.\n"
                  "Clue 2: The wife was recorded entering the penthouse at 1:55 AM, then leaving at 2:30 AM.\n"
                  "Clue 3: The business partner's call history shows a 2-minute call at 2:03 AM.\n"
                  "Clue 4: The balcony window was opened from inside at 2:12 AM.")

    tk.Label(board, text=clues_text,
             fg=WARNING, bg=BG, wraplength=580, justify="left", font=("Consolas", 11)).pack(pady=10)

    option_frame = tk.Frame(board, bg=BG)
    option_frame.pack(pady=10)

    def choose_suspect(name):
        if name == "Wife":
            response = [
                "The wife's timeline matches the camera entry and exit.",
                "She had access, but her movements are consistent.",
                "Her alibi is plausible."
            ]
            correct = False
        elif name == "Partner":
            response = [
                "The partner claims a call at 2:03 AM.",
                "The elevator log shows the victim still in the building at 2:08 AM.",
                "He could still have been present."
            ]
            correct = False
        else:
            response = [
                "The driver says he left by 2:05 AM.",
                "The victim's 2:08 AM presence and the opened balcony at 2:12 AM conflict with a driver far outside.",
                "The driver's timeline cannot explain how the balcony was accessed."
            ]
            correct = True

        show_story(board, [
            *response,
            "The contradictory timeline points to the liar.",
            "Now narrow it down and name the killer."
        ], lambda: final_choice(correct))

    tk.Button(option_frame, text="▶ Wife", width=18, height=3,
              bg="#020617", fg=GREEN,
              command=lambda: choose_suspect("Wife")).pack(side="left", padx=10)
    tk.Button(option_frame, text="▶ Partner", width=18, height=3,
              bg="#020617", fg=GREEN,
              command=lambda: choose_suspect("Partner")).pack(side="left", padx=10)
    tk.Button(option_frame, text="▶ Driver", width=18, height=3,
              bg="#020617", fg=GREEN,
              command=lambda: choose_suspect("Driver")).pack(side="left", padx=10)


# ---------------- FINAL DECISION ----------------
def final_choice(driver_is_guilty=False):
    f = tk.Toplevel()
    f.title("CIS // Final Decision")
    f.configure(bg=BG)
    f.geometry("520x380")

    tk.Label(f, text="WHO IS THE KILLER?",
             fg=CYAN, bg=BG,
             font=("Consolas", 18, "bold")).pack(pady=12)

    def result(choice):
        f.destroy()
        if choice == "Driver" and driver_is_guilty:
            ending = [
                "You present the timeline and the driver crumbles.",
                "His window contradicts the elevator log and balcony activity.",
                "Security footage confirms he was the last to leave the penthouse.",
                "He confesses under pressure.",
                "🎉 CASE SOLVED — INVESTIGATION COMPLETE"
            ]
        else:
            ending = [
                "You accuse the wrong person.",
                "The real suspect vanishes in the night.",
                "The case becomes cold.",
                "⚠️ MISSION FAILED"
            ]

        show_story(f, ending, lambda: None)

    button_frame = tk.Frame(f, bg=BG)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Wife", width=12,
              bg="#020617", fg=GREEN,
              command=lambda: result("Wife")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Partner", width=12,
              bg="#020617", fg=GREEN,
              command=lambda: result("Partner")).pack(side="left", padx=10)
    tk.Button(button_frame, text="Driver", width=12,
              bg="#020617", fg=GREEN,
              command=lambda: result("Driver")).pack(side="left", padx=10)