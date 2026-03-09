from langgraph.graph import StateGraph, START, END
from state import State,load_document,chunk_document,summarize_chunks,combine_summaries,analyze_summary

graph = StateGraph(State)

graph.add_node("load_document", load_document)
graph.add_node("chunk_document", chunk_document)
graph.add_node("summarize_chunks", summarize_chunks)
graph.add_node("combine_summaries", combine_summaries)
graph.add_node("analyze_summary", analyze_summary)

graph.add_edge(START, "load_document")
graph.add_edge("load_document", "chunk_document")
graph.add_edge("chunk_document", "summarize_chunks")
graph.add_edge("summarize_chunks", "combine_summaries")
graph.add_edge("combine_summaries", "analyze_summary")
graph.add_edge("analyze_summary", END)

app = graph.compile()