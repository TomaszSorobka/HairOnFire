from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, chrome_options=options)

driver.get("https://www.mumsnet.com/talk/extra_curricular_activities?page=1&order-by=newest")

try:
    main = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.TAG_NAME, 'main'))
    )

    headlines = main.find_elements(By.CSS_SELECTOR, '[data-click-id="topic-thread-1"]')
    for head in headlines:
        print(head.text)
    
finally:
    driver.quit()
