
import logging
from fuzzywuzzy import fuzz

class WordFinder:
    """
    WordFinder is a class designed to find words in a sentence with a given similarity threshold.

    Attributes:
        sentence (str): The input sentence to search for words.
        logger (logging.Logger): A logger for the WordFinder class.

    Methods:
        _clean_sentence(): Cleans the input sentence by removing non-alphabetic characters and converting to lowercase.
        find_words(target_words, similarity_threshold=80): Finds words in the cleaned sentence that match the target words
            based on a similarity threshold.

    Example:
        word_finder = WordFinder("This is a sample sentence.")
        result = word_finder.find_words(["example", "word"])
        print(result)  # Output: {'example'}
    """

    def __init__(self, sentence=None):
        """
        Initializes a new instance of the WordFinder class.

        Args:
            sentence (str): The input sentence to be processed.
        """
        self.sentence = sentence
        self.logger = logging.getLogger(__name__)

    def _clean_sentence(self):
        """
        Cleans the input sentence by removing non-alphabetic characters and converting to lowercase.

        Returns:
            str: Cleaned sentence.
        """
        if self.sentence is None:
            return ""

        return ''.join(char.lower() if char.isalpha() else ' ' for char in self.sentence)

    def find_words(self, target_words, similarity_threshold=80):
        """
        Finds words in the cleaned sentence that match the target words based on a similarity threshold.

        Args:
            target_words (list): List of target words to search for.
            similarity_threshold (int): Minimum similarity threshold (default is 80).

        Returns:
            set: Set of found words.
        """
        cleaned_string = self._clean_sentence()
        cleaned_words = set(cleaned_string.split())

        found_words = set()
        for target_word in target_words:
            for cleaned_word in cleaned_words:
                if fuzz.ratio(target_word.lower(), cleaned_word) >= similarity_threshold:
                    found_words.add(cleaned_word)
                    break

        return found_words