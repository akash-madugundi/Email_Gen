import re
from html import unescape

def clean_text(text: str) -> str:
    if not isinstance(text, str):
        return ""

    # Unescape HTML entities
    text = unescape(text)

    # Remove HTML tags
    text = re.sub(r'<[^>]+>', ' ', text)

    # Remove URLs
    text = re.sub(r'http\S+|www\.\S+', ' ', text)

    # Remove special characters except alphanumeric and common punctuation
    text = re.sub(r'[^a-zA-Z0-9.,!?;:\'\"()\[\]\s]', ' ', text)

    # Replace multiple whitespace characters (spaces, newlines, tabs) with a single space
    text = re.sub(r'\s+', ' ', text)

    # Trim leading and trailing whitespace
    return text.strip()