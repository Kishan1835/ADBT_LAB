from pymongo import MongoClient

client = MongoClient('localhost', 27017)

db = client['db_name']

collection = db['collection_name']

sample_data = [
    {"name": 'john doe', 'age': 25},
    {"name": 'jauume', 'age': 49},
    {"name": 'ram', 'age': 48},

]

collection.insert_many(sample_data)

records = collection.find()

for record in records:
    print(record)
