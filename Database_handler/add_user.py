from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Modern project"]
def insert_vaccine_record(aadhar_number, name, mobile_number, vaccine_name, date_of_dose1, serial_number_dose1, date_of_dose2, serial_number_dose2, city, state):
    # Convert date strings to datetime objects
    date_of_dose1 = datetime.strptime(date_of_dose1, "%Y-%m-%d")
    date_of_dose2 = datetime.strptime(date_of_dose2, "%Y-%m-%d")
    
    # Create record object
    record = {
        "aadhar_number": aadhar_number,
        "name": name,
        "mobile_number": mobile_number,
        "vaccine_name": vaccine_name,
        "date_of_dose1": date_of_dose1,
        "serial_number_dose1": serial_number_dose1,
        "date_of_dose2": date_of_dose2,
        "serial_number_dose2": serial_number_dose2,
        "city": city,
        "state": state
    }
    
    # Insert record into MongoDB
    collection.insert_one(record)
    print("Record inserted successfully!")

if __name__ == "__main__":
    # Example usage
    insert_vaccine_record(
        "123456789012",
        "John Doe",
        "9876543210",
        "Pfizer",
        "2023-01-15",
        "12345",
        "2023-02-15",
        "54321",
        "New York",
        "NY"
    )