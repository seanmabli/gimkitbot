from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

answers = {}

username = 'mablis25@lsrhs.net' # input('enter username: ')
password = 'alphabeta' # input('enter password: ')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.gimkit.com/hub")

while True:
  try:
    usernameinput = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div[2]/div[2]/input")
    usernameinput.send_keys(username)
    usernameinput.send_keys(Keys.RETURN)
  except:
    pass
  else:
    break

while True:
  try:
    passwordinput = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/span/input")
    passwordinput.send_keys(password)
    passwordinput.send_keys(Keys.RETURN)
  except:
    pass
  else:
    break

bait = 0

while True:
  try:
    joincode = driver.find_element(by=By.XPATH, value="/html/body/div[1]/div/div/div[2]/div/div/div/div[2]/div/div/div/div/div[2]/div[1]/div/div[2]/a").click()
  except:
    pass
  else:
    break

while True:
  try:
    driver.find_element(by=By.XPATH, value="/html/body/div/div/div/div[2]/div/div/div/div/div/div[5]/div/div/div[2]/div/div[2]/div[1]")
  except:
    humancontrol = True
  else:
    humancontrol = False

  if humancontrol:
    print('human')
  else:
    print('robot')
    # questioninfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
    # question = questioninfo[0].text
    # firstanswer = questioninfo[1].text
    # if question in answers.keys():
    #   for i in range(4):
    #     if answers[question] == questioninfo[i + 1].text:
    #       questioninfo[i + 1].click()
    #   
    #   answerinfo = []
    #   while answerinfo == []:
    #     answerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
    #   answerinfo[2].click()
    #   bait += 1
    # else:
    #   questioninfo[1].click()
    #   
    #   answerinfo = []
    #   while answerinfo == []:
    #     answerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
    #   if answerinfo[0].text == '+1 Bait':
    #     answers[question] = firstanswer
    #     answerinfo[2].click()
    #     bait += 1
    #   else:
    #     answerinfo[1].click()
    #     correctanswerinfo = []
    #     while correctanswerinfo == []:
    #       correctanswerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
    #     answers[question] = correctanswerinfo[2].text
    #     correctanswerinfo[3].click()
    #     bait -= 1
    # bait = 0 if bait < 0 else bait
    # if bait >= 100:
    #   while True:
    #     try:
    #       driver.find_element(by=By.CLASS_NAME, value="anticon.anticon-close").click()
    #     except:
    #       pass
    #     else:
    #       break
    #   sleep(0.4)


sleep(1000)
driver.close()