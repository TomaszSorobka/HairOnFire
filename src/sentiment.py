import pandas as pd
import nltk
from pprint import pprint
#download it if first time
#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

class ProblemRecognition:
    def __init__(self):
        self.sia = SIA()

    def progressBar(self, progress, total):
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        print(f'\r|{bar}|{percent:.2f}%', end="\r")

    def getPolarityScores(self, posts):
        for post in posts:
            pol_score = self.sia.polarity_scores(post['headline'])
            post['compound'] = pol_score['compound']
        return posts

    def interpretPolarityScores(self, posts):
        polaredPosts = self.getPolarityScores(posts)
        counter = 0
        for post in polaredPosts:
            if post['compound'] > 0.2:
                post['label'] = 1
            elif post['compound'] < -0.2:
                post['label'] = -1
            else:
                post['label'] = 0
            self.progressBar(counter + 1, len(polaredPosts))
            counter+=1
        return polaredPosts
    
    def getNegativePosts(self, posts):
        interpretedPosts = self.interpretPolarityScores(posts)
        negativePosts = [post for post in interpretedPosts if post['label'] == -1]
        print()
        print('Negative posts extracted successfully. Number of posts: ', len(negativePosts))
        return negativePosts
