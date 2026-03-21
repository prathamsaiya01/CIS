import tkinter as tk
from logic.puzzles import pattern_game, cipher_game
import random

def open_case4(prev):
    prev.destroy()

    story = tk.Toplevel()
    story.title("Case 4: Kidnapping")

    tk.Label(story, text="CASE: Kidnapping", font=("Arial", 16)).pack(pady=10)

    tk.Label(
        story,
        text="A child has been kidnapped.\nYou received a suspicious message.\nTime is running out!",
        wraplength=300
    ).pack(pady=10)

    tk.Button(story, text="Start Rescue Mission",
              command=lambda: phone_clue(story)).pack(pady=10)

# ---------------- STEP 1: PHONE CLUE ----------------

def phone_clue(prev):
    prev.destroy()

    phone = tk.Toplevel()
    phone.title("Phone Clue")

    tk.Label(phone, text="Kidnapper Message:", font=("Arial", 12)).pack(pady=10)
    tk.Label(phone, text="VJG NQECVKQP KU UGETGV").pack()

    tk.Label(phone, text="Hint: Shift letters back by 2").pack(pady=5)

    entry = tk.Entry(phone)
    entry.pack()

    result_label = tk.Label(phone, text="")
    result_label.pack()

    def check():
        correct, _ = cipher_game(entry.get())

        if correct:
            result_label.config(text="✅ Message decoded!")
            tk.Button(phone, text="Analyze Location",
                      command=lambda: location_puzzle(phone)).pack()
        else:
            result_label.config(text="❌ Wrong decryption")

    tk.Button(phone, text="Submit", command=check).pack(pady=10)

# ---------------- STEP 2: LOCATION PUZZLE ----------------

def location_puzzle(prev):
    prev.destroy()

    loc = tk.Toplevel()
    loc.title("Location Puzzle")

    tk.Label(loc, text="Find next number to trace coordinates").pack(pady=10)
    tk.Label(loc, text="5, 10, 20, 40, ?").pack()

    entry = tk.Entry(loc)
    entry.pack()

    result_label = tk.Label(loc, text="")
    result_label.pack()

    def check():
        correct, _ = pattern_game(entry.get())

        if correct:
            result_label.config(text="✅ Coordinates matched!")
            tk.Button(loc, text="Search Area",
                      command=lambda: hidden_clue(loc)).pack()
        else:
            result_label.config(text="❌ Wrong answer")

    tk.Button(loc, text="Submit", command=check).pack(pady=10)

# ---------------- STEP 3: HIDDEN CLUE ----------------

def hidden_clue(prev):
    prev.destroy()

    clue = tk.Toplevel()
    clue.title("Search Area")

    tk.Label(clue, text="Searching abandoned warehouse...").pack(pady=10)

    found = random.choice([True, False])

    if found:
        tk.Label(clue, text="🎉 Hidden clue found: Rope + Footprints").pack()
    else:
        tk.Label(clue, text="No obvious clues found...").pack()

    tk.Button(clue, text="Final Decision",
              command=lambda: final_choice(clue)).pack(pady=10)

# ---------------- FINAL DECISION ----------------

def final_choice(prev):
    prev.destroy()

    f = tk.Toplevel()
    f.title("Final Decision")

    tk.Label(f, text="Where is the victim?", font=("Arial", 14)).pack(pady=10)

    def result(choice):
        if choice == "Warehouse":
            tk.Label(f, text="✅ Correct! Victim rescued in time").pack()
        else:
            tk.Label(f, text="❌ Wrong location! Time lost").pack()

    tk.Button(f, text="Warehouse", command=lambda: result("Warehouse")).pack(pady=5)
    tk.Button(f, text="Apartment", command=lambda: result("Apartment")).pack(pady=5)
    tk.Button(f, text="Office", command=lambda: result("Office")).pack(pady=5)