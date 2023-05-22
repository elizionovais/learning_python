from pymongo import MongoClient

con = MongoClient('localhost', 27017)

db = con.db_cadastro

collections = db.db_cadastro