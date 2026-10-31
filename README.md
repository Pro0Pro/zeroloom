# ZeroLoom

A lightweight Python toolkit for analyzing text files.

ZeroLoom provides simple tools for counting words,
characters, lines, and analyzing word frequencies.

## Features

- Text statistics
- Word frequency analysis
- Command-line interface
- UTF-8 text support
- Unit tests

## Installation

Clone the repository and install locally:

```bash
pip install -e .
```

## Usage

Analyze a file:

```bash
zeroloom examples/sample.txt
```

Display word frequencies:

```bash
zeroloom examples/sample.txt --frequency --top 5
```

## Development

Run the tests:

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
## License

No license has been specified.# zeroloom
A small collection of experimental developer utilities.
