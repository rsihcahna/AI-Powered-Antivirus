# /backend/database.py

from pymongo import MongoClient
from logger import log_event

# Setup MongoDB connection
client = MongoClient("mongodb+srv://<username>:<password>@<your-cluster>.mongodb.net/antivirus?retryWrites=true&w=majority")
db = client["antivirus"]

# Collections
logs_collection = db["logs"]
threats_collection = db["threats"]

def insert_log(log_data):
    try:
        logs_collection.insert_one(log_data)
        log_event("Log inserted to MongoDB", log_data)
    except Exception as e:
        log_event("MongoDB Insert Error", {"error": str(e), "log_data": log_data})

def insert_threat(threat_data):
    try:
        threats_collection.insert_one(threat_data)
        log_event("Threat inserted to MongoDB", threat_data)
    except Exception as e:
        log_event("MongoDB Insert Error", {"error": str(e), "threat_data": threat_data})

def get_all_threats():
    return list(threats_collection.find({}))

def get_all_logs():
    return list(logs_collection.find({}))
