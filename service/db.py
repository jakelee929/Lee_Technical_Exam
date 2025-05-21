from pymongo import MongoClient, ASCENDING
import os
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")
DB_NAME = "medals_db"
COLLECTION_NAME = "medalists"

try:
    client = MongoClient(MONGO_URI, serverSelectionTimeoutMS=5000)
    # Trigger a connection check
    client.server_info()
except Exception as e:
    raise RuntimeError(f"Could not connect to MongoDB at {MONGO_URI}: {e}")

# Access DB and collection (created lazily by MongoDB on insert)
db = client[DB_NAME]
collection = db[COLLECTION_NAME]

# Optional: Confirm collection exists or log a message
if COLLECTION_NAME not in db.list_collection_names():
    print(f"⚠️ Collection '{COLLECTION_NAME}' does not yet exist in '{DB_NAME}' (will be created on first insert)")
else:
    print(f"✅ Connected to MongoDB collection '{DB_NAME}.{COLLECTION_NAME}' successfully!")

client = MongoClient(os.getenv("MONGO_URI"))
db = client["medals_db"]
collection = db["medalists"]

def insert_medalists(data):
    if data:
        collection.insert_many(data)

def get_aggregated_event_stats(page, limit=10):
    skip = (page - 1) * limit
    pipeline = [
        {"$group": {
            "_id": {"discipline": "$discipline", "event": "$event", "event_date": "$event_date"},
            "medalists": {"$push": {
                "name": "$name",
                "medal_type": "$medal_type",
                "gender": "$gender",
                "country": "$country",
                "country_code": "$country_code",
                "nationality": "$nationality",
                "medal_code": "$medal_code",
                "medal_date": "$medal_date"
            }}
        }},
        {"$skip": skip},
        {"$limit": limit}
    ]
    results = list(collection.aggregate(pipeline))
    return {"data": results}
