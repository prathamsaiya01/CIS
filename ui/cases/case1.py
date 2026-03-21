import tkinter as tk
from logic.puzzles import password_cracker, cipher_game

# ---------------- STORY ENGINE ----------------

def show_story(prev, text_list, next_func):
    prev.destroy()

    story = tk.Toplevel()
    story.title("Story")

    label = tk.Label(story, text="", wraplength=400, font=("Arial", 11))
    label.pack(pady=20)

    index = [0]

    def next_text():
        if index[0] < len(text_list):
            label.config(text=text_list[index[0]])
            index[0] += 1
        else:
            story.destroy()
            next_func()

    tk.Button(story, text="Next", command=next_text).pack(pady=10)

    next_text()


# ---------------- ENTRY ----------------

def open_case1(prev):
    story_text = [
        "It was a cold, silent night...",
        "A wealthy businessman was found dead in his apartment.",
        "No signs of forced entry.",
        "Only one thing was clear...",
        "This was not a normal murder."
    ]

    show_story(prev, story_text, crime_scene)


# ---------------- CRIME SCENE ----------------

def crime_scene():
    scene = tk.Toplevel()
    scene.title("Crime Scene")

    tk.Label(scene, text="Crime Scene Evidence", font=("Arial", 14)).pack(pady=10)
    tk.Label(scene, text="• Broken Glass\n• Laptop\n• Blood Stain").pack()

    tk.Button(scene, text="Examine Laptop",
              command=lambda: show_story(scene, [
                  "You approach the laptop...",
                  "It is locked with a password...",
                  "This might contain crucial evidence..."
              ], laptop_puzzle)).pack(pady=10)


# ---------------- PASSWORD PUZZLE ----------------

def laptop_puzzle():
    game = tk.Toplevel()
    game.title("Laptop Locked")

    tk.Label(game, text="Enter password to unlock laptop").pack()

    entry = tk.Entry(game)
    entry.pack()

    result_label = tk.Label(game, text="")
    result_label.pack()

    def check():
        correct, _ = password_cracker(entry.get())

        if correct:
            result_label.config(text="✅ Laptop Unlocked!")

            tk.Button(game, text="Next",
                command=lambda: show_story(game, [
                    "The laptop opens...",
                    "You find suspicious messages...",
                    "Three people were in contact with the victim..."
                ], suspects)
            ).pack()

        else:
            result_label.config(text="❌ Wrong password")

    tk.Button(game, text="Submit", command=check).pack()


# ---------------- SUSPECTS ----------------

def suspects():
    s = tk.Toplevel()
    s.title("Suspects")

    tk.Label(s, text="Choose a suspect to interrogate").pack()

    tk.Button(s, text="Wife", command=lambda: interrogation(s)).pack()
    tk.Button(s, text="Partner", command=lambda: interrogation(s)).pack()
    tk.Button(s, text="Employee", command=lambda: interrogation(s)).pack()


# ---------------- INTERROGATION ----------------

def interrogation(prev):
    prev.destroy()

    i = tk.Toplevel()
    i.title("Interrogation")

    tk.Label(i, text="Suspect gives encrypted message: EQFG").pack()

    entry = tk.Entry(i)
    entry.pack()

    result_label = tk.Label(i, text="")
    result_label.pack()

    def check():
        correct, _ = cipher_game(entry.get())

        if correct:
            result_label.config(text="✅ Message decrypted!")

            tk.Button(i, text="Next",
                command=lambda: show_story(i, [
                    "The message reveals a hidden truth...",
                    "The suspect is lying...",
                    "You are close to solving the case..."
                ], final_choice)
            ).pack()

        else:
            result_label.config(text="❌ Wrong decryption")

    tk.Button(i, text="Submit", command=check).pack()


# ---------------- FINAL DECISION ----------------

def final_choice():
    f = tk.Toplevel()
    f.title("Final Decision")

    tk.Label(f, text="Who is the killer?", font=("Arial", 14)).pack(pady=10)

    def result(choice):
        f.destroy()

        if choice == "Partner":
            ending = [
                "You accuse the partner...",
                "He breaks down under pressure...",
                "Confession recorded.",
                "🎉 Case Solved Successfully!"
            ]
        else:
            ending = [
                "Your accusation was wrong...",
                "The real killer escapes...",
                "The case remains unsolved..."
            ]

        show_story(f, ending, lambda: None)

    tk.Button(f, text="Wife", command=lambda: result("Wife")).pack()
    tk.Button(f, text="Partner", command=lambda: result("Partner")).pack()
    tk.Button(f, text="Employee", command=lambda: result("Employee")).pack()