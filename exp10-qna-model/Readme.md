### Readme.md

# Multi-Page PDF Q&A Application

This project implements a multi-page PDF Q&A application using Streamlit and FastAPI. It consists of three main components:

1. **FastAPI Server**: Handles file uploads and vector store operations.
2. **Streamlit Uploader**: Allows users to upload PDF files and processes them.
3. **Streamlit Chatbot**: Provides a Q&A interface for users to interact with the content of the uploaded PDFs.

## Requirements

- Python 3.7+
- Streamlit
- FastAPI
- Uvicorn
- PyPDF2
- LangChain
- Requests
- Python-dotenv

## Setup

1. **Clone the Repository**:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. **Create a Virtual Environment**:
    ```sh
    python -m venv env
    source env/bin/activate  # On Windows use `env\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```sh
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your OpenAI API key:
    ```
    OPENAI_API_KEY=your-openai-api-key
    ```

## Running the Application

### 1. FastAPI Server

The FastAPI server handles the backend operations such as processing PDF uploads and managing the vector store. Start the server using the following command:

```sh
uvicorn server:app --reload
```

### 2. Streamlit Uploader

The Streamlit Uploader application provides an interface for users to upload PDF files and process them. It runs on port 8501 by default. Start the uploader application using the following command:

```sh
streamlit run uploader.py --server.port 8501
```

Access the Uploader application at [http://localhost:8501](http://localhost:8501).

### 3. Streamlit Chatbot

The Streamlit Chatbot application provides a Q&A interface for users to interact with the content of the uploaded PDFs. It runs on port 8502 by default. Start the chatbot application using the following command:

```sh
streamlit run chatbot.py --server.port 8502
```

Access the Chatbot application at [http://localhost:8502](http://localhost:8502).

## Summary

- **FastAPI Server**: Handles the backend processing and storage of PDF contents and vector stores.
- **Streamlit Uploader**: Provides a user interface for uploading and processing PDF files.
- **Streamlit Chatbot**: Provides a user interface for asking questions about the uploaded PDF content.

Make sure to start all three components for the application to work correctly. The Uploader application allows users to upload and process PDFs, while the Chatbot application provides a Q&A interface for the processed content. The FastAPI server acts as the backend for both applications, managing the vector store and processing the PDF files.