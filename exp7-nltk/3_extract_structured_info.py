import spacy

# Load the pre-trained model
nlp = spacy.load("en_core_web_sm")

# Sample text data
texts = [
    "John Doe paid $29.99 for a book on January 5th, 2023.",
    "The conference will be held in New York on 21st July, 2024.",
    "Jane Smith purchased a new car for €20,000 on 3rd March 2022."
]

# Extract information
for text in texts:
    doc = nlp(text)
    print(f"Text: {text}")
    
    # Extract entities
    for ent in doc.ents:
        print(f"Entity: {ent.text}, Label: {ent.label_}")
    print("\n")

