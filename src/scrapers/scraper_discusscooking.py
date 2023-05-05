from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapers.scraper import Scraper


class ScrapeDiscussCooking(Scraper):
    def __init__(self, driver):
        self.driver = driver
        self.links = [{'category': 'cooking', 'url': 'https://www.discusscooking.com/forums/general-cooking.17/page-'}]
        self.subpages = 2
    def getThreads(self):
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.CLASS_NAME, 'js-threadList')))
            
            return main
        except:
            print("Error: could not get threadList from Discuss Cooking")

    def getHeadlines(self, category):
        threads = self.getThreads()
        headlinesText = []
        headlines = threads.find_elements(By.CLASS_NAME, 'structItem-title')
        for headline in headlines:
            headlinesText.append(dict(headline=headline.text, url = headline.get_attribute('href'), category = 'cooking')) 
        return headlinesText
    
    def scrapeData(self):
        print('Initializing scraping Discuss Cooking...')
        allHeadlines = []
        counter = 1
        for link in self.links:
            for i in range(1,self.subpages):
                self.driver.get(link['url'] + str(i))
                allHeadlines += self.getHeadlines(link['category'])
            self.progressBar(counter+1, self.subpages)
            counter +=1
        print()
        print('Discuss Cooking successfully scraped! Number of posts: ', len(allHeadlines))
        return allHeadlines
