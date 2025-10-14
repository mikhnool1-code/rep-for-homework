import re


def fix_duplicates(sentence):
    return re.sub(r'\b(\w+)( \1\b)', r'\1', sentence)
