import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

import praw

user_agent = 'Scraper 1.0 by /u/Content-Crew1246'
reddit = praw.Reddit(
    client_id='3TTUd3_fSgbGLu5y5NjeVg',
    client_secret='jcyZ7b4sV8l0uNnmlELzUfArUD1Mgg',
    user_agent=user_agent
)

#hot new rising top
posts = list()
for submission in reddit.subreddit('lifehacks').hot(limit=20):
    posts.append(dict(title =submission.title, body = submission.selftext))
print(len(posts))
df = pd.DataFrame(posts)
print(df)
df.to_csv('posts.csv', encoding= 'utf-8', index = False)

