import dropbox
from config import config
from lib.db import *

def generateAccessToken(driver):
  """Automatically generates an authentication code for the master app"""
  app_key = config['app_key']
  app_secret = config['app_secret']
  flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
  authorize_url = flow.start()

  driver.implicitly_wait(10)
  driver.get(authorize_url)

  driver.execute_script("document.getElementById('login_email').value = 'BacteroidalKali@maildrop.cc';")
  driver.execute_script("document.getElementById('login_password').value = 'PhGmJJf389BA8z8DHJAX';")
  driver.find_element_by_id('login_submit').click()
  driver.find_element_by_name('allow_access').click()
  auth_code = driver.find_element_by_class_name('auth-code').text
  driver.quit()

  access_token, user_id = flow.finish(auth_code)
  return access_token

def uploadFileToAccount(file_path, access_token):
  """Uploads a file to a dropbo account"""
  client = dropbox.client.DropboxClient(access_token)
  file = open(file_path)
  file_name = file_path.split("/")[-1]
  file_name_path = "/" + file_name
  response = client.put_file(file_name_path, file)
  short_link = client.share(file_name_path)['url']
  pub_link = client.share(file_name_path, short_url=False)['url']
  downloadable_link = pub_link.replace('www.dropbox.com', 'dl.dropboxusercontent.com', 1)
  updateAccountSpace(access_token, getSpaceInAccount(access_token))
  saveUploadedFile(file_name, short_link, pub_link, downloadable_link)
  print "successfully put!"
  print "pub link: " + short_link
  print "DL link: " + downloadable_link

def getSpaceInAccount(access_token):
  """Gets the available space in an account given an access_token"""
  client = dropbox.client.DropboxClient(access_token)
  account_info = client.account_info()
  quota = account_info['quota_info']['quota']
  used = account_info['quota_info']['normal'] + account_info['quota_info']['shared']
  return quota - used