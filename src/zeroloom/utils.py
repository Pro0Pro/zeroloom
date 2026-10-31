from pathlib import Path


def is_text_file(filename):
    path = Path(filename)

    if not path.is_file():
        return False

    try:
        path.read_text(encoding="utf-8")
        return True
    except (UnicodeError, OSError):
        return False


def normalize_whitespace(text):
    return " ".join(text.split())


def get_file_size(filename):
    return Path(filename).stat().st_size
