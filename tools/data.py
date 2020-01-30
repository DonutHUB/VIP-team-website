from pymongo import MongoClient
from pprint import pprint

def fullSend():
    connection = MongoClient()
    db = connection.SubTeams
    collection = db.SubTeamData
    data = collection.find({})
    returnable = []
    for i, d in enumerate(data):
        d['index'] = i
        returnable.append(d)
    return returnable
