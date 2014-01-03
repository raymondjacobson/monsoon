"""
    monsoon.py
    ~~~~~~~~~~~~~~~~~~

    Unlimited cloud storage

    :copyright: (c) 2013 Raymond Jacobson

"""
import cli.app, os
from lib.db import *
from lib.dbox import *
from lib.generator import *

def put(file):
  print "putting..."
  if (decideNewAccount(os.stat(file).st_size)):
    generateNewAccount()
  account = getNewestAccount()
  uploadFileToAccount(file, account['access_token'])

def grab(file):
  print "grabbing..."
  db_file = getUploadedFile(file)
  print "pub link: " + db_file['short_link']
  print "DL link: " + db_file['downloadable_link']

@cli.app.CommandLineApp
def monsoon(app):
  if (app.params.action == 'put'):
    put(app.params.file)
  elif (app.params.action == 'grab'):
    grab(app.params.file)
  else:
    print "invalid arguments. -h for help."
    exit(1)

monsoon.add_param("action", help="either 'put' or 'grab' a file", default=1)
monsoon.add_param("file", help="file to commit action on", default=2)

if __name__ == "__main__":
    monsoon.run()