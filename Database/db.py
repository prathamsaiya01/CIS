import sqlite3

def connect_db():
    conn = sqlite3.connect("cis.db", check_same_thread=False)
    return conn


def create_tables():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        avatar TEXT,
        role TEXT DEFAULT 'investigator',
        score INTEGER DEFAULT 0,
        level INTEGER DEFAULT 1,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    )
    """)

    conn.commit()
    conn.close()