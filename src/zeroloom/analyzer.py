from pathlib import Path
from collections import Counter
import re


def analyze_text(text):
    words = re.findall(r"\b\w+\b", text.lower())

    return {
        "characters": len(text),
        "words": len(words),
        "lines": len(text.splitlines()),
        "unique_words": len(set(words)),
    }


def analyze_file(filename):
    text = Path(filename).read_text(encoding="utf-8")
    return analyze_text(text)


def word_frequency(text, limit=10):
    words = re.findall(r"\b\w+\b", text.lower())
    return Counter(words).most_common(limit)
