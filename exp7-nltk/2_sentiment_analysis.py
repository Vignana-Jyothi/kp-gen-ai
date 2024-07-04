import nltk
nltk.download('vader_lexicon')

from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Initialize the sentiment analyzer
sia = SentimentIntensityAnalyzer()

# Sample text data (customer reviews, social media posts, etc.)
texts = [
    "I love this product! It's fantastic.",
    "This is the worst service I have ever received.",
    "The movie was okay, not great but not bad either.",
    "I'm extremely happy with my purchase!",
    "The food was terrible and the place was dirty."
]

# Analyze the sentiment of each text
for text in texts:
    sentiment = sia.polarity_scores(text)
    print(f"Text: {text}")
    print(f"Sentiment: {sentiment}\n")
