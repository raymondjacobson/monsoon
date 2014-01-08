from pymongo import MongoClient

client = MongoClient()
db = client.monsoon_db

def saveAccountIntoDB(fname, lname, email, password, access_token, available_space):
  """Saves new account credentials into the mongodb"""
  account = {"first_name": fname,
             "last_name": lname,
             "email": email,
             "password": password,
             "access_token": access_token,
             "available_space": available_space}
  accounts = db.accounts
  account_id = accounts.insert(account)

def getNewestAccount():
  """Gets the most recently make account in the db"""
  accounts = db.accounts
  account = accounts.find().sort('_id', -1).limit(1)[0]
  return account

def decideNewAccount(file_size):
  """Decides if we need a new account based on incoming file size"""
  accounts = db.accounts
  if (accounts.count() == 0):
    return True
  newest_account = getNewestAccount()
  if (newest_account['available_space'] - file_size < 1024): # 1kB buffer
    return True
  return False # OK to upload

def saveUploadedFile(file_name, short_link, pub_link, downloadable_link):
  """Saves file_name:short_link:pub_link:downloadable_link into db"""
  file = {"file_name": file_name,
          "short_link": short_link,
          "pub_link": pub_link,
          "downloadable_link": downloadable_link}
  files = db.files
  file_id = files.insert(file)

def getUploadedFile(file_name):
  """Gets the pub_link for a specified file_name"""
  files = db.files
  file = files.find_one({"file_name": file_name})
  return file

def updateAccountSpace(access_token, space):
  """Updates the available_space in an account"""
  accounts = db.accounts
  accounts.update({'access_token':access_token}, {"$set": {"available_space": space}}, upsert=False)