import time
import random

score = 0
risk_level = 0

# ---------------- TIMER ----------------

def start_timer():
    return time.time()

def check_timer(start, limit=20):
    return (time.time() - start) <= limit

# ---------------- RISK ----------------

def update_risk(correct):
    global risk_level
    if correct:
        risk_level -= 5
    else:
        risk_level += 10
    return risk_level

# ---------------- RANK ----------------

def calculate_rank(score):
    if score >= 300:
        return "Elite Investigator"
    elif score >= 200:
        return "Pro Detective"
    return "Rookie"

# ---------------- CLUES ----------------

def get_clue():
    if random.randint(1, 5) == 3:
        return "Hidden clue found! Bonus +50"
    return None