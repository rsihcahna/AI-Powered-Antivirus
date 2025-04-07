from database import db

def test_mongo_connection():
    try:
        collections = db.list_collection_names()
        print("✅ MongoDB connection successful!")
        print("Collections:", collections)
    except Exception as e:
        print("❌ Connection failed:", e)

if __name__ == "__main__":
    test_mongo_connection()
