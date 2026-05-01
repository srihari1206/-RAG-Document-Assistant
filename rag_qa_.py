import os
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

# 1. ADD YOUR KEY HERE
os.environ["GOOGLE_API_KEY"] = "YOUR_API_KEY_HERE"

# 2. LOAD EVERYTHING GLOBALLY (So it doesn't reload on every single question)
embeddings = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
db = Chroma(persist_directory="./chroma_db", embedding_function=embeddings)
retriever = db.as_retriever(search_kwargs={"k": 2})
llm = ChatGoogleGenerativeAI(model="gemini-2.5-flash", temperature=0)

template = """Answer the question based ONLY on the following context:
{context}

Question: {question}"""
prompt = ChatPromptTemplate.from_template(template)

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

rag_chain = (
    {"context": retriever | format_docs, "question": RunnablePassthrough()}
    | prompt
    | llm
    | StrOutputParser()
)

# 3. THE FUNCTION YOUR API WILL CALL
def get_answer(question: str):
    return rag_chain.invoke(question)
