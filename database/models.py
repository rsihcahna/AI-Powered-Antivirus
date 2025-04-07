# /database/models.py
from database.db_connection import connect_db

def create_tables():
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS malware_signatures (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            signature TEXT UNIQUE NOT NULL,
            description TEXT,
            threat_level TEXT,
            source TEXT
        );
    ''')
    conn.commit()
    conn.close()
