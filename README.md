# SummarizerAgent

A production-ready AI agent that summarizes PDF documents using modern LLM orchestration.
The project demonstrates an **agentic document summarization pipeline** built with **LangChain**, **LangGraph-style orchestration**, and **PyPDFium2** for efficient PDF processing.

This repository showcases how to build a scalable **AI-powered summarization system** with a clean architecture and CI/CD integration.

---

# Features

* Load and process PDF documents efficiently
* Automatic text chunking for large documents
* LLM-powered summarization
* Modular agent-based architecture
* CI/CD pipeline for testing and validation
* Easily extensible for additional document analysis tasks

---

# Tech Stack

* Python
* LangChain
* LangChain OpenAI
* PyPDFium2
* GitHub Actions (CI/CD)

---
### Components

**PDF Loader**

* Extracts text from PDFs using PyPDFium2

**Summarizer**

* Splits text into manageable chunks
* Sends chunks to an LLM for summarization

**Agent**

* Orchestrates the pipeline
* Coordinates document loading and summarization

---

# Installation

Clone the repository:

```
git clone https://github.com/roymohanaroy/SummarizerAgent.git
cd SummarizerAgent
```

Create a virtual environment:

```
python -m venv venv
```

Activate the environment:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

Install dependencies:

```
pip install -r requirements.txt
```

---

# Environment Variables

Set your API key before running the agent.

Example:

```
export OPENAI_API_KEY="your_api_key"
```

Windows:

```
set OPENAI_API_KEY=your_api_key
```

---

# Usage

Run the summarizer agent from the command line:

```
python main.py path_to_pdf
```

Example:

```
python main.py research_paper.pdf
```

The agent will:

1. Load the PDF
2. Extract text
3. Split text into chunks
4. Generate summaries
5. Output the final combined summary

---

# Example Workflow

```
PDF → Text Extraction → Chunking → LLM Summaries → Final Summary
```

---

# Testing

Run unit tests with:

```
pytest tests/
```

---

# CI/CD Pipeline

The project includes a **GitHub Actions workflow** that automatically:

* Installs dependencies
* Runs tests
* Validates the build

Triggered on:

* Pull Requests
* Pushes to main branch

---

# Future Improvements

* Add LangGraph workflow orchestration
* Support multiple document formats
* Add vector database for retrieval
* Build a web interface using Streamlit or FastAPI
* Deploy as a microservice

---

# Use Cases

* Research paper summarization
* Legal document analysis
* Business report summarization
* Knowledge extraction pipelines

---

# Contributing

Contributions are welcome. Please open an issue or submit a pull request.

---

# License

MIT License
