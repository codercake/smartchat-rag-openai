from langchain.document_loaders import PyMuPDFLoader
from langchain.vectorstores import FAISS
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
import os


def get_qa_chain(pdf_path):
    loader = PyMuPDFLoader(pdf_path)
    documents = loader.load()
    embeddings = OpenAIEmbeddings()
    db = FAISS.from_documents(documents, embeddings)
    retriever = db.as_retriever()
    qa = RetrievalQA.from_chain_type(llm=OpenAI(), retriever=retriever)
    return qa

    