import nltk
from nltk.tokenize import word_tokenize
from nltk import pos_tag, ne_chunk

# Download necessary resources
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')
nltk.download('maxent_ne_chunker')
nltk.download('words')

# Sample text
text = "Apple is looking at buying U.K. startup for $1 billion"

# Tokenization
tokens = word_tokenize(text)

# POS Tagging
tagged = pos_tag(tokens)

# Named Entity Recognition
entities = ne_chunk(tagged)

print("Tokens:", tokens)
print("POS Tags:", tagged)
print("Named Entities:", entities)

import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Process the text
text = "Apple is looking at buying U.K. startup for $1 billion."
doc = nlp(text)

# Extract entities
entities = [(ent.text, ent.label_) for ent in doc.ents]

print("Named Entities:", entities)

