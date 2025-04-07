# 📄 predict.py
# 🔍 ML-based malware threat predictor

import os
import json
import joblib
import numpy as np

# Updated model path
MODEL_PATH = "backend/ai_model/backend/malware_model.pkl"

# ✅ Load the model once
try:
    model = joblib.load(MODEL_PATH)
except FileNotFoundError:
    print(f"Model not found at {MODEL_PATH}")
    model = None

def extract_features(file_path):
    """
    Placeholder for actual feature extraction logic.
    For now, returns dummy numerical features.
    """
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            size = len(content) % 100  # Simplified dummy logic
        return [size]
    except Exception as e:
        print(f"Feature extraction failed: {e}")
        return []

def predict_malware(file_path):
    """
    Predicts whether a file is malware or benign using the trained ML model.
    Returns a dictionary with the label and probability.
    """
    features = extract_features(file_path)

    if not features or model is None:
        return {"error": "Feature extraction or model loading failed."}

    try:
        prediction = model.predict([features])[0]
        proba = model.predict_proba([features])[0].max()
        label = "malware" if prediction == 1 else "benign"
        return {"label": label, "confidence": round(proba, 4)}
    except Exception as e:
        return {"error": str(e)}

if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python predict.py <file_path>")
        exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        exit(1)

    result = predict_malware(file_path)
    print(json.dumps(result, indent=2))
