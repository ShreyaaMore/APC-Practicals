"""Text tokenization module."""
import re

def tokenize_words(text):
    return re.findall(r'\b\w+\b', text)

def tokenize_sentences(text):
    sentences = re.split(r'[.!?]+', text)
    return [s.strip() for s in sentences if s.strip()]

