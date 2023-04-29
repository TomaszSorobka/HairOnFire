import pandas as pd
import nltk
from pprint import pprint
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA

sia = SIA()
results = []

df = pd.read_csv('posts.csv')
for line in df['title']:
    pol_score = sia.polarity_scores(line)
    pol_score['title'] = line
    results.append(pol_score)

#pprint(results[:3], width=100)
df_results = pd.DataFrame.from_records(results)
#print(df_results)
df_results['label'] = 0
df_results.loc[df_results['compound'] > 0.2, 'label'] = 1
df_results.loc[df_results['compound'] < -0.2, 'label'] = -1

df_label = df_results[['title', 'label']]
print(df_label)
df_label.to_csv('reddit_headlines_labels.csv', encoding = 'utf-8', index = False)
print(df_results.label.value_counts())

df_negative = df_label[df_label['label'] == -1]
df_negative.to_csv('reddit_headlines_negative_labels.csv', encoding = 'utf-8', index = False)