from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from fake_useragent import UserAgent
from time import sleep

username = "mablis25@lsrhs.net" # input('enter username: ')
password = "alphabeta" # input('enter password: ')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.gimkit.com/hub")

sleep(1)

usernameinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
usernameinput.send_keys(username)
usernameinput.send_keys(Keys.RETURN)

sleep(1)

passwordinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
passwordinput.send_keys(password)
passwordinput.send_keys(Keys.RETURN)

sleep(1)

try:
  joincode = driver.find_element(by=By.CLASS_NAME, value="sc-jGFFOr.cKOjwg.flex.vc.hc")
  joincode.click()
except:
  quit()

while True:
  pass

driver.close()