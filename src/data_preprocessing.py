# src/data_preprocessing.py
import re
import string

def clean_text(text):
    """Cleans text by removing URLs, punctuation, numbers, and extra spaces."""
    if not isinstance(text, str):
        return ""
    # Remove URLs
    text = re.sub(r'http\S+|www\S+|https\S+', '', text, flags=re.MULTILINE)
    # Remove numbers
    text = re.sub(r'\d+', '', text)
    # Remove punctuation
    text = text.translate(str.maketrans('', '', string.punctuation))
    # Remove extra spaces and lowercase
    text = text.lower().strip()
    return text
