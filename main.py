from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

answers = {}

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

while True:
  try:
    joincode = driver.find_element(by=By.CLASS_NAME, value="sc-jGFFOr.cKOjwg.flex.vc.hc").click()
  except:
    pass
  else:
    break

while True:
  try:
    driver.find_element(by=By.CLASS_NAME, value="sc-eylKsO.denLGz.flex-column")
  except:
    humancontrol = True
  else:
    humancontrol = False

  if humancontrol:
    print('human')
  else:
    # print('bot')
    question = driver.find_element(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM").text
    possibleanswers = [driver.find_elements(by=By.CLASS_NAME, value="sc-iDsUSg.cVPfqH"), driver.find_elements(by=By.CLASS_NAME, value="sc-iDsUSg.esDDTm"), driver.find_elements(by=By.CLASS_NAME, value="sc-iDsUSg.lgneBT"), driver.find_elements(by=By.CLASS_NAME, value="sc-iDsUSg.cpbUXN")]
    # if question in answers.keys():
    #   for i in range(4):
    #     if answers[question] == possibleanswers[i].get_attribute('id'):
    #       possibleanswers[i].click()
    # else:
    #   driver.find_elements(by=By.CLASS_NAME, value="sc-iDsUSg.cVPfqH").click()
    #   sleep(100)
    #   quit()

    # sleep(1)
    # driver.find_element(by=By.CLASS_NAME, value="anticon.anticon-close").click()

driver.close()