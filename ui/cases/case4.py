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

# Global game state - HIGHEST DIFFICULTY SETTINGS
evidence_collected = []
decisions_made = []
suspects = {
    "Business Rival": {
        "profile": "CEO of competing tech firm, history of aggressive takeovers, recently lost major contract",
        "motives": ["Corporate sabotage", "Market elimination"],
        "alibi": "Board meeting in another city",
        "hints": ["Financial records show desperation", "Recent threats made", "Access to kidnapping network"]
    },
    "Disgruntled Employee": {
        "profile": "Former executive fired 6 months ago, technical expert with security clearance",
        "motives": ["Revenge", "Blackmail attempt"],
        "alibi": "Unverified - claims personal emergency",
        "hints": ["Still has company access codes", "Knows victim's routines", "Recent suspicious communications"]
    },
    "Foreign Agent": {
        "profile": "Diplomatic cover, suspected intelligence operative, recently arrived in country",
        "motives": ["Industrial espionage", "State-sponsored kidnapping"],
        "alibi": "Official diplomatic function",
        "hints": ["Encrypted communications intercepted", "Foreign bank transfers", "Advanced surveillance equipment"]
    },
    "Family Member": {
        "profile": "Distant relative with inheritance dispute, financial difficulties, gambling debts",
        "motives": ["Inheritance manipulation", "Debt settlement"],
        "alibi": "Claims to be out of town",
        "hints": ["Large unexplained withdrawals", "Recent contact with victim", "Insurance policy beneficiary"]
    },
    "Organized Crime": {
        "profile": "Local crime syndicate leader, known for high-profile kidnappings, professional operation",
        "motives": ["Ransom profit", "Territorial expansion"],
        "alibi": "Multiple witnesses place him elsewhere",
        "hints": ["Signature kidnapping methods", "Known associates in area", "Previous similar cases"]
    }
}
timeline_events = [
    {"time": "18:30", "event": "Victim leaves office building", "location": "Corporate HQ"},
    {"time": "18:45", "event": "Security camera shows suspicious vehicle", "location": "Parking Garage"},
    {"time": "19:00", "event": "Phone call to family - 'business trip'", "location": "Unknown"},
    {"time": "19:15", "event": "Credit card used at gas station", "location": "Highway Exit 47"},
    {"time": "19:30", "event": "Vehicle enters industrial district", "location": "Warehouse Area"},
    {"time": "20:00", "event": "Ransom demand received", "location": "Unknown"},
    {"time": "20:30", "event": "Second phone call - proof of life", "location": "Unknown"},
    {"time": "21:00", "event": "False lead - abandoned vehicle found", "location": "Rural Road"},
    {"time": "21:30", "event": "Encrypted message intercepted", "location": "Digital Network"},
    {"time": "22:00", "event": "Deadline approaches", "location": "Unknown"}
]
accuracy_score = 100
time_remaining = 7200  # 2 hours in seconds
suspect_suspicion = {name: 0 for name in suspects.keys()}
interrogation_rounds = 0
critical_decisions = []

# ---------------- UTILITY FUNCTIONS ----------------
def animate_text(label, text, delay=0.03):
    """Ultra-fast animated text for high-stakes scenarios"""
    label.config(text="")
    for char in text:
        label.config(text=label.cget("text") + char)
        time.sleep(delay)
        label.update()

def update_suspicion(suspect, change):
    """Update suspicion with severe penalties for wrong accusations"""
    global suspect_suspicion, accuracy_score
    old_level = suspect_suspicion[suspect]
    suspect_suspicion[suspect] = max(0, min(100, suspect_suspicion[suspect] + change))

    # Severe accuracy penalty for false accusations
    if change > 20 and suspect_suspicion[suspect] > 80:
        accuracy_score -= 15
        critical_decisions.append(f"High suspicion on {suspect} - {change} point increase")

def random_event():
    """High-stakes random events with time pressure"""
    events = [
        "🚨 URGENT: New ransom demand - 30 minutes to respond!",
        "📱 Encrypted call intercepted - partial location data",
        "⚠️ False lead discovered - abandoned vehicle with misleading clues",
        "💰 Wire transfer attempt blocked - suspect financial trail",
        "🕐 TIME CRITICAL: Victim's condition deteriorating",
        "🔍 Witness emerges - saw suspicious activity",
        "📡 Signal intelligence: Tracking device activated briefly",
        "🚔 Police raid on suspect location - evidence recovered"
    ]
    return random.choice(events)

