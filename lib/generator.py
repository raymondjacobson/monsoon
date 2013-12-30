from ghost import Ghost
import time
ghost = Ghost()

FNAME = 'Raymond'
LNAME = 'Jacobson'
PASSWORD = 'password' #replace with personal generated hash for security

def getNewEmailAddress():
  # ghost.open("http://maildrop.cc/")
  # result, resources = ghost.evaluate(
  #   "(document.getElementById('suggestion')).childNodes[0].innerHTML")
  # return result
  return 'PolysemanticGlosivie@maildrop.cc'

def generateNewAccount():
  _fname = FNAME
  _lname = LNAME
  _email = getNewEmailAddress()
  _password = PASSWORD
  ghost.open("http://dropbox.com")
  ghost.evaluate("document.getElementById('register-submit').click();alert('done')")
  ghost.wait_for_alert()
  ghost.capture_to('hxs.png')
  ghost.wait_for_selector('input[name=password]')
  ghost.fill("#signup-form", {
    "fname": _fname,
    "lname": _lname,
    "email": _email,
    "password": _password
  })
  # ghost.evaluate("document.getElementById('register-submit').click();")
  # ghost.evaluate("document.getElementById('fname').value = '%s';" % _fname)
  # ghost.evaluate("document.getElementById('lname').value = '%s';" % _lname)
  # ghost.evaluate("document.getElementById('email').value = '%s';" % _email)
  # ghost.evaluate("document.getElementById('password').value = '%s';" % _password)
  ghost.evaluate("document.getElementById('tos_agree').checked = true;")
  # result, resources = ghost.evaluate("document.getElementById('register-submit').click();")
  # ghost.evaluate("document.getElementById('register-submit').click();")
  # result, resources = ghost.evaluate("document.getElementById('signup-form').submit();")
  # print "wait"
  # time.sleep(5)
  result, resources = ghost.fire_on("#signup-form", "submit")
  # print page
  # print resource
  # ghost.click('#register-submit')
  # result, resources = ghost.evaluate("document.getElementById('register-submit').click();")
  # ghost.click('#register-submit')
  # result, resources = ghost.evaluate("document.getElementById('fname').value = 'Ray'; document.getElementById('lname').value = 'Jay';document.getElementById('email').value = 'PolysemanticDlosive@maildrop.cc';document.getElementById('password').value = 'PASSWD';document.getElementById('tos_agree').checked = true; alert('done');")
  # ghost.wait_for_alert()
  # ghost.evaluate("document.getElementById('signup-form').submit();")
  # result, resources = ghost.evaluate("document.getElementById('fname').value;")
  print result
  print resources
  # page, resources = ghost.wait_for_page_loaded()
  # ghost.capture_to('hxs.png')

  # print _email