"""
YouTube Assistant - Streamlit Application
Ask questions about YouTube videos using their transcripts
"""
import streamlit as st
from transcript_processor import create_vector_db_from_youtube
from qa_engine import get_response_from_query, format_sources
from config import MAX_URL_CHARS, MAX_QUERY_CHARS, TEXT_WRAP_WIDTH
import textwrap


# Page configuration
st.set_page_config(
    page_title="YouTube Assistant",
    page_icon="🎥",
    layout="wide"
)

st.title("🎥 YouTube Assistant")
st.markdown("*Ask questions about any YouTube video with transcripts*")

# Custom CSS
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        font-size: 14px;
    }
    .answer-box {
        background-color: #f0f2f6;
        padding: 1.5rem;
        border-radius: 0.5rem;
        border-left: 5px solid #4CAF50;
        color: #1f1f1f;
        margin: 1rem 0;
    }
    </style>
    """, unsafe_allow_html=True)

# Sidebar for inputs
with st.sidebar:
    st.header("📋 Input")
    
    with st.form(key='video-query-form'):
        youtube_url = st.text_area(
            label="🔗 YouTube Video URL",
            max_chars=MAX_URL_CHARS,
            placeholder="https://www.youtube.com/watch?v=...",
            help="Paste the full YouTube video URL"
        )
        
        query = st.text_area(
            label="❓ Your Question",
            max_chars=MAX_QUERY_CHARS,
            key='query',
            placeholder="What is the main topic discussed?",
            help="Ask anything about the video content"
        )
        
        show_sources = st.checkbox("Show source excerpts", value=False)
        
        submit_button = st.form_submit_button(label="🚀 Submit")
    
    # Info section
    st.markdown("---")
    st.markdown("### ℹ️ About")
    st.info(
        "This app uses AI to answer questions about YouTube videos "
        "by analyzing their transcripts. Powered by OpenAI and LangChain."
    )

# Main content area
if submit_button:
    if not youtube_url or not query:
        st.warning("⚠️ Please provide both a YouTube URL and a question.")
    else:
        try:
            # Process video and generate answer
            with st.spinner("🔄 Loading video transcript..."):
                db = create_vector_db_from_youtube(youtube_url)
            
            with st.spinner("🤔 Generating answer..."):
                response, docs = get_response_from_query(db, query)
            
            # Display results
            st.success("✅ Analysis complete!")
            
            st.subheader("💡 Answer")
            st.markdown(
                f'<div class="answer-box">{response}</div>',
                unsafe_allow_html=True
            )
            
            # Show sources if requested
            if show_sources and docs:
                with st.expander("📚 View Source Excerpts"):
                    st.markdown(format_sources(docs))
                    
        except ValueError as e:
            st.error(f"❌ Invalid input: {str(e)}")
        except Exception as e:
            st.error(f"❌ An error occurred: {str(e)}")
            st.info("💡 Please check that the video has transcripts available and try again.")
else:
    # Welcome message
    st.markdown("""
    ## 👋 Welcome!
    
    To get started:
    1. Paste a YouTube video URL in the sidebar
    2. Ask a question about the video
    3. Click Submit to get your answer
    
    ### Example questions:
    - "What are the main points discussed in this video?"
    - "Can you summarize the key takeaways?"
    - "What examples were provided?"
    - "What is the speaker's opinion on [topic]?"
    """)
