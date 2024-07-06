
from preprocess import preprocess_corpus
from index_corpus import create_index
from retrieve import load_index, retrieve
from generate import generate

def rag_pipeline(query):
    index = load_index("../index/corpus.index")
    corpus = preprocess_corpus("../data/corpus")
    top_k_indices = retrieve(query, index)
    retrieved_docs = " ".join([corpus[i] for i in top_k_indices[0]])
    prompt = query + " " + retrieved_docs
    response = generate(prompt)
    return response

if __name__ == "__main__":
    query = "What is topic A?"
    response = rag_pipeline(query)
    print("Response:", response)
