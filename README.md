# 🧠 CogniDoc: Autonomous RAG Knowledge Agent

CogniDoc is a modular Retrieval-Augmented Generation (RAG) pipeline designed to extract, embed, and synthesize insights from unstructured PDF documents. It utilizes LangChain to orchestrate a connection between a local Vector Database (ChromaDB) and a Large Language Model (Gemini 2.5 Flash), ensuring that all AI responses are grounded strictly in the provided source material to eliminate hallucination.

## 🚀 Key Features
*   **Modular Architecture:** Clean separation of concerns between data ingestion (`rag_database_.py`), AI reasoning (`rag_qa_.py`), and backend routing (`api.py`).
*   **Automated Text Chunking:** Utilizes `RecursiveCharacterTextSplitter` to intelligently break down dense PDFs while preserving semantic overlap.
*   **Local Vector Embeddings:** Leverages HuggingFace's `all-MiniLM-L6-v2` model to generate high-dimensional embeddings locally, reducing API costs and latency.
*   **Hallucination-Free Generation:** A custom LangChain prompt forces the Gemini 2.5 Flash model to answer questions based *only* on the retrieved ChromaDB context.
*   **FastAPI Backend:** Fully deployed as an asynchronous REST API, ready for enterprise integration.

## 🛠️ Tech Stack
*   **Framework:** LangChain
*   **Backend Server:** FastAPI, Uvicorn
*   **LLM Engine:** Google Gemini 2.5 Flash (`langchain-google-genai`)
*   **Vector Database:** ChromaDB
*   **Embedding Model:** HuggingFace Sentence Transformers (`all-MiniLM-L6-v2`)
*   **Document Processing:** PyPDF

---

## ⚙️ Installation & Setup

### 1. Clone the Repository
```bash
git clone https://github.com/YOUR_USERNAME/CogniDoc-RAG-Agent.git
cd CogniDoc-RAG-Agent
