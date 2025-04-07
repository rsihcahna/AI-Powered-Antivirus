# 🔗 VirusTotal integration
import requests
fromdotenv import load_dotenv
import os
API_KEY = "9f0d7727dc1171f23299ee492131f1ae6aa29d7a9b3b2d8053f1ec67e54c098e"
VT_URL = "https://www.virustotal.com/api/v3/files"

def scan_file_virustotal(file_path):
    headers = {
        "x-apikey": API_KEY
    }
    with open(file_path, "rb") as file:
        files = {"file": file}
        response = requests.post(VT_URL, files=files, headers=headers)
    return response.json()
