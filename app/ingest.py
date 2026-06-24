from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter

def load_and_split_pdf(pdf_path: str):
    # Load PDF
    loader = PyPDFLoader(pdf_path)
    documents = loader.load()

    print(f"Loaded{len(documents)} pages")

    # Split PDF into chunks
    splitter = RecursiveCharacterTextSplitter(
        chunk_size = 1000,
        chunk_overlap = 200
    )
    chunks = splitter.split_documents(documents)
    print(f"Created {len(chunks)} chunks")
    return chunks

if __name__ == "__main__":
    chunks = load_and_split_pdf("data/sample.pdf")

    print(f"\nTotal Chunks: {len(chunks)}")

for i, chunk in enumerate(chunks[:3]):
    print(f"\n{'='*50}")
    print(f"Chunk {i+1}")
    print(f"{'='*50}")

    print(chunk.page_content[:500])

    print("\nMetadata:")
    print(chunk.metadata)

print("\n First Chunk:\n")