import unittest

from zeroloom.formatter import (
    format_statistics,
    format_frequencies
)


class TestFormatter(unittest.TestCase):

    def test_statistics_format(self):
        stats = {
            "characters": 20,
            "words": 4,
            "lines": 2
        }

        result = format_statistics(stats)

        self.assertIn("Characters: 20", result)
        self.assertIn("Words: 4", result)
        self.assertIn("Lines: 2", result)

    def test_frequency_format(self):
        frequencies = [
            ("python", 3),
            ("code", 2)
        ]

        result = format_frequencies(frequencies)

        self.assertIn("python", result)
        self.assertIn("code", result)


if __name__ == "__main__":
    unittest.main()
