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

def getNewestAccount():
  """Gets the most recently make account in the db"""
  accounts = db.accounts
  account = accounts.find().sort(_id, -1).limit(1)
  return account

def saveUploadedFile(file_name, pub_link, downloadable_link):
  """Saves file_name:pub_link:downloadable_link into db"""
  file = {"file_name": file_name,
          "pub_link": pub_link,
          "downloadable_link": downloadable_link}
  files = db.files
  file_id = files.insert(file)