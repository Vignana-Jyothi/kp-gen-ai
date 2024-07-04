import streamlit as st
import requests
import base64
import pickle
from htmlTemplates import css, bot_template, user_template
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationalRetrievalChain
from dotenv import load_dotenv
import os

st.set_page_config(page_title="Chatbot", page_icon=":speech_balloon:")
st.write(css, unsafe_allow_html=True)

load_dotenv()  # Load environment variables from .env file

def base64_to_vectorstore(base64_str):
    pickled_vectorstore = base64.b64decode(base64_str)
    return pickle.loads(pickled_vectorstore)

def load_vectorstore():
    response = requests.get("http://localhost:8000/vectorstore/")
    if response.status_code == 200:
        vectorstore_data = response.json()
        if "vectorstore" in vectorstore_data:
            return base64_to_vectorstore(vectorstore_data["vectorstore"])
    return None

def get_conversation_chain(vectorstore):
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        st.error("OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")
        return None
    
    llm = ChatOpenAI(openai_api_key=api_key)
    memory = ConversationBufferMemory(
        memory_key='chat_history', return_messages=True)
    conversation_chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vectorstore.as_retriever(),
        memory=memory
    )
    return conversation_chain

vectorstore = load_vectorstore()
if vectorstore:
    if "conversation" not in st.session_state:
        st.session_state.conversation = get_conversation_chain(vectorstore)
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = None

    if st.session_state.conversation:
        st.header("Ask Questions about your PDFs :speech_balloon:")
        user_question = st.text_input("Ask a question about your documents:")
        if user_question:
            response = st.session_state.conversation({'question': user_question})
            st.session_state.chat_history = response['chat_history']

            for i, message in enumerate(st.session_state.chat_history):
                if i % 2 == 0:
                    st.write(user_template.replace(
                        "{{MSG}}", message.content), unsafe_allow_html=True)
                else:
                    st.write(bot_template.replace(
                        "{{MSG}}", message.content), unsafe_allow_html=True)
else:
    st.error("No vector store found. Please upload PDFs first.")
