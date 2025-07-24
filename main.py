from pdf_utils import get_texts
from llm import build_retriever
from llm import ollamaChatbot
import streamlit as st
import os
from io import BytesIO
import urllib
import streamlit as st

 

# chunks = get_texts('sample_text/somatosensory.pdf')

# question = "What is the primary function of the somatosensory system?"

# retreiver = build_retriever(chunks)

# results = retreiver.invoke(question)
# print(results)

# answer = ollamaChatbot(question, results)
# print(answer)

os.makedirs('static/uploads', exist_ok=True)


height = 600
title = "HiNC Local AI"
icon = ":robot:"
def generate_message(user_input, uploaded_files, retreiver):
    context_chunks = retreiver.invoke(user_input)
    # Extract just the text parts for the chatbot
    context_text = "\n\n".join(chunk.page_content for chunk in context_chunks)


    answers = ollamaChatbot(user_input, context_text)
    answer = answers.content

    st.session_state.conversation.append({
        "user": user_input,
        "assistant": answer,
        "context": context_chunks
    })


    for entry in st.session_state.conversation:
        messages.chat_message("user").write(entry['user'])
        messages.chat_message("assistant").write(entry['assistant'])
    if st.session_state.conversation:
        latest_entry = st.session_state.conversation[-1]
        for c in latest_entry["context"]:
            doc = c.metadata.get('doc_name', None)
            page = c.metadata.get('page', 1)
            safe_doc = urllib.parse.quote(doc)
            pdfjs_url = f"http://localhost:8502/pdf.js/web/viewer.html?file=/uploads/{safe_doc}#page={page}"
            st.write(f"**{doc}** (Page {page})  [Open PDF]({pdfjs_url})")
                

               
            




if 'conversation' not in st.session_state:
    st.session_state.conversation = []

if 'clicked' not in st.session_state:
    st.session_state.clicked = False


st.set_page_config(page_title=title, page_icon=icon)


def toggle_clicked():
    if st.session_state.clicked is True:
        st.session_state.clicked = False
    else:
        st.session_state.clicked = True

col1, col2 = st.columns([4, 1], gap="large", vertical_alignment="bottom")
with col1:
    st.header(title)

if 'uploaded_files' not in st.session_state:
    st.session_state.uploaded_files = []
if 'retriever' not in st.session_state:
    st.session_state.retriever = None

uploaded_files = st.file_uploader(
    "Upload PDF files", type=["pdf"], accept_multiple_files=True
)


if uploaded_files and uploaded_files != st.session_state.uploaded_files: 
    st.session_state.uploaded_files = uploaded_files
    all_chunks = []
    for uploaded_file in uploaded_files:
        
        file_bytes = uploaded_file.read()
    
    # Save to disk
        with open(f'static/uploads/{uploaded_file.name}', 'wb') as f:
            f.write(file_bytes)
        
        all_chunks.extend(get_texts(BytesIO(file_bytes), uploaded_file.name))
        st.write(f"Uploaded file: {uploaded_file.name}")
    
    st.session_state.retriever = build_retriever(all_chunks)


messages = st.container(border=True, height=height)



if prompt := st.chat_input("Enter your question...", key="prompt"):
    if 'retriever' in st.session_state and 'uploaded_files' in st.session_state:
        generate_message(prompt, st.session_state.uploaded_files, st.session_state.retriever)
    else:
        st.error("Please upload PDF files first.")





#cd static
#python -m http.server 8502
