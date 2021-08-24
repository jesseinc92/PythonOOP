"""Word Finder: finds random words from a dictionary."""
import random 

class WordFinder:
    """Finds random words from a file passed by the user."""

    def __init__(self, url):
        self.url = url

        word_file = open(url, 'r')

        self.words = self.parse(open(self.url))

    def __repr__(self):
        return f'WordFinder(url={self.url})' 

    def parse(self, word_file):
        """Puts all words in a list"""

        return [w.strip() for w in word_file]

    def random(self):
        """Prints out a random word from the list"""

        return random.choice(self.words)




class SpecialWordFinder(WordFinder):
    """Returns a random word from a file, ignoring blank lines and comments"""

    def random(self, word_file):
        
        return [w.strip() for w in word_file if w.strip() and not w.startswith('#')]