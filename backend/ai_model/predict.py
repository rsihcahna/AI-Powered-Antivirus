# 📄 predict.py
# 🔍 ML-based threat predictor

import pickle
import os
import json

def load_model(model_path='ai_model/model.pkl'):
    with open(model_path, 'rb') as f:
        model = pickle.load(f)
    return model

def extract_features(file_path):
    # Dummy feature extractor for now
    return [len(open(file_path, 'rb').read()) % 100]

def predict_malware(file_path):
    model = load_model()
    features = extract_features(file_path)
    prediction = model.predict([features])
    return prediction[0]

if __name__ == "__main__":
    import sys
    if len(sys.argv) < 2:
        print("Usage: python predict.py <file_path>")
        exit(1)

    file_path = sys.argv[1]
    if not os.path.isfile(file_path):
        print(f"File not found: {file_path}")
        exit(1)

    result = predict(file_path)
    print(json.dumps({"prediction": result}))