def start_timer(window, duration, callback):
    """Critical decision timer with severe consequences"""
    def countdown():
        nonlocal duration
        if duration > 0:
            timer_label.config(text=f"⏰ TIME: {duration//60}:{duration%60:02d}")
            duration -= 1
            window.after(1000, countdown)
        else:
            callback()
    timer_label = tk.Label(window, text="", fg=RED, bg=BG, font=("Consolas", 12, "bold"))
    timer_label.pack(pady=5)
    countdown()

# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 4 - The Corporate Kidnapping")
    story.configure(bg=BG)
    story.geometry("700x500")

    label = tk.Label(
        story,
        text="",
        wraplength=650,
        font=("Consolas", 13),
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

# ---------------- CASE BRIEFING ----------------
def open_case4(prev):
    global time_remaining
    story_text = [
        "🚨 EMERGENCY ALERT - PRIORITY ONE INVESTIGATION",
        "VICTIM: CEO of TechNova Corporation - Age 45",
        "INCIDENT: Kidnapped during evening commute",
        "LOCATION: Downtown business district",
        "TIME: Approximately 6:30 PM yesterday",
        "DEMANDS: $50 million cryptocurrency ransom",
        "COMPLICATIONS: Multiple suspects, international elements",
        "Corporate secrets at risk, victim's life in danger",
        "INVESTIGATION WINDOW: 2 hours remaining",
        "Failure means corporate collapse and potential victim death",
        "Your decisions determine everything..."
    ]

    show_story(prev, story_text, case_briefing)

# ---------------- CASE BRIEFING ----------------
def case_briefing():
    briefing = tk.Toplevel()
    briefing.title("CIS // Case Briefing - Corporate Kidnapping")
    briefing.configure(bg=BG)
    briefing.geometry("900x600")

    # Header with timer
    header_frame = tk.Frame(briefing, bg=BG)
    header_frame.pack(pady=10)

    tk.Label(header_frame, text="🚨 CASE BRIEFING - TIME SENSITIVE",
             font=("Consolas", 18, "bold"), fg=MAGENTA, bg=BG).pack()

    global time_remaining
    timer_label = tk.Label(header_frame, text=f"⏰ INVESTIGATION TIME: {time_remaining//3600}:{(time_remaining%3600)//60:02d}:{time_remaining%60:02d}",
                          fg=RED, bg=BG, font=("Consolas", 14, "bold"))
    timer_label.pack()

    # Start global timer
    def update_global_timer():
        global time_remaining
        if time_remaining > 0:
            time_remaining -= 1
            timer_label.config(text=f"⏰ INVESTIGATION TIME: {time_remaining//3600}:{(time_remaining%3600)//60:02d}:{time_remaining%60:02d}")
            if time_remaining % 60 == 0:  # Update every minute
                briefing.after(60000, update_global_timer)
        else:
            # Time's up - automatic failure
            auto_failure(briefing)

    threading.Thread(target=update_global_timer, daemon=True).start()

    # Case details
    details_frame = tk.Frame(briefing, bg=BG)
    details_frame.pack(side=tk.LEFT, padx=20, pady=20)

    tk.Label(details_frame, text="📋 CASE DETAILS",
             font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack()

    case_info = tk.Text(details_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                       height=15, width=50)
    case_info.pack(pady=10)
    case_info.insert(tk.END, """VICTIM PROFILE:
• Name: Marcus Reynolds
• Position: CEO, TechNova Corp
• Net Worth: $2.8 billion
• Recent Activities: Hostile takeover bid
• Personal: Divorced, one child

KIDNAPPING DETAILS:
• Method: Professional - no struggle
• Location: Underground parking
• Time: 6:30 PM, rush hour
• Witnesses: None
• Vehicle: Black SUV, no plates

RANSOM DEMANDS:
• Amount: $50M in cryptocurrency
• Deadline: 48 hours from abduction
• Proof: Video of victim alive
• Threats: Corporate data release

SUSPECTS IDENTIFIED:
• Business Rival (Corporate sabotage)
• Disgruntled Employee (Revenge)
• Foreign Agent (Espionage)
• Family Member (Inheritance)
• Organized Crime (Profit)

EVIDENCE STATUS: MINIMAL
INVESTIGATION PRIORITY: CRITICAL""")
    case_info.config(state=tk.DISABLED)

    # Initial actions
    actions_frame = tk.Frame(briefing, bg=BG)
    actions_frame.pack(side=tk.RIGHT, padx=20, pady=20)

    tk.Label(actions_frame, text="🎯 INITIAL ACTIONS",
             font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack()

    def start_investigation():
        decisions_made.append("Started investigation - evidence collection phase")
        crime_scene_investigation(briefing)

    tk.Button(actions_frame, text="🔍 BEGIN CRIME SCENE INVESTIGATION",
              bg="#020617", fg=GREEN, font=("Consolas", 11),
              command=start_investigation).pack(pady=10)

    tk.Button(actions_frame, text="📞 CONTACT FAMILY FIRST",
              bg="#020617", fg=WARNING, font=("Consolas", 11),
              command=lambda: contact_family(briefing)).pack(pady=5)

    tk.Button(actions_frame, text="🚔 ALERT AUTHORITIES",
              bg="#020617", fg=CYAN, font=("Consolas", 11),
              command=lambda: alert_authorities(briefing)).pack(pady=5)

# ---------------- CRIME SCENE INVESTIGATION ----------------
def crime_scene_investigation(prev):
    prev.destroy()

    scene = tk.Toplevel()
    scene.title("CIS // Crime Scene Analysis")
    scene.configure(bg=BG)
    scene.geometry("1000x700")

    # Header
    tk.Label(scene, text="🔍 CRIME SCENE ANALYSIS REPORT",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Evidence Panel
    evidence_frame = tk.Frame(scene, bg=BG, relief="ridge", bd=2)
    evidence_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    tk.Label(evidence_frame, text="📋 EVIDENCE COLLECTED",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    evidence_list = tk.Listbox(evidence_frame, bg="black", fg=GREEN, selectbackground=CYAN,
                              font=("Consolas", 10), height=20, width=40)
    evidence_list.pack(pady=10)

    # Scene Description
    desc_frame = tk.Frame(scene, bg=BG)
    desc_frame.pack(side=tk.TOP, padx=20, pady=10, fill=tk.X)

    tk.Label(desc_frame, text="🏢 PARKING GARAGE CRIME SCENE",
             font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack()

    scene_desc = tk.Text(desc_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                        height=8, width=60, wrap=tk.WORD)
    scene_desc.pack(pady=5)
    scene_desc.insert(tk.END, """LOCATION: TechNova HQ Underground Parking - Level B3
TIME OF INCIDENT: 6:30 PM
WEATHER: Clear, well-lit area

PHYSICAL EVIDENCE:
• Tire marks: Professional drifting pattern
• Security footage: 3-second clip of black SUV
• DNA traces: Unknown male profile
• Digital footprint: WiFi connection logged
• Witness statement: Garage attendant heard 'business meeting'

FORENSIC ANALYSIS:
• Vehicle make: Likely Mercedes or BMW executive
• Entry method: Victim's keycard used at 6:28 PM
• Exit route: Service elevator bypassed security
• Communication: Encrypted signal detected briefly

INITIAL HYPOTHESES:
• Inside job (keycard access)
• Professional kidnapping team
• Victim cooperation possible
• Corporate espionage angle""")
    scene_desc.config(state=tk.DISABLED)

    # Actions Panel
    actions_frame = tk.Frame(scene, bg=BG, relief="ridge", bd=2)
    actions_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    tk.Label(actions_frame, text="🎯 INVESTIGATION ACTIONS",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    def collect_evidence(item, description):
        if item not in [e.split(": ")[0] for e in evidence_list.get(0, tk.END)]:
            evidence_list.insert(tk.END, f"{item}: {description}")
            evidence_collected.append(item)
            decisions_made.append(f"Collected evidence: {item}")

            # Update suspicions based on evidence
            if "Security footage" in item:
                update_suspicion("Disgruntled Employee", 15)
            elif "Encrypted signal" in item:
                update_suspicion("Foreign Agent", 20)
            elif "Tire marks" in item:
                update_suspicion("Organized Crime", 15)

    tk.Button(actions_frame, text="📹 Analyze Security Footage",
              command=lambda: collect_evidence("Security Footage", "Black SUV with professional driver")).pack(pady=3)
    tk.Button(actions_frame, text="🔍 Examine Tire Marks",
              command=lambda: collect_evidence("Tire Pattern", "High-performance vehicle, professional driving")).pack(pady=3)
    tk.Button(actions_frame, text="📡 Check Digital Signals",
              command=lambda: collect_evidence("Encrypted Signal", "Brief military-grade encryption detected")).pack(pady=3)
    tk.Button(actions_frame, text="🧬 Process DNA Evidence",
              command=lambda: collect_evidence("DNA Profile", "Unknown male, possible Eastern European origin")).pack(pady=3)
    tk.Button(actions_frame, text="💳 Trace Financial Records",
              command=lambda: collect_evidence("Financial Trail", "Recent large transfers to offshore accounts")).pack(pady=3)
    tk.Button(actions_frame, text="📞 Interview Witnesses",
              command=lambda: collect_evidence("Witness Statement", "Garage attendant heard 'corporate pickup'")).pack(pady=3)

    tk.Button(scene, text="▶ PROCEED TO TIMELINE ANALYSIS",
              bg="#020617", fg=GREEN, command=lambda: timeline_analysis(scene)).pack(pady=20)

# ---------------- TIMELINE ANALYSIS ----------------
def timeline_analysis(prev):
    prev.destroy()

    timeline_win = tk.Toplevel()
    timeline_win.title("CIS // Timeline Reconstruction")
    timeline_win.configure(bg=BG)
    timeline_win.geometry("900x600")

    tk.Label(timeline_win, text="⏰ TIMELINE RECONSTRUCTION - CRITICAL ANALYSIS",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Timeline display
    timeline_frame = tk.Frame(timeline_win, bg=BG)
    timeline_frame.pack(pady=20)

    tk.Label(timeline_frame, text="📅 EVENT TIMELINE",
             font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack()

    timeline_text = tk.Text(timeline_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                           height=12, width=70, wrap=tk.WORD)
    timeline_text.pack(pady=10)

    for event in timeline_events:
        timeline_text.insert(tk.END, f"{event['time']} - {event['event']} ({event['location']})\n")

    timeline_text.config(state=tk.DISABLED)

    # Reconstruction puzzle
    puzzle_frame = tk.Frame(timeline_win, bg=BG)
    puzzle_frame.pack(pady=20)

    tk.Label(puzzle_frame, text="🔍 TIMELINE PUZZLE - RECONSTRUCT SEQUENCE",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    tk.Label(puzzle_frame, text="What event happened FIRST? (Enter exact time)",
             fg=GREEN, bg=BG).pack()

    time_entry = tk.Entry(puzzle_frame, bg="black", fg=GREEN, insertbackground=GREEN, width=20)
    time_entry.pack(pady=5)

    tk.Label(puzzle_frame, text="What was the KIDNAPPING METHOD? (professional/inside/false_flag)",
             fg=GREEN, bg=BG).pack()

    method_entry = tk.Entry(puzzle_frame, bg="black", fg=GREEN, insertbackground=GREEN, width=20)
    method_entry.pack(pady=5)

    result_label = tk.Label(puzzle_frame, text="", bg=BG, font=("Consolas", 10))
    result_label.pack(pady=10)

    def check_timeline():
        global accuracy_score
        time_correct = time_entry.get().strip() in ["18:30", "6:30", "6:30 PM"]
        method_correct = method_entry.get().lower().strip() in ["professional", "inside job"]

        if time_correct and method_correct:
            result_label.config(text="✅ EXCELLENT TIMELINE ANALYSIS!", fg=GREEN)
            accuracy_score += 10
            decisions_made.append("Perfect timeline reconstruction")
            tk.Button(timeline_win, text="▶ SUSPECT ANALYSIS",
                      command=lambda: suspect_analysis(timeline_win)).pack(pady=10)
        elif time_correct or method_correct:
            result_label.config(text="⚠️ PARTIALLY CORRECT - Proceed with caution", fg=WARNING)
            accuracy_score -= 5
            decisions_made.append("Incomplete timeline analysis")
            tk.Button(timeline_win, text="▶ SUSPECT ANALYSIS",
                      command=lambda: suspect_analysis(timeline_win)).pack(pady=10)
        else:
            result_label.config(text="❌ CRITICAL TIMELINE ERROR - Accuracy severely impacted", fg=RED)
            accuracy_score -= 20
            critical_decisions.append("Failed timeline reconstruction")
            tk.Button(timeline_win, text="▶ RETRY ANALYSIS",
                      command=lambda: timeline_analysis(timeline_win)).pack(pady=10)

    tk.Button(puzzle_frame, text="SUBMIT TIMELINE ANALYSIS", command=check_timeline).pack(pady=10)

# ---------------- SUSPECT ANALYSIS ----------------
def suspect_analysis(prev):
    prev.destroy()

    analysis = tk.Toplevel()
    analysis.title("CIS // Suspect Analysis")
    analysis.configure(bg=BG)
    analysis.geometry("1000x700")

    tk.Label(analysis, text="👤 SUSPECT ANALYSIS - MOTIVE EVALUATION",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Suspect profiles
    profiles_frame = tk.Frame(analysis, bg=BG, relief="ridge", bd=2)
    profiles_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    tk.Label(profiles_frame, text="📋 SUSPECT PROFILES",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    suspect_listbox = tk.Listbox(profiles_frame, bg="black", fg=GREEN, selectbackground=CYAN,
                                font=("Consolas", 10), height=15, width=45)
    suspect_listbox.pack(pady=10)

    for suspect, info in suspects.items():
        suspect_listbox.insert(tk.END, f"{suspect}: {info['profile'][:60]}...")

    # Analysis panel
    analysis_frame = tk.Frame(analysis, bg=BG, relief="ridge", bd=2)
    analysis_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    tk.Label(analysis_frame, text="🔍 DETAILED ANALYSIS",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    analysis_text = tk.Text(analysis_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                           height=15, width=50, wrap=tk.WORD)
    analysis_text.pack(pady=10)

    def show_suspect_details():
        selection = suspect_listbox.curselection()
        if selection:
            suspect_name = suspect_listbox.get(selection[0]).split(": ")[0]
            info = suspects[suspect_name]

            analysis_text.delete(1.0, tk.END)
            analysis_text.insert(tk.END, f"SUSPECT: {suspect_name}\n\n")
            analysis_text.insert(tk.END, f"PROFILE: {info['profile']}\n\n")
            analysis_text.insert(tk.END, f"MOTIVES: {', '.join(info['motives'])}\n\n")
            analysis_text.insert(tk.END, f"ALIBI: {info['alibi']}\n\n")
            analysis_text.insert(tk.END, f"SUSPICION LEVEL: {suspect_suspicion[suspect_name]}%\n\n")
            analysis_text.insert(tk.END, f"HINTS: {', '.join(info['hints'])}\n\n")

            # Pattern recognition puzzle
            analysis_text.insert(tk.END, "PATTERN ANALYSIS:\n")
            analysis_text.insert(tk.END, "Recent activity pattern: Calls, Locations, Financial\n")
            analysis_text.insert(tk.END, "Look for connections to kidnapping timeline...\n")

    tk.Button(profiles_frame, text="VIEW DETAILS", command=show_suspect_details).pack(pady=5)

    # Motive analysis puzzle
    tk.Label(analysis_frame, text="🧩 MOTIVE ANALYSIS PUZZLE",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(analysis_frame, text="Which suspect has the STRONGEST motive? (Enter name)",
             fg=GREEN, bg=BG).pack()

    motive_entry = tk.Entry(analysis_frame, bg="black", fg=GREEN, insertbackground=GREEN, width=25)
    motive_entry.pack(pady=5)

    result_label = tk.Label(analysis_frame, text="", bg=BG, font=("Consolas", 10))
    result_label.pack(pady=5)

    def check_motive():
        global accuracy_score
        suspect = motive_entry.get().strip()

        if suspect in suspects:
            # Complex motive evaluation
            if suspect == "Foreign Agent" and len(evidence_collected) >= 3:
                result_label.config(text="✅ STRONG ESPIONAGE CONNECTION IDENTIFIED!", fg=GREEN)
                update_suspicion(suspect, 25)
                accuracy_score += 15
                decisions_made.append(f"Identified strong motive for {suspect}")
            elif suspect == "Business Rival":
                result_label.config(text="⚠️ COMPETITIVE MOTIVE POSSIBLE", fg=WARNING)
                update_suspicion(suspect, 15)
                accuracy_score += 5
            else:
                result_label.config(text="❌ WEAK MOTIVE ANALYSIS", fg=RED)
                update_suspicion(suspect, 5)
                accuracy_score -= 10
                critical_decisions.append(f"Questionable motive analysis for {suspect}")

            tk.Button(analysis, text="▶ BEGIN INTERROGATIONS",
                      command=lambda: interrogation_phase(analysis)).pack(pady=20)
        else:
            result_label.config(text="❌ INVALID SUSPECT NAME", fg=RED)

    tk.Button(analysis_frame, text="ANALYZE MOTIVE", command=check_motive).pack(pady=10)

# ---------------- INTERROGATION PHASE ----------------
def interrogation_phase(prev):
    prev.destroy()

    global interrogation_rounds
    interrogation_rounds += 1

    interrog = tk.Toplevel()
    interrog.title("CIS // Interrogation Room - Round " + str(interrogation_rounds))
    interrog.configure(bg=BG)
    interrog.geometry("1100x700")

    tk.Label(interrog, text=f"🕵️ INTERROGATION ROUND {interrogation_rounds} - LIE DETECTION ACTIVE",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Suspect selection
    select_frame = tk.Frame(interrog, bg=BG)
    select_frame.pack(side=tk.TOP, padx=20, pady=10)

    tk.Label(select_frame, text="👤 SELECT SUSPECT TO INTERROGATE",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    suspect_var = tk.StringVar()
    suspect_var.set(list(suspects.keys())[0])

    for suspect in suspects.keys():
        suspicion_level = suspect_suspicion[suspect]
        color = GREEN if suspicion_level < 30 else WARNING if suspicion_level < 70 else RED
        tk.Radiobutton(select_frame, text=f"{suspect} ({suspicion_level}%)",
                      variable=suspect_var, value=suspect,
                      bg=BG, fg=color, selectcolor=BG, activebackground=BG,
                      activeforeground=CYAN).pack(anchor=tk.W)

    # Question selection
    questions_frame = tk.Frame(interrog, bg=BG, relief="ridge", bd=2)
    questions_frame.pack(side=tk.LEFT, padx=20, pady=20, fill=tk.Y)

    tk.Label(questions_frame, text="❓ INTERROGATION QUESTIONS",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    questions = [
        "Where were you between 6:00-7:00 PM yesterday?",
        "Do you have knowledge of the victim's business dealings?",
        "Have you made any large financial transactions recently?",
        "Can you explain your communications with the victim?",
        "What is your relationship with organized crime elements?",
        "Have you traveled internationally in the last month?"
    ]

    question_var = tk.StringVar()
    question_var.set(questions[0])

    for q in questions:
        tk.Radiobutton(questions_frame, text=q, variable=question_var, value=q,
                      bg=BG, fg=GREEN, selectcolor=BG, activebackground=BG,
                      activeforeground=CYAN, wraplength=300, justify=tk.LEFT).pack(anchor=tk.W, pady=2)

    # Response panel
    response_frame = tk.Frame(interrog, bg=BG, relief="ridge", bd=2)
    response_frame.pack(side=tk.RIGHT, padx=20, pady=20, fill=tk.Y)

    tk.Label(response_frame, text="🎭 SUSPECT RESPONSE & LIE DETECTION",
             font=("Consolas", 12, "bold"), fg=CYAN, bg=BG).pack()

    response_text = tk.Text(response_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                           height=15, width=50, wrap=tk.WORD)
    response_text.pack(pady=10)

    result_label = tk.Label(response_frame, text="", bg=BG, font=("Consolas", 10))
    result_label.pack(pady=5)

    def ask_question():
        global accuracy_score
        suspect = suspect_var.get()
        question = question_var.get()

        # Advanced lie detection simulation
        truth_probability = random.random()
        is_lying = truth_probability < 0.4  # 40% chance of lying

        if is_lying:
            responses = [
                f"{suspect} appears nervous... 'I was at home alone.' (LIE DETECTED - alibi unverifiable)",
                f"{suspect} avoids eye contact... 'Business as usual.' (LIE DETECTED - inconsistent with records)",
                f"{suspect} hesitates... 'No comment.' (LIE DETECTED - suspicious evasion)",
                f"{suspect} contradicts previous statement... (LIE DETECTED - pattern inconsistency)"
            ]
            response = random.choice(responses)
            update_suspicion(suspect, random.randint(15, 25))
            accuracy_score -= random.randint(5, 10)
            lie_penalty = "MAJOR SUSPICION INCREASE"
        else:
            responses = [
                f"{suspect} maintains steady eye contact... 'I can provide documentation.' (TRUTH DETECTED)",
                f"{suspect} answers confidently... 'Check my phone records.' (TRUTH DETECTED)",
                f"{suspect} provides specific details... 'Meeting minutes available.' (TRUTH DETECTED)",
                f"{suspect} offers cooperation... 'Happy to help investigation.' (TRUTH DETECTED)"
            ]
            response = random.choice(responses)
            update_suspicion(suspect, random.randint(-10, 5))
            accuracy_score += random.randint(5, 10)
            lie_penalty = "TRUSTWORTHY RESPONSE"

        response_text.insert(tk.END, f"Question: {question}\n")
        response_text.insert(tk.END, f"Response: {response}\n")
        response_text.insert(tk.END, f"Analysis: {lie_penalty}\n\n")

        result_label.config(text=f"Current suspicion on {suspect}: {suspect_suspicion[suspect]}%",
                           fg=RED if suspect_suspicion[suspect] > 70 else WARNING if suspect_suspicion[suspect] > 40 else GREEN)

        # Random event trigger
        if random.random() < 0.25:  # 25% chance
            event = random_event()
            response_text.insert(tk.END, f"RANDOM EVENT: {event}\n\n")

        decisions_made.append(f"Interrogated {suspect}: {lie_penalty}")

    tk.Button(questions_frame, text="ASK QUESTION", command=ask_question).pack(pady=10)

    # Round progression
    if interrogation_rounds < 3:
        tk.Button(interrog, text=f"▶ COMPLETE ROUND {interrogation_rounds} - NEXT ROUND",
                  command=lambda: interrogation_phase(interrog)).pack(pady=20)
    else:
        tk.Button(interrog, text="▶ FINAL ACCUSATION - TIME CRITICAL",
                  command=lambda: final_accusation(interrog)).pack(pady=20)

# ---------------- FINAL ACCUSATION ----------------
def final_accusation(prev):
    prev.destroy()

    final = tk.Toplevel()
    final.title("CIS // Final Accusation - Critical Decision")
    final.configure(bg=BG)
    final.geometry("800x600")

    tk.Label(final, text="🎯 FINAL ACCUSATION - INVESTIGATION CONCLUSION",
             font=("Consolas", 16, "bold"), fg=MAGENTA, bg=BG).pack(pady=10)

    # Final status display
    status_frame = tk.Frame(final, bg=BG)
    status_frame.pack(pady=20)

    tk.Label(status_frame, text="INVESTIGATION SUMMARY:",
             font=("Consolas", 14, "bold"), fg=CYAN, bg=BG).pack()

    summary_text = tk.Text(status_frame, bg="black", fg=GREEN, font=("Consolas", 10),
                          height=8, width=60)
    summary_text.pack(pady=10)

    summary_text.insert(tk.END, f"Evidence Collected: {len(evidence_collected)} items\n")
    summary_text.insert(tk.END, f"Decisions Made: {len(decisions_made)}\n")
    summary_text.insert(tk.END, f"Interrogation Rounds: {interrogation_rounds}\n")
    summary_text.insert(tk.END, f"Time Remaining: {time_remaining//60} minutes\n")
    summary_text.insert(tk.END, f"Accuracy Score: {accuracy_score}%\n\n")

    summary_text.insert(tk.END, "SUSPECT SUSPICION LEVELS:\n")
    for suspect, level in suspect_suspicion.items():
        summary_text.insert(tk.END, f"{suspect}: {level}%\n")

    summary_text.config(state=tk.DISABLED)

    tk.Label(final, text="WHO IS THE KIDNAPPER?",
             font=("Consolas", 14), fg=CYAN, bg=BG).pack(pady=10)

    culprit_var = tk.StringVar()

    for suspect in suspects.keys():
        suspicion = suspect_suspicion[suspect]
        color = GREEN if suspicion < 30 else WARNING if suspicion < 70 else RED
        tk.Radiobutton(final, text=f"{suspect} ({suspicion}% suspicion)",
                      variable=culprit_var, value=suspect,
                      bg=BG, fg=color, selectcolor=BG, activebackground=BG,
                      activeforeground=CYAN).pack()

    def make_final_accusation():
        culprit = culprit_var.get()
        if not culprit:
            return

        final.destroy()

        # Complex ending determination - HIGHEST DIFFICULTY THRESHOLDS
        max_suspicion = max(suspect_suspicion.values())
        correct_culprit = "Foreign Agent"  # The actual kidnapper

        # Perfect solve requirements (extremely strict)
        perfect_conditions = (
            culprit == correct_culprit and
            accuracy_score >= 90 and
            suspect_suspicion[correct_culprit] >= 80 and
            len(evidence_collected) >= 5 and
            len(critical_decisions) == 0 and
            time_remaining > 1800  # At least 30 minutes left
        )

        if perfect_conditions:
            ending = [
                "💎 PERFECT INVESTIGATION - ELITE LEVEL CLEARANCE",
                "Evidence analysis was flawless across all domains",
                "Timeline reconstruction revealed the complete operation",
                "Lie detection exposed the espionage network",
                f"Foreign agent {culprit} arrested with full network dismantlement",
                "Corporate secrets secured, victim rescued unharmed",
                "International cooperation initiated",
                "🎉 CASE SOLVED WITH MASTERFUL PRECISION"
            ]
        elif culprit == correct_culprit and accuracy_score >= 75 and suspect_suspicion[correct_culprit] >= 60:
            ending = [
                "✅ CASE SOLVED - HIGH PROFICIENCY",
                "The espionage operation has been disrupted",
                f"{culprit} apprehended with substantial evidence",
                "Most corporate data secured, victim rescued",
                "Some network elements escaped but operation crippled",
                "International intelligence agencies notified",
                "⚠️ PARTIAL NETWORK DISMANTLEMENT"
            ]
        elif culprit == correct_culprit and accuracy_score >= 50:
            ending = [
                "⚠️ CASE PARTIALLY SOLVED - ADEQUATE PERFORMANCE",
                "Wrong suspect initially pursued but correct culprit identified",
                f"{culprit} arrested but with incomplete evidence",
                "Victim rescued but some data compromised",
                "Corporate damage contained but not eliminated",
                "Further investigation required for full network",
                "📋 INCONCLUSIVE NETWORK ANALYSIS"
            ]
        elif accuracy_score >= 60 and max_suspicion >= 50:
            ending = [
                "⚠️ CASE PARTIALLY SOLVED - SUSPECT IDENTIFIED",
                "Wrong accusation but strong investigative work",
                "Alternative suspect shows high probability",
                "Victim location narrowed but rescue complicated",
                "Corporate investigation continues",
                "Some evidence suggests organized crime involvement",
                "📋 ALTERNATIVE THEORY DEVELOPED"
            ]
        else:
            ending = [
                "❌ INVESTIGATION CRITICAL FAILURE",
                "Wrong accusations led to disaster",
                "Culprit remains at large with full network intact",
                "Victim's location unknown, corporate collapse imminent",
                "Massive data breach initiated",
                "International incident declared",
                "🚨 CATASTROPHIC MISSION FAILURE"
            ]

        # Add detailed summary
        ending.extend([
            "",
            "INVESTIGATION SUMMARY:",
            f"• Accuracy Score: {accuracy_score}%",
            f"• Evidence Collected: {len(evidence_collected)} items",
            f"• Critical Decisions: {len(critical_decisions)}",
            f"• Time Remaining: {time_remaining//60} minutes",
            f"• Interrogation Rounds: {interrogation_rounds}",
            "",
            "KEY DECISIONS MADE:"
        ])

        for decision in decisions_made[-5:]:  # Show last 5 decisions
            ending.append(f"• {decision}")

        show_story(final, ending, lambda: None)

    tk.Button(final, text="MAKE FINAL ACCUSATION", command=make_final_accusation).pack(pady=20)

# ---------------- UTILITY FUNCTIONS ----------------
def contact_family(prev):
    decisions_made.append("Contacted family first - potential emotional compromise")
    # This would complicate the investigation
    accuracy_score -= 10
    crime_scene_investigation(prev)

def alert_authorities(prev):
    decisions_made.append("Alerted authorities - potential leaks")
    # Mixed impact
    accuracy_score -= 5
    crime_scene_investigation(prev)

def auto_failure(prev):
    prev.destroy()
    ending = [
        "⏰ TIME EXPIRED - AUTOMATIC FAILURE",
        "Investigation window closed",
        "Kidnapper executed contingency plan",
        "Victim's location lost forever",
        "Corporate data released globally",
        "💀 MISSION CRITICAL FAILURE"
    ]
    show_story(prev, ending, lambda: None)
    f.configure(bg=BG)
    f.geometry("400x300")

    tk.Label(f, text="WHERE IS THE VICTIM?",
             fg=CYAN, bg=BG).pack(pady=10)

    def result(choice):
        f.destroy()

        if choice == "Warehouse":
            ending = [
                "You storm the warehouse...",
                "The kidnapper tries to escape...",
                "But your team intercepts him.",
                "The child is rescued safely.",
                "💥 MISSION SUCCESSFUL"
            ]
        else:
            ending = [
                "You chose the wrong location...",
                "Time runs out...",
                "The trail goes cold...",
                "⚠ MISSION FAILED"
            ]

        show_story(f, ending, lambda: None)

    tk.Button(f, text="Warehouse", command=lambda: result("Warehouse")).pack(pady=5)
    tk.Button(f, text="Apartment", command=lambda: result("Apartment")).pack(pady=5)
    tk.Button(f, text="Office", command=lambda: result("Office")).pack(pady=5)