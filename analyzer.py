# analyzer.py
import spacy

# Load the small English language model from spaCy
# You will need to download this model first!
try:
    nlp = spacy.load("en_core_web_sm")
except OSError:
    print("Spacy model not found. Please run: python -m spacy download en_core_web_sm")
    nlp = None

def analyze_text(text):
    """Analyzes text to extract key nouns, adjectives, and named entities."""
    if not nlp or not text:
        return "Analysis not available."
    
    doc = nlp(text)
    
    keywords = set() # Use a set to avoid duplicates
    
    # Extract named entities (like organizations, locations)
    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE", "PERSON", "PRODUCT"]:
            keywords.add(ent.text.lower())
            
    # Extract important nouns and adjectives, avoiding stop words
    for token in doc:
        if not token.is_stop and not token.is_punct and token.pos_ in ["NOUN", "PROPN", "ADJ"]:
            keywords.add(token.lemma_.lower()) # Use lemma for the root form of the word
            
    return ", ".join(sorted(list(keywords)))