# src/feature_engineering.py
from sklearn.feature_extraction.text import TfidfVectorizer
import joblib
import os

VECTORIZER_PATH = os.path.join("vectorizers", "tfidf_vectorizer.pkl")

def create_vectorizer(train_texts):
    """Creates and fits a TF-IDF vectorizer."""
    vectorizer = TfidfVectorizer(max_features=5000)
    vectorizer.fit(train_texts)
    joblib.dump(vectorizer, VECTORIZER_PATH)
    return vectorizer

def load_vectorizer():
    """Loads a saved TF-IDF vectorizer."""
    return joblib.load(VECTORIZER_PATH)
