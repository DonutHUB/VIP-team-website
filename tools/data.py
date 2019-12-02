from pymongo import MongoClient
from pprint import pprint

def fullSend():
    connection = MongoClient()
    db = connection.VIP
    collection = db.subteams
    data = collection.find({})
    returnable = []
    for i, d in enumerate(data):
        d['index'] = i
        returnable.append(d)
    return returnable