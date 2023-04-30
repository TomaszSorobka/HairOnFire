import pandas as pd
import nltk
from pprint import pprint
#download it if first time
#nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

class ProblemRecognition:
    def __init__(self):
        self.sia = SIA()


    def getPolarityScores(self, posts):
        for post in posts:
            pol_score = self.sia.polarity_scores(post['headline'])
            post['compound'] = pol_score['compound']
        return posts

    def interpretPolarityScores(self, posts):
        polaredPosts = self.getPolarityScores(posts)
        for post in polaredPosts:
            if post['compound'] > 0.2:
                post['label'] = 1
            elif post['compound'] < -0.2:
                post['label'] = -1
            else:
                post['label'] = 0
        return polaredPosts
    
    def getNegativePosts(self, posts):
        interpretedPosts = self.interpretPolarityScores(posts)
        negativePosts = [post for post in interpretedPosts if post['label'] == -1]
        return negativePosts
# a = ProblemRecognition()
# print(a.getPolarityScores([{"headline": "wtf is that", "url": "lobocoobo"}]))

#pprint(results[:3], width=100)
# df_results = pd.DataFrame.from_records(results)
# #print(df_results)
# df_results['label'] = 0
# df_results.loc[df_results['compound'] > 0.2, 'label'] = 1
# df_results.loc[df_results['compound'] < -0.2, 'label'] = -1

# df_label = df_results[['title', 'label']]
# print(df_label)
# df_label.to_csv('reddit_headlines_labels.csv', encoding = 'utf-8', index = False)
# print(df_results.label.value_counts())

# df_negative = df_label[df_label['label'] == -1]
# df_negative.to_csv('reddit_headlines_negative_labels.csv', encoding = 'utf-8', index = False)