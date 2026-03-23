<<<<<<< HEAD
=======
from database.db import connect_db

def signup(username, password, avatar):
    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute(
            "INSERT INTO users (username, password, avatar) VALUES (?, ?, ?)",
            (username, password, avatar)
        )
        conn.commit()
        return True
    except:
        return False
    finally:
        conn.close()


>>>>>>> fb7855b8f66b1a487003ea679eeffb4acf2fc5e6
def login(username, password):
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM users WHERE username=? AND password=?",
        (username, password)
    )

    user = cursor.fetchone()
    conn.close()

    return user