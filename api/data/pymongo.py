from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

user = os.getenv("MONGO_USER")
password = os.getenv("MONGO_PASS")

URL = f"mongodb+srv://{user}:{password}@midapi.mtd98.mongodb.net/"

db = MongoClient(URL).get_database("penguin_iter").penguin