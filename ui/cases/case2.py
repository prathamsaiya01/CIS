import tkinter as tk
import time
import threading
import random

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"
MAGENTA = "#ff5fe3"
WARNING = "#ff9f00"
RED = "#ff0040"

# Game State
evidence_collected = []
suspects = {
    "IT_Manager": {"name": "Rajesh Kumar", "access": "Full", "alibi": "Home", "suspicion": 0},
    "IT_Employee": {"name": "Priya Sharma", "access": "Limited", "alibi": "Office", "suspicion": 0},
    "Security_Guard": {"name": "Vikram Singh", "access": "None", "alibi": "Patrol", "suspicion": 0},
    "Bank_Manager": {"name": "Anita Desai", "access": "Partial", "alibi": "Meeting", "suspicion": 0}
}
current_suspicion = 0
accuracy_score = 100
game_timer = None
random_events = ["new_clue", "misleading_info", "time_bonus"]


# ---------------- ANIMATED TEXT ENGINE ----------------
def animate_text(label, text, delay=50):
    """Animate text appearance character by character"""
    label.config(text="")
    for i, char in enumerate(text):
        def update_char(c=char, idx=i):
            current = label.cget("text")
            label.config(text=current + c)
        label.after(delay * (i + 1), update_char)


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    if prev:
        prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 2 - Bank Breach")
    story.configure(bg=BG)
    story.geometry("600x350")

    label = tk.Label(
        story,
        text="",
        wraplength=550,
        font=("Consolas", 12),
        fg=GREEN,
        bg=BG,
        justify="left"
    )
    label.pack(pady=30)

    index = [0]

    def next_text():
        if index[0] < len(text_list):
            animate_text(label, text_list[index[0]], 30)
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
def open_case2(prev):
    global current_suspicion, accuracy_score, evidence_collected
    current_suspicion = 0
    accuracy_score = 100
    evidence_collected = []

    story_text = [
        "🚨 CYBER BREACH ALERT — National Bank Headquarters",
        "💰 ₹2.5 Crores transferred to offshore accounts in under 60 seconds.",
        "🔒 No physical breach detected. Attack originated from internal network.",
        "⏰ Incident occurred between 23:45 and 00:15. Security cameras show normal activity.",
        "💻 Only the main transaction server was accessed. All other systems untouched.",
        "👥 Four personnel had access during the window: IT Manager, IT Employee, Security Guard, Bank Manager.",
        "🕵️ Your mission: Identify the insider, reconstruct the timeline, and prevent further damage.",
        "⚠️ ALERT: Suspicion levels will rise with wrong decisions. Time is critical."
    ]

    show_story(prev, story_text, case_briefing)


