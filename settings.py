

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

db.collection.update_many(<filter>, <update>)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Filter
select_accounts = {"account_type": "savings"}

# Update
set_field = {"$set": {"minimum_balance": 100}}

# Write an expression that adds a 'minimum_balance' field to each savings acccount and sets its value to 100.
result = accounts_collection.update_many(select_accounts, set_field)

print("Documents matched: " + str(result.matched_count))
print("Documents updated: " + str(result.modified_count))
pprint.pprint(accounts_collection.find_one(select_accounts))

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

=============GET=============
db.collection.find_one
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query by ObjectId
document_to_find = {"_id": ObjectId("62d6e04ecab6d8e1304974ae")}

# Write an expression that retrieves the document matching the query constraint in the 'accounts' collection.
result = accounts_collection.find_one(document_to_find)
pprint.pprint(result)

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$4

db.collection.find()

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Query
documents_to_find = {"balance": {"$gt": 4700}}

# Write an expression that selects the documents matching the query constraint in the 'accounts' collection.
cursor = accounts_collection.find(documents_to_find)

num_docs = 0
for document in cursor:
    num_docs += 1
    pprint.pprint(document)
    print()
print("# of documents found: " + str(num_docs))

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

======DELETE============
db.collection.delete_one()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter by ObjectId
document_to_delete = {"_id": ObjectId("62d6e04ecab6d8e130497485")}

# Search for document before delete
print("Searching for target document before delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

# Write an expression that deletes the target account.
result = accounts_collection.delete_one(document_to_delete)

# Search for document after delete
print("Searching for target document after delete: ")
pprint.pprint(accounts_collection.find_one(document_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

db.collection.delete_many()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Filter for accounts with balance less than $2000
documents_to_delete = {"balance": {"$lt": 2000}}

# Search for sample document before delete
print("Searching for sample target document before delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

# Write an expression that deletes the target accounts.
result = accounts_collection.delete_many(documents_to_delete)

# Search for sample document after delete
print("Searching for sample target document after delete: ")
pprint.pprint(accounts_collection.find_one(documents_to_delete))

print("Documents deleted: " + str(result.deleted_count))

client.close()
$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$

"""


