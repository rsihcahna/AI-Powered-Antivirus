# 📄 virustotal_test.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("VIRUSTOTAL_API_KEY")

def check_file_with_virustotal(file_path):
    url = "https://www.virustotal.com/api/v3/files"

    headers = {
        "x-apikey": API_KEY
    }

    files = {
        'file': (os.path.basename(file_path), open(file_path, 'rb'))
    }

    print("[*] Uploading file to VirusTotal...")

    response = requests.post(url, headers=headers, files=files)

    if response.status_code == 200:
        result = response.json()
        scan_id = result["data"]["id"]
        print(f"[+] File uploaded. Scan ID: {scan_id}")
        return scan_id
    else:
        print("[!] Failed to upload file:", response.status_code, response.text)
        return None

if __name__ == "__main__":
    test_file = "test_sample.py"  # Replace with a real file path to test
    if os.path.isfile(test_file):
        check_file_with_virustotal(test_file)
    else:
        print("[!] Test file does not exist. Please add a file named 'test_sample.exe' in the backend folder.")
