import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from rag.loader import load_pdf

st.title("📄 AI Document Chatbot")

uploaded_file = st.file_uploader("Upload a PDF", type="pdf")

if uploaded_file:
    text = load_pdf(uploaded_file)

    st.subheader("Extracted Text")
    st.write(text[:2000])