# ---------------- CASE BRIEFING ----------------
def case_briefing():
    briefing = tk.Toplevel()
    briefing.title("CIS // Case Briefing")
    briefing.configure(bg=BG)
    briefing.geometry("700x500")

    # Header with suspicion meter
    header_frame = tk.Frame(briefing, bg="#081327", height=50)
    header_frame.pack(fill="x", pady=(0, 10))
    header_frame.pack_propagate(False)

    tk.Label(header_frame, text="CASE 2: BANK BREACH INVESTIGATION",
             font=("Consolas", 16, "bold"), fg=CYAN, bg="#081327").pack(side="left", padx=20)

    suspicion_label = tk.Label(header_frame, text="SUSPICION: 0%",
                               fg=GREEN, bg="#081327", font=("Consolas", 12, "bold"))
    suspicion_label.pack(side="right", padx=20)

    # Main content
    content_frame = tk.Frame(briefing, bg=BG)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Evidence Panel (Left)
    evidence_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    evidence_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    tk.Label(evidence_frame, text="EVIDENCE LOG",
             font=("Consolas", 14, "bold"), bg="#081327", fg=GREEN).pack(pady=10)

    evidence_text = tk.Text(evidence_frame, bg="#020617", fg=CYAN,
                           font=("Consolas", 10), bd=0, wrap="word",
                           padx=10, pady=10, state=tk.DISABLED)
    evidence_text.pack(fill="both", expand=True, padx=10, pady=10)

    # Actions Panel (Right)
    actions_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    actions_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    tk.Label(actions_frame, text="INVESTIGATION ACTIONS",
             font=("Consolas", 14, "bold"), bg="#081327", fg=MAGENTA).pack(pady=10)

    actions_content = tk.Frame(actions_frame, bg="#081327")
    actions_content.pack(fill="both", expand=True, padx=10, pady=5)

    def add_evidence(text, color=GREEN):
        evidence_text.config(state=tk.NORMAL)
        evidence_text.insert(tk.END, f"• {text}\n")
        evidence_text.tag_add("latest", "end-2l", "end-1l")
        evidence_text.tag_config("latest", foreground=color)
        evidence_text.config(state=tk.DISABLED)
        evidence_text.see(tk.END)
        evidence_collected.append(text)

    def update_suspicion():
        suspicion_label.config(text=f"SUSPICION: {current_suspicion}%")
        if current_suspicion >= 80:
            suspicion_label.config(fg=RED)
        elif current_suspicion >= 50:
            suspicion_label.config(fg=WARNING)

    # Initial evidence
    add_evidence("Transfer occurred: 23:58:42 - ₹2.5 Crores to Cayman Islands account")
    add_evidence("Source IP: Internal network (192.168.100.X range)")
    add_evidence("Access method: Authorized credentials, no brute force detected")
    add_evidence("Security logs: Clean until 23:55, then encrypted entries")

    # Action buttons
    action_buttons = {}

    def disable_action(name):
        if name in action_buttons:
            action_buttons[name].config(state=tk.DISABLED, bg="#03212e")

    def examine_server_room():
        add_evidence("Server room access: Magnetic lock shows entry at 23:40 by authorized card")
        add_evidence("Physical evidence: Coffee cup with lipstick mark, USB drive hidden in vent")
        add_evidence("Network cable: Burn mark on port 7, consistent with data surge")
        disable_action("server")
        update_suspicion()

    def analyze_network_logs():
        add_evidence("Network traffic: Unusual spike at 23:57 from workstation 192.168.100.15")
        add_evidence("Login pattern: 47 failed attempts from external IP, then successful internal login")
        add_evidence("Data transfer: 2.3GB outbound, compressed and encrypted")
        disable_action("network")
        update_suspicion()

    def review_security_footage():
        add_evidence("Camera footage: IT Manager enters server room at 23:35, exits at 23:50")
        add_evidence("Footage gap: 15-second blackout at 23:58:30, likely deliberate")
        add_evidence("Parking lot: Security Guard's car leaves at 23:45, returns at 00:20")
        disable_action("footage")
        update_suspicion()

    def interview_witnesses():
        add_evidence("Bank Manager: 'I was in a client meeting until midnight'")
        add_evidence("IT Employee: 'Working late on system maintenance'")
        add_evidence("Security Guard: 'Routine patrol, nothing unusual'")
        disable_action("witnesses")
        update_suspicion()

    action_buttons["server"] = tk.Button(actions_content, text="Examine Server Room",
                                        width=25, height=2, bg="#020617", fg=GREEN,
                                        activebackground=MAGENTA, command=examine_server_room)
    action_buttons["server"].pack(pady=4)

    action_buttons["network"] = tk.Button(actions_content, text="Analyze Network Logs",
                                         width=25, height=2, bg="#020617", fg=GREEN,
                                         activebackground=MAGENTA, command=analyze_network_logs)
    action_buttons["network"].pack(pady=4)

    action_buttons["footage"] = tk.Button(actions_content, text="Review Security Footage",
                                         width=25, height=2, bg="#020617", fg=GREEN,
                                         activebackground=MAGENTA, command=review_security_footage)
    action_buttons["footage"].pack(pady=4)

    action_buttons["witnesses"] = tk.Button(actions_content, text="Interview Witnesses",
                                           width=25, height=2, bg="#020617", fg=GREEN,
                                           activebackground=MAGENTA, command=interview_witnesses)
    action_buttons["witnesses"].pack(pady=4)

    # Progress to analysis
    def proceed_to_analysis():
        if len(evidence_collected) >= 6:
            show_story(briefing, [
                "Evidence collected. Now for the critical analysis phase.",
                "Each piece of evidence must be connected to form a timeline.",
                "Wrong assumptions will increase suspicion and alert the suspect.",
                "Choose your analytical approach carefully."
            ], evidence_analysis)
        else:
            # Penalty for rushing
            global current_suspicion
            current_suspicion += 15
            update_suspicion()
            add_evidence("WARNING: Insufficient evidence collected. Suspicion increased.", WARNING)

    tk.Button(actions_content, text="▶ PROCEED TO ANALYSIS",
              width=25, height=2, bg="#020617", fg=CYAN,
              command=proceed_to_analysis).pack(pady=10)

    tk.Label(actions_content, text="Collect at least 6 clues before proceeding",
             fg=GREEN, bg="#081327", font=("Consolas", 9, "italic")).pack(pady=5)


