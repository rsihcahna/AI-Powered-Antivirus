# /backend/alert_system.py

import datetime
from logger import log_event
from database import store_threat, using_json_storage

def trigger_alert(filename, confidence, label="malware"):
    """
    Triggers an alert when a malicious file is detected.
    Stores the alert in the database (MongoDB or JSON based on availability).
    """
    alert = {
        "filename": filename,
        "label": label,
        "confidence": confidence,
        "timestamp": datetime.datetime.now().isoformat(),
        "source": "AI Engine"
    }

    try:
        store_threat(alert)
        log_event("Threat detected and stored", alert)
    except Exception as e:
        log_event("Failed to trigger alert", {"error": str(e), "alert": alert})
