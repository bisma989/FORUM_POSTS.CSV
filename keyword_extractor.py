import spacy
from src.preprocess import preprocess_text

# Load spaCy model safely
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    import os
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_keywords_spacy(text):
    """
    Extracts keywords using spaCy by filtering Nouns, Proper Nouns, and Adjectives.
    Fallback to all alphanumeric tokens if specific POS tags are empty.
    """
    doc = nlp(text)
    keywords = [
        token.lemma_.lower() 
        for token in doc 
        if token.is_alpha and not token.is_stop and token.pos_ in ["NOUN", "PROPN", "ADJ", "VERB"]
    ]
    
    # Fallback if strict POS filtering returns nothing
    if not keywords:
        keywords = [token.lemma_.lower() for token in doc if token.is_alpha and not token.is_stop]
        
    return list(set(keywords))

def extract_keywords_nltk(text):
    """
    Extracts keywords using NLTK preprocessed tokens.
    """
    tokens = preprocess_text(text)
    # Keep words with length greater than 2 to filter out tiny noise words
    keywords = [word for word in tokens if len(word) > 2]
    
    # Fallback if filtered list is empty
    if not keywords and tokens:
        keywords = tokens
        
    return list(set(keywords))