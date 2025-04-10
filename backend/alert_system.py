# 📄 backend/alert_system.py
# 🚨 Handles threat alerts

from database import store_threat, using_json_storage
from logger import log_event
import datetime

def trigger_alert(filename, prediction=None, confidence=None):
    """
    Triggers an alert when malware is detected.
    Stores the threat details and logs the event.
    """
    threat_data = {
        "filename": filename,
        "prediction": prediction or "malware",
        "confidence": confidence or "N/A",
        "timestamp": datetime.datetime.now().isoformat()
    }

    try:
        store_threat(threat_data)
        log_event("ALERT", f"Malware detected in {filename} (confidence: {confidence})")
        if using_json_storage:
            print(f"[🔴] ALERT: {filename} flagged as malware. Logged in local JSON.")
        else:
            print(f"[🔴] ALERT: {filename} flagged as malware. Stored in MongoDB.")
    except Exception as e:
        log_event("ALERT_FAILURE", f"Failed to trigger alert for {filename}: {str(e)}")
