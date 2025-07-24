A privacy-first, multi-PDF AI search tool. Upload any PDFs, ask real questions, get answers and one-click links—entirely local. Powered by LangChain, Ollama, Streamlit, and Chroma vector search.

Features
Upload multiple PDFs (any subject, any length)

Ask any question in plain English

Get direct answers (using a local LLM, not the cloud)

Semantic chunk retrieval (using nomic-embed-text embeddings)

Clickable links open matched PDF/page in browser

Streamlit chat UI shows full conversation

Only links from the latest answer are shown (no clutter)

How it Works
PDF Upload

User uploads one or more PDFs via the Streamlit UI

PDFs are saved to static/uploads/

PDF Parsing & Chunking

Each PDF is read page-by-page with PyMuPDF (pymupdf)

Each page is split into overlapping text chunks (text_splitter)

Chunks are stored with doc name, page, and chunk index

Semantic Embedding & Index

Each chunk is embedded using local Ollama (nomic-embed-text)

Chunks + metadata are stored in a Chroma vectorstore

Vectorstore is used to build a semantic retriever

Chat Q&A

User submits a question in chat

Retriever finds the most semantically similar chunks across all PDFs

These chunks are combined and fed as context to a local LLM (Ollama/llama3.2)

The LLM generates a focused answer using only the returned context

UI Output

The chat interface shows the user’s question and AI answer (history is preserved)

Only the most recent search’s matching document links are shown below the latest answer
(links open the exact page in the PDF.js browser viewer)

How To Run Locally
Install dependencies

bash
Copy
Edit
pip install -r requirements.txt
Start Streamlit app

bash
Copy
Edit
streamlit run app.py
Start PDF.js static server (in another terminal)

bash
Copy
Edit
cd static
python -m http.server 8502
Go to http://localhost:8501 in your browser

Project File Structure
graphql
Copy
Edit
.
├── app.py                # Main Streamlit UI/app code
├── llm.py                # Ollama retriever and chatbot code
├── pdf_utils.py          # PDF chunking and reading logic
├── static/
│   └── uploads/          # Where uploaded PDFs are stored
│   └── pdf.js/           # PDF.js web viewer
├── requirements.txt
└── README.md
Key Functions (How It All Connects)
get_texts(uploaded_file, doc_name)
→ Extracts and chunks all text from each PDF page (using pymupdf), returns metadata for chunk, page, and doc

build_retriever(chunks)
→ Indexes all chunks with local Ollama embeddings, builds a Chroma vectorstore retriever

ollamaChatbot(question, context)
→ Takes user’s question and top-matching context, feeds to local LLM for answer

Chat logic (Streamlit)

Stores full conversation history in st.session_state.conversation

On each new question: appends a Q/A to the conversation, but only displays document links for the latest response

Tech Stack
Python 3.10+

Streamlit — frontend and chat UI

PyMuPDF (pymupdf) — PDF reading/chunking

LangChain — chaining and prompt templating

Ollama — local LLM and local embedding models

Chroma — vectorstore for semantic search

PDF.js — browser PDF viewer

Example Usage
Upload 3 math, 3 chem, 3 bio PDFs (or any other mix)

Ask:

“Show me all calculus questions”
or
“Find all acid-base reactions”

Instantly get:

The most relevant passages (from any PDF)

Page numbers & document names

One-click “Open PDF” links (loads correct page in browser)

Notes & Gotchas
No cloud, no external API calls. All AI, search, and file processing is 100% local.

PDF.js must be served locally at port 8502 for one-click links to work (see setup above).

Chunking & embedding size can be tuned in get_texts() and text_splitter() for best results.

Only current links shown: your chat Q/A history stays, but only the latest links render (no buildup).

Troubleshooting
PDF not displaying?
Make sure static/uploads/ and static/pdf.js/ exist and your static server is running.

LLM not answering?
Make sure Ollama is running with llama3.2 and nomic-embed-text models installed.

Credits
