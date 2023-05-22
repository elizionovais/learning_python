from pymongo import MongoClient
import datetime

con = MongoClient('localhost', 27017)

db = con.db_cadastro

collections = db.db_cadastro

post1 = {"autor": "Dennis Ritchie", 
         "titulo": "The C Programming Language", 
         "ano": 1978,
         "date": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post1).inserted_id
print(post_id)

post2 = {"autor": "Brian W. Kernighan",
            "titulo": "The C Programming Language",
            "ano": 1978,
            "date": datetime.datetime.utcnow()}

collection = db.posts
post_id = collection.insert_one(post2).inserted_id
print(post_id)

for post in collection.find():
    print(post)
    
print(db.name)
