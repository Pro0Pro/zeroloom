import argparse

from zeroloom.analyzer import analyze_file, word_frequency
from zeroloom.formatter import format_statistics, format_frequencies
from zeroloom.utils import is_text_file
from pathlib import Path


def main():
    parser = argparse.ArgumentParser(
        prog="zeroloom",
        description="A lightweight text analysis toolkit."
    )

    parser.add_argument(
        "file",
        help="Path to the text file to analyze"
    )

    parser.add_argument(
        "--frequency",
        action="store_true",
        help="Display the most common words"
    )

    parser.add_argument(
        "--top",
        type=int,
        default=10,
        help="Number of words to display (default: 10)"
    )

    args = parser.parse_args()

    if not is_text_file(args.file):
        parser.error("File does not exist or is not valid UTF-8 text.")

    if args.top < 1:
        parser.error("--top must be a positive integer.")

    stats = analyze_file(args.file)
    print(format_statistics(stats))

    if args.frequency:
        text = Path(args.file).read_text(encoding="utf-8")
        frequencies = word_frequency(text, args.top)

        print()
        print(format_frequencies(frequencies))


if __name__ == "__main__":
    main()
