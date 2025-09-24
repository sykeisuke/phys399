from langchain_openai import OpenAIEmbeddings, ChatOpenAI
from langchain_community.vectorstores import Chroma
from langchain_core.documents import Document
from langchain.tools.retriever import create_retriever_tool
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import AgentExecutor, create_openai_tools_agent
import pandas as pd

CSV_PATH = "../data/lec11_ex1.csv"
PERSIST_DIR = "../data/chroma_lec11_ex1_db"
EMB_MODEL = "text-embedding-3-small"
CHAT_MODEL = "gpt-5-nano"

# ----------------- Load CSV -> Documents -----------------
def csv_to_documents(csv_path):
    df = pd.read_csv(csv_path)   
    docs = []

    for i in range(len(df)):
        row = df.iloc[i]
        content = (
            "Course code: " + str(row["Course code"]) + "\n"
            "Title: " + str(row["Title"]) + "\n"
            "Credits: " + str(row["Credits"]) + "\n"
            "Instructor: " + str(row["Instructor"]) + "\n"
            "Days: " + str(row["Days"]) + "\n"
            "Time: " + str(row["Time"]) + "\n"
            "Room: " + str(row["Room"]) + "\n"
            "Capacity: " + str(row["Capacity"]) + "\n"
            "Semester: " + str(row["Semester"])
        )
        docs.append(Document(page_content=content))
    
    return docs

# ----------------- Build / Load Chroma -----------------
def build_chroma(docs):
    embeddings = OpenAIEmbeddings(model=EMB_MODEL)
    vectordb = Chroma.from_documents(
        documents=docs,
        embedding=embeddings,
        persist_directory=PERSIST_DIR
    )
    return vectordb

# ----------------- Create a retriever tool for agent -----------------
def build_retriever_tool(vectordb):
    retriever = vectordb.as_retriever(search_kwargs={"k": 4})
    tool = create_retriever_tool(
        retriever=retriever,
        name="physics_courses",
        description="Search for physics courses by code, title, instructor, credits, days, time, room, or semester."
    )
    return tool

# ----------------- Minimal RAG agent (optional demo) -----------------
def build_agent(tool):
    llm = ChatOpenAI(model=CHAT_MODEL)

    prompt = ChatPromptTemplate.from_messages([
        ("system",
         "You are a helpful assistant Phoebe for the UH Manoa Physics course catalog. "
         "Answer clearly and concisely about courses, instructors, schedules, credits, or semesters. "
         "If the answer is not in the data, say you don't know."),
        MessagesPlaceholder("chat_history"),
        ("human", "{input}"),
        MessagesPlaceholder("agent_scratchpad"),
    ])

    agent = create_openai_tools_agent(llm, tools=[tool], prompt=prompt)
    executor = AgentExecutor(agent=agent, tools=[tool], verbose=False)
    return executor

# ----------------- Main -----------------
def main():
    # 1) Read CSV -> Documents
    docs = csv_to_documents(CSV_PATH)

    # 2) Build or load Chroma vector DB
    vectordb = build_chroma(docs)

    # 3) Build RAG agent (LLM + retriever tool)
    tool = build_retriever_tool(vectordb)
    agent = build_agent(tool)

    # 4) Run the agent
    chat_history = []
    user_q = "Which physics courses are taught by Prof. Yoshihara in Fall 2025?"
    print(f"Student Question: {user_q}")
    res = agent.invoke({"input": user_q, "chat_history": chat_history})

    print("\n--- Agent answer ---")
    print(res["output"])

if __name__ == "__main__":
    main()

