from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer

from ingest import load_and_split_pdf


def create_vector_store():
    model = SentenceTransformer(
        "models/bge-small-en-v1.5"
    )

    client = PersistentClient(
        path="chroma_db"
    )

    collection = client.get_or_create_collection(
        name="pdf_chunks"
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

    print(f"Stored {len(chunks)} chunks")
    print(f"Collection count: {collection.count()}")


if __name__ == "__main__":
    create_vector_store()