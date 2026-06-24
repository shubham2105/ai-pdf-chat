import streamlit as st
from app.rag import answer_question

st.set_page_config(
    page_title="AI PDF Chat",
    page_icon="📄",
    layout="wide"
)

st.title("📄 AI PDF Chat")
st.caption("Chat with your PDF using RAG + Groq")

# Initialize chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# Chat input
question = st.chat_input("Ask about the PDF...")

if question:

    # User message
    st.session_state.messages.append(
        {
            "role": "user",
            "content": question
        }
    )

    with st.chat_message("user"):
        st.write(question)

    # Assistant message
    with st.chat_message("assistant"):

        with st.spinner("Thinking..."):
            result = answer_question(question)

        st.write(result["answer"])

        # Show sources
        seen_pages = set()

        for source in result["sources"]:
            page = source.get("page_label")

            if page and page not in seen_pages:
                seen_pages.add(page)

        if seen_pages:
            st.caption(
                "Sources: " +
                ", ".join(
                    [f"Page {page}" for page in sorted(seen_pages)]
                )
            )

    st.session_state.messages.append(
        {
            "role": "assistant",
            "content": result["answer"]
        }
    )