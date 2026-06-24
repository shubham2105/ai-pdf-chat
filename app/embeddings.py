from sentence_transformers import SentenceTransformer

print("Loading Model...")

model = SentenceTransformer("models/bge-small-en-v1.5")

print("Model Loaded!")

text = """
Attention is all you need
"""

embeddings = model.encode(text)

print(type(embeddings))
print(f"Vector Dimensions: {len(embeddings)})")
print(f"First 10 values: {embeddings[:10]}")