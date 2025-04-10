# 📄 clamav_scanner.py
# 🔬 ClamAV-based signature scanner

import subprocess
import os
from logger import log_event

CLAMAV_SCAN_COMMAND = "clamscan"

def scan_with_clamav(file_path):
    """
    Scans the given file using ClamAV and returns the scan result.
    Returns:
        - 'clean' if no threats found.
        - 'infected' if a virus/malware is detected.
        - 'error' if something goes wrong.
    """
    try:
        if not os.path.exists(file_path):
            return {"status": "error", "message": "File not found"}

        result = subprocess.run(
            [CLAMAV_SCAN_COMMAND, "--no-summary", file_path],
            capture_output=True, text=True
        )
        
        output = result.stdout.strip()
        if "OK" in output:
            status = "clean"
        elif "FOUND" in output:
            status = "infected"
        else:
            status = "unknown"

        log_event("ClamAV scan result", {"file": file_path, "status": status})
        return {"status": status, "output": output}

    except Exception as e:
        log_event("ClamAV scan error", {"file": file_path, "error": str(e)})
        return {"status": "error", "message": str(e)}
