import os

# Load text data from file
def load_data(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()

# Simple text cleaning
def clean_text(text):
    return text.replace("\n", " ").strip()
    