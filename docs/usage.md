# ZeroLoom Usage Guide

## Basic Analysis

Analyze a UTF-8 text file:

```bash
zeroloom examples/sample.txt
```

The program reports:

- Character count
- Word count
- Line count
- Unique word count

## Frequency Analysis

To display the most frequent words:

```bash
zeroloom examples/sample.txt --frequency --top 5
```

## Running Tests

```bash
PYTHONPATH=src python3 -m unittest discover -s tests -v
```
