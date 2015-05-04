from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

browser = webdriver.Firefox()

browser.get('http://www.firebase.com')

elem_signup = browser.find_element_by_id('nav-signup')
#elem.send_keys('seleniumhq' + Keys.RETURN)
elem_signup.click()
time.sleep(5)
#browser.quit()
browser.find_element_by_id('signup-email').send_keys('x2011bhb@gmail.com')
time.sleep(5)
#elem_signup_email.send_keys('x2011bhb@gmail.com')
browser.find_element_by_id('signup-password').send_keys('qwer1234')
time.sleep(5)
#elem_signup_password.send_keys('qwer1234')
browser.find_element_by_id('signup-button').click()
time.sleep(5)

browser.find_element_by_name('appName').send_keys('chatlitelulu')
time.sleep(5)
browser.find_element_by_class('update button button-flat-primary button-block button-rounded').click()
