import unittest

from zeroloom.analyzer import analyze_text, word_frequency
from zeroloom.utils import normalize_whitespace


class TestAnalyzer(unittest.TestCase):

    def test_basic_statistics(self):
        result = analyze_text("Hello world. Hello again!")

        self.assertEqual(result["characters"], 25)
        self.assertEqual(result["words"], 4)
        self.assertEqual(result["lines"], 1)
        self.assertEqual(result["unique_words"], 3)

    def test_empty_text(self):
        result = analyze_text("")

        self.assertEqual(result["characters"], 0)
        self.assertEqual(result["words"], 0)
        self.assertEqual(result["lines"], 0)

    def test_word_frequency(self):
        result = word_frequency("apple banana apple cherry")

        self.assertEqual(result[0], ("apple", 2))

    def test_normalize_whitespace(self):
        text = "Hello   world\nPython"
        self.assertEqual(
            normalize_whitespace(text),
            "Hello world Python"
        )


if __name__ == "__main__":
    unittest.main()
