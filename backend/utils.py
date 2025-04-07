# /backend/utils.py

def extract_features(file_bytes):
    """
    Extract features from a binary file content.
    Currently, this is a dummy implementation using file size mod 100.
    """
    try:
        size = len(file_bytes) % 100  # Basic logic
        return [size]
    except Exception as e:
        from logger import log_event
        log_event("Feature extraction error", {"error": str(e)})
        return []
