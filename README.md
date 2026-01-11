# YouTube Assistant 🎥

A Streamlit-based application that allows you to ask questions about YouTube videos using their transcripts. This tool leverages LangChain, OpenAI, and FAISS to provide intelligent answers based on video content.

## Features

- 📺 Extract transcripts from YouTube videos
- 🤖 Ask natural language questions about video content
- 🔍 Uses vector similarity search for relevant context retrieval
- 💬 Powered by OpenAI's language models
- 🎨 User-friendly Streamlit interface

## How It Works

1. **Transcript Extraction**: The application fetches the transcript from a YouTube video URL
2. **Text Chunking**: The transcript is split into manageable chunks for processing
3. **Vector Embeddings**: Each chunk is converted into vector embeddings using OpenAI
4. **FAISS Vector Store**: Embeddings are stored in a FAISS database for efficient similarity search
5. **Question Answering**: When you ask a question, the app finds relevant transcript sections and generates an answer using GPT-3.5

## Installation

1. Clone this repository:
```bash
git clone <your-repo-url>
cd youtube_transcript
```

2. Install required dependencies:
```bash
pip install -r requirements.txt
```

3. Create a `.env` file in the project root and add your OpenAI API key:
```
OPENAI_API_KEY=your_api_key_here
```

## Usage

1. Run the Streamlit application:
```bash
streamlit run main.py
```

2. In the sidebar:
   - Enter a YouTube video URL
   - Type your question about the video
   - Click "Submit"

3. The application will process the video transcript and provide a detailed answer based on the content.

## Project Structure

```
youtube_transcript/
├── main.py                    # Streamlit application interface
├── transcript_processor.py    # YouTube transcript extraction & vector DB
├── qa_engine.py              # Question answering logic
├── config.py                 # Configuration constants
├── utils.py                  # Utility functions
├── requirements.txt          # Python dependencies
└── README.md                 # Project documentation
```

## Key Features & Optimizations

- **🚀 Caching**: Vector databases and models are cached to improve performance
- **📦 Modular Design**: Separated concerns into distinct modules
- **⚡ Efficient Processing**: Optimized text chunking and retrieval
- **🛡️ Error Handling**: Comprehensive error handling and user feedback
- **🎨 Enhanced UI**: Improved styling and user experience
- **📊 Source Display**: Option to view source excerpts from transcript

## Dependencies

- **streamlit**: Web application framework
- **langchain**: Framework for LLM applications
- **langchain-openai**: OpenAI integration for LangChain
- **langchain-community**: Community integrations for LangChain
- **openai**: OpenAI API client
- **youtube-transcript-api**: YouTube transcript extraction
- **faiss-cpu**: Vector similarity search
- **python-dotenv**: Environment variable management

## Requirements

- Python 3.8+
- OpenAI API key
- Internet connection for API calls and video transcript fetching

## Example Questions

- "What are the main topics discussed in this video?"
- "Can you summarize the key points?"
- "What did the speaker say about [specific topic]?"
- "What examples were provided in the video?"

## Limitations

- Only works with videos that have transcripts available
- Answers are limited to information present in the transcript
- Requires an active OpenAI API key (usage may incur costs)

## Future Improvements

- [ ] Support for multiple languages
- [ ] Add caching for previously processed videos
- [ ] Implement conversation history
- [ ] Add support for video timestamps in answers
- [ ] Include cost estimation for API usage

## License

This project is open source and available under the MIT License.

## Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the issues page.

---

Built with ❤️ using LangChain, OpenAI, and Streamlit
