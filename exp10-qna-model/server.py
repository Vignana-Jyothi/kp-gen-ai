import os
import pickle
import base64
from fastapi import FastAPI, UploadFile
from dotenv import load_dotenv
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS

load_dotenv()  # Load environment variables from .env file

app = FastAPI()
VECTOR_STORE_PATH = "vector_store.pkl"

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf.file)
        for page in pdf_reader.pages:
            text += page.extract_text()
    return text

def get_text_chunks(text):
    text_splitter = CharacterTextSplitter(
        separator="\n",
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len
    )
    chunks = text_splitter.split_text(text)
    return chunks

def save_vectorstore(vectorstore):
    with open(VECTOR_STORE_PATH, "wb") as f:
        pickle.dump(vectorstore, f)

def load_vectorstore():
    if os.path.exists(VECTOR_STORE_PATH):
        with open(VECTOR_STORE_PATH, "rb") as f:
            return pickle.load(f)
    return None

def get_vectorstore(text_chunks):
    embeddings = OpenAIEmbeddings(openai_api_key=os.getenv("OPENAI_API_KEY"))
    vectorstore = FAISS.from_texts(texts=text_chunks, embedding=embeddings)
    save_vectorstore(vectorstore)
    return vectorstore

def vectorstore_to_base64(vectorstore):
    pickled_vectorstore = pickle.dumps(vectorstore)
    return base64.b64encode(pickled_vectorstore).decode('utf-8')

def base64_to_vectorstore(base64_str):
    pickled_vectorstore = base64.b64decode(base64_str)
    return pickle.loads(pickled_vectorstore)

@app.post("/upload/")
async def upload_pdf(files: list[UploadFile]):
    raw_text = get_pdf_text(files)
    text_chunks = get_text_chunks(raw_text)
    vectorstore = get_vectorstore(text_chunks)
    save_vectorstore(vectorstore)
    return {"message": "PDFs processed successfully!"}

@app.get("/vectorstore/")
async def get_vector_store():
    vectorstore = load_vectorstore()
    if vectorstore:
        return {"vectorstore": vectorstore_to_base64(vectorstore)}
    else:
        return {"error": "No vector store found"}
