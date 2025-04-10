# /backend/database.py

import os
import json
from pymongo import MongoClient, errors
from urllib.parse import quote_plus
from logger import log_event

# MongoDB credentials
username = quote_plus("rsihcahna")
password = quote_plus("Shaan_@1808")
uri = f"mongodb+srv://{username}:{password}@cluster0.lmnljuf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# JSON fallback files
DATA_DIR = "backend/data"
LOGS_FILE = os.path.join(DATA_DIR, "logs.json")
THREATS_FILE = os.path.join(DATA_DIR, "threats.json")

# Ensure fallback directory and files exist
os.makedirs(DATA_DIR, exist_ok=True)
for file_path in [LOGS_FILE, THREATS_FILE]:
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            f.write("")  # Create empty file

# MongoDB connection attempt
try:
    client = MongoClient(uri, serverSelectionTimeoutMS=5000)
    client.server_info()  # Trigger exception if not connected
    db = client["antivirus"]
    logs_collection = db["logs"]
    threats_collection = db["threats"]
    mongodb_connected = True
    log_event("MongoDB connected", {})
except errors.ServerSelectionTimeoutError as e:
    mongodb_connected = False
    log_event("MongoDB connection failed", {"error": str(e)})

# ✅ Expose fallback flag to other modules
using_json_storage = not mongodb_connected

# Insert log (MongoDB or fallback)
def insert_log(log_data):
    if mongodb_connected:
        try:
            logs_collection.insert_one(log_data)
            log_event("Log inserted to MongoDB", log_data)
        except Exception as e:
            log_event("MongoDB Log Insert Error", {"error": str(e)})
    else:
        with open(LOGS_FILE, 'a') as f:
            f.write(json.dumps(log_data) + "\n")
        log_event("Log saved to local file", log_data)

# Insert threat (MongoDB or fallback)
def insert_threat(threat_data):
    if mongodb_connected:
        try:
            threats_collection.insert_one(threat_data)
            log_event("Threat inserted to MongoDB", threat_data)
        except Exception as e:
            log_event("MongoDB Threat Insert Error", {"error": str(e)})
    else:
        with open(THREATS_FILE, 'a') as f:
            f.write(json.dumps(threat_data) + "\n")
        log_event("Threat saved to local file", threat_data)

# Get all logs
def get_all_logs():
    if mongodb_connected:
        return list(logs_collection.find({}))
    else:
        return [json.loads(line) for line in open(LOGS_FILE, 'r') if line.strip()]

# Get all threats
def get_all_threats():
    if mongodb_connected:
        return list(threats_collection.find({}))
    else:
        return [json.loads(line) for line in open(THREATS_FILE, 'r') if line.strip()]
