from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapers.scraper import Scraper


class ScrapeMumsnet(Scraper):
    def __init__(self, driver):
        self.driver = driver
        self.links = [{'category': 'education', 'url': 'https://www.mumsnet.com/talk/education?order-by=newest&page='},
                      {'category': 'extra curriculars', 'url': 'https://www.mumsnet.com/talk/extra_curricular_activities?order-by=newest&page='},
                      {'category': 'holidays', 'url': 'https://www.mumsnet.com/talk/holidays?order-by=newest&page='}]
        self.subpages = 2
    def getMain(self):
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'main')))
            
            return main
        except:
            print("Error: could not get main from Mumsnet")

    def getHeadlines(self, category):
        main = self.getMain()
        headlinesText = []
        headlines = main.find_elements(By.CSS_SELECTOR, '[data-click-id*="topic-thread-"]')
        for headline in headlines:
            headlinesText.append(dict(headline=headline.text, url = headline.get_attribute('href'), category = 'parenting')) 
        return headlinesText
    
    def scrapeData(self):
        print('Initializing scraping Mumsnet...')
        allHeadlines = []
        counter = 1
        for link in self.links:
            for i in range(1,self.subpages):
                self.driver.get(link['url'] + str(i))
                allHeadlines += self.getHeadlines(link['category'])
            self.progressBar(counter, len(self.links))
            counter +=1
        print()
        print('Mumsnet successfully scraped! Number of posts: ', len(allHeadlines))
        return allHeadlines
