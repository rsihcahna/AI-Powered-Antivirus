from flask import Flask, request, jsonify
from scanner import scan_file
from ai_model.predict import predict_malware
import os
import requests
import time

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

API_KEY = os.getenv("VT_API_KEY")  # Set your VirusTotal API key in env variable

@app.route('/')
def home():
    return "✅ AI-Powered Antivirus Backend is Running."

@app.route('/scan', methods=['POST'])
def scan():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    # 🧠 AI-based prediction
    ml_prediction = predict_malware(file_path)

    # 🔎 Signature-based scan
    signature_result = scan_file(file_path)

    # 🛡 Upload to VirusTotal
    vt_url = "https://www.virustotal.com/api/v3/files"
    headers = {"x-apikey": API_KEY}
    with open(file_path, "rb") as f:
        response = requests.post(vt_url, files={"file": f}, headers=headers)
    if response.status_code != 200:
        return jsonify({"error": "VirusTotal upload failed"}), 500

    analysis_id = response.json()["data"]["id"]

    # ⏳ Wait and fetch scan result
    report_url = f"https://www.virustotal.com/api/v3/analyses/{analysis_id}"
    for _ in range(10):  # Retry for 10 seconds
        report_resp = requests.get(report_url, headers=headers)
        report_data = report_resp.json()
        status = report_data['data']['attributes']['status']
        if status == "completed":
            break
        time.sleep(1)
    else:
        return jsonify({"error": "VirusTotal scan timed out"}), 504

    stats = report_data['data']['attributes']['stats']
    results = report_data['data']['attributes']['results']
    detailed_results = {
        engine: {
            "category": details["category"],
            "result": details.get("result", "N/A")
        } for engine, details in results.items()
    }

    return jsonify({
        "ai_prediction": ml_prediction,
        "signature_scan_result": signature_result,
        "virustotal_summary": stats,
        "virustotal_detailed_results": detailed_results
    })

if __name__ == '__main__':
    app.run(debug=True)
