import streamlit as st
import langchain_helper as lch
import textwrap


st.title("Youtube Assistant")

with st.sidebar:
    with st.form(key='my-form'):
        youtube_url = st.sidebar.text_area(
            label="what is the youTube video url",
            max_chars=200
        )
        query = st.sidebar.text_area(
            label="Ask me about the video?",
            max_chars=200,
            key='query'
        )
        submit_button = st.form_submit_button(label="submit")
        
# if query and youtube_url:
print("DID THIS RUN ")
db = lch.create_vector_db_from_youtube(youtube_url)
response, docs = lch.get_response_from_query(db, query)
print(response, "RESPONSE" )
st.subheader("Answer")
st.text(textwrap.fill(response, width=85))
        
