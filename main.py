from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get("http://www.youtube.com")
elem = driver.find_element_by_class_name("search_query")
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)
sleep(100)
driver.close()