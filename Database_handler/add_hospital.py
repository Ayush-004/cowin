from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Hospital name"]
def insert_hospital_data(hospital_name, city, state, hospital_id):
    # Create record object
    record = {
        "hospital_name": hospital_name,
        "city": city,
        "state": state,
        "hospital_id": hospital_id,
    }
    
    # Insert record into MongoDB
    collection.insert_one(record)
    print("Hospital data inserted successfully!")