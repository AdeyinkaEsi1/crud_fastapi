#mongo_uri = mongodb+srv://Hamid:Hmongp0))odb1=-21@cluster0.zaaveoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0

"""
connection str = mongodb+srv://Hamid:<password>@cluster0.zaaveoa.mongodb.net/
"""
# 102.88.33.58

from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

MONGODB_URI = "mongodb+srv://Hamid:Hmongp0))odb1=-21@cluster0.zaaveoa.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"

# Create a new client and connect to the server
client = MongoClient(MONGODB_URI, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
try:
    client.admin.command('ping')
    print("Pinged your deployment. You successfully connected to MongoDB!")
except Exception as e:
    print(e)

for db in client.list_database_names():
    print(db)

