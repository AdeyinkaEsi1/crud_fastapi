

# Create a new client and connect to the server
# client = MongoClient(uri, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# for db in client.list_database_names():
#     print(db)



# # Get reference to the CRUD_FASTAPI database
# db = client.sample_mflix

# get reference to users collection
# users_collection = db.users

# new_users = {
#     "name": "catelyn Starka",
#     "email": "joe_bean@gameofthronesa",
#     "password": "$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAq1egt64wqq9+9ye"
# }

# result = users_collection.insert_one(new_users)
# document_id = result.inserted_id
# print(f"id of inserted document(new users) is {document_id}")
# client.close

""""
MOMGODB COMMS
------------------------------
list_database_names()

====POST====
db.collection.insert_one(new_doc)
db.collection.insert_many(new_docs)

=====PUT===
db.collection.update_one(<filter>, <update>)

$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
document_to_update = {"_id": ObjectId("62d6e04ecab6d8e130497482")}

# Update
add_to_balance = {"$inc": {"balance": 100}}

# Print original document
pprint.pprint(accounts_collection.find_one(document_to_update))

# Write an expression that adds to the target account balance by the specified amount.
result = accounts_collection.update_one(document_to_update, add_to_balance)
print("Documents updated: " + str(result.modified_count))

# Print updated document
pprint.pprint(accounts_collection.find_one(document_to_update))

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""


