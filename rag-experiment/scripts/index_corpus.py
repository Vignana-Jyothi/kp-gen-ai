
import faiss
import numpy as np
from preprocess import preprocess_corpus

def embed(texts):
    # Dummy embedding for illustration
    return np.array([np.random.rand(768) for _ in texts])

def create_index(corpus):
    corpus_embeddings = embed(corpus)
    index = faiss.IndexFlatL2(corpus_embeddings.shape[1])
    index.add(corpus_embeddings)
    faiss.write_index(index, '../index/corpus.index')
    return index

if __name__ == "__main__":
    corpus = preprocess_corpus("../data/corpus")
    index = create_index(corpus)
    print("Index created and saved.")
