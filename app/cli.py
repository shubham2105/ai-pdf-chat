from rag import answer_question

while True:

    question = input("Ask a Question: ")

    if question.lower() == "exit":
        break

    result = answer_question(question)

    print("\nAnswer:\n")
    print(result["answer"])

    print("\nSources:")

    seen_pages = set()

    for source in result["sources"]:
        page = source.get("page_label")

        if page not in seen_pages:
            seen_pages.add(page)
            print(f"Page {page}")