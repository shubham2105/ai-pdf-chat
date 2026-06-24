# 📄 AI PDF Chat

Chat with PDF documents using Retrieval-Augmented Generation (RAG), local embeddings, ChromaDB, and Groq LLMs.

## 🚀 Live Demo

👉 https://ai-pdf-chat-pzh4acbbwnswzhvjcqqm49.streamlit.app/

---

## 📌 Features

- 📄 PDF document ingestion
- ✂️ Intelligent document chunking
- 🔎 Semantic search using vector embeddings
- 🧠 Retrieval-Augmented Generation (RAG)
- ⚡ Fast inference using Groq
- 📚 Source page citations
- 💬 Chat-style Streamlit interface
- 🏠 Local embedding generation with BGE Small

---

## 🏗️ Architecture

```text
PDF
 │
 ▼
PyPDFLoader
 │
 ▼
Text Chunking
 │
 ▼
BGE-Small Embeddings
 │
 ▼
ChromaDB Vector Store
 │
 ▼
Semantic Retrieval
 │
 ▼
Groq LLM
 │
 ▼
Answer + Sources
```

---

## 🛠️ Tech Stack

### Frontend

- Streamlit

### Backend

- Python

### AI / RAG

- LangChain
- ChromaDB
- Sentence Transformers
- BAAI/bge-small-en-v1.5
- Groq API
- Llama 4 Scout

---

## 📂 Project Structure

```text
ai-pdf-chat/
│
├── app/
│   ├── ingest.py
│   ├── embeddings.py
│   ├── vector_store.py
│   ├── search.py
│   ├── rag.py
│   ├── cli.py
│   └── setup_vector_store.py
│
├── data/
│   └── sample.pdf
│
├── chroma_db/
│
├── streamlit_app.py
├── requirements.txt
├── .env
└── README.md
```

---

## ⚙️ Installation

### Clone Repository

```bash
git clone https://github.com/shubham2105/ai-pdf-chat.git

cd ai-pdf-chat
```

### Create Virtual Environment

Using uv:

```bash
uv venv
source .venv/bin/activate
```

### Install Dependencies

```bash
uv pip install -r requirements.txt
```

---

## 🔑 Environment Variables

Create a `.env` file:

```env
GROQ_API_KEY=your_groq_api_key
HF_TOKEN=your_huggingface_token
```

---

## 📄 Add PDF

Place your PDF inside:

```text
data/
```

Example:

```text
data/sample.pdf
```

---

## 🧠 Generate Embeddings & Vector Store

```bash
uv run app/setup_vector_store.py
```

This will:

- Load PDF
- Split into chunks
- Generate embeddings
- Store vectors in ChromaDB

---

## 💻 Run CLI Version

```bash
uv run app/cli.py
```

Example:

```text
Ask a Question:
What is self-attention?
```

---

## 🌐 Run Streamlit App

```bash
streamlit run streamlit_app.py
```

Open:

```text
http://localhost:8501
```

---

## 📸 Example Questions

- What is a Transformer?
- What is self-attention?
- What is multi-head attention?
- What BLEU score did the Transformer achieve?
- Why are positional encodings used?

---

## 🎯 Future Improvements

- Upload your own PDFs
- Multi-document support
- Chat memory
- Hybrid Search (BM25 + Vector Search)
- Re-ranking
- Citation highlighting
- PDF page preview

---

## 📖 Sample Document

Current demo uses:

**Attention Is All You Need (Transformer Paper)**

Authors:

- Ashish Vaswani
- Noam Shazeer
- Niki Parmar
- Jakob Uszkoreit
- Llion Jones
- Aidan Gomez
- Łukasz Kaiser
- Illia Polosukhin

---

## 👨‍💻 Author

**Shubham Dhole**

GitHub:

https://github.com/shubham2105

---

## ⭐ If you found this project useful

Please consider giving it a star on GitHub.
