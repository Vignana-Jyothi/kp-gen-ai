import pandas as pd
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from sklearn.feature_extraction.text import TfidfVectorizer

from sklearn.metrics.pairwise import cosine_similarity

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

stop_words = set(stopwords.words('english'))
lemmatizer = WordNetLemmatizer()

def preprocess(text):
    tokens = nltk.word_tokenize(text.lower())
    tokens = [lemmatizer.lemmatize(token) for token in tokens if token.isalpha() and token not in stop_words]
    return ' '.join(tokens)

data = pd.read_csv('projects.csv')  # Assuming the project titles are in a CSV file
data['processed_titles'] = data['titles'].apply(preprocess)
data.to_csv('processed_projects.csv', index=False)


vectorizer = TfidfVectorizer()
X = vectorizer.fit_transform(data['processed_titles'])


# Compute cosine similarity matrix
similarity_matrix = cosine_similarity(X)

# Convert to DataFrame for easier analysis
similarity_df = pd.DataFrame(similarity_matrix, index=data['titles'], columns=data['titles'])

# Set a threshold for similarity score
threshold = 0.8  # You can adjust this value

# Find pairs with similarity above the threshold
duplicates = []
for idx, row in similarity_df.iterrows():
    similar_titles = row[row > threshold].index.tolist()
    similar_titles.remove(idx)  # Remove self-match
    if similar_titles:
        duplicates.append((idx, similar_titles))

# Print or save duplicate pairs
for title, dupes in duplicates:
    print(f"Title: {title}")
    print(f"Duplicates: {', '.join(dupes)}\n")

