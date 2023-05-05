from abc import ABC, abstractmethod

class Scraper(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def scrapeData(self):
        pass

    def progressBar(self, progress, total):
        percent = 100 * (progress / float(total))
        bar = '█' * int(percent) + '-' * (100-int(percent))
        print(f'\r|{bar}|{percent:.2f}%', end="\r")

    