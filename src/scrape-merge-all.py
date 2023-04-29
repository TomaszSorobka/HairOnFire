from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

from scrapers.scraper_mumsnet import ScrapeMumsnet
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, options=options)


# Mumsnet
mumsnet = ScrapeMumsnet(driver)
scrapedData = mumsnet.scrapeData()


#print(type(scrapedData))
#for i in scrapedData:
 #   print(i)