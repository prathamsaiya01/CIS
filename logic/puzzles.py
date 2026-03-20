import random

# ---------------- PUZZLES ----------------

def password_cracker(answer):
    return (answer == "1234", 100 if answer == "1234" else 0)

def cipher_game(answer):
    return (answer.upper() == "CODE", 100 if answer.upper() == "CODE" else 0)

def pattern_game(answer):
    return (answer == "32", 100 if answer == "32" else 0)

def cyber_quiz(answer):
    return ("structured query language" in answer.lower(), 100 if "structured query language" in answer.lower() else 0)

def get_random_puzzle():
    return random.choice(["password", "cipher", "pattern", "quiz"])