from selenium import webdriver
from selenium.webdriver.common.keys import Keys

username = "Sample"
password = "123456789"

url = ("https://www.instagram.com/accounts/login/")

driver = webdriver.Chrome()
driver.get(url)

driver.implicitly_wait(10)
usrField = driver.find_element_by_name('username')
usrField.send_keys(username)

pwField = driver.find_element_by_name('password')
pwField.send_keys(password)
pwField.send_keys(Keys.ENTER)
