# 📝 Log scan history
import sqlite3
from datetime import datetime

DB_NAME = 'scan_results.db'

def init_db():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE IF NOT EXISTS scans (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        file_name TEXT,
        scan_result TEXT,
        prediction TEXT,
        timestamp TEXT
    )''')
    conn.commit()
    conn.close()

def log_scan(file_name, scan_result, prediction):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO scans (file_name, scan_result, prediction, timestamp) VALUES (?, ?, ?, ?)", 
                   (file_name, scan_result, prediction, datetime.now().strftime("%Y-%m-%d %H:%M:%S")))
    conn.commit()
    conn.close()

# Initialize DB on module import
init_db()
