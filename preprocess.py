import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK data is downloaded
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def preprocess_text(text):
    """
    Tokenizes text, converts to lowercase, and removes stopwords and punctuation.
    """
    stop_words = set(stopwords.words('english'))
    tokens = word_tokenize(text.lower())
    
    # Filter out stopwords and non-alphabetic tokens
    cleaned_tokens = [word for word in tokens if word.isalnum() and word not in stop_words]
    return cleaned_tokens