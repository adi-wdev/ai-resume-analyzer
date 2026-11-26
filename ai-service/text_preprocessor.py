import re
import unicodedata


def normalize_text(text):

    # Normalize Unicode characters
    text = unicodedata.normalize("NFKC", text)

    # Convert to lowercase
    text = text.lower()

    # Remove spaces at beginning and end
    text = text.strip()

    # Normalize multiple spaces and tabs
    text = re.sub(r"[ \t]+", " ", text)

    # Normalize multiple consecutive newlines
    text = re.sub(r"\n+", "\n", text)

    return text


def tokenize_text(text):

    normalized = normalize_text(text)

    tokens = normalized.split()

    return tokens


def count_tokens(text):

    tokens = tokenize_text(text)

    return len(tokens)