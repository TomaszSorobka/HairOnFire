# Import necessary modules
from abc import ABC, abstractmethod

# Create an abstract base class called Scraper that other scraper classes will inherit from
class Scraper(ABC):
    @abstractmethod
    def __init__(self):
        pass

    # Define an abstract method called scrapeData that subclasses must implement
    @abstractmethod
    def scrapeData(self):
        pass

    # Define a method called progressBar that shows a progress bar in the terminal
    # This method is not abstract, so it does not have to be implemented in subclasses
    def progressBar(self, progress, total):
        # Calculate the percentage of progress and create a bar that represents the percentage
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        # Print the progress bar with the percentage
        print(f'\r|{bar}|{percent:.2f}%', end="\r")