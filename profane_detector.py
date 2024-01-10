# Importing necessary modules
import logging
from word_finder import WordFinder

# Defining the ProfaneDetector class
class ProfaneDetector:
    def __init__(self):
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ProfanityDetector")

    def _load_swear_words(self, language):
        # Assuming swear word files are named after language codes in the "swear-words" directory
        with open(f"swear-words/{language}", "r", encoding="utf-8") as f:
            return {line.strip().lower() for line in f}

    def _detect_internal(self, language, sentence):
        swear_words = self._load_swear_words(language)
        word_finder = WordFinder(sentence)
        found_words = word_finder.find_words(swear_words)

        for found_word in found_words:
            self.logger.info(f"Profanity detected: {found_word}")

        return bool(found_words), found_words

    def detect_api(self, language, sentence):
        did_found, words = self._detect_internal(language, sentence)
        return did_found

# Example usage:
prof = ProfaneDetector()

if __name__ == "__main__":
    detected = prof.detect_api("en", "Fuck")
    print(detected)
