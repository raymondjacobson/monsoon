from ghost import Ghost
import names, random, string
from lib.db import *

ghost = Ghost()

def getNewEmailAddress():
  """Queries maildrop.cc to grab a new unique email address"""
  ghost.open("http://maildrop.cc/")
  result, resources = ghost.evaluate(
    "(document.getElementById('suggestion')).childNodes[0].innerHTML")
  return result

def getNewPassword(size=20):
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for x in range(size))

def generateNewAccount():
  """Generates a new account on dropbox.com"""
  _fname = names.get_first_name()
  _lname = names.get_last_name()
  _email = getNewEmailAddress()
  _password = getNewPassword()
  ghost.open("http://dropbox.com")
  ghost.fill("#signup-form", {
    "fname": _fname,
    "lname": _lname,
    "email": _email,
    "password": _password
  })
  ghost.evaluate("document.getElementById('tos_agree').checked = true;")
  ghost.fire_on("#signup-form", "submit")
  ghost.wait_for_text("Welcome to Dropbox!")
  saveAccountIntoDB(_fname, _lname, _email, _password)