from flask import Blueprint, request, jsonify
from predict import predict_file
from logger import log_threat
from threat_analysis import analyze_threat
from database import save_to_db

api = Blueprint('api', __name__)

@api.route('/scan', methods=['POST'])
def scan_file():
    uploaded_file = request.files.get('file')
    if not uploaded_file:
        return jsonify({'error': 'No file uploaded'}), 400

    file_path = f"/tmp/{uploaded_file.filename}"
    uploaded_file.save(file_path)

    prediction = predict_file(file_path)
    analysis = analyze_threat(file_path)
    log_threat(file_path, prediction)
    save_to_db(file_path, prediction, analysis)

    return jsonify({
        'file': uploaded_file.filename,
        'prediction': prediction,
        'analysis': analysis
    })
