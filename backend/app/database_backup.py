from pymongo import MongoClient
import os
from dotenv import load_dotenv
# from .database import messages_collection

load_dotenv()

client = MongoClient(os.getenv('MONGO_URI'))
db = client["chat_app"]
messages_collection = db["messages"]

