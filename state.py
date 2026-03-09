from typing import TypedDict, List
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

class State(TypedDict):
    document: str
    chunks: List[str]
    summaries: List[str]
    final_summary: str
    analysis: str
    


llm = ChatOpenAI(model="gpt-4o-mini", 
                 api_key= os.getenv('OPENAI_API_KEY'),
                 temperature=0)
    
def load_document(state: State):
    doc = state["document"]
    return {"document": doc}

def chunk_document(state: State):
    text = state["document"]
    chunks = [text[i:i+1000] for i in range(0, len(text), 1000)]
    return {"chunks": chunks}

def summarize_chunks(state: State):
    summaries = []

    for chunk in state["chunks"]:
        response = llm.invoke(f"Summarize this text:\n{chunk}")
        summaries.append(response.content)

    return {"summaries": summaries}

def combine_summaries(state: State):
    combined = "\n".join(state["summaries"])

    final_summary = llm.invoke(
        f"Combine these summaries into one concise summary:\n{combined}"
    )

    return {"final_summary": final_summary.content}

def analyze_summary(state: State):

    analysis = llm.invoke(
        f"""
        Analyze this summary and extract:
        - Key insights
        - Important themes
        - Potential risks
        
        Summary:
        {state["final_summary"]}
        """
    )

    return {"analysis": analysis.content}