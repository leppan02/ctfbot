import pymongo
def connect():
    myclient = pymongo.MongoClient("mongodb+srv://test:password12345@cluster0.hausm.gcp.mongodb.net/")
    mydb = myclient["mydatabase"]

def retrieve(col, query):


def insert(data):
    