from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

driver = webdriver.Chrome(PATH)

driver.get("https://www.mumsnet.com/talk/extra_curricular_activities?page=3&order-by=newest")
main = driver.find_element(By.TAG_NAME, 'main')
print(main.text)

driver.quit()