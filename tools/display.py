from pymongo import MongoClient
from pprint import pprint

def displayImage():
    connection = MongoClient()
    db = connection.Jokes
    collection = db.Image
    data = collection.find({})
    returnable = []
    for i, d in enumerate(data):
        d['index'] = i
        returnable.append(d)
    return returnable

def displayText():
    connection = MongoClient()
    db = connection.Jokes
    collection = db.Text
    data = collection.find({})
    returnable = []
    for i, d in enumerate(data):
        d['index'] = i
        returnable.append(d)
    return returnable

def displayURL():
    connection = MongoClient()
    db = connection.Jokes
    collection = db.URL
    data = collection.find({})
    returnable = []
    for i, d in enumerate(data):
        d['index'] = i
        returnable.append(d)
    return returnable
