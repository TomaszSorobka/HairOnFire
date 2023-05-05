from selenium import webdriver
import random
from scrapers.scraper_mumsnet import ScrapeMumsnet
from scrapers.scraper_reddit import ScrapeReddit
from scrapers.scraper_discusscooking import ScrapeDiscussCooking
from sentiment import ProblemRecognition
from db_connect import DataBaseConnect
import time

def setUpDriver():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(PATH, options=options)
    return driver

def main():
    start = time.time()
    driver = setUpDriver()
    database = DataBaseConnect()
    scrapedData = []

    try:
        reddit = ScrapeReddit()
        scrapedData += reddit.scrapeData()

        mumsnet = ScrapeMumsnet(driver)
        scrapedData += mumsnet.scrapeData()    

        discusscooking = ScrapeDiscussCooking(driver)
        scrapedData += discusscooking.scrapeData()  

        print('Scraping finished! Initializing problem recognition...')
        driver.quit()
        # Problem recognition
        analyzeProblem = ProblemRecognition()
        analyzedPosts = analyzeProblem.getNegativePosts(scrapedData)
    except Exception as e:
        print('Something went wrong: ', e)
        if input('Would you like me to continue? Type y or n: ') == 'n':
            driver.quit()
            print('Indicated no continuation. Closing...')
            return

    random.shuffle(analyzedPosts)
    insertCount = 0
    print('Inserting negative posts to the database...')
    for post in analyzedPosts:
        if not database.isPostAlreadyInDb(post['headline']):
            database.insertPost(post)
            insertCount +=1
    print('Posts inserted successfully! Closing...')
    end = time.time()
    print('Time: ', end-start)

main()
