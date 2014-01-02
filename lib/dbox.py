import dropbox
# from selenium import webdriver

def generateAuthCode(driver):

  app_key = 'y56d5gksg6oo46o'
  app_secret = 'utczpw6u3g8gt81'
  flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
  authorize_url = flow.start()

  driver = webdriver.PhantomJS()
  driver.implicitly_wait(10)
  driver.get(authorize_url)

  driver.execute_script("document.getElementById('login_email').value = 'BacteroidalKali@maildrop.cc';")
  driver.execute_script("document.getElementById('login_password').value = 'PhGmJJf389BA8z8DHJAX';")
  driver.find_element_by_id('login_submit').click()
  driver.find_element_by_name('allow_access').click()
  auth_code = driver.find_element_by_class_name('auth-code').text
  driver.quit()

  access_token, user_id = flow.finish(code)
  return auth_code
