### The ProblemRecognition class is used for sentiment analysis of headlines in a given set of posts.
# It uses the VADER (Valence Aware Dictionary and sEntiment Reasoner)
# sentiment analysis tool from NLTK library to compute the polarity scores of headlines,
# and then interpret the scores to assign a label of 1, 0 or -1 to each headline,
# representing positive, neutral or negative sentiment respectively.
# This class also has a method to extract negative posts based on their assigned labels.

# Import necessary modules
import nltk
#download it if first time
#nltk.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA 

class ProblemRecognition:  
    def __init__(self):
        # Initializing an object of the SentimentIntensityAnalyzer class
        self.sia = SIA()  

    # Defining a progress bar function
    def progressBar(self, progress, total):  
        # Calculating the percentage of progress
        percent = 100 * (progress / float(total))  
        # Creating a progress bar
        bar = '█' * int(percent) + '-' * (100-int(percent))  
        # Displaying the progress bar on the console
        print(f'\r|{bar}|{percent:.2f}%', end="\r")  

    # Defining a function to get polarity scores for posts
    def getPolarityScores(self, posts):  
        # Looping through all the posts
        for post in posts: # Getting the polarity score for the post
            pol_score = self.sia.polarity_scores(post['headline']) 
            # Adding the compound score to the post dictionary
            post['compound'] = pol_score['compound']  
        return posts  
    
    # Defining a function to interpret polarity scores
    def interpretPolarityScores(self, posts):  
        # Getting the polarity scores for all the posts
        polaredPosts = self.getPolarityScores(posts)  
        # Initializing a counter variable to keep track of progress
        counter = 0  
        # Looping through all the posts with polarity scores
        for post in polaredPosts:  
            if post['compound'] > 0.2:  # If the compound score is positive
                post['label'] = 1  # Label the post as positive
            elif post['compound'] < -0.2:  # If the compound score is negative
                post['label'] = -1  # Label the post as negative
            else:  # If the compound score is neutral
                post['label'] = 0  # Label the post as neutral
            # Updating the progress bar
            self.progressBar(counter + 1, len(polaredPosts))  
            counter+=1 
        return polaredPosts  
    
    # Defining a function to get negative posts
    def getNegativePosts(self, posts):  
        # Interpreting polarity scores for all posts
        interpretedPosts = self.interpretPolarityScores(posts)  
        # Extracting negative posts
        negativePosts = [post for post in interpretedPosts if post['label'] == -1]  
        print()
        print('Negative posts extracted successfully. Number of posts: ', len(negativePosts))
        return negativePosts
