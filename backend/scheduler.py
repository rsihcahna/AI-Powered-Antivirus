# /backend/scheduler.py

import threading
import time
from logger import log_event

def background_task():
    """
    This function runs in the background for periodic operations.
    You can customize it to perform scheduled directory scans,
    periodic log cleanups, or health checks.
    """
    while True:
        log_event("Scheduler heartbeat", "Background task is alive.")
        # You can plug in any periodic functionality here
        time.sleep(3600)  # Run every 1 hour

def start_scheduler():
    """
    Starts the background scheduler in a separate daemon thread.
    """
    thread = threading.Thread(target=background_task)
    thread.daemon = True
    thread.start()
    log_event("Scheduler", "Background task started.")
