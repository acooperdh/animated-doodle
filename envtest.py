import os
from dotenv import load_dotenv
load_dotenv()

token = os.getenv('MONGO_URI')
print(token)