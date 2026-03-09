from graph import graph
from state import llm
from dotenv import load_dotenv
from state import State
from langchain_community.document_loaders import PyPDFLoader, PyPDFium2Loader

graph_builder = graph.compile()

def load_pdf(file_path: str) -> str:
    text = ""
    with open(file_path, 'rb') as f:
        #reader = PyPDF2.PdfReader(f)
        loader = PyPDFium2Loader(file_path)
        docs = loader.load()
        text = "\n".join([doc.page_content for doc in docs])
    return text

initial_state = State(
            document=load_pdf("agentic_ai.pdf"),
            chunks="",
            summaries="",
            final_summary="",
            analysis=""
        )

final_state = graph_builder.invoke(initial_state)

print("FINAL SUMMARY:\n", final_state["final_summary"])
print("\nANALYSIS:\n", final_state["analysis"])