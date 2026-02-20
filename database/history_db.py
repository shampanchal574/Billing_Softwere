import sqlite3
from datetime import datetime
import os

DB_PATH = os.path.join(os.path.dirname(__file__), "history.db")

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

# ---- Create table if not exists (basic) ----
cur.execute("""
CREATE TABLE IF NOT EXISTS history (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer TEXT,
    datetime TEXT
)
""")
conn.commit()

# ---- Auto-migrate missing columns safely ----
def ensure_column(name, col_type):
    cur.execute("PRAGMA table_info(history)")
    columns = [c[1] for c in cur.fetchall()]
    if name not in columns:
        cur.execute(f"ALTER TABLE history ADD COLUMN {name} {col_type}")
        conn.commit()

ensure_column("phone", "TEXT")
ensure_column("total", "REAL")
ensure_column("pdf", "TEXT")

# ---- Database functions ----
def add_history(customer, phone, total, pdf):
    cur.execute("""
        INSERT INTO history (customer, phone, total, datetime, pdf)
        VALUES (?, ?, ?, ?, ?)
    """, (
        customer,
        phone,
        total,
        datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        pdf
    ))
    conn.commit()

def search_history(keyword=""):
    cur.execute("""
        SELECT customer, phone, total, datetime, pdf
        FROM history
        WHERE customer LIKE ? OR phone LIKE ?
        ORDER BY id DESC
    """, (f"%{keyword}%", f"%{keyword}%"))
    return cur.fetchall()

def get_sales_summary(period):
    if period == "today":
        cur.execute("""
            SELECT SUM(total) FROM history
            WHERE date(datetime) = date('now')
        """)
    elif period == "week":
        cur.execute("""
            SELECT SUM(total) FROM history
            WHERE datetime >= date('now','-7 day')
        """)
    elif period == "month":
        cur.execute("""
            SELECT SUM(total) FROM history
            WHERE strftime('%Y-%m', datetime) = strftime('%Y-%m', 'now')
        """)
    return cur.fetchone()[0] or 0
def get_yearly_income():
    cur.execute("""
        SELECT SUM(total) FROM history
        WHERE strftime('%Y', datetime) = strftime('%Y', 'now')
    """)
    return cur.fetchone()[0] or 0
