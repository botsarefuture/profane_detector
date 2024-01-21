# ProfanityDetector
A Python library for profanity detection in text, providing a customizable ProfaneDetector class. Easily integrate into your projects to filter or flag content.

## Installing

```bash
pip install profane-detector
```

## Usage examples

```python
from profane_detector import ProfaneDetector

profane_detector = ProfaneDetector()

to_detect = "fuck you!"
language = "en"

did_detect = profane_detector.detect_api(language, to_detect)
print(did_detect)
```
