# 📄 backend/api_routes.py
# 🌐 Flask API Routes for AI-Powered Antivirus

from flask import Blueprint, request, jsonify
from ai_model.predict import predict_malware
from utils import extract_features
from database import insert_log as store_log, insert_threat as store_threat, using_json_storage
from alert_system import trigger_alert
import os
import datetime

api = Blueprint("api", __name__)

UPLOAD_FOLDER = "backend/uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@api.route('/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    file_path = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(file_path)

    result = predict_malware(file_path)

    log_data = {
        "filename": file.filename,
        "timestamp": datetime.datetime.now().isoformat(),
        "prediction": result.get("label", "error"),
        "confidence": result.get("confidence", 0)
    }

    store_log(log_data)

    if result.get("label") == "malware":
        store_threat(log_data)
        trigger_alert(file.filename)

    return jsonify({
        "filename": file.filename,
        "result": result,
        "storage": "JSON" if using_json_storage else "MongoDB"
    })

@api.route('/logs', methods=['GET'])
def get_logs():
    from database import get_all_logs
    logs = get_all_logs()
    return jsonify(logs)

@api.route('/threats', methods=['GET'])
def get_threats():
    from database import get_all_threats
    threats = get_all_threats()
    return jsonify(threats)
