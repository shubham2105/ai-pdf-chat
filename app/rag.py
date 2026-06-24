from chromadb import PersistentClient
from sentence_transformers import SentenceTransformer
from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()

embedding_model = SentenceTransformer(
    "models/bge-small-en-v1.5"
)

client = PersistentClient(path="chroma_db")

collection = client.get_collection(
    name="pdf_chunks"
)

groq_client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)


def retrieval_context(question):

    embedding = embedding_model.encode(
        question
    ).tolist()

    results = collection.query(
        query_embeddings=[embedding],
        n_results=3
    )

    return "\n\n".join(
        results["documents"][0]
    )


def answer_question(question):

    context = retrieval_context(
        question
    )

    prompt = f"""
You are a helpful AI assistant.

Answer ONLY using the provided context.

If the answer cannot be found in the context, say:
"I could not find that information in the document."

Context:
{context}

Question:
{question}

Answer:
"""

    response = groq_client.chat.completions.create(
        model="meta-llama/llama-4-scout-17b-16e-instruct",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ]
    )

    return response.choices[0].message.content


while True:

    question = input("\nAsk a Question: ")

    if question.lower() == "exit":
        break

    answer = answer_question(
        question
    )

    print("\nAnswer:\n")
    print(answer)