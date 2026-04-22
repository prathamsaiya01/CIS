import tkinter as tk
import threading
import time
import random

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"
MAGENTA = "#ff5fe3"
WARNING = "#ff9f00"
RED = "#ff4444"

# Global game state
evidence_collected = []
suspects = {
    "System Admin": {"profile": "Senior IT staff, 10+ years experience, access to all systems", "hints": ["Admin logs show unusual activity", "Has override privileges"]},
    "Intern": {"profile": "New hire, limited access, joined 2 months ago", "hints": ["No admin privileges", "Recent hire with basic training"]},
    "External Hacker": {"profile": "Unknown entity, no internal access", "hints": ["Firewall shows no breach", "All activity internal"]},
    "Data Analyst": {"profile": "Mid-level employee, database access, 5 years tenure", "hints": ["SQL injection knowledge", "Access to sensitive data"]}
}
timeline_events = [
    {"time": "00:45 AM", "event": "System Admin logged in remotely"},
    {"time": "01:07 AM", "event": "SQL injection attempt detected"},
    {"time": "01:15 AM", "event": "Encrypted file created"},
    {"time": "01:20 AM", "event": "Data export initiated"},
    {"time": "01:30 AM", "event": "Leak discovered"}
]
accuracy_score = 100
suspect_suspicion = {"System Admin": 0, "Intern": 0, "External Hacker": 0, "Data Analyst": 0}

# ---------------- UTILITY FUNCTIONS ----------------
def animate_text(label, text, delay=0.05):
    """Animate text typing effect"""
    label.config(text="")
    for char in text:
        label.config(text=label.cget("text") + char)
        time.sleep(delay)
        label.update()

def update_suspicion(suspect, change):
    """Update suspicion level for a suspect"""
    global suspect_suspicion
    suspect_suspicion[suspect] = max(0, min(100, suspect_suspicion[suspect] + change))

def random_event():
    """Generate random events during investigation"""
    events = [
        "🔍 New evidence discovered: Unusual login pattern detected",
        "⚠️ Time pressure: Security team closing in...",
        "💡 Hint: Check the timeline carefully",
        "🚨 Alert: System logs show additional anomalies"
    ]
    return random.choice(events)

# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 3 - TechCorp Data Leak")
    story.configure(bg=BG)
    story.geometry("600x400")

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
            threading.Thread(target=animate_text, args=(label, text_list[index[0]])).start()
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
        command=next_text
    ).pack(pady=10)

    next_text()

# ---------------- ENTRY ----------------
def open_case3(prev):
    story_text = [
        "🚨 URGENT CASE ALERT - TechCorp Data Leak",
        "Time: 01:30 AM - TechCorp Headquarters",
        "INCIDENT: Massive data breach detected",
        "• 500GB of sensitive customer data leaked",
        "• No external firewall breach detected",
        "• Internal network activity shows admin access",
        "• SQL injection traces found in logs",
        "INVESTIGATION STATUS: ACTIVE",
        "Your mission: Identify the insider threat",
        "Time is critical - security protocols activating..."
    ]

    show_story(prev, story_text, crime_scene_analysis)

