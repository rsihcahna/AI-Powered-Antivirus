# 🛡️ ClamAV Scanner Integration
import subprocess

def scan_with_clamav(file_path):
    try:
        result = subprocess.run(['clamscan', file_path], capture_output=True, text=True)
        return result.stdout
    except Exception as e:
        return f"Error running ClamAV: {str(e)}"
