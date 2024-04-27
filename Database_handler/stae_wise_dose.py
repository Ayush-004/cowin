from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from datetime import datetime
uri = "mongodb+srv://BITS:BITS@clustermodern.baoilaf.mongodb.net/?retryWrites=true&w=majority&appName=ClusterModern"
client = MongoClient(uri)
db = client["people_data"]
collection = db["Modern project"]
import pandas as pd

def statewise_vaccinated_by_dose(dose_number):
    # Define the pipeline based on the dose number
    pipeline = [
        {"$match": {"date_of_dose{}".format(dose_number): {"$exists": True}}},
        {"$group": {"_id": "$state", "total_vaccinated": {"$sum": 1}}}
    ]
    
    # Execute the aggregation pipeline
    result = collection.aggregate(pipeline)
    
    # Create a list of dictionaries for DataFrame construction
    data = [{"State": doc["_id"], "Total Vaccinated": doc["total_vaccinated"]} for doc in result]
    
    # Create DataFrame
    df = pd.DataFrame(data)
    
    return df