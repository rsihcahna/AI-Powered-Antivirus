# alert_system.py
from logger import log_event

def send_alert(threat_type: str, location: str, severity: str):
    alert_message = (
        f"[ALERT] Threat Detected!\n"
        f"Type: {threat_type}\n"
        f"Location: {location}\n"
        f"Severity: {severity}\n"
    )
    print(alert_message)
    log_event(f"ALERT: {alert_message}")
