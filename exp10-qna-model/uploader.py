import streamlit as st
import requests

st.set_page_config(page_title="Upload PDFs", page_icon=":books:")

st.header("Upload PDF Files :books:")
uploaded_files = st.file_uploader("Upload your PDFs here and click on 'Process'", accept_multiple_files=True)

if st.button("Process"):
    if uploaded_files:
        with st.spinner("Processing"):
            files = [("files", (file.name, file, file.type)) for file in uploaded_files]
            response = requests.post("http://localhost:8000/upload/", files=files)
            if response.status_code == 200:
                st.success("PDFs processed successfully!")
            else:
                st.error("Failed to process PDFs")
    else:
        st.warning("Please upload PDF files")
