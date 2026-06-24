# app/setup_vector_store.py

from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from app.ingest import load_and_split_pdf

def initialize_vector_store():
    client = PersistentClient(path="chroma_db")

    try:
        client.get_collection("pdf_chunks")
        print("Collection already exists")
        return

    except Exception:
        print("Creating collection...")

    collection = client.create_collection("pdf_chunks")

    model = SentenceTransformer(
        "BAAI/bge-small-en-v1.5"
    )

    chunks = load_and_split_pdf(
        "data/sample.pdf"
    )

    for i, chunk in enumerate(chunks):

        embedding = model.encode(
            chunk.page_content
        ).tolist()

        collection.add(
            ids=[str(i)],
            documents=[chunk.page_content],
            embeddings=[embedding],
            metadatas=[chunk.metadata]
        )

    print("Vector store created")