# 📄 predict.py
# 🔍 ML-based malware threat predictor

import os
import json
import joblib
import numpy as np

# Dynamically resolve absolute path to the model
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH = os.path.join(BASE_DIR, "backend", "malware_model.pkl")

# ✅ Load the model once
if os.path.exists(MODEL_PATH):
    model = joblib.load(MODEL_PATH)
else:
    print(f"❌ Model not found at {MODEL_PATH}")
    model = None


def extract_features(file_path):
    """
    Placeholder for actual feature extraction logic.
    Currently uses dummy feature based on file size.
    """
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            size = len(content) % 100  # Dummy numerical feature
        return [size]
    except Exception as e:
        print(f"❌ Feature extraction failed: {e}")
        return []

def predict_malware(file_path):
    """
    Predicts whether a file is malware or benign using the trained ML model.
    Returns a dictionary with the label and probability.
    """
    if not model:
        return {"error": "Model not loaded."}

    features = extract_features(file_path)
    if not features:
        return {"error": "Failed to extract features."}

    try:
        prediction = model.predict([features])[0]
        proba = model.predict_proba([features])[0].max()
        label = "malware" if prediction == 1 else "benign"
        return {"label": label, "confidence": round(proba, 4)}
    except Exception as e:
        return {"error": str(e)}

# CLI Test Mode
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
