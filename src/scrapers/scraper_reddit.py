from dotenv import load_dotenv
import os

import praw

class ScrapeReddit:
    def __init__(self):
        self.configure()
        self.user_agent = 'Scraper 1.0 by /u/Content-Crew1246'
        self.reddit = praw.Reddit(
            client_id='3TTUd3_fSgbGLu5y5NjeVg',
            client_secret=os.getenv('client_secret_reddit'),#'jcyZ7b4sV8l0uNnmlELzUfArUD1Mgg',
            user_agent=self.user_agent
        )

    def configure(self):
        load_dotenv()

    def scrapeData(self, database):
        posts = list()
        #hot new rising top
        for submission in self.reddit.subreddit('lifehacks').hot(limit=20):
            # if database.isPostAlreadyInDb(submission.title):
            #     break
            posts.append(dict(headline =submission.title, url = submission.url, category = 'lifehacks'))
        return posts

#hot new rising top


