"""
Question answering engine using LangChain and OpenAI
"""
from typing import Tuple, List
import streamlit as st
from langchain_openai import OpenAI
from langchain_core.prompts import PromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.documents import Document

from config import DEFAULT_K_RESULTS, LLM_MODEL, QA_TEMPLATE


@st.cache_resource
def get_llm():
    """Get OpenAI LLM instance (cached)"""
    return OpenAI(model=LLM_MODEL, temperature=0.7)


def get_response_from_query(
    db: FAISS, 
    query: str, 
    k: int = DEFAULT_K_RESULTS
) -> Tuple[str, List[Document]]:
    """
    Get answer to a query using the vector database
    
    Args:
        db: FAISS vector database
        query: User's question about the video
        k: Number of similar documents to retrieve
        
    Returns:
        Tuple of (answer string, list of relevant documents)
        
    Raises:
        Exception: If query processing fails
    """
    if not query or not query.strip():
        raise ValueError("Query cannot be empty")
    
    try:
        # Find similar documents
        docs = db.similarity_search(query, k=k)
        
        if not docs:
            return "I couldn't find relevant information in the video transcript.", []
        
        # Combine document content
        docs_page_content = " ".join([d.page_content for d in docs])
        
        # Create prompt
        prompt = PromptTemplate(
            input_variables=["question", "docs"],
            template=QA_TEMPLATE
        )
        
        # Get LLM and create chain
        llm = get_llm()
        chain = prompt | llm
        
        # Generate response
        response = chain.invoke({
            "question": query,
            "docs": docs_page_content
        })
        
        # Clean up response
        if isinstance(response, str):
            response = response.strip()
        else:
            response = str(response).strip()
            
        return response, docs
        
    except Exception as e:
        raise Exception(f"Error generating response: {str(e)}")


def format_sources(docs: List[Document], max_sources: int = 3) -> str:
    """
    Format source documents for display
    
    Args:
        docs: List of relevant documents
        max_sources: Maximum number of sources to show
        
    Returns:
        Formatted string of sources
    """
    if not docs:
        return ""
    
    sources = []
    for i, doc in enumerate(docs[:max_sources], 1):
        content_preview = doc.page_content[:150].replace("\n", " ")
        sources.append(f"**Source {i}:** {content_preview}...")
    
    return "\n\n".join(sources)
