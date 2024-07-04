import streamlit as st


def main():
    st.set_page_config(page_title="Multi-Page Streamlit App", page_icon=":books:")

    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Upload PDFs", "Chatbot"])

    if page == "Upload PDFs":
        st.experimental_set_query_params(page="uploader")
        st.write("Redirecting to uploader...")
        st.experimental_rerun()
    elif page == "Chatbot":
        st.experimental_set_query_params(page="chatbot")
        st.write("Redirecting to chatbot...")
        st.experimental_rerun()

if __name__ == '__main__':
    main()
