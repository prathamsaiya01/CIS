import tkinter as tk
from logic.puzzles import pattern_game, cipher_game

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Case 4")
    story.configure(bg=BG)
    story.geometry("550x320")

    label = tk.Label(
        story,
        text="",
        wraplength=500,
        font=("Consolas", 11),
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
        command=next_text
    ).pack(pady=10)

    next_text()


# ---------------- ENTRY ----------------
def open_case4(prev):
    story_text = [
        "📍 08:45 PM — Emergency Call Received",
        "A child has been kidnapped.",
        "Parents received a strange coded message.",
        "No witnesses. No clear suspects.",
        "But the kidnapper made one mistake...",
        "The message contains a hidden clue.",
        "Time is running out. You must act fast.",
        "Every second matters."
    ]

    show_story(prev, story_text, phone_clue)


# ---------------- STEP 1: PHONE CLUE ----------------
def phone_clue():
    phone = tk.Toplevel()
    phone.title("CIS // Phone Message")
    phone.configure(bg=BG)
    phone.geometry("500x300")

    tk.Label(phone, text="KIDNAPPER MESSAGE",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(phone, text="VJG YCTGJQWUG KU PGCT",
             fg=GREEN, bg=BG).pack()

    tk.Label(phone, text="Hint: Shift letters back by 2",
             fg=GREEN, bg=BG).pack(pady=5)

    entry = tk.Entry(phone, bg="black", fg=GREEN, insertbackground=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(phone, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get().lower() == "the warehouse is near":
            result_label.config(text="✅ MESSAGE DECODED", fg=GREEN)

            tk.Button(phone, text="▶ ANALYZE LOCATION",
                      command=lambda: location_puzzle(phone)).pack()
        else:
            result_label.config(text="❌ WRONG DECRYPTION", fg="red")

    tk.Button(phone, text="SUBMIT", command=check).pack(pady=10)


# ---------------- STEP 2: LOCATION PUZZLE ----------------
def location_puzzle(prev):
    prev.destroy()

    loc = tk.Toplevel()
    loc.title("CIS // Location Trace")
    loc.configure(bg=BG)
    loc.geometry("450x300")

    tk.Label(loc, text="TRACE COORDINATES",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(loc, text="Pattern: 5, 10, 20, 40, ?",
             fg=GREEN, bg=BG).pack()

    tk.Label(loc, text="Hint: Each number doubles",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(loc, bg="black", fg=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(loc, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get() == "80":
            result_label.config(text="✅ LOCATION MATCHED", fg=GREEN)

            tk.Button(loc, text="▶ SEARCH AREA",
                      command=lambda: hidden_clue(loc)).pack()
        else:
            result_label.config(text="❌ WRONG", fg="red")

    tk.Button(loc, text="SUBMIT", command=check).pack(pady=10)


# ---------------- STEP 3: HIDDEN CLUE ----------------
def hidden_clue(prev):
    prev.destroy()

    clue = tk.Toplevel()
    clue.title("CIS // Search Operation")
    clue.configure(bg=BG)
    clue.geometry("450x300")

    tk.Label(clue, text="SEARCHING WAREHOUSE...",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(clue,
             text="• Rope found\n• Small footprints\n• Broken window\n• Fresh tire marks",
             fg=GREEN, bg=BG).pack(pady=10)

    tk.Label(clue,
             text="All evidence points to one location...",
             fg=GREEN, bg=BG).pack()

    tk.Button(clue, text="▶ FINAL DECISION",
              command=lambda: final_choice(clue)).pack(pady=10)


# ---------------- FINAL DECISION ----------------
def final_choice(prev):
    prev.destroy()

    f = tk.Toplevel()
    f.title("CIS // Final Decision")
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