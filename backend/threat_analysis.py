# 📄 backend/threat_analysis.py
# 📊 Provides basic analytics on detected threats

from database import get_all_threats
from collections import Counter
import datetime

def analyze_threats():
    """
    Analyzes all logged threats and returns summary statistics.
    """
    threats = get_all_threats()
    if not threats:
        return {
            "total_threats": 0,
            "by_filename": {},
            "by_day": {}
        }

    # Count threats by filename
    filename_counts = Counter([t.get("filename", "unknown") for t in threats])

    # Count threats by day
    day_counts = Counter()
    for t in threats:
        timestamp = t.get("timestamp")
        if timestamp:
            try:
                dt = datetime.datetime.fromisoformat(timestamp)
                day = dt.date().isoformat()
                day_counts[day] += 1
            except Exception:
                pass

    return {
        "total_threats": len(threats),
        "by_filename": dict(filename_counts),
        "by_day": dict(day_counts)
    }

if __name__ == "__main__":
    # For testing directly
    summary = analyze_threats()
    print(summary)
