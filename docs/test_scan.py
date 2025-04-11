import requests

# Replace with your actual backend URL
URL = "https://antivirus-backend.onrender.com/api/scan"

# Replace with the path to your test file
FILE_PATH = "sample_file.exe"  # or sample.txt, etc.

with open(FILE_PATH, 'rb') as file:
    files = {'file': file}
    response = requests.post(URL, files=files)

print("Status Code:", response.status_code)
print("Response:")
print(response.text)
