from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

answers = {}

username = input('enter username: ')
password = input('enter password: ')

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.maximize_window()
driver.get("http://www.gimkit.com/hub")

usernameinput = []
while usernameinput == []:
  usernameinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
usernameinput.send_keys(username)
usernameinput.send_keys(Keys.RETURN)

passwordinput = []
while passwordinput = []:
  passwordinput = driver.find_element(by=By.CLASS_NAME, value="ant-input.ant-input-lg")
passwordinput.send_keys(password)
passwordinput.send_keys(Keys.RETURN)

bait = 0

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
    pass
  else:
    questioninfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
    question = questioninfo[0].text
    firstanswer = questioninfo[1].text
    if question in answers.keys():
      for i in range(4):
        if answers[question] == questioninfo[i + 1].text:
          questioninfo[i + 1].click()
      
      answerinfo = []
      while answerinfo == []:
        answerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
      answerinfo[2].click()
      bait += 1
    else:
      questioninfo[1].click()
      

      answerinfo = []
      while answerinfo == []:
        answerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")

      if answerinfo[0].text == '+1 Bait':
        answers[question] = firstanswer
        answerinfo[2].click()
        bait += 1
      else:
        answerinfo[1].click()
        correctanswerinfo = []
        while correctanswerinfo == []:
          correctanswerinfo = driver.find_elements(by=By.CLASS_NAME, value="sc-gHpXsY.criBYM")
        answers[question] = correctanswerinfo[2].text
        correctanswerinfo[3].click()
        bait -= 1

    bait = 0 if bait < 0 else bait

    if bait >= 100:
      while True:
        try:
          driver.find_element(by=By.CLASS_NAME, value="anticon.anticon-close").click()
        except:
          pass
        else:
          break
      sleep(0.4)

driver.close()