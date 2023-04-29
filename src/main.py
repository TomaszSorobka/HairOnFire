from selenium import webdriver

from scrapers.scraper_mumsnet import ScrapeMumsnet
from scrapers.scraper_reddit import ScrapeReddit
from sentiment import ProblemRecognition
PATH = "C:\Program Files (x86)\chromedriver.exe"

options = webdriver.ChromeOptions()
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
driver = webdriver.Chrome(PATH, options=options)

# username : tomaszsorobka

# Mumsnet
mumsnet = ScrapeMumsnet(driver)
scrapedData = mumsnet.scrapeData()

# Reddit
reddit = ScrapeReddit()
scrapedData += reddit.scrapeData()


# Problem recognition
analyzeProblem = ProblemRecognition()
analyzedPosts = analyzeProblem.interpretPolarityScores(scrapedData)



# to csv/db
#df_results = pd.DataFrame.from_records(analyzedPosts)

# df = pd.DataFrame(posts)
# print(df)
# df.to_csv('posts.csv', encoding= 'utf-8', index = False)
#print(type(scrapedData))
#for i in scrapedData:
 #   print(i)