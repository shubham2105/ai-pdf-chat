from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
import time

start = time.time()

print("Model Laoding")

model= SentenceTransformer("BAAI/bge-small-en-v1.5")

client = PersistentClient(path="chroma_db")
collection = client.get_collection(name="pdf_chunks")

while True:

    query = input("\n Ask a Question: ")
    if query.lower() == "exit":
        break

    query_embedding = model.encode(query).tolist()

    results = collection.query(
        query_embeddings = [query_embedding], 
        n_results =3 
    )
    print(
    f"Search took {time.time() - start:.4f}s"
    )


    for i, doc in enumerate(results["documents"][0]):
        print(f"\n{"="*50}")
        print(f"Result {i+1}")
        print(f"{"="*50}")
        print(doc[:1000])