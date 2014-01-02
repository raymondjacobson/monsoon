from selenium import webdriver
import names, random, string
from lib.db import *
from lib.dbox import *

driver = webdriver.PhantomJS()
driver.implicitly_wait(10)
maildropURL = "http://maildrop.cc"
dropboxURL = "http://dropbox.com"

def getNewEmailAddress():
  """Queries maildrop.cc to grab a new unique email address"""
  driver.get(maildropURL)
  emailAddr = driver.find_element_by_id('suggestion').text
  return emailAddr

def getNewPassword(size=20):
  chars = string.ascii_uppercase + string.ascii_lowercase + string.digits
  return ''.join(random.choice(chars) for x in range(size))

def generateNewAccount():
  """Generates a new account on dropbox.com"""
  _fname = names.get_first_name()
  _lname = names.get_last_name()
  _email = getNewEmailAddress()
  _password = getNewPassword()
  driver.get(dropboxURL)
  driver.execute_script("document.getElementById('fname').value = '%s';" % _fname)
  driver.execute_script("document.getElementById('lname').value = '%s';" % _lname)
  driver.execute_script("document.getElementById('email').value = '%s';" % _email)
  driver.execute_script("document.getElementById('password').value = '%s';" % _password)
  driver.execute_script("document.getElementById('tos_agree').checked = true;")
  driver.execute_script("document.getElementById('signup-form').submit();")
  auth_code = generateAuthCode(driver)
  saveAccountIntoDB(_fname, _lname, _email, _password, auth_code)