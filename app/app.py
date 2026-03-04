import sys
import os
import streamlit as st

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from rag.loader import load_pdf
from rag.chunker import split_text
from rag.vector_store import create_vector_store

st.title("📄 AI Document Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:

    text = load_pdf(uploaded_file)

    chunks = split_text(text)

    vector_store = create_vector_store(chunks)

    st.success("Vector database created successfully!")

    st.write(f"Total chunks stored: {len(chunks)}")