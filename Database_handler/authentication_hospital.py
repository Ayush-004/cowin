from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Hospital name"]
def identify_hospital(hospital_id):
    # Query the database for the hospital record
    query = {"hospital_id": hospital_id}
    hospital_record = collection.find_one(query)
    
    if hospital_record:
        print("Hospital identified successfully!")
        return hospital_record
    else:
        print("Hospital not found.")
        return None

if __name__ == "__main__":
    # Example usage
    hospital = identify_hospital("123456")
    if hospital:
        print("Hospital Name:", hospital["hospital_name"])
        print("Location:", hospital["city"], ",", hospital["state"])
    else:
        print("Hospital not found.")

