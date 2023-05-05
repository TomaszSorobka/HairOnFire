from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

class DataBaseConnect:
    db_name = 'db_problems'
    collection_name = 'collection_problems'

    def __init__(self):
        self.configure()
        self.setMongoClientConnection()
        self.sendPing()

    def configure(self):
        load_dotenv()

    def setMongoClientConnection(self):
        uri = f"mongodb+srv://tomaszsorobka:{os.getenv('dbpass')}@cluster-haironfire.p99kbdf.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri)
        self.database = self.client[self.db_name]
        self.collection = self.database[self.collection_name]

    def sendPing(self):
        # Send a ping to confirm a successful connection
        try:
            self.client.admin.command('ping')
            print("Pinged database. Connection to MongoDB established successfully!")
        except Exception as e:
            print(e)

    def insertPost(self, dataRow : dict):
        try:
            self.collection.insert_one(dataRow)
        except Exception as e:
            print("Could not insert row into database: ", e)

    def isPostAlreadyInDb(self, dataHeadline):
        try:
            if self.collection.find({'headline':dataHeadline}).count() > 0:
                return True
            return False
        except Exception as e:
            print("Could not check post existance: ", e)

    


