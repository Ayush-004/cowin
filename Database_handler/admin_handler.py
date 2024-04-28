from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
import os
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Modern project"]
addar=os.getenv("AADHAR_NUMBER")
dose_number=os.getenv("DOSE_NUMBER")
date=os.getenv("DATE")
serial_number=os.getenv("SERIAL_NUMBER")
def update_vaccine_info(aadhar_number, dose_number, date_of_dose=None, serial_number=None):
    # Check if the record exists
    query = {"aadhar_number": aadhar_number}
    record = collection.find_one(query)
    
    if record:
        update_data = {}
        if dose_number == 1:
            if date_of_dose and serial_number:
                update_data["date_of_dose1"] = datetime.strptime(date_of_dose, "%Y-%m-%d")
                update_data["serial_number_dose1"] = serial_number
            else:
                print("Please provide both date of dose and serial number for dose 1.")
                return
        elif dose_number == 2:
            if date_of_dose and serial_number:
                update_data["date_of_dose2"] = datetime.strptime(date_of_dose, "%Y-%m-%d")
                update_data["serial_number_dose2"] = serial_number
            else:
                print("Please provide both date of dose and serial number for dose 2.")
                return
        else:
            print("Invalid dose number. Please provide either 1 or 2.")
            return
        
        # If dose 2 information exists, update the record; otherwise, insert new information
        if dose_number == 2 and "date_of_dose2" in record and "serial_number_dose2" in record:
            collection.update_one(query, {"$set": update_data})
            print("Vaccine information for dose 2 updated successfully!")
        else:
            collection.update_one(query, {"$set": update_data})
            print("Vaccine information for dose 1 inserted successfully!")
    else:
        print("Record not found for the given Aadhar number.")

if __name__ == "__main__":
    # Example usage to insert dose 1 information
    update_vaccine_info(addar, dose_number, date, serial_number)
    
    
