from pymongo import MongoClient

client = MongoClient("mongodb://admin:eliana_banana@localhost:27017")
db = client["mongo_db"]
print(
    db.list_collection_names()
)  # [] si la db esta vacia, es señal de que conecto bien
