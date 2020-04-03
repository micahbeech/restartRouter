from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

driver = webdriver.Chrome('/Users/micahbeech/chromedriver')

credentials = open("/Users/micahbeech/routerCredentials.txt", "r").readlines()

if len(credentials) != 3:
    print("Please add the username and password for your router admin in ~/routerCredentials.txt")

IP = credentials[0]
username = credentials[1]
password = credentials[2]

driver.get('http://' + IP)
time.sleep(5)

usernameInput = driver.find_element_by_id('user_login')
usernameInput.send_keys(username)
passwordInput = driver.find_element_by_id('user_password')
passwordInput.send_keys(password)
passwordInput.send_keys(Keys.ENTER)
time.sleep(10)

admin = driver.find_element_by_link_text('Admin')
admin.click()
time.sleep(5)

deviceReset = driver.find_element_by_link_text('Device Reset')
deviceReset.click()
time.sleep(5)

reboot = driver.find_element_by_id('reboot')
reboot.click()

confirmation = driver.switch_to.alert
confirmation.accept()
time.sleep(5)

driver.quit()
