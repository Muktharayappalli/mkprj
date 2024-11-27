import os
from pymongo import MongoClient
import certifi
from pymongo.server_api import ServerApi


MONGO_DB = os.getenv("MONGO_DB", "mydatabase")
uri = "mongodb+srv://backend:12345@cluster0.e7itw.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'),tls=True,tlsCAFile=certifi.where())
dbconn = client[MONGO_DB]