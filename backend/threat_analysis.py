# /backend/threat_analysis.py

from ai_model.predict import predict_threat
from utils import load_file_content
from logger import log_event

def analyze_file(file_path):
    try:
        # Load the file content
        content = load_file_content(file_path)
        
        # Run prediction
        is_threat, confidence = predict_threat(content)

        # Log result
        result = {
            "file": file_path,
            "threat_detected": is_threat,
            "confidence": confidence
        }
        log_event("Threat Analysis Result", result)
        
        return result
    except Exception as e:
        log_event("Error", {"error": str(e), "file": file_path})
        return {"error": str(e), "file": file_path}