# ---------------- EVIDENCE ANALYSIS ----------------
def evidence_analysis():
    analysis = tk.Toplevel()
    analysis.title("CIS // Evidence Analysis")
    analysis.configure(bg=BG)
    analysis.geometry("750x550")

    # Header
    header_frame = tk.Frame(analysis, bg="#081327", height=50)
    header_frame.pack(fill="x", pady=(0, 10))
    header_frame.pack_propagate(False)

    tk.Label(header_frame, text="EVIDENCE ANALYSIS CENTER",
             font=("Consolas", 16, "bold"), fg=CYAN, bg="#081327").pack(side="left", padx=20)

    suspicion_label = tk.Label(header_frame, text=f"SUSPICION: {current_suspicion}%",
                               fg=GREEN if current_suspicion < 50 else WARNING, bg="#081327",
                               font=("Consolas", 12, "bold"))
    suspicion_label.pack(side="right", padx=20)

    # Main content
    content_frame = tk.Frame(analysis, bg=BG)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Analysis Panel (Left)
    analysis_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    analysis_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    tk.Label(analysis_frame, text="ANALYSIS TOOLS",
             font=("Consolas", 14, "bold"), bg="#081327", fg=GREEN).pack(pady=10)

    analysis_content = tk.Frame(analysis_frame, bg="#081327")
    analysis_content.pack(fill="both", expand=True, padx=10, pady=5)

    # Puzzle selection
    puzzle_buttons = {}

    def disable_puzzle(name):
        if name in puzzle_buttons:
            puzzle_buttons[name].config(state=tk.DISABLED, bg="#03212e")

    def logical_reasoning_puzzle():
        puzzle_window = tk.Toplevel(analysis)
        puzzle_window.title("CIS // Logical Reasoning")
        puzzle_window.configure(bg=BG)
        puzzle_window.geometry("500x400")

        tk.Label(puzzle_window, text="LOGICAL REASONING: ACCESS PATTERN ANALYSIS",
                 font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack(pady=10)

        tk.Label(puzzle_window,
                 text="Network logs show access from workstation 192.168.100.15\n"
                      "This workstation is assigned to the IT Employee.\n"
                      "However, the IT Manager has system override privileges.\n"
                      "The Security Guard has no technical access.\n"
                      "The Bank Manager has read-only access.\n\n"
                      "QUESTION: Who could have initiated the transfer?",
                 fg=GREEN, bg=BG, wraplength=450, justify="left").pack(pady=10)

        options_frame = tk.Frame(puzzle_window, bg=BG)
        options_frame.pack(pady=10)

        feedback = tk.Label(puzzle_window, text="", bg=BG)
        feedback.pack()

        def check_answer(choice):
            global accuracy_score, current_suspicion
            if choice == "IT Employee":
                feedback.config(text="✅ CORRECT: Only IT Employee had direct workstation access", fg=GREEN)
                accuracy_score += 10
                puzzle_window.after(2000, puzzle_window.destroy)
                disable_puzzle("logic")
            else:
                feedback.config(text="❌ INCORRECT: Check access privileges again", fg=RED)
                current_suspicion += 10
                accuracy_score -= 15
            suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                                 fg=GREEN if current_suspicion < 50 else WARNING)

        tk.Button(options_frame, text="IT Manager", width=15,
                  command=lambda: check_answer("IT Manager")).pack(side="left", padx=5)
        tk.Button(options_frame, text="IT Employee", width=15,
                  command=lambda: check_answer("IT Employee")).pack(side="left", padx=5)
        tk.Button(options_frame, text="Security Guard", width=15,
                  command=lambda: check_answer("Security Guard")).pack(side="left", padx=5)
        tk.Button(options_frame, text="Bank Manager", width=15,
                  command=lambda: check_answer("Bank Manager")).pack(side="left", padx=5)

    def pattern_recognition_puzzle():
        puzzle_window = tk.Toplevel(analysis)
        puzzle_window.title("CIS // Pattern Recognition")
        puzzle_window.configure(bg=BG)
        puzzle_window.geometry("500x400")

        tk.Label(puzzle_window, text="PATTERN RECOGNITION: LOGIN SEQUENCE",
                 font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack(pady=10)

        tk.Label(puzzle_window,
                 text="Login attempts show this pattern:\n"
                      "23:45:12 - Failed (wrong password)\n"
                      "23:46:33 - Failed (wrong password)\n"
                      "23:47:45 - Failed (wrong password)\n"
                      "23:48:58 - Success\n\n"
                      "The successful login used a password that was NOT tried before.\n"
                      "QUESTION: What type of attack pattern is this?",
                 fg=GREEN, bg=BG, wraplength=450, justify="left").pack(pady=10)

        options_frame = tk.Frame(puzzle_window, bg=BG)
        options_frame.pack(pady=10)

        feedback = tk.Label(puzzle_window, text="", bg=BG)
        feedback.pack()

        def check_answer(choice):
            global accuracy_score, current_suspicion
            if choice == "Dictionary Attack":
                feedback.config(text="✅ CORRECT: Systematic password testing", fg=GREEN)
                accuracy_score += 10
                puzzle_window.after(2000, puzzle_window.destroy)
                disable_puzzle("pattern")
            else:
                feedback.config(text="❌ INCORRECT: Analyze the timing and method", fg=RED)
                current_suspicion += 10
                accuracy_score -= 15
            suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                                 fg=GREEN if current_suspicion < 50 else WARNING)

        tk.Button(options_frame, text="Brute Force", width=15,
                  command=lambda: check_answer("Brute Force")).pack(side="left", padx=5)
        tk.Button(options_frame, text="Dictionary Attack", width=15,
                  command=lambda: check_answer("Dictionary Attack")).pack(side="left", padx=5)
        tk.Button(options_frame, text="Social Engineering", width=15,
                  command=lambda: check_answer("Social Engineering")).pack(side="left", padx=5)
        tk.Button(options_frame, text="Keylogger", width=15,
                  command=lambda: check_answer("Keylogger")).pack(side="left", padx=5)

    def timeline_reconstruction():
        puzzle_window = tk.Toplevel(analysis)
        puzzle_window.title("CIS // Timeline Reconstruction")
        puzzle_window.configure(bg=BG)
        puzzle_window.geometry("600x500")

        tk.Label(puzzle_window, text="TIMELINE RECONSTRUCTION",
                 font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack(pady=10)

        tk.Label(puzzle_window,
                 text="Reconstruct the sequence of events. Drag events to correct chronological order:",
                 fg=GREEN, bg=BG, wraplength=550).pack(pady=10)

        # Timeline puzzle - simplified for Tkinter
        events = [
            "23:35 - IT Manager enters server room",
            "23:45 - Security Guard leaves parking lot",
            "23:50 - IT Manager exits server room",
            "23:55 - Network traffic spike begins",
            "23:58:30 - 15-second camera blackout",
            "23:58:42 - Money transfer executed",
            "00:15 - Security Guard returns",
            "00:20 - System logs show cleanup"
        ]

        # For simplicity, present as multiple choice
        tk.Label(puzzle_window,
                 text="What happened FIRST in the sequence?",
                 fg=WARNING, bg=BG).pack(pady=5)

        options_frame = tk.Frame(puzzle_window, bg=BG)
        options_frame.pack(pady=10)

        feedback = tk.Label(puzzle_window, text="", bg=BG)
        feedback.pack()

        def check_answer(choice):
            global accuracy_score, current_suspicion
            if choice == "23:35 - IT Manager enters server room":
                feedback.config(text="✅ CORRECT: Timeline established", fg=GREEN)
                accuracy_score += 15
                puzzle_window.after(2000, puzzle_window.destroy)
                disable_puzzle("timeline")
            else:
                feedback.config(text="❌ INCORRECT: Check the evidence timestamps", fg=RED)
                current_suspicion += 15
                accuracy_score -= 20
            suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                                 fg=GREEN if current_suspicion < 50 else WARNING)

        for event in events:
            tk.Button(options_frame, text=event, width=40, height=1,
                      command=lambda e=event: check_answer(e)).pack(pady=2)

    puzzle_buttons["logic"] = tk.Button(analysis_content, text="Logical Reasoning Puzzle",
                                       width=25, height=2, bg="#020617", fg=GREEN,
                                       activebackground=MAGENTA, command=logical_reasoning_puzzle)
    puzzle_buttons["logic"].pack(pady=4)

    puzzle_buttons["pattern"] = tk.Button(analysis_content, text="Pattern Recognition",
                                         width=25, height=2, bg="#020617", fg=GREEN,
                                         activebackground=MAGENTA, command=pattern_recognition_puzzle)
    puzzle_buttons["pattern"].pack(pady=4)

    puzzle_buttons["timeline"] = tk.Button(analysis_content, text="Timeline Reconstruction",
                                          width=25, height=2, bg="#020617", fg=GREEN,
                                          activebackground=MAGENTA, command=timeline_reconstruction)
    puzzle_buttons["timeline"].pack(pady=4)

    # Suspect Profiles (Right Panel)
    profiles_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    profiles_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    tk.Label(profiles_frame, text="SUSPECT PROFILES",
             font=("Consolas", 14, "bold"), bg="#081327", fg=MAGENTA).pack(pady=10)

    profiles_content = tk.Frame(profiles_frame, bg="#081327")
    profiles_content.pack(fill="both", expand=True, padx=10, pady=5)

    profile_buttons = {}

    def show_profile(suspect_key):
        profile_win = tk.Toplevel(analysis)
        profile_win.title(f"CIS // {suspects[suspect_key]['name']}")
        profile_win.configure(bg=BG)
        profile_win.geometry("400x300")

        tk.Label(profile_win, text=f"SUSPECT PROFILE: {suspects[suspect_key]['name']}",
                 font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack(pady=10)

        info_text = f"""
Name: {suspects[suspect_key]['name']}
Access Level: {suspects[suspect_key]['access']}
Alibi: {suspects[suspect_key]['alibi']}
Current Suspicion: {suspects[suspect_key]['suspicion']}%
"""

        tk.Label(profile_win, text=info_text, fg=GREEN, bg=BG, justify="left").pack(pady=10)

        # Hidden hint based on evidence
        hint = ""
        if suspect_key == "IT_Employee":
            hint = "HINT: Workstation matches transfer IP. Coffee cup suggests late night work."
        elif suspect_key == "IT_Manager":
            hint = "HINT: Server room access matches timeline. Override privileges noted."
        elif suspect_key == "Security_Guard":
            hint = "HINT: Parking lot departure creates access window. No technical skills."
        elif suspect_key == "Bank_Manager":
            hint = "HINT: Meeting alibi unverified. Transfer amount suggests insider knowledge."

        tk.Label(profile_win, text=hint, fg=WARNING, bg=BG, wraplength=350).pack(pady=10)

    for suspect_key, suspect_data in suspects.items():
        profile_buttons[suspect_key] = tk.Button(profiles_content,
                                                text=f"{suspect_data['name']} ({suspect_data['access']})",
                                                width=30, height=2, bg="#020617", fg=GREEN,
                                                activebackground=MAGENTA,
                                                command=lambda k=suspect_key: show_profile(k))
        profile_buttons[suspect_key].pack(pady=3)

    # Proceed to interrogation
    def proceed_to_interrogation():
        solved_puzzles = sum(1 for btn in puzzle_buttons.values() if btn.cget("state") == "disabled")
        if solved_puzzles >= 2:
            show_story(analysis, [
                "Analysis complete. Suspicion levels are rising.",
                "Time to interrogate the suspects directly.",
                "Choose your questions carefully - lies will be revealed through contradictions.",
                "Each wrong accusation increases suspicion and may alert the culprit."
            ], suspect_interrogation)
        else:
            global current_suspicion
            current_suspicion += 20
            suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                                 fg=GREEN if current_suspicion < 50 else WARNING)

    tk.Button(profiles_content, text="▶ BEGIN INTERROGATION",
              width=30, height=2, bg="#020617", fg=CYAN,
              command=proceed_to_interrogation).pack(pady=15)

    tk.Label(profiles_content, text="Solve at least 2 puzzles before proceeding",
             fg=GREEN, bg="#081327", font=("Consolas", 9, "italic")).pack(pady=5)


