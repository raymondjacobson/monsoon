"""
    Throw.py
    ~~~~~~~~~~~~~~~~~~

    Unlimited cloud storage

    :copyright: (c) 2013 Raymond Jacobson

"""
import cli.app
from lib.db import *
from lib.dbox import *
from lib.generator import *

def put(file):
  if (decideNewAccount()):
    generateNewAccount()
  print "uploading..."
  uploadFileToAccount(file_path, getNewestAccountAuthCode())

def grab(file):
  print "please visit the following link:"
  print getUploadedFile(file)

@cli.app.CommandLineApp
def throw(app):
  if (app.params.action == 'put'):
    put(app.params.file)
  elif (app.params.action == 'grab'):
    grab(app.params.file)
  else:
    print "invalid arguments. -h for help."
    exit(1)

throw.add_param("action", help="either 'put' or 'grab' a file into the cloud", default=1)
throw.add_param("file", help="file to put or grab", default=2)

if __name__ == "__main__":
    throw.run()