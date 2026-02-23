
# preprocessing.py
# Text preprocessing functions for Resume Analyzer project

import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

# FUNCTION 1: Clean text
def clean_text(text):
    """Converts to lowercase and removes special characters"""
    text = text.lower()  # Convert to lowercase
    text = re.sub(r'[^a-z\s]', '', text)  # Keep only letters and spaces
    text = re.sub(r'\s+', ' ', text)  # Remove extra spaces
    text = text.strip()  # Remove leading/trailing spaces
    return text

# FUNCTION 2: Remove stop words
def remove_stop_words(text):
    """Removes common words like the, is, a, with"""
    stop_words = set(stopwords.words('english'))  # Get English stop words
    words = text.split()  # Split into words
    filtered_words = [word for word in words if word not in stop_words]  # Filter
    return ' '.join(filtered_words)  # Join back

# FUNCTION 3: Tokenize text
def tokenize_text(text):
    """Splits text into list of words"""
    tokens = word_tokenize(text)  # Tokenize using NLTK
    return tokens

# COMBINED FUNCTION: Complete preprocessing
def preprocess_resume(text):
    """
    Complete preprocessing pipeline:
    1. Clean text
    2. Remove stop words
    3. Tokenize
    Returns: List of cleaned words
    """
    text = clean_text(text)  # Step 1
    text = remove_stop_words(text)  # Step 2
    tokens = tokenize_text(text)  # Step 3
    return tokens
