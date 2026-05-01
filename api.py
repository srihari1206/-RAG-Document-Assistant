from fastapi import FastAPI
from pydantic import BaseModel

from rag_database_ import create_db
from rag_qa_ import get_answer

app=FastAPI(title="Modular RAG API")

class QueryRequest(BaseModel):
    question:str

@app.post("/built-database")
async def build_database():
    print("Building the database...")
    chunk_count=create_db("AI+PPT.pdf ")
    return {"status": "Success", "message": f"Database updated with {chunk_count} chunks."}

# Endpoint 2: The actual Q&A chatbot
@app.post("/ask")
async def ask_question(request: QueryRequest):
    print(f"User asked: {request.question}")
    answer = get_answer(request.question)
    return {"answer": answer}
if __name__ == "__main__":
    print("Starting server internally to bypass Device Guard...")
    uvicorn.run("api:app", host="http://127.0.0.1:8000/docs", port=8000, reload=True)