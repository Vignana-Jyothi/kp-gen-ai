
import os

def preprocess_corpus(corpus_dir):
    documents = []
    for filename in os.listdir(corpus_dir):
        with open(os.path.join(corpus_dir, filename), 'r') as file:
            documents.append(file.read())
    return documents

if __name__ == "__main__":
    corpus_dir = "../data/corpus"
    documents = preprocess_corpus(corpus_dir)
    print("Preprocessed Documents:", documents)
