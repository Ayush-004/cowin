from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["User Name"]
def authenticate_user(aadhar_number):
    # Query the database for the user record
    query = {"aadhar_number": aadhar_number}
    user_record = collection.find_one(query)
    
    if user_record:
        print("User authenticated successfully!")
        return True
    else:
        print("User not found. Authentication failed.")
        return False

if __name__ == "__main__":
    # Example usage
    authenticate_user("12345678sdfa2")
