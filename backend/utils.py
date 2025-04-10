# 📄 backend/utils.py
# 🧰 Utility functions

import os

def extract_features(file_path):
    """
    Simplified feature extractor. Replace with real logic later.
    Currently returns the modulo of file size as dummy feature.
    """
    try:
        with open(file_path, 'rb') as f:
            content = f.read()
            size_feature = len(content) % 100  # Simple numerical feature
        return [size_feature]
    except Exception as e:
        print(f"[Feature Extraction Error] {e}")
        return []

def ensure_directory_exists(path):
    """
    Ensures a directory exists; creates it if it doesn't.
    """
    if not os.path.exists(path):
        os.makedirs(path)

if __name__ == "__main__":
    # Test feature extraction
    test_file = "test.bin"
    with open(test_file, "wb") as f:
        f.write(os.urandom(1234))

    features = extract_features(test_file)
    print("Extracted features:", features)
