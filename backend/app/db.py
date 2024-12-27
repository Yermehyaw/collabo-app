"""
Setup the database connection via a mongodb client

"""
from motor.motor_asyncio import AsyncIOMotorClient  # AsyncIOMotorClient is the async version of the pymongo MongoClient
import os
from dotenv import load_dotenv

load_dotenv()  # Load the .env file

MONGO_URL = os.getenv("MONGO_URL")
DB_NAME = os.getenv("DB_NAME")

client = AsyncIOMotorClient(MONGO_URL)
db = client["Test"]  # create/get database instance from the client, revert to DB_NAME after testing


async def get_collection(name: str):
    """
    Get a collection from the database

    ARGUMENTS:
        - name: str

    RETURNS:
        - collection: Collection

    """
    collection = db[name]
    return collection