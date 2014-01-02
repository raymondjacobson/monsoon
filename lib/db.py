from pymongo import MongoClient

client = MongoClient()
db = client.throw_db

def saveAccountIntoDB(fname, lname, email, password, auth_code):
  """Saves new account credentials into the mongodb"""
  account = {"first_name": fname,
             "last_name": lname,
             "email": email,
             "password": password,
             "auth_code": auth_code}
  accounts = db.accounts
  account_id = accounts.insert(account)
  print account

def uploadFile():
  """Uploads a file into the cloud and saves file:pub_link pair into db"""
  files = db.files

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