from selenium import webdriver

from scrapers.scraper_mumsnet import ScrapeMumsnet
from scrapers.scraper_reddit import ScrapeReddit
from sentiment import ProblemRecognition
from db_connect import DataBaseConnect

def setUpDriver():
    PATH = "C:\Program Files (x86)\chromedriver.exe"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--ignore-ssl-errors')
    driver = webdriver.Chrome(PATH, options=options)
    return driver

def main():
    driver = setUpDriver()
    database = DataBaseConnect()
    scrapedData = []

    reddit = ScrapeReddit()
    scrapedData += reddit.scrapeData()


    mumsnet = ScrapeMumsnet(driver)
    scrapedData += mumsnet.scrapeData()

    # Reddit
    

    driver.quit()
    # Problem recognition
    analyzeProblem = ProblemRecognition()
    analyzedPosts = analyzeProblem.getNegativePosts(scrapedData)

    print(analyzedPosts)
    for post in analyzedPosts:
        if not database.isPostAlreadyInDb(post['headline']):
            database.insertPost(post)


main()

# to csv/db
#df_results = pd.DataFrame.from_records(analyzedPosts)

# df = pd.DataFrame(posts)
# print(df)
# df.to_csv('posts.csv', encoding= 'utf-8', index = False)
#print(type(scrapedData))
#for i in scrapedData:
 #   print(i)