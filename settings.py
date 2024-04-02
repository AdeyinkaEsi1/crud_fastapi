from bson import ObjectId
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
import os
from pymongo.errors import OperationFailure

DATABASE_URL = os.environ.get("MONGO_CONNECTION_URI")

# Create a new client and connect to the server
client = MongoClient(DATABASE_URL, server_api=ServerApi('1'))

# Send a ping to confirm a successful connection
# try:
#     client.admin.command('ping')
#     print("Pinged your deployment. You successfully connected to MongoDB!")
# except Exception as e:
#     print(e)


# for db in client.list_database_names():
#     print(db)



# Get reference to the CRUD_FASTAPI database
db = client.Test_Database

# get reference to users collection
sec_collection = db.sec_collection

# new_users = {
#     "name": "catelyn Starka",
#     "email": "joe_bean@gameofthronesa",
#     "password": "$2b$12$UREFwsRUoyF0CRqGNK0LzO0HM/jLhgUCNNIJ9RJAq1egt64wqq9+9ye"
# }

# new_users = {
#     "name": "james penelope",
#     "email": "james01@mail.com",
#     "password": "jamenojamesnoamesnookjames0109/+y21" 
# }

# try:
#     result = first_collection.insert_one(new_users)
#     document_id = result.inserted_id
#     print(f"id of inserted document(new users) is {document_id}")
# except OperationFailure as e:
#     print("Error while inserting document:", e)

documents_to_delete = {"_id": ObjectId('660b83331d0b63f1e1c525cd')}
result = sec_collection.delete_one(documents_to_delete)

client.close

cursor = sec_collection.find({})
print()
for doc in cursor:
    print(doc)

# db.getCollection('first_collection').dropIndexes()




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

============DB TRANSACTION=================

Creating MongoDB Transactions in Python Applications
Review the following code, which demonstrates how to create multi-document transactions in MongoDB by using PyMongo.


Create a Transaction
Note that you must have an active database connection to create a transaction. Once you're connected to a database, complete the following steps:

Define the callback that specifies the sequence of operations to perform inside the transaction. Make sure to do the following:

In the callback, include the required parameter, which is the client session. You can also add additional parameters for your particular transaction if needed. In the following example, there are four keyword parameters specific to this bank transfer: transfer_id, account_id_receiver, account_id_sender, and transfer_amount.

Within the callback function, get references to the collections that the operations will take place on.

Write the transaction operations. Note that you must pass the session to each operation.

Start a client session by calling the start_session method on the client object in a with statement.

