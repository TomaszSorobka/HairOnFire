# Import necessary modules
from dotenv import load_dotenv
from scrapers.scraper import Scraper
import os
import praw

# Define ScrapeReddit class and inherit from Scraper class
class ScrapeReddit(Scraper):
    # Define constructor method
    def __init__(self):
        self.configure() #load environment variables
        self.user_agent = 'Scraper 1.0 by /u/Content-Crew1246' #Reddit API requires user agent
        self.reddit = praw.Reddit( #create instance of Reddit class
            client_id='3TTUd3_fSgbGLu5y5NjeVg', #unique client id
            client_secret=os.getenv('client_secret_reddit'), #client secret loaded from environment variable
            user_agent=self.user_agent #user agent string
        )
        self.limit = 100 #default limit for number of posts to scrape
        self.subreddits = ['Entrepreneur', 'lifehacks', 'VideoEditing'] #list of subreddits to scrape

    # Define method to configure environment variables
    def configure(self):
        load_dotenv() #load environment variables from .env file

    # Define method to set limit for number of posts to scrape
    def setLimit(self, limit):
        self.limit = limit

    # Define method to scrape data from Reddit
    def scrapeData(self):
        print('Initializing scraping Reddit...')
        posts = list() #create empty list to store posts
        count = 0 #initialize count for progress bar
        for subreddit in self.subreddits: #iterate through list of subreddits
            for submission in self.reddit.subreddit(subreddit).hot(limit=self.limit): #iterate through hot posts in each subreddit
                posts.append(dict(headline=submission.title, url=submission.url, category=subreddit.lower())) # add post information to dictionary and append to list
                self.progressBar(count + 1, len(self.subreddits * self.limit)) #update progress bar
                count +=1 #increment count
        print()
        print('Reddit successfully scraped! Number of posts: ', len(posts))
        return posts #return list of scraped posts