# ---------------- SUSPECT INTERROGATION ----------------
def suspect_interrogation():
    interrogation = tk.Toplevel()
    interrogation.title("CIS // Suspect Interrogation")
    interrogation.configure(bg=BG)
    interrogation.geometry("700x550")

    # Header
    header_frame = tk.Frame(interrogation, bg="#081327", height=50)
    header_frame.pack(fill="x", pady=(0, 10))
    header_frame.pack_propagate(False)

    tk.Label(header_frame, text="INTERROGATION ROOM",
             font=("Consolas", 16, "bold"), fg=CYAN, bg="#081327").pack(side="left", padx=20)

    suspicion_label = tk.Label(header_frame, text=f"SUSPICION: {current_suspicion}%",
                               fg=GREEN if current_suspicion < 50 else WARNING, bg="#081327",
                               font=("Consolas", 12, "bold"))
    suspicion_label.pack(side="right", padx=20)

    # Main content
    content_frame = tk.Frame(interrogation, bg=BG)
    content_frame.pack(fill="both", expand=True, padx=20, pady=10)

    # Question Panel (Left)
    question_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    question_frame.pack(side="left", fill="both", expand=True, padx=(0, 10))

    tk.Label(question_frame, text="INTERROGATION QUESTIONS",
             font=("Consolas", 14, "bold"), bg="#081327", fg=GREEN).pack(pady=10)

    question_content = tk.Frame(question_frame, bg="#081327")
    question_content.pack(fill="both", expand=True, padx=10, pady=5)

    # Response Panel (Right)
    response_frame = tk.Frame(content_frame, bg="#081327", bd=2, relief="sunken")
    response_frame.pack(side="right", fill="both", expand=True, padx=(10, 0))

    tk.Label(response_frame, text="SUSPECT RESPONSES",
             font=("Consolas", 14, "bold"), bg="#081327", fg=MAGENTA).pack(pady=10)

    response_text = tk.Text(response_frame, bg="#020617", fg=CYAN,
                           font=("Consolas", 10), bd=0, wrap="word",
                           padx=10, pady=10, state=tk.DISABLED)
    response_text.pack(fill="both", expand=True, padx=10, pady=10)

    current_suspect = None
    questions_asked = 0

    def select_suspect(suspect_key):
        nonlocal current_suspect
        current_suspect = suspect_key
        response_text.config(state=tk.NORMAL)
        response_text.delete(1.0, tk.END)
        response_text.insert(tk.END, f"Interrogating: {suspects[suspect_key]['name']}\n\n")
        response_text.config(state=tk.DISABLED)

        # Enable question buttons
        for btn in question_buttons.values():
            btn.config(state=tk.NORMAL)

    def ask_question(question_type):
        nonlocal questions_asked
        if not current_suspect:
            return

        questions_asked += 1
        global current_suspicion, accuracy_score

        responses = {
            "IT_Manager": {
                "whereabouts": "I was in the server room checking backups until 23:50.",
                "access": "I have full system access for maintenance purposes.",
                "timeline": "I entered at 23:35 and left at 23:50. The transfer happened after I left.",
                "motive": "I've worked here for 15 years. This breach hurts my reputation too."
            },
            "IT_Employee": {
                "whereabouts": "I was working late on system updates from my workstation.",
                "access": "I have standard IT access, but not override privileges.",
                "timeline": "I logged in at 22:30 and was working until after midnight.",
                "motive": "I needed the money for my sister's medical treatment."
            },
            "Security_Guard": {
                "whereabouts": "I was on patrol. Left the parking lot at 23:45 for rounds.",
                "access": "I have no computer access. I just monitor cameras.",
                "timeline": "I returned at 00:20. The transfer was already done by then.",
                "motive": "I'm just a security guard. I don't know anything about computers."
            },
            "Bank_Manager": {
                "whereabouts": "I was in a client meeting that ran late until midnight.",
                "access": "I have read-only access for compliance monitoring.",
                "timeline": "I was in the conference room the entire evening.",
                "motive": "This breach could ruin the bank's reputation. I would never do this."
            }
        }

        response = responses[current_suspect][question_type]

        # Lie detection logic
        is_lie = False
        if current_suspect == "IT_Employee" and question_type == "motive":
            is_lie = True  # Contradicts evidence of premeditation
        elif current_suspect == "Security_Guard" and question_type == "whereabouts":
            is_lie = True  # Camera shows different timing
        elif current_suspect == "Bank_Manager" and question_type == "timeline":
            is_lie = True  # Meeting room was empty

        response_text.config(state=tk.NORMAL)
        response_text.insert(tk.END, f"Q: {question_type.title()}\nA: {response}\n")

        if is_lie:
            response_text.insert(tk.END, "⚠️ LIE DETECTED: Response contradicts evidence\n")
            suspects[current_suspect]["suspicion"] += 25
            current_suspicion += 10
            accuracy_score += 5
        else:
            response_text.insert(tk.END, "✓ Response appears truthful\n")
            accuracy_score += 2

        response_text.config(state=tk.DISABLED)
        response_text.see(tk.END)

        suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                             fg=GREEN if current_suspicion < 50 else WARNING)

        # Random event trigger
        if random.random() < 0.3 and questions_asked > 3:
            trigger_random_event()

        # Disable question after asking to prevent spam
        question_buttons[question_type].config(state=tk.DISABLED)

    def trigger_random_event():
        event = random.choice(random_events)
        if event == "new_clue":
            response_text.config(state=tk.NORMAL)
            response_text.insert(tk.END, "\n🚨 NEW CLUE: Suspicious email found in IT Employee's drafts\n")
            response_text.config(state=tk.DISABLED)
        elif event == "misleading_info":
            response_text.config(state=tk.NORMAL)
            response_text.insert(tk.END, "\n⚠️ MISLEADING INFO: False trail points to Security Guard\n")
            response_text.config(state=tk.DISABLED)
            current_suspicion += 5
        elif event == "time_bonus":
            response_text.config(state=tk.NORMAL)
            response_text.insert(tk.END, "\n⏰ TIME BONUS: Additional 30 seconds granted\n")
            response_text.config(state=tk.DISABLED)

    # Suspect selection
    suspect_frame = tk.Frame(question_content, bg="#081327")
    suspect_frame.pack(fill="x", pady=(0, 10))

    tk.Label(suspect_frame, text="SELECT SUSPECT:", fg=GREEN, bg="#081327").pack(side="left")

    for suspect_key in suspects:
        tk.Button(suspect_frame, text=suspects[suspect_key]['name'].split()[0],
                  width=8, bg="#020617", fg=GREEN,
                  command=lambda k=suspect_key: select_suspect(k)).pack(side="left", padx=2)

    # Question buttons
    question_buttons = {}

    question_buttons["whereabouts"] = tk.Button(question_content, text="Where were you during the breach?",
                                               width=30, height=2, bg="#020617", fg=GREEN,
                                               activebackground=MAGENTA, state=tk.DISABLED,
                                               command=lambda: ask_question("whereabouts"))
    question_buttons["whereabouts"].pack(pady=3)

    question_buttons["access"] = tk.Button(question_content, text="What system access do you have?",
                                          width=30, height=2, bg="#020617", fg=GREEN,
                                          activebackground=MAGENTA, state=tk.DISABLED,
                                          command=lambda: ask_question("access"))
    question_buttons["access"].pack(pady=3)

    question_buttons["timeline"] = tk.Button(question_content, text="Walk me through your timeline",
                                            width=30, height=2, bg="#020617", fg=GREEN,
                                            activebackground=MAGENTA, state=tk.DISABLED,
                                            command=lambda: ask_question("timeline"))
    question_buttons["timeline"].pack(pady=3)

    question_buttons["motive"] = tk.Button(question_content, text="Do you have any motive?",
                                          width=30, height=2, bg="#020617", fg=GREEN,
                                          activebackground=MAGENTA, state=tk.DISABLED,
                                          command=lambda: ask_question("motive"))
    question_buttons["motive"].pack(pady=3)

    # Proceed to final decision
    def proceed_to_final():
        if questions_asked >= 4:
            show_story(interrogation, [
                "Interrogation complete. Evidence is mounting.",
                "It's time to make your final accusation.",
                "Choose wisely - the wrong suspect will escape justice.",
                "The bank's future depends on your decision."
            ], final_accusation)
        else:
            current_suspicion += 15
            suspicion_label.config(text=f"SUSPICION: {current_suspicion}%",
                                 fg=GREEN if current_suspicion < 50 else WARNING)

    tk.Button(question_content, text="▶ MAKE FINAL ACCUSATION",
              width=30, height=2, bg="#020617", fg=CYAN,
              command=proceed_to_final).pack(pady=15)

    tk.Label(question_content, text="Ask at least 4 questions before accusing",
             fg=GREEN, bg="#081327", font=("Consolas", 9, "italic")).pack(pady=5)


