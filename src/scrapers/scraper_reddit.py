from dotenv import load_dotenv

from scrapers.scraper import Scraper
import os

import praw

class ScrapeReddit(Scraper):
    def __init__(self):
        self.configure()
        self.user_agent = 'Scraper 1.0 by /u/Content-Crew1246'
        self.reddit = praw.Reddit(
            client_id='3TTUd3_fSgbGLu5y5NjeVg',
            client_secret=os.getenv('client_secret_reddit'),
            user_agent=self.user_agent
        )
        self.limit = 100 #default limit
        self.subreddits = ['Entrepreneur', 'lifehacks', 'VideoEditing']

    def configure(self):
        load_dotenv()

    def setLimit(self, limit):
        self.limit = limit

    def scrapeData(self):
        print('Initializing scraping Reddit...')
        posts = list()
        #hot new rising top
        count = 0
        for subreddit in self.subreddits:
            for submission in self.reddit.subreddit(subreddit).hot(limit=self.limit):
                posts.append(dict(headline =submission.title, url = submission.url, category = subreddit.lower()))
                self.progressBar(count + 1, len(self.subreddits * self.limit))
                count +=1
        print()
        print('Reddit successfully scraped! Number of posts: ', len(posts))
        return posts
