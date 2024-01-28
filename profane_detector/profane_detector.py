import logging
import os
from profane_detector.word_finder import WordFinder
from pkg_resources import resource_filename

class ProfaneDetector:
    def __init__(self):
        self._configure_logging()

    def _configure_logging(self):
        logging.basicConfig(level=logging.INFO)
        self.logger = logging.getLogger("ProfanityDetector")

    def _load_swear_words(self, language=None):
        # Get the path to the "swear-words" directory inside the installed package
        package_dir = resource_filename(__name__, 'swear-words')
        
        if language == None:
            swear_words = []
            for dirname, dirpath, files in os.walk(package_dir):
                for file in files:
                    full_file_path = os.path.join(package_dir, file)
                    with open(full_file_path, "r", encoding="utf-8") as f:
                        swear_words.extend([line.strip().lower() for line in f])
            
            return swear_words                   
        
        else:
            swear_words_path = os.path.join(package_dir, language)

            # Load swear words from the file
            with open(swear_words_path, "r", encoding="utf-8") as f:
                return {line.strip().lower() for line in f}

    def _detect_internal(self, language=None, sentence=None):
        swear_words = self._load_swear_words(language)
        word_finder = WordFinder(sentence)
        found_words = word_finder.find_words(swear_words)

        for found_word in found_words:
            self.logger.info(f"Profanity detected: {found_word}")

        return bool(found_words), found_words       
    
    def detect_api(self, language=None, sentence=None, return_words = False):
        to_return = None
        did_found, words = self._detect_internal(language, sentence)
        
        if return_words == True:
            to_return = did_found, words
        
        if return_words == False:
            to_return = did_found
        
        return to_return

if __name__ == "__main__":
    prof = ProfaneDetector()

    detected = prof.detect_api(input("Language: "), input("Swear sentence: "))
    print(detected)
