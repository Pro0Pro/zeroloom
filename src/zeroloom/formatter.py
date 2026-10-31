def format_statistics(stats):
    lines = ["ZeroLoom - Text Analysis", "-" * 28]

    for key, value in stats.items():
        label = key.replace("_", " ").title()
        lines.append(f"{label}: {value}")

    return "\n".join(lines)


def format_frequencies(frequencies):
    lines = ["Most Common Words", "-" * 28]

    for word, count in frequencies:
        lines.append(f"{word:<20} {count}")

    return "\n".join(lines)
