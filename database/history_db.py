import sqlite3
from datetime import datetime

conn = sqlite3.connect("history.db")
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    datetime TEXT,
    pdf_path TEXT
)
""")
conn.commit()

def add_history(customer, pdf_path):
    cur.execute(
        "INSERT INTO history VALUES (NULL, ?, ?, ?)",
        (customer, datetime.now().strftime("%Y-%m-%d %H:%M:%S"), pdf_path)
    )
    conn.commit()

def get_history():
    cur.execute("SELECT customer, datetime, pdf_path FROM history ORDER BY id DESC")
    return cur.fetchall()
