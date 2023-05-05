# Import required libraries
from dotenv import load_dotenv
import os
from pymongo.mongo_client import MongoClient

# Define a class for database connection
class DataBaseConnect:
    # Declare constants for database and collection name
    db_name = 'db_problems'
    collection_name = 'collection_problems'

    # Initialize the class
    def __init__(self):
        self.configure()  # Load the environment variables
        self.setMongoClientConnection()  # Set the MongoDB client connection
        self.sendPing()  # Send a ping to confirm a successful connection

    # Load the environment variables
    def configure(self):
        load_dotenv()

    # Set the MongoDB client connection
    def setMongoClientConnection(self):
        # Set the URI to connect with MongoDB using environment variable
        uri = f"mongodb+srv://tomaszsorobka:{os.getenv('dbpass')}@cluster-haironfire.p99kbdf.mongodb.net/?retryWrites=true&w=majority"
        # Create a new client and connect to the server
        self.client = MongoClient(uri)
        self.database = self.client[self.db_name]  # Select the database
        self.collection = self.database[self.collection_name]  # Select the collection

    # Send a ping to confirm a successful connection
    def sendPing(self):
        try:
            self.client.admin.command('ping')
            print("Pinged database. Connection to MongoDB established successfully!")
        except Exception as e:
            print(e)

    # Insert a row into the collection
    def insertPost(self, dataRow: dict):
        try:
            self.collection.insert_one(dataRow)
        except Exception as e:
            print("Could not insert row into database: ", e)

    # Check if a post with the given headline already exists in the collection
    def isPostAlreadyInDb(self, dataHeadline):
        try:
            # Check the count of posts with the given headline
            if self.collection.find({'headline': dataHeadline}).count() > 0:
                return True
            return False
        except Exception as e:
            print("Could not check post existance: ", e)
    


