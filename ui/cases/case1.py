import tkinter as tk
from logic.puzzles import password_cracker, cipher_game

BG = "#020617"
GREEN = "#00ff9f"
CYAN = "#00f5ff"


# ---------------- STORY ENGINE ----------------
def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("CIS // Story")
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
def open_case1(prev):
    story_text = [
        "📍 02:13 AM — Penthouse Apartment",
        "Rain hits the windows as you enter the crime scene.",
        "Victim: Raj Malhotra, age 42 — a powerful businessman.",
        "His body lies near the desk. No struggle. No forced entry.",
        "You notice a family photo nearby...",
        "📸 The frame reads: 'Raj Malhotra — Born 17/08/1983'",
        "The laptop beside him is locked...",
        "That date might not be just sentimental..."
    ]

    show_story(prev, story_text, crime_scene)


# ---------------- CRIME SCENE ----------------
def crime_scene():
    scene = tk.Toplevel()
    scene.title("CIS // Crime Scene")
    scene.configure(bg=BG)
    scene.geometry("550x350")

    tk.Label(scene, text="CRIME SCENE",
             font=("Consolas", 16, "bold"),
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(scene,
             text="• Victim: Raj Malhotra\n"
                  "• No forced entry\n"
                  "• Laptop (locked)\n"
                  "• Family photo (DOB visible)\n"
                  "• Minimal blood stains",
             fg=GREEN, bg=BG, justify="left").pack(pady=10)

    tk.Button(scene,
              text="▶ EXAMINE LAPTOP",
              bg="#020617", fg=GREEN,
              command=lambda: show_story(scene, [
                  "You open the laptop...",
                  "Password protected system detected.",
                  "Hint: Victim often used personal data as passwords.",
                  "You recall the photo frame...",
                  "Maybe the birth date is the key..."
              ], laptop_puzzle)
              ).pack(pady=20)


# ---------------- PASSWORD PUZZLE ----------------
def laptop_puzzle():
    game = tk.Toplevel()
    game.title("CIS // Laptop Access")
    game.configure(bg=BG)
    game.geometry("450x300")

    tk.Label(game, text="🔐 ENTER PASSWORD",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(game, text="Hint: DDMMYYYY format",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(game, bg="black", fg=GREEN, insertbackground=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(game, text="", bg=BG)
    result_label.pack()

    def check():
        password = entry.get()

        # Correct password based on story
        if password == "17081983":
            result_label.config(text="✅ ACCESS GRANTED", fg=GREEN)

            tk.Button(game, text="▶ CONTINUE",
                      command=lambda: show_story(game, [
                          "Laptop unlocked...",
                          "You access recent emails...",
                          "A message stands out:",
                          "'Deal is off. You talk, you die.'",
                          "Three contacts appear frequently...",
                          "All are now suspects."
                      ], suspects)
                      ).pack(pady=10)
        else:
            result_label.config(text="❌ WRONG PASSWORD", fg="red")

    tk.Button(game, text="SUBMIT", command=check).pack()


# ---------------- SUSPECTS ----------------
def suspects():
    s = tk.Toplevel()
    s.title("CIS // Suspects")
    s.configure(bg=BG)
    s.geometry("400x300")

    tk.Label(s, text="SELECT SUSPECT",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Button(s, text="▶ Wife", bg="#020617", fg=GREEN,
              command=lambda: interrogation(s, "Wife")).pack(pady=5)

    tk.Button(s, text="▶ Business Partner", bg="#020617", fg=GREEN,
              command=lambda: interrogation(s, "Partner")).pack(pady=5)

    tk.Button(s, text="▶ Employee", bg="#020617", fg=GREEN,
              command=lambda: interrogation(s, "Employee")).pack(pady=5)


# ---------------- INTERROGATION ----------------
def interrogation(prev, suspect):
    prev.destroy()

    i = tk.Toplevel()
    i.title("CIS // Interrogation")
    i.configure(bg=BG)
    i.geometry("450x300")

    tk.Label(i, text=f"Interrogating: {suspect}",
             fg=CYAN, bg=BG).pack(pady=10)

    tk.Label(i, text="Encrypted Message: SDUWHU",
             fg=GREEN, bg=BG).pack()

    tk.Label(i, text="Hint: Caesar Cipher (+3)",
             fg=GREEN, bg=BG).pack()

    entry = tk.Entry(i, bg="black", fg=GREEN)
    entry.pack(pady=10)

    result_label = tk.Label(i, text="", bg=BG)
    result_label.pack()

    def check():
        if entry.get().lower() == "partner":
            result_label.config(text="✅ DECRYPTED", fg=GREEN)

            tk.Button(i, text="▶ CONTINUE",
                      command=lambda: show_story(i, [
                          "The message reveals the truth...",
                          "The partner feared exposure...",
                          "Financial fraud was about to be exposed...",
                          "Motive confirmed.",
                          "Time to make your final decision."
                      ], final_choice)
                      ).pack()
        else:
            result_label.config(text="❌ WRONG", fg="red")

    tk.Button(i, text="SUBMIT", command=check).pack()


# ---------------- FINAL DECISION ----------------
def final_choice():
    f = tk.Toplevel()
    f.title("CIS // Final Decision")
    f.configure(bg=BG)
    f.geometry("400x300")

    tk.Label(f, text="WHO IS THE KILLER?",
             fg=CYAN, bg=BG).pack(pady=10)

    def result(choice):
        f.destroy()

        if choice == "Partner":
            ending = [
                "You accuse the partner...",
                "He tries to escape...",
                "But security catches him.",
                "He confesses everything.",
                "🎉 CASE SOLVED"
            ]
        else:
            ending = [
                "Wrong accusation...",
                "The real killer escapes...",
                "Case remains unsolved...",
                "⚠ MISSION FAILED"
            ]

        show_story(f, ending, lambda: None)

    tk.Button(f, text="Wife", command=lambda: result("Wife")).pack(pady=5)
    tk.Button(f, text="Partner", command=lambda: result("Partner")).pack(pady=5)
    tk.Button(f, text="Employee", command=lambda: result("Employee")).pack(pady=5)