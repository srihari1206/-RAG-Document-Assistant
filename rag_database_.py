import os
import shutil
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import Chroma

def create_db(pdf_filename=r"C:\Users\Srihari\Downloads\AI+PPT.pdf"):
    db_directory = "./chroma_db"
    
    # Clear old DB
    if os.path.exists(db_directory):
        shutil.rmtree(db_directory)
        
    # Load and Chunk
    loader = PyPDFLoader(pdf_filename)
    documents = loader.load()
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
    chunks = text_splitter.split_documents(documents)
    
    # Embed and Save
    embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")
    Chroma.from_documents(chunks, embedding_model, persist_directory=db_directory)
    
    return len(chunks) # Return how many chunks we saved