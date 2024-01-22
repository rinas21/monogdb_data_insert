from pymongo import MongoClient
from bson import ObjectId
import random
import string

# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client['day22data']
collection = db['data_set']

# Define the base record
base_record = {
    "da": "5501",
    "display_name": {
        "value": "to5501",
        "defined": True,
        "empty": False,
        "is_defined": True
    },
    "routing_parameters": [
        {
            "smsc": "",
            "oa": "#",
            "esme": "5a0abef3e4b09df2181a837f",
            "key_word": "",
            "standby_esme": "",
            "file_name": "",
            "destination_type": "ESME"
        },
        {
            "smsc": "",
            "oa": "#",
            "esme": "5a0abef3e4b09df2181a837f",
            "key_word": "abc1",
            "standby_esme": "",
            "file_name": "",
            "destination_type": "ESME"
        }
    ]
}

# Generate more than 300 records with different keywords
for i in range(300):
    # Clone the base record
    new_record = base_record.copy()

    # Generate a random keyword and update the record
    keyword = ''.join(random.choices(string.ascii_lowercase, k=4))
    new_record["name"] = f"Right(5501):ATRoutingParameter{{smscId: , oa: Right(#), keyWord: {keyword}, destinationType: ESME, esmeId: e0, standByEsmeId: None, fileName: }}ATRoutingParameter{{smscId: , oa: Right(#), keyWord: , destinationType: ESME, esmeId: e1, standByEsmeId: None, fileName: }}"
    new_record["routing_parameters"][0]["key_word"] = keyword

    # Insert the new record into the collection
    collection.insert_one(new_record)

print("Records inserted successfully.")
