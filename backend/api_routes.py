# /backend/api_routes.py

from flask import Blueprint, request, jsonify
from werkzeug.utils import secure_filename
import os
import tempfile

from ai_model.predict import predict_malware
from database import insert_threat, insert_log, get_all_threats, get_all_logs
from alert_system import trigger_alert

api = Blueprint("api", __name__)

@api.route('/api/scan', methods=['POST'])
def scan_file():
    if 'file' not in request.files:
        return jsonify({"error": "No file part in the request"}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    filename = secure_filename(file.filename)

    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
        file.save(temp_file.name)
        result = predict_malware(temp_file.name)

    # Log result
    threat_data = {
        "filename": filename,
        "result": result,
        "status": result.get("label", "error")
    }

    insert_threat(threat_data)
    insert_log({
        "event": "File Scanned",
        "filename": filename,
        "result": result
    })

    if result.get("label") == "malware":
        trigger_alert(filename)

    return jsonify({
        "filename": filename,
        "prediction": result.get("label"),
        "confidence": result.get("confidence", "N/A")
    })

@api.route('/api/logs', methods=['GET'])
def get_logs():
    logs = get_all_logs()
    return jsonify(logs)

@api.route('/api/threats', methods=['GET'])
def get_threats():
    threats = get_all_threats()
    return jsonify(threats)
