import streamlit as st
import tempfile
from graph import graph
from state import State
from langchain_community.document_loaders import PyPDFium2Loader
from dotenv import load_dotenv

# Load env variables (API keys etc.)
load_dotenv()

# Compile graph once
graph_builder = graph.compile()

st.set_page_config(page_title="Summarizer Agent", layout="wide")

st.title("🧠 Agentic PDF Summarizer")
st.markdown("Upload a PDF and get structured summary + analysis")

# ---- FILE UPLOAD ----
uploaded_file = st.file_uploader("Upload a PDF", type=["pdf"])

def load_pdf(file_path: str) -> str:
    loader = PyPDFium2Loader(file_path)
    docs = loader.load()
    return "\n".join([doc.page_content for doc in docs])

# ---- PROCESS BUTTON ----
if uploaded_file:
    if st.button("Run Summarizer"):
        with st.spinner("Processing document..."):

            # Save uploaded file temporarily
            with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
                tmp.write(uploaded_file.read())
                tmp_path = tmp.name

            # Load PDF text
            document_text = load_pdf(tmp_path)

            # Create initial state
            initial_state = State(
                document=document_text,
                chunks="",
                summaries="",
                final_summary="",
                analysis=""
            )

            # Run graph
            final_state = graph_builder.invoke(initial_state)

            # ---- OUTPUT ----
            st.subheader("📄 Final Summary")
            st.success(final_state["final_summary"])

            st.subheader("🔍 Analysis")
            st.info(final_state["analysis"])

            # ---- DOWNLOAD ----
            st.download_button(
                "Download Summary",
                final_state["final_summary"],
                file_name="summary.txt"
            )