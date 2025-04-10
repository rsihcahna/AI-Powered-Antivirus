# 📄 backend/logger.py
# 📘 Logging utility for events

import os
import datetime
import json

LOG_DIR = "backend/logs"
os.makedirs(LOG_DIR, exist_ok=True)

LOG_FILE = os.path.join(LOG_DIR, "events.log")

def log_event(event_type, data=None):
    """
    Logs an event with a timestamp, type, and optional data.
    """
    log_entry = {
        "timestamp": datetime.datetime.now().isoformat(),
        "event_type": event_type,
        "data": data
    }

    try:
        with open(LOG_FILE, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"[Logger Error] Failed to write log: {e}")

if __name__ == "__main__":
    # Test logging
    log_event("test_log", {"example": "test"})
