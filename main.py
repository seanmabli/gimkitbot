from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

username = "mablis25@lsrhs.net" # input('enter username: ')
password = "alphabeta" # input('enter password: ')

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.gimkit.com/hub")

sleep(1)

usernameinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
usernameinput.send_keys(username)
usernameinput.send_keys(Keys.RETURN)

sleep(1)

passwordinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
passwordinput.send_keys(password)
passwordinput.send_keys(Keys.RETURN)

sleep(100)
driver.close()