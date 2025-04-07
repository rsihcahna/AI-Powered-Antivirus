# /backend/logger.py

import os
import json
from datetime import datetime

LOG_FILE_PATH = "backend/data/system_logs.json"

# Ensure the logs directory and file exist
os.makedirs(os.path.dirname(LOG_FILE_PATH), exist_ok=True)
if not os.path.exists(LOG_FILE_PATH):
    with open(LOG_FILE_PATH, "w") as f:
        f.write("")

def log_event(event, details=None):
    """
    Logs events with a timestamp to a JSON lines file.
    """
    log_entry = {
        "timestamp": datetime.utcnow().isoformat() + "Z",
        "event": event,
        "details": details or {}
    }

    try:
        with open(LOG_FILE_PATH, "a") as f:
            f.write(json.dumps(log_entry) + "\n")
    except Exception as e:
        print(f"Failed to write log: {e}")
