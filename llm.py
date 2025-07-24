from pdf_utils import get_texts
from langchain_community.vectorstores import Chroma
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain.prompts import ChatPromptTemplate

def build_retriever(chunks):
    """
    Builds a vector store retriever from chunked texts and metadata using local Ollama embeddings
    """
    vectostore = Chroma.from_texts(
        texts=[chunk["text"] for chunk in chunks],
        metadatas=[{"doc_name": chunk["doc_name"], "page": chunk["page"], "chunk": chunk["chunk"]} for chunk in chunks],
        collection_name = 'rag_chroma',
        embedding= OllamaEmbeddings(model= 'nomic-embed-text')
    )
    retriever = vectostore.as_retriever()
    return retriever

def ollamaChatbot(question, context):
    model = ChatOllama(model = 'llama3.2')
    template = """
    Use only the following context to answer the question as accurately as possible.
    Context: {context} 
    question: {question}
    """
    # Create a prompt template
    prompt = ChatPromptTemplate.from_template(template)
    chain = prompt | model
    
    # Invoke the chain with context and question
    response = chain.invoke({"context": context, "question": question})
    return response 
