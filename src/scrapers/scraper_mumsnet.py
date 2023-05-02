from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapers.scraper import Scraper


class ScrapeMumsnet(Scraper):
    def __init__(self, driver):
        self.driver = driver

    def getMain(self):
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'main')))
            
            return main
        except:
            print("Error: could not get main from Mumsnet")

    def getHeadlines(self):
        main = self.getMain()
        headlinesText = []
        headlines = main.find_elements(By.CSS_SELECTOR, '[data-click-id*="topic-thread-"]')
        for headline in headlines:
            headlinesText.append(dict(headline=headline.text, url = headline.get_attribute('href'), category = 'education')) 
        return headlinesText
    
    def scrapeData(self):
        link = 'https://www.mumsnet.com/talk/education?order-by=newest&page='#'https://www.mumsnet.com/talk/extra_curricular_activities?order-by=newest&page='
        allHeadlines = []
        for i in range(1,5):
            self.driver.get(link + str(i))
            allHeadlines += self.getHeadlines()
        return allHeadlines
