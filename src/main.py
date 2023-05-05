# Import necessary modules and classes
from selenium import webdriver
import random
from scrapers.scraper_mumsnet import ScrapeMumsnet
from scrapers.scraper_reddit import ScrapeReddit
from scrapers.scraper_discusscooking import ScrapeDiscussCooking
from sentiment import ProblemRecognition
from db_connect import DataBaseConnect
import time

# Set up the WebDriver with certain options
def setUpDriver():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(PATH, options=options)
    return driver

# Main function to perform web scraping and sentiment analysis
def main():
    # Set start time and initialize list for scraped data
    start = time.time()
    scrapedData = []
    
    # Create WebDriver instance and database instance
    driver = setUpDriver()
    database = DataBaseConnect()
    
    try:
        # Scrape data from Reddit using ScraperReddit class
        reddit = ScrapeReddit()
        scrapedData += reddit.scrapeData()

        # Scrape data from Mumsnet using ScraperMumsnet class
        mumsnet = ScrapeMumsnet(driver)
        scrapedData += mumsnet.scrapeData()

        # Scrape data from DiscussCooking using ScraperDiscussCooking class
        discusscooking = ScrapeDiscussCooking(driver)
        scrapedData += discusscooking.scrapeData()  

        # Initialize ProblemRecognition instance and get negative posts
        print('Scraping finished! Initializing problem recognition...')
        driver.quit()
        analyzeProblem = ProblemRecognition()
        analyzedPosts = analyzeProblem.getNegativePosts(scrapedData)

    except Exception as e:
        # Handle exceptions during scraping process
        print('Something went wrong: ', e)
        # Ask user if they want to continue or quit
        if input('Would you like me to continue? Type y or n: ') == 'n':
            driver.quit()
            print('Indicated no continuation. Closing...')
            return

    # Shuffle the negative posts randomly and insert them into the database if they are not already in the database
    random.shuffle(analyzedPosts)
    insertCount = 0
    print('Inserting negative posts to the database...')
    for post in analyzedPosts:
        if not database.isPostAlreadyInDb(post['headline']):
            database.insertPost(post)
            insertCount +=1
    # Print success message with total number of inserted posts and elapsed time
    print('Posts inserted successfully! Closing...')
    end = time.time()
    print('Time: ', end-start)

# Call the main function
main()