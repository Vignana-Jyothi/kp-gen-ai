
import faiss
import numpy as np
from preprocess import preprocess_corpus

def embed(texts):
    # Dummy embedding for illustration
    return np.array([np.random.rand(768) for _ in texts])

def load_index(index_path):
    return faiss.read_index(index_path)

def retrieve(query, index, top_k=5):
    query_embedding = embed([query])
    _, I = index.search(query_embedding, top_k)
    return I

if __name__ == "__main__":
    index = load_index("../index/corpus.index")
    query = "What is topic A?"
    corpus = preprocess_corpus("../data/corpus")
    top_k_indices = retrieve(query, index)
    retrieved_docs = [corpus[i] for i in top_k_indices[0]]
    print("Retrieved Documents:", retrieved_docs)
