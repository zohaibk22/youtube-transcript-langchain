"""
Configuration settings for YouTube Assistant
"""

# Text Splitting Configuration
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 100

# Query Configuration
DEFAULT_K_RESULTS = 4

# OpenAI Model Configuration
LLM_MODEL = "gpt-3.5-turbo-instruct"
EMBEDDING_MODEL = "text-embedding-ada-002"

# UI Configuration
MAX_URL_CHARS = 200
MAX_QUERY_CHARS = 500
TEXT_WRAP_WIDTH = 85

# Prompt Template
QA_TEMPLATE = """
You are a helpful assistant that can answer questions about YouTube videos 
based on the video's transcript.

Answer the following question: {question}
By searching the following video transcript: {docs}

Only use the factual information from the transcript to answer the question.

If you feel like you don't have enough information to answer the question, say "I don't know".

Your answers should be verbose and detailed.
"""
