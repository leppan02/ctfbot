import pymongo
def connect():
    myclient = pymongo.MongoClient("mongodb+srv://test:password12345@cluster0.hausm.gcp.mongodb.net/")
    return myclient["mydatabase"]

def retrieve(col, query):
    mycol = connect()[col]
    return mycol.find(query)

def insert(col, data):
    mycol = connect()[col]
    return mycol.insert_one(data)

def remove(col, query):
    mycol = connect()[col]
    return mycol.delete_one(query)
    