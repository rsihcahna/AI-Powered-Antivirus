# File: backend/main.py

from flask import Flask, request, jsonify
from scanner import scan_file
from ai_model.predict import predict_malware
import os

app = Flask(__name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def home():
    return "AI-Powered Antivirus Backend is running."

@app.route('/scan', methods=['POST'])
def scan():
    if 'file' not in request.files:
        return jsonify({"error": "No file provided"}), 400

    file = request.files['file']
    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    scan_result = scan_file(file_path)
    ml_prediction = predict_malware(file_path)

    return jsonify({
        "signature_scan_result": scan_result,
        "ml_prediction": ml_prediction
    })

if __name__ == '__main__':
    app.run(debug=True)
