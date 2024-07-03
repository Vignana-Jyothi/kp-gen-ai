import nltk
from nltk.tokenize import word_tokenize
from nltk.util import bigrams
from nltk.metrics import edit_distance
import numpy as np

# Function to read sentences from a file
def read_sentences_from_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        sentences = file.readlines()
    return [sentence.strip() for sentence in sentences]

# Load sentences from files
source_of_truth = read_sentences_from_file('source_of_truth.txt') 
input_sentences = read_sentences_from_file('input.txt')

# Function to compute edit distance at word level
def word_level_edit_distance(input_sentence, source_sentence):
    input_words = word_tokenize(input_sentence.lower())
    source_words = word_tokenize(source_sentence.lower())
    distances = np.zeros((len(input_words), len(source_words)))
    for i, input_word in enumerate(input_words):
        for j, source_word in enumerate(source_words):
            distances[i, j] = edit_distance(input_word, source_word)
    return np.sum(np.min(distances, axis=1)) / len(input_words)

# Function to compute bigram similarity
def bigram_similarity(input_sentence, source_sentence):
    input_bigrams = list(bigrams(word_tokenize(input_sentence.lower())))
    source_bigrams = list(bigrams(word_tokenize(source_sentence.lower())))
    common_bigrams = set(input_bigrams).intersection(set(source_bigrams))
    return len(common_bigrams) / max(len(input_bigrams), len(source_bigrams))

# Function to combine edit distance and bigram similarity
def combined_score(input_sentence, source_sentence):
    ed_score = word_level_edit_distance(input_sentence, source_sentence)
    bigram_score = bigram_similarity(input_sentence, source_sentence)
    combined = bigram_score - ed_score  # Combine by subtracting edit distance from bigram similarity
    return combined

# Function to find the best match from the source of truth sentences
def find_best_match(input_sentence, source_of_truth):
    scores = [combined_score(input_sentence, source_sentence) for source_sentence in source_of_truth]
    best_match_idx = np.argmax(scores)
    return source_of_truth[best_match_idx]

# Process each input sentence and find the best match from source of truth
for input_sentence in input_sentences:
    best_match_sentence = find_best_match(input_sentence, source_of_truth)
    print(f"Input Sentence: {input_sentence}")
    print(f"Best Match Sentence: {best_match_sentence}\n")