# ---------------- CRIME SCENE ANALYSIS ----------------
def crime_scene_analysis():
    scene = tk.Toplevel()
    scene.title("CIS // Crime Scene Analysis")
    scene.configure(bg=BG)
    scene.geometry("700x500")

    # Header
    tk.Label(scene, text="🔍 CRIME SCENE ANALYSIS REPORT",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Evidence Panel
    evidence_frame = tk.Frame(scene, bg=BG)
    evidence_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(evidence_frame, text="📋 EVIDENCE COLLECTED",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    evidence_list = tk.Listbox(evidence_frame, bg="black", fg=GREEN, selectbackground=CYAN,
                              font=("Consolas", 10), height=15, width=40)
    evidence_list.pack(pady=10)

    # Actions Panel
    actions_frame = tk.Frame(scene, bg=BG)
    actions_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    tk.Label(actions_frame, text="🎯 INVESTIGATION ACTIONS",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    def collect_evidence(item):
        if item not in evidence_collected:
            evidence_collected.append(item)
            evidence_list.insert(tk.END, f"✓ {item}")
            update_suspicion("System Admin", 10)  # Example suspicion update

    tk.Button(actions_frame, text="📊 Analyze Server Logs",
              command=lambda: collect_evidence("Server logs show internal admin access")).pack(pady=5)
    tk.Button(actions_frame, text="🔐 Check Access Patterns",
              command=lambda: collect_evidence("Unusual login from admin account")).pack(pady=5)
    tk.Button(actions_frame, text="💾 Examine Data Export",
              command=lambda: collect_evidence("500GB data exported to unknown location")).pack(pady=5)
    tk.Button(actions_frame, text="🕐 Review Timeline",
              command=lambda: collect_evidence("Timeline shows coordinated attack")).pack(pady=5)

    tk.Button(scene, text="▶ PROCEED TO PUZZLES",
              bg="#020617", fg=GREEN, command=lambda: puzzle_challenge(scene)).pack(pady=20)

# ---------------- PUZZLE CHALLENGE ----------------
def puzzle_challenge(prev):
    prev.destroy()

    puzzle = tk.Toplevel()
    puzzle.title("CIS // Logic Puzzles")
    puzzle.configure(bg=BG)
    puzzle.geometry("600x500")

    tk.Label(puzzle, text="🧩 LOGIC PUZZLE CHALLENGE",
             font=("Consolas", 14, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Puzzle 1: Pattern Recognition
    tk.Label(puzzle, text="PATTERN RECOGNITION:",
             font=("Consolas", 12), fg=CYAN, bg=BG).pack(pady=5)
    tk.Label(puzzle, text="Login attempts: 3 failed, 1 success, 2 failed, 1 success...",
             fg=GREEN, bg=BG).pack()
    tk.Label(puzzle, text="What's the next pattern? (success/fail)",
             fg=GREEN, bg=BG).pack()

    pattern_entry = tk.Entry(puzzle, bg="black", fg=GREEN, insertbackground=GREEN)
    pattern_entry.pack()

    # Puzzle 2: Logical Reasoning
    tk.Label(puzzle, text="LOGICAL REASONING:",
             font=("Consolas", 12), fg=CYAN, bg=BG).pack(pady=5)
    tk.Label(puzzle, text="If Admin has access but Intern doesn't, and Data Analyst",
             fg=GREEN, bg=BG).pack()
    tk.Label(puzzle, text="has partial access, who could perform SQL injection?",
             fg=GREEN, bg=BG).pack()

    logic_entry = tk.Entry(puzzle, bg="black", fg=GREEN, insertbackground=GREEN)
    logic_entry.pack()

    result_label = tk.Label(puzzle, text="", bg=BG, font=("Consolas", 10))
    result_label.pack(pady=10)

    def check_puzzles():
        global accuracy_score
        correct = 0

        if pattern_entry.get().lower() in ["2 failed", "fail"]:
            correct += 1
        else:
            accuracy_score -= 10

        if logic_entry.get().lower() in ["admin", "system admin", "data analyst"]:
            correct += 1
        else:
            accuracy_score -= 10

        if correct == 2:
            result_label.config(text="✅ EXCELLENT ANALYSIS!", fg=GREEN)
            tk.Button(puzzle, text="▶ TIMELINE RECONSTRUCTION",
                      command=lambda: timeline_puzzle(puzzle)).pack(pady=10)
        elif correct == 1:
            result_label.config(text="⚠️ PARTIALLY CORRECT - Proceed with caution", fg=WARNING)
            tk.Button(puzzle, text="▶ TIMELINE RECONSTRUCTION",
                      command=lambda: timeline_puzzle(puzzle)).pack(pady=10)
        else:
            result_label.config(text="❌ ANALYSIS FAILED - Accuracy decreased", fg=RED)
            accuracy_score -= 20
            tk.Button(puzzle, text="▶ RETRY ANALYSIS",
                      command=lambda: puzzle_challenge(puzzle)).pack(pady=10)

    tk.Button(puzzle, text="SUBMIT ANALYSIS", command=check_puzzles).pack(pady=10)

# ---------------- TIMELINE RECONSTRUCTION ----------------
def timeline_puzzle(prev):
    prev.destroy()

    timeline_win = tk.Toplevel()
    timeline_win.title("CIS // Timeline Reconstruction")
    timeline_win.configure(bg=BG)
    timeline_win.geometry("700x500")

    tk.Label(timeline_win, text="⏰ TIMELINE RECONSTRUCTION",
             font=("Consolas", 14, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Display timeline
    timeline_text = tk.Text(timeline_win, bg="black", fg=GREEN, font=("Consolas", 10),
                           height=10, width=60)
    timeline_text.pack(pady=10)

    for event in timeline_events:
        timeline_text.insert(tk.END, f"{event['time']}: {event['event']}\n")

    timeline_text.config(state=tk.DISABLED)

    tk.Label(timeline_win, text="RECONSTRUCT THE SEQUENCE:",
             font=("Consolas", 12), fg=CYAN, bg=BG).pack(pady=5)
    tk.Label(timeline_win, text="What happened first? (Enter time)",
             fg=GREEN, bg=BG).pack()

    time_entry = tk.Entry(timeline_win, bg="black", fg=GREEN, insertbackground=GREEN)
    time_entry.pack()

    result_label = tk.Label(timeline_win, text="", bg=BG)
    result_label.pack()

    def check_timeline():
        global accuracy_score
        if time_entry.get() in ["00:45 AM", "00:45"]:
            result_label.config(text="✅ CORRECT SEQUENCE!", fg=GREEN)
            tk.Button(timeline_win, text="▶ SUSPECT INTERROGATION",
                      command=lambda: interrogation_phase(timeline_win)).pack(pady=10)
        else:
            result_label.config(text="❌ INCORRECT - Try again", fg=RED)
            accuracy_score -= 15

    tk.Button(timeline_win, text="SUBMIT", command=check_timeline).pack(pady=10)

# ---------------- INTERROGATION PHASE ----------------
def interrogation_phase(prev):
    prev.destroy()

    interrog = tk.Toplevel()
    interrog.title("CIS // Suspect Interrogation")
    interrog.configure(bg=BG)
    interrog.geometry("800x600")

    tk.Label(interrog, text="🕵️ SUSPECT INTERROGATION ROOM",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Suspect profiles
    profile_frame = tk.Frame(interrog, bg=BG)
    profile_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(profile_frame, text="👤 SUSPECT PROFILES",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    suspect_listbox = tk.Listbox(profile_frame, bg="black", fg=GREEN, selectbackground=CYAN,
                                font=("Consolas", 10), height=10, width=40)
    suspect_listbox.pack(pady=10)

    for suspect, info in suspects.items():
        suspect_listbox.insert(tk.END, f"{suspect}: {info['profile']}")

    # Interrogation panel
    question_frame = tk.Frame(interrog, bg=BG)
    question_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    tk.Label(question_frame, text="❓ INTERROGATION QUESTIONS",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    questions = [
        "Where were you at 01:07 AM?",
        "Do you have SQL injection knowledge?",
        "Have you accessed admin systems recently?",
        "Can you explain the unusual login pattern?"
    ]

    question_var = tk.StringVar()
    question_var.set(questions[0])

    for q in questions:
        tk.Radiobutton(question_frame, text=q, variable=question_var, value=q,
                      bg=BG, fg=GREEN, selectcolor=BG, activebackground=BG,
                      activeforeground=CYAN).pack(anchor=tk.W)

    result_text = tk.Text(question_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                         height=8, width=50)
    result_text.pack(pady=10)

    def ask_question():
        global accuracy_score
        suspect = suspect_listbox.get(suspect_listbox.curselection()) if suspect_listbox.curselection() else None
        if not suspect:
            result_text.insert(tk.END, "Select a suspect first!\n")
            return

        suspect_name = suspect.split(":")[0]
        question = question_var.get()

        # Simulate lie detection (randomized for gameplay)
        is_lying = random.choice([True, False])
        if is_lying:
            response = f"⚠️ LIE DETECTED: {suspect_name}'s response seems inconsistent"
            update_suspicion(suspect_name, 20)
            accuracy_score -= 5
        else:
            response = f"✅ TRUTHFUL: {suspect_name} answered consistently"
            update_suspicion(suspect_name, -10)

        result_text.insert(tk.END, f"Question: {question}\n{response}\n\n")

        # Random event
        if random.random() < 0.3:
            event = random_event()
            result_text.insert(tk.END, f"RANDOM EVENT: {event}\n\n")

    tk.Button(question_frame, text="ASK QUESTION", command=ask_question).pack(pady=5)
    tk.Button(interrog, text="▶ MAKE FINAL ACCUSATION",
              command=lambda: final_accusation(interrog)).pack(pady=20)

# ---------------- FINAL ACCUSATION ----------------
def final_accusation(prev):
    prev.destroy()

    final = tk.Toplevel()
    final.title("CIS // Final Accusation")
    final.configure(bg=BG)
    final.geometry("600x500")

    tk.Label(final, text="🎯 FINAL ACCUSATION",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Display suspicion levels
    suspicion_frame = tk.Frame(final, bg=BG)
    suspicion_frame.pack(pady=20)

    tk.Label(suspicion_frame, text="SUSPECT SUSPICION LEVELS:",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    for suspect, level in suspect_suspicion.items():
        color = GREEN if level < 30 else WARNING if level < 70 else RED
        tk.Label(suspicion_frame, text=f"{suspect}: {level}%",
                 fg=color, bg=BG, font=("Consolas", 10)).pack()

    tk.Label(final, text=f"INVESTIGATION ACCURACY: {accuracy_score}%",
             fg=GREEN if accuracy_score > 70 else WARNING if accuracy_score > 40 else RED,
             bg=BG, font=("Consolas", 12)).pack(pady=10)

    tk.Label(final, text="WHO IS THE CULPRIT?",
             font=("Consolas", 14), fg=CYAN, bg=BG).pack(pady=10)

    culprit_var = tk.StringVar()

    for suspect in suspects.keys():
        tk.Radiobutton(final, text=suspect, variable=culprit_var, value=suspect,
                      bg=BG, fg=GREEN, selectcolor=BG, activebackground=BG,
                      activeforeground=CYAN).pack()

    def make_accusation():
        culprit = culprit_var.get()
        if not culprit:
            return

        final.destroy()

        # Determine ending based on accuracy and suspicion
        max_suspicion = max(suspect_suspicion.values())
        correct_culprit = "System Admin"  # The actual culprit

        if culprit == correct_culprit and accuracy_score >= 80 and suspect_suspicion[culprit] >= 60:
            ending = [
                "💥 PERFECT INVESTIGATION!",
                "Evidence analysis was flawless",
                "Timeline reconstruction accurate",
                "Lie detection confirmed the culprit",
                f"Suspect {culprit} arrested successfully",
                "Data breach contained - company secure",
                "🎉 CASE SOLVED WITH EXCELLENCE"
            ]
        elif culprit == correct_culprit and accuracy_score >= 60:
            ending = [
                "✅ CASE SOLVED",
                "The insider threat has been identified",
                f"{culprit} will face prosecution",
                "Some evidence was missed, but the core facts align",
                "Company data partially recovered",
                "⚠️ PARTIAL SUCCESS"
            ]
        elif accuracy_score >= 50:
            ending = [
                "⚠️ CASE PARTIALLY SOLVED",
                "Wrong suspect accused, but investigation revealed issues",
                "Internal security protocols strengthened",
                "Data breach contained, but culprit escaped",
                "Further investigation needed",
                "📋 INCONCLUSIVE RESULT"
            ]
        else:
            ending = [
                "❌ INVESTIGATION FAILED",
                "Wrong accusations led to chaos",
                "Culprit remains at large",
                "Data breach consequences severe",
                "Company reputation damaged",
                "🚨 MISSION CRITICAL FAILURE"
            ]

        show_story(final, ending, lambda: None)

    tk.Button(final, text="MAKE ACCUSATION", command=make_accusation).pack(pady=20)