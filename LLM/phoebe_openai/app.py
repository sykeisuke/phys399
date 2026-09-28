"""PHYS399 Exercise 1: a small course-catalog RAG app using the OpenAI API.

Run from the repository root with:
    streamlit run LLM/phoebe_openai/app.py
"""

from hashlib import sha256
from pathlib import Path

import pandas as pd
import streamlit as st
from langchain.agents import create_agent
from langchain.tools import tool
from langchain_chroma import Chroma
from langchain_core.documents import Document
from langchain_openai import ChatOpenAI, OpenAIEmbeddings


CSV_PATH = Path(__file__).resolve().parents[2] / "JupyterNote/data/lec11_ex1.csv"
CHAT_MODEL = "gpt-6-luna"
EMBEDDING_MODEL = "text-embedding-3-small"


def load_documents(csv_path: Path) -> list[Document]:
    """Turn each CSV row into one searchable LangChain document."""
    catalog = pd.read_csv(csv_path).fillna("")
    documents = []
    for row_number, row in catalog.iterrows():
        content = "\n".join(f"{column}: {row[column]}" for column in catalog.columns)
        documents.append(
            Document(page_content=content, metadata={"row_number": int(row_number)})
        )
    return documents


def build_store(documents: list[Document], api_key: str) -> Chroma:
    """Embed the catalog once and keep Chroma in memory for this browser session."""
    embeddings = OpenAIEmbeddings(model=EMBEDDING_MODEL, api_key=api_key)
    store = Chroma(
        collection_name="phys399_course_catalog",
        embedding_function=embeddings,
    )
    ids = [f"course-{document.metadata['row_number']}" for document in documents]
    store.add_documents(documents=documents, ids=ids)
    return store


def build_agent(store: Chroma, api_key: str):
    @tool
    def search_courses(query: str) -> str:
        """Search the provided Physics course catalog by course, instructor, topic, or schedule."""
        matches = store.similarity_search(query, k=8)
        if not matches:
            return "No matching courses found in the provided catalog."
        return "\n\n".join(document.page_content for document in matches)

    model = ChatOpenAI(
        model=CHAT_MODEL,
        api_key=api_key,
        use_responses_api=True,
        reasoning_effort="none",
    )
    return create_agent(
        model=model,
        tools=[search_courses],
        system_prompt=(
            "You are Phoebe, a friendly guide to the provided UH Manoa Physics "
            "course catalog. Always call search_courses before answering a course "
            "question. Base your answer only on the returned catalog rows. Mention "
            "course codes when possible. If the results do not support an answer, "
            "say that you do not know. The catalog is for Fall 2025; do not present "
            "it as a current schedule. Keep answers concise."
        ),
    )


st.set_page_config(page_title="Phoebe | PHYS399", page_icon="🌺")
st.title("🌺 Phoebe: Physics course guide")
st.caption("PHYS399 Exercise 1 · Fall 2025 sample catalog · OpenAI API")

with st.sidebar:
    st.header("Setup")
    api_key = st.text_input("OpenAI API key", type="password")
    st.caption("The key is used for this local app session and is not saved to disk.")
    st.caption(f"Chat: {CHAT_MODEL} · Embeddings: {EMBEDDING_MODEL}")
    if st.button("Clear conversation"):
        st.session_state.pop("conversation", None)
        st.rerun()

if not api_key:
    st.info("Enter your own OpenAI API key in the sidebar to start.")
    st.stop()

if not CSV_PATH.is_file():
    st.error(f"Course CSV not found: {CSV_PATH}. Download the complete repository ZIP.")
    st.stop()

key_fingerprint = sha256(api_key.encode()).hexdigest()
if st.session_state.get("key_fingerprint") != key_fingerprint:
    st.session_state.pop("store", None)
    st.session_state.pop("conversation", None)
    st.session_state.key_fingerprint = key_fingerprint

if "store" not in st.session_state:
    try:
        with st.spinner("Embedding the course catalog (first run only)..."):
            documents = load_documents(CSV_PATH)
            st.session_state.store = build_store(documents, api_key)
    except Exception as exc:
        st.error(f"Could not build the course index: {exc}")
        st.stop()

if "conversation" not in st.session_state:
    st.session_state.conversation = []

for message in st.session_state.conversation:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

if question := st.chat_input("Ask about a course, instructor, or meeting time..."):
    with st.chat_message("user"):
        st.markdown(question)
    messages = st.session_state.conversation + [{"role": "user", "content": question}]
    try:
        agent = build_agent(st.session_state.store, api_key)
        with st.chat_message("assistant"):
            with st.spinner("Searching the catalog..."):
                result = agent.invoke({"messages": messages})
            answer = result["messages"][-1].text
            st.markdown(answer)
    except Exception as exc:
        st.error(f"The request failed: {exc}")
    else:
        st.session_state.conversation = messages + [
            {"role": "assistant", "content": answer}
        ]