Carry out the transaction by calling with_transaction on the session object. with_transaction starts a transaction, runs the callback, and commits (or cancels if there's an error). For this step, consider the following:

with_transaction has one required parameter, which is the callback function that specifies the sequence of operations to perform inside the transaction. In the following example, we passed in the callback_wrapper function to pass the additional arguments to the callback: transfer_id, account_id_receiver, account_id_sender, and transfer_amount.

Note that the general best practice for passing arbitrary arguments to the callback is to use a lambda function. In this example, we used the callback wrapper for simplicity.

Here's the code to create the transaction:

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Step 1: Define the callback that specifies the sequence of operations to perform inside the transactions.
def callback(
    session,
    transfer_id=None,
    account_id_receiver=None,
    account_id_sender=None,
    transfer_amount=None,
):

    # Get reference to 'accounts' collection
    accounts_collection = session.client.bank.accounts

    # Get reference to 'transfers' collection
    transfers_collection = session.client.bank.transfers

    transfer = {
        "transfer_id": transfer_id,
        "to_account": account_id_receiver,
        "from_account": account_id_sender,
        "amount": {"$numberDecimal": transfer_amount},
    }

    # Transaction operations
    # Important: You must pass the session to each operation

    # Update sender account: subtract transfer amount from balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_sender},
        {
            "$inc": {"balance": -transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Update receiver account: add transfer amount to balance and add transfer ID
    accounts_collection.update_one(
        {"account_id": account_id_receiver},
        {
            "$inc": {"balance": transfer_amount},
            "$push": {"transfers_complete": transfer_id},
        },
        session=session,
    )

    # Add new transfer to 'transfers' collection
    transfers_collection.insert_one(transfer, session=session)

    print("Transaction successful")

    return


def callback_wrapper(s):
    callback(
        s,
        transfer_id="TR218721873",
        account_id_receiver="MDB343652528",
        account_id_sender="MDB574189300",
        transfer_amount=100,
    )


# Step 2: Start a client session
with client.start_session() as session:
    # Step 3: Use with_transaction to start a transaction, execute the callback, and commit (or cancel on error)
    session.with_transaction(callback_wrapper)


client.close()

"""


"""
Using MongoDB Aggregation Stages with Python: $match and $group
Review the following code, which demonstrates how to use the $match and $group stages in a MongoDB aggregation pipeline by using PyMongo.


Using $match
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we used the $match and $group stages.

Use the $match operator to select documents that match the specified query condition(s) and pass the matching documents to the next stage. $match takes a document that specifies the query.

$match should be placed early in a pipeline to reduce the number of documents that will be processed later in the pipeline.

Here's an example of the $match stage:

# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

Using $group
Use the $group stage to separate documents into groups. The $group stage must have an _id field that specifies the group key. The group key is preceded by a $ and enclosed in quotation marks.

A $group stage can include additional field(s) that are computed by using accumulator operators, such as $avg.

Here's an example of the $group stage:

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

Aggregation Example That Uses $match and $group
The following is an example of an aggregation pipeline that uses $match and $group.

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get reference to 'accounts' collection
accounts_collection = db.accounts

# Calculate the average balance of checking and savings accounts with balances of less than $1000.

# Select accounts with balances of less than $1000.
select_by_balance = {"$match": {"balance": {"$lt": 1000}}}

# Separate documents by account type and calculate the average balance for each account type.
separate_by_account_calculate_avg_balance = {
    "$group": {"_id": "$account_type", "avg_balance": {"$avg": "$balance"}}
}

# Create an aggegation pipeline using 'stage_match_balance' and 'stage_group_account_type'.
pipeline = [
    select_by_balance,
    separate_by_account_calculate_avg_balance,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print()
print(
    "Average balance of checking and savings accounts with balances of less than $1000:", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()
"""


"""
Using MongoDB Aggregation Stages with Python: $sort and $project
Review the following code, which demonstrates how to use the $sort and $project stages in a MongoDB aggregation pipeline by using PyMongo.


Using $sort
When we build queries by using the aggregation framework, each stage transforms or organizes data in a specific way. In this lesson, we focused on the $sort and $project stages.

Use the $sort operator to organize the input documents in ascending or descending order. $sort takes a document that specifies the field(s) to sort by and the respective sort order. To sort in ascending order, use the value of 1. For descending order, use the value of -1.

Here's an example of a $sort stage:

# Organize documents in order from highest balance to lowest.
organize_by_original_balance = {"$sort": {"balance": -1}}

Using $project
Use the $project stage to specify the fields returned by the aggregation. $project can be used to include or exclude existing fields by setting a field to 1 to include or 0 to exclude. It can also be used to add new fields or reset the value of existing fields.

To add a new field by using $project, specify the field name and set its value to an expression like this: <field>: <expression>. In this example, the new field name is gbp_balance. The expression contains the $divide arithmetic operator, the $balance field reference, and the conversion_rate_usd_to_gbp variable.

When creating an aggregation pipeline, the $project stage should usually be the last stage in a pipeline because it specifies the exact fields to be returned to the client.

Here's an example of a $project stage:

# Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
return_specified_fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}

Aggregation Example That Uses $match, $sort, and $project
The following is an example of an aggregation pipeline that uses $match, $sort, and $project:

# Connect to MongoDB cluster with MongoClient
client = MongoClient(MONGODB_URI)

# Get reference to 'bank' database
db = client.bank

# Get a reference to the 'accounts' collection
accounts_collection = db.accounts

# Return the account type, original balance, and balance converted to Great British Pounds (GBP)
# of all checking accounts with an original balance of greater than $1,500 US dollars, in order from highest original balance to lowest.

# To calculate the balance in GBP, divide the original balance by the conversion rate
conversion_rate_usd_to_gbp = 1.3

# Select checking accounts with balances of more than $1,500.
select_accounts = {"$match": {"account_type": "checking", "balance": {"$gt": 1500}}}

# Organize documents in order from highest balance to lowest.
organize_by_original_balance = {"$sort": {"balance": -1}}

# Return only the account type & balance fields, plus a new field containing balance in Great British Pounds (GBP).
return_specified_fields = {
    "$project": {
        "account_type": 1,
        "balance": 1,
        "gbp_balance": {"$divide": ["$balance", conversion_rate_usd_to_gbp]},
        "_id": 0,
    }
}

# Create an aggegation pipeline containing the four stages created above
pipeline = [
    select_accounts,
    organize_by_original_balance,
    return_specified_fields,
]

# Perform an aggregation on 'pipeline'.
results = accounts_collection.aggregate(pipeline)

print(
    "Account type, original balance and balance in GDP of checking accounts with original balance greater than $1,500,"
    "in order from highest original balance to lowest: ", "\n"
)

for item in results:
    pprint.pprint(item)

client.close()
"""