# ---------------- FINAL ACCUSATION ----------------
def final_accusation():
    accusation = tk.Toplevel()
    accusation.title("CIS // Final Accusation")
    accusation.configure(bg=BG)
    accusation.geometry("600x450")

    tk.Label(accusation, text="FINAL ACCUSATION",
             font=("Consolas", 18, "bold"), fg=CYAN, bg=BG).pack(pady=15)

    tk.Label(accusation, text="Based on all evidence collected and analysis performed,\n"
                              "who do you believe committed the bank breach?",
             fg=GREEN, bg=BG, wraplength=550).pack(pady=10)

    tk.Label(accusation, text=f"Current Suspicion Level: {current_suspicion}%\n"
                              f"Investigation Accuracy: {accuracy_score}%",
             fg=WARNING if current_suspicion > 50 else GREEN, bg=BG).pack(pady=10)

    button_frame = tk.Frame(accusation, bg=BG)
    button_frame.pack(pady=20)

    def make_accusation(choice):
        accusation.destroy()

        # Determine ending based on choice and game state
        if choice == "IT_Employee":
            if accuracy_score >= 80 and current_suspicion <= 60:
                ending_type = "perfect"
            elif accuracy_score >= 60:
                ending_type = "solved"
            else:
                ending_type = "partial"
        else:
            ending_type = "failed"

        show_final_summary(ending_type, choice)

    for suspect_key, suspect_data in suspects.items():
        tk.Button(button_frame, text=f"{suspect_data['name']} ({suspect_data['access']})",
                  width=25, height=2, bg="#020617", fg=GREEN,
                  activebackground=MAGENTA,
                  command=lambda c=suspect_key: make_accusation(c)).pack(pady=3)


