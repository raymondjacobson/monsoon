from pymongo import MongoClient

client = MongoClient()
db = client.throw_db

def saveAccountIntoDB(fname, lname, email, password, auth_code, available_space):
  """Saves new account credentials into the mongodb"""
  account = {"first_name": fname,
             "last_name": lname,
             "email": email,
             "password": password,
             "auth_code": auth_code,
             "available_space": available_space}
  accounts = db.accounts
  account_id = accounts.insert(account)
  print account

def getNewestAccountAuthCode():
  """Gets the most recently make account in the db"""
  accounts = db.accounts
  account = accounts.find().sort(_id, -1).limit(1)
  return account['auth_code']

def decideNewAccount(file_size):
  """Decides if we need a new account based on incoming file size"""
  accounts = db.accounts
  if (len(accounts) == 0):
    return True
  newest_account = getNewestAccount()
  if (newest_account['available_space'] - file_size < 1000): # 1kB buffer
    return True
  return False # OK to upload

def saveUploadedFile(file_name, pub_link, downloadable_link):
  """Saves file_name:pub_link:downloadable_link into db"""
  file = {"file_name": file_name,
          "pub_link": pub_link,
          "downloadable_link": downloadable_link}
  files = db.files
  file_id = files.insert(file)

def getUploadedFile(file_name):
  """Gets the pub_link for a specified file_name"""
  files = db.files
  file = files.find_one({"file_name": file_name})
  return file['pub_link']

def updateAccountSpace(access_token, space):
  """Updates the available_space in an account"""
  accounts = db.accounts
  accounts.update({'auth_code':access_token}, {"available_space": space}, upsert=False)