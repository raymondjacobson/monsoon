import dropbox
from lib.db import *

def generateAuthCode(driver):
  app_key = 'y56d5gksg6oo46o'
  app_secret = 'utczpw6u3g8gt81'
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
  return auth_code

def uploadFileToAccount(file_path, access_token):
  client = dropbox.client.DropboxClient(access_token)
  file = open(file_path)
  file_name = file.split("/")[-1]
  file_name_path = "/" + file_name
  response = client.put_file(file_name_path, file)
  pub_link = client.share(file_name_path)
  downloadable_link = shareLink.replace('www.dropbox.com', 'dl.dropboxusercontent.com', 1)
  updateAccountSpace(access_token, getSpaceInAccount(access_token))
  saveUploadedFile(file_name, pub_link, downloadable_link)
  print "uploaded!"
  print "pub link: " + pub_link
  print "DL link: " + downloadable_link

def getSpaceInAccount(access_token):
  client = dropbox.client.DropboxClient(access_token)
  account_info = client.account_info
  quota = account_info['quota_info']['quota']
  used = account_info['quota_info']['normal'] + account_info['quota_info']['shared']
  return quota - used