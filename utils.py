"""
Utility functions for YouTube Assistant
"""
import re
from typing import Optional


def is_valid_youtube_url(url: str) -> bool:
    """
    Validate if a URL is a valid YouTube URL
    
    Args:
        url: URL string to validate
        
    Returns:
        True if valid YouTube URL, False otherwise
    """
    if not url:
        return False
    
    youtube_regex = (
        r'(https?://)?(www\.)?'
        r'(youtube|youtu|youtube-nocookie)\.(com|be)/'
        r'(watch\?v=|embed/|v/|.+\?v=)?([^&=%\?]{11})'
    )
    
    match = re.match(youtube_regex, url)
    return match is not None


def truncate_text(text: str, max_length: int = 150, suffix: str = "...") -> str:
    """
    Truncate text to a maximum length
    
    Args:
        text: Text to truncate
        max_length: Maximum length
        suffix: Suffix to add if truncated
        
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    return text[:max_length - len(suffix)].strip() + suffix


def clean_response(response: str) -> str:
    """
    Clean up LLM response text
    
    Args:
        response: Raw response text
        
    Returns:
        Cleaned response text
    """
    # Remove excessive newlines
    response = re.sub(r'\n{3,}', '\n\n', response)
    
    # Remove leading/trailing whitespace
    response = response.strip()
    
    return response
