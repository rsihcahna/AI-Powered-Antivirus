# utils.py

import hashlib
import os
import time

def calculate_sha256(file_path):
    """Calculate SHA256 hash of a file."""
    sha256 = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for chunk in iter(lambda: f.read(4096), b""):
                sha256.update(chunk)
        return sha256.hexdigest()
    except Exception as e:
        return f"Error: {str(e)}"

def get_all_files(directory):
    """Recursively list all files in a directory."""
    file_list = []
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_list.append(os.path.join(root, file))
    return file_list

def format_time(timestamp=None):
    """Return human-readable time format."""
    if timestamp is None:
        timestamp = time.time()
    return time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(timestamp))

# Example usage
if __name__ == "__main__":
    print("Hash:", calculate_sha256("utils.py"))
    print("Files:", get_all_files("."))
    print("Time:", format_time())
