from pymongo import MongoClient

client = MongoClient()
db = client.throw_db

def saveAccountIntoDB(fname, lname, email, password):
  """Saves new account credentials into the mongodb"""
  account = {"first_name": fname,
             "last_name": lname,
             "email": email,
             "password": password}
  accounts = db.accounts
  account_id = accounts.insert(account)
  print account

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