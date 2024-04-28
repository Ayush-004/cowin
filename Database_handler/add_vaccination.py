from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Modern project"]
addar=os.getenv("AADHAR_NUMBER")
name=os.getenv("NAME")
date=os.getenv("DATE")
mobile_number=os.getenv("MOBILE_NUMBER")
vaccine_name=os.getenv("VACCINE_NAME")
date_of_dose1=os.getenv("DATE1")
serial_number1=os.getenv("SERIAL_NUMBER")
date_of_dose2=os.getenv("DATE2")
serial_number2=os.getenv("SERIAL_NUMBER")
city=os.getenv("CITY")
state=os.getenv("STATE")
def insert_vaccine_record(aadhar_number, name, mobile_number, vaccine_name, date_of_dose1, serial_number_dose1, date_of_dose2=None, serial_number_dose2=None, city=None, state=None):
    # Convert date strings to datetime objects
    date_of_dose1 = datetime.strptime(date_of_dose1, "%Y-%m-%d")
    if date_of_dose2:
        date_of_dose2 = datetime.strptime(date_of_dose2, "%Y-%m-%d")
    
    # Create record object
    record = {
        "aadhar_number": aadhar_number,
        "name": name,
        "mobile_number": mobile_number,
        "vaccine_name": vaccine_name,
        "date_of_dose1": date_of_dose1,
        "serial_number_dose1": serial_number_dose1,
    }
    
    # Add dose 2 information if provided
    if date_of_dose2 and serial_number_dose2:
        record["date_of_dose2"] = date_of_dose2
        record["serial_number_dose2"] = serial_number_dose2
        
    # Add city and state if provided
    if city:
        record["city"] = city
    if state:
        record["state"] = state
    
    # Insert record into MongoDB
    collection.insert_one(record)
    print("Record inserted successfully!")

if __name__ == "__main__":
    # Example usage
    insert_vaccine_record(
        addar,
        name,
        mobile_number,
        vaccine_name,
        date_of_dose1,
        serial_number1,
        date_of_dose2,
        serial_number2,
        city,
        state
    )