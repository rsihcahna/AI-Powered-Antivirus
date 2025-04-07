import os
import csv
from pymongo import MongoClient
from urllib.parse import quote_plus

# --- MongoDB Credentials ---
username = quote_plus("rsihcahna")  # Replace
password = quote_plus("Shaan_@1808")  # Replace

cluster_uri = "cluster0.lmnljuf.mongodb.net"
database_name = "antivirus"
collection_name = "signatures"

mongo_uri = f"mongodb+srv://{username}:{password}@{cluster_uri}/{database_name}?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(mongo_uri)
db = client[database_name]
collection = db[collection_name]

# --- Path to your CSV folder ---
csv_folder = "malware_signatures"

def is_valid_row(row):
    return all(isinstance(k, str) and k.strip() != "" for k in row.keys())

def import_all_csvs(folder_path):
    total_inserted = 0
    for file in os.listdir(folder_path):
        if file.endswith(".csv"):
            file_path = os.path.join(folder_path, file)
            print(f"🔍 Processing: {file}")
            with open(file_path, newline='', encoding='utf-8') as f:
                reader = csv.DictReader(f)

                # Clean header
                if reader.fieldnames is None:
                    print(f"⚠️ Skipping file (no headers): {file}")
                    continue
                if any(h is None or h.strip() == "" for h in reader.fieldnames):
                    print(f"⚠️ Skipping file (malformed headers): {file}")
                    continue

                records = []
                for row in reader:
                    if is_valid_row(row):
                        records.append(row)

                if records:
                    collection.insert_many(records)
                    print(f"✅ Inserted {len(records)} from {file}")
                    total_inserted += len(records)
                else:
                    print(f"⚠️ No valid records found in {file}")

    print(f"\n🎉 Done. Total records inserted: {total_inserted}")

if __name__ == "__main__":
    import_all_csvs(csv_folder)
