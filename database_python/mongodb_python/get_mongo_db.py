import pymongo

con = pymongo.MongoClient()

db = con.cadastrodb

# db.create_collection("mycollection")

# db.mycollection.insert_one({
#     'titulo': 'MongoDB com Python',
#     'descricao': 'MongoDB é um Banco de Dados NoSQL',
#     'by': 'Data Science Academy',
#     'url': 'http://www.datascienceacademy.com.br',
#     'tags': ['mongodb', 'database', 'NoSQL'],
#     'likes': 100
# })

data = db.mycollection.find_one()
print(data)