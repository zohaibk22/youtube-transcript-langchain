"""
YouTube transcript processing and vector database creation
"""
from typing import Optional
import streamlit as st
from langchain_community.document_loaders import YoutubeLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

from config import CHUNK_SIZE, CHUNK_OVERLAP

load_dotenv()


@st.cache_resource
def get_embeddings():
    """Get OpenAI embeddings model (cached)"""
    return OpenAIEmbeddings()


@st.cache_resource(show_spinner=False)
def create_vector_db_from_youtube(video_url: str) -> FAISS:
    """
    Create a FAISS vector database from YouTube video transcript
    
    Args:
        video_url: YouTube video URL
        
    Returns:
        FAISS vector database containing document embeddings
        
    Raises:
        ValueError: If video URL is invalid or transcript unavailable
        Exception: For other processing errors
    """
    if not video_url or not video_url.strip():
        raise ValueError("Video URL cannot be empty")
    
    try:
        # Load transcript from YouTube
        loader = YoutubeLoader.from_youtube_url(video_url)
        transcript = loader.load()
        
        if not transcript:
            raise ValueError("No transcript found for this video")
        
        # Split transcript into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=CHUNK_SIZE,
            chunk_overlap=CHUNK_OVERLAP
        )
        docs = text_splitter.split_documents(transcript)
        
        # Create vector database
        embeddings = get_embeddings()
        db = FAISS.from_documents(docs, embeddings)
        
        return db
        
    except ValueError as e:
        raise e
    except Exception as e:
        raise Exception(f"Error processing video: {str(e)}")


def extract_video_id(url: str) -> Optional[str]:
    """
    Extract video ID from YouTube URL for caching purposes
    
    Args:
        url: YouTube video URL
        
    Returns:
        Video ID if found, None otherwise
    """
    try:
        from urllib.parse import urlparse, parse_qs
        
        parsed_url = urlparse(url)
        
        if parsed_url.hostname in ['www.youtube.com', 'youtube.com']:
            return parse_qs(parsed_url.query).get('v', [None])[0]
        elif parsed_url.hostname == 'youtu.be':
            return parsed_url.path[1:]
            
    except Exception:
        pass
    
    return None
