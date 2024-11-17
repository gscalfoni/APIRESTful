from pymongo import MongoClient

client = MongoClient("mongodb+srv://Username:RL6wMc7Htct82yaS@cluster0.5h9vq.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")

db = client.product_db

collection = db['product_collection']
user_collection = db['user_collection']