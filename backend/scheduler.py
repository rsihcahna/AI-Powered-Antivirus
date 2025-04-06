# scheduler.py
import time
import threading
from ai_model.predict import run_ai_scan
from rust_engine.scanner import run_rust_scan
from go_model.network_monitor import run_network_monitor

def scheduled_task():
    while True:
        print("[Scheduler] Running scheduled scans...")
        run_ai_scan()
        run_rust_scan()
        run_network_monitor()
        print("[Scheduler] Waiting for the next cycle...\n")
        time.sleep(3600)  # Run every hour

def start_scheduler():
    thread = threading.Thread(target=scheduled_task)
    thread.daemon = True
    thread.start()
