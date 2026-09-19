import os
import streamlit as st
from dotenv import load_dotenv
from rag_pipeline import MultimodalRAG

load_dotenv()
st.set_page_config(page_title="VisionVault AI", page_icon="🧠", layout="wide")
st.title("🧠 VisionVault AI")
st.caption("Multimodal RAG for PDFs, images, DOCX and text")

@st.cache_resource
def get_rag():
    return MultimodalRAG()

rag = get_rag()

with st.sidebar:
    st.header("Knowledge Base")
    files = st.file_uploader(
        "Upload documents",
        type=["pdf", "png", "jpg", "jpeg", "docx", "txt", "md"],
        accept_multiple_files=True
    )
    if st.button("Process Files", use_container_width=True):
        if files:
            with st.spinner("Processing files..."):
                count = rag.ingest_files(files)
            st.success(f"Indexed {count} chunks.")
        else:
            st.info("Upload files first.")

    if st.button("Clear Knowledge Base", use_container_width=True):
        rag.clear_database()
        st.success("Knowledge base cleared.")

question = st.text_area("Ask a question", placeholder="Compare information from the uploaded documents...")

if st.button("Ask AI", type="primary"):
    if not os.getenv("GROQ_API_KEY"):
        st.error("Add GROQ_API_KEY in your .env file.")
    elif not question.strip():
        st.warning("Enter a question.")
    else:
        with st.spinner("Searching and generating answer..."):
            answer, sources = rag.ask(question)
        st.subheader("Answer")
        st.write(answer)
        if sources:
            st.subheader("Sources")
            for source in sources:
                st.write(f"- {source}")
