import dropbox, os, re, sys
from StringIO import StringIO
from config import config
from lib.db import saveUploadedFile, updateAccountSpace

def generateAccessToken(driver, email, password):
  """Automatically generates an authentication code for the master app"""
  app_key = config['app_key']
  app_secret = config['app_secret']
  flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
  authorize_url = flow.start()

  driver.implicitly_wait(10)
  driver.get(authorize_url)

  driver.execute_script("document.getElementById('login_email').value = '%s';" % email)
  driver.execute_script("document.getElementById('login_password').value = '%s';" % password)
  driver.find_element_by_id('login_submit').click()
  driver.find_element_by_name('allow_access').click()
  auth_code = driver.find_element_by_class_name('auth-code').text
  driver.quit()

  access_token, user_id = flow.finish(auth_code)
  return access_token

def format_path(path):
  """Normalize path for use with the Dropbox API."""
  if not path:
      return path
  path = re.sub(r'/+', '/', path)
  if path == '/':
      return (u"" if isinstance(path, unicode) else "")
  else:
      return '/' + path.strip('/')

def uploadByChunk(client, file, file_size, file_name_path,
                  offset=0, last_block=None, upload_id=None,
                  chunk_size = 1024 * 1024, overwrite=True):
  """
  Loosely copied from Dropbox API.
  - Handles chunked uploading of files; allows large files & pauses in upload
  - Displays percentage of file uploaded
  """
  while offset < file_size:
    next_chunk_size = min(chunk_size, file_size - offset)
    if last_block == None:
      last_block = file.read(next_chunk_size)
    percent_uploaded = offset/float(file_size) * 100
    sys.stdout.write("\r%i%%" % percent_uploaded)
    sys.stdout.flush()
    (offset, upload_id) = client.upload_chunk(StringIO(last_block), next_chunk_size, offset, upload_id)
    last_block = None
  sys.stdout.write("\n")
  path = "/commit_chunked_upload/%s%s" % (client.session.root, format_path(file_name_path))
  params = dict(
      overwrite = bool(overwrite),
      upload_id = upload_id
  )
  url, params, headers = client.request(path, params, content_server=True)
  return client.rest_client.POST(url, params, headers)

def uploadFileToAccount(file_path, access_token):
  """Uploads a file to a dropbox account"""
  client = dropbox.client.DropboxClient(access_token)
  file = open(file_path)
  file_name = file_path.split("/")[-1]
  file_name_path = "/" + file_name
  file_size = os.stat(file_path).st_size
  uploadByChunk(client, file, file_size, file_name_path)
  file.close()

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