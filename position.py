# api to create position in mongodb 
import pymongo
from dotenv import load_dotenv 
from pprint import pprint
import os 

def create_position(symbol, price, entry_price, price_targets, exchange):
    load_dotenv()
    mongoToken = os.getenv('MONGO_URI')
    client = pymongo.MongoClient(mongoToken)
    db=client.SimplePicks
    positionCollection = db['position']
    position = {
        "symbol": symbol,
        "price": price,
        "entry_price": entry_price,
        "price_targets": price_targets,
        "exchange": exchange
    }
    positionCollection.insert_one(position)
    return position
