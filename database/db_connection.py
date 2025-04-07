# /database/db_connection.py
import sqlite3

def connect_db(db_name="antivirus.db"):
    conn = sqlite3.connect(db_name)
    return conn
