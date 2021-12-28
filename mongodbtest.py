from pymongo import MongoClient
from dotenv import load_dotenv
# pprint library is used to make the output look more pretty
from pprint import pprint
import os

# loading .env file 
load_dotenv()

# setting tokens 
mongoToken = os.getenv('MONGO_URI')
# connect to MongoDB, change the << MONGODB URL >> to reflect your own connection string
client = MongoClient(mongoToken)
db=client.SimplePicks
# list_collection_names() returns an iterator that can be used to find the list of collection names
collectionNames = db.list_collection_names()
positionCollection = db['position']
cursor = positionCollection.find({})
print("docs in position collection:")
for doc in cursor:
    print(doc)
print("list of collection names:")
for name in collectionNames:
    print(name)