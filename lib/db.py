from pymongo import MongoClient

client = MongoClient()
db = client.throw_db

def saveNewAccountInfo(email, password):
  """Inserts new valid dropbox account into mongodb"""


# post = {"author": "Mike",
#         "text": "My firfst blog post!",
#         "tags": ["mongodb", "python", "pymongo"]}

# posts = db.posts
# # post_id = posts.insert(post)
# # print post_id
# print db.collection_names()
# for pot in posts.find():
#   print pot


# generateNewAccount()