# ---------------- FINAL SUMMARY ----------------
def show_final_summary(ending_type, accused):
    summary = tk.Toplevel()
    summary.title("CIS // Case Resolution")
    summary.configure(bg=BG)
    summary.geometry("650x500")

    if ending_type == "perfect":
        title = "🎉 CASE SOLVED - PERFECT INVESTIGATION"
        color = GREEN
        score_bonus = 100
    elif ending_type == "solved":
        title = "✅ CASE SOLVED - SUSPECT APPREHENDED"
        color = CYAN
        score_bonus = 75
    elif ending_type == "partial":
        title = "⚠️ PARTIAL RESOLUTION - EVIDENCE RECOVERED"
        color = WARNING
        score_bonus = 50
    else:
        title = "❌ CASE FAILED - SUSPECT ESCAPED"
        color = RED
        score_bonus = 0

    tk.Label(summary, text=title,
             font=("Consolas", 16, "bold"), fg=color, bg=BG).pack(pady=15)

    # Summary stats
    stats_frame = tk.Frame(summary, bg="#081327", bd=2, relief="sunken")
    stats_frame.pack(fill="both", expand=True, padx=20, pady=10)

    tk.Label(stats_frame, text="INVESTIGATION SUMMARY",
             font=("Consolas", 14, "bold"), bg="#081327", fg=GREEN).pack(pady=10)

    summary_text = f"""
Final Suspicion Level: {current_suspicion}%
Investigation Accuracy: {accuracy_score}%
Evidence Collected: {len(evidence_collected)} pieces
Suspect Accused: {suspects[accused]['name']}

DECISIONS MADE:
• Evidence Collection: {'Thorough' if len(evidence_collected) >= 8 else 'Incomplete'}
• Puzzle Solving: {'Excellent' if accuracy_score >= 80 else 'Adequate' if accuracy_score >= 60 else 'Poor'}
• Interrogation: {'Effective' if current_suspicion <= 60 else 'Raised Suspicion'}

OUTCOME: {ending_type.upper().replace('_', ' ')}
"""

    tk.Label(stats_frame, text=summary_text, fg=CYAN, bg="#081327",
             justify="left", font=("Consolas", 11)).pack(pady=10)

    # Closing message
    if ending_type == "perfect":
        message = "Outstanding work! The breach was contained and the culprit apprehended."
    elif ending_type == "solved":
        message = "Good work. The suspect was caught, though some evidence was missed."
    elif ending_type == "partial":
        message = "Partial success. Evidence recovered but suspect remains at large."
    else:
        message = "Investigation failed. The suspect escaped and may strike again."

    tk.Label(summary, text=message, fg=color, bg=BG, wraplength=600).pack(pady=10)

    tk.Button(summary, text="CLOSE CASE", bg="#020617", fg=CYAN,
              command=summary.destroy).pack(pady=10)
    tk.Button(f, text="Customer", command=lambda: result("Customer")).pack(pady=5)