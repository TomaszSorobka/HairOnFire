# Import necessary modules
from selenium.webdriver.common.by import By  
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from scrapers.scraper import Scraper  # Importing the Scraper class from scrapers.scraper module


class ScrapeMumsnet(Scraper):  # Defining a class ScrapeMumsnet which inherits from Scraper class
    def __init__(self, driver): 
        self.driver = driver  # Assigning the driver to an instance variable
        self.links = [  # A list of dictionaries containing category and URL of Mumsnet forums to scrape
            {'category': 'education', 'url': 'https://www.mumsnet.com/talk/education?order-by=newest&page='},
            {'category': 'extra curriculars', 'url': 'https://www.mumsnet.com/talk/extra_curricular_activities?order-by=newest&page='},
            {'category': 'holidays', 'url': 'https://www.mumsnet.com/talk/holidays?order-by=newest&page='}]
        self.subpages = 2  # Number of subpages to scrape for each forum

    def getMain(self):  # A method to get the main element of the page
        try:
            main = WebDriverWait(self.driver, 10).until(
                EC.presence_of_element_located((By.TAG_NAME, 'main')))  # Waiting for the main tag to be present=
            return main  
        except:
            print("Error: could not get main from Mumsnet")  # If there is an error, print an error message

    def getHeadlines(self, category):  # A method to get the headlines of a given category
        main = self.getMain()  # Getting the main tag
        headlinesText = []  # An empty list to store the headlines
        headlines = main.find_elements(By.CSS_SELECTOR, '[data-click-id*="topic-thread-"]')  # Finding all headlines
        for headline in headlines:
            headlinesText.append(dict(headline=headline.text, url=headline.get_attribute('href'), category='parenting'))
            # Appending the headline text, URL and category to the headlinesText list as a dictionary
        return headlinesText 

    def scrapeData(self):  # A method to scrape data from Mumsnet forums
        print('Initializing scraping Mumsnet...') 
        allHeadlines = []  # An empty list to store all headlines from all forums
        counter = 1  # A counter variable to keep track of the progress
        for link in self.links:  # Looping through all links
            for i in range(1, self.subpages):  # Looping through all subpages for each link
                self.driver.get(link['url'] + str(i))  # Navigating to the current subpage
                allHeadlines += self.getHeadlines(link['category'])  # Getting the headlines and adding them to allHeadlines
            self.progressBar(counter, len(self.links))  # Updating the progress bar
            counter += 1  
        print()
        print('Mumsnet successfully scraped! Number of posts: ', len(allHeadlines)) 
        return allHeadlines 