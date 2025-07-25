# 🤖 HiNC Local AI PDF Q&A System

> **Semantic, multi-PDF search powered by local AI.**  
> Upload any PDF. Ask real questions. Get instant answers & exact PDF links.  
> **Runs fully local. No cloud.**

---

## 🚩 **What Is This?**

- Upload **any number of PDFs** (textbooks, notes, whatever)
- **Ask in natural language:**  
  _“Show me all calculus questions”_  
  _“Find acid-base reactions”_
- **AI searches across every doc:**  
  - Finds matching passages by meaning, not just keywords  
  - Returns: document name, page number, direct link to the right spot in the PDF
- **Streamlit chat UI:**  
  - See your Q/A history  
  - Only links from your latest search appear (no clutter)

---

## ⚡️ **How It Works**

1. **Upload PDFs**  
   PDFs go in `static/uploads/`
2. **PDFs are chunked & embedded**  
   - Uses `pymupdf` for text/page extraction  
   - Text split into overlapping chunks  
   - Each chunk embedded via **Ollama (`nomic-embed-text`)**
3. **Semantic Indexing**  
   - All chunks stored in a **Chroma** vector DB
4. **Ask Anything**  
   - Retriever returns most relevant chunks  
   - Local LLM (**Ollama** `llama3.2`) answers, using only those chunks as context
5. **Results**  
   - See answer + matching PDF passages, page numbers, and one-click links  
   - Click a link to open the PDF **right at the answer** (served by PDF.js)

---

## 🏗️ **File Structure**
```
├── app.py # Main Streamlit app code
├── llm.py # Local LLM, retriever, embedding logic
├── pdf_utils.py # PDF chunking/extraction
├── static/
│ └── uploads/ # Where PDFs get stored
│ └── pdf.js/ # PDF.js viewer (for in-browser links)
├── requirements.txt
└── README.md
```
---

## 📁 Static Folder Setup: PDF.js

This project requires the full [PDF.js](https://github.com/mozilla/pdf.js/) distribution in `static/pdf.js/` for in-browser PDF viewing.

### 🟢 How to Set Up PDF.js

1. **Download PDF.js**  
   - Go to [https://github.com/mozilla/pdf.js/releases](https://github.com/mozilla/pdf.js/releases)
   - Download the latest release ZIP file (example: `pdfjs-<version>-dist.zip`)

2. **Extract the entire ZIP.**

3. **Copy the entire extracted contents into your `static/pdf.js/` directory.**  
   - You should have all subfolders like `web/`, `build/`, `cmaps/`, etc., inside `static/pdf.js/`
   - **Do NOT just copy the `web` folder—copy everything from the distribution ZIP.**

4. **Check your structure:**  

```
static/
├── pdf.js/
│ ├── web/
│ │ └── viewer.html
│ ├── build/
│ ├── cmaps/
│ └── ...other PDF.js folders/files
└── uploads/
```

---

## 🚀 **Getting Started**

**1. Install dependencies**
pip install -r requirements.txt

**2. Start the Streamlit app**
streamlit run app.py

**3. Serve PDF.js for links (in a separate terminal):**
cd static
python -m http.server 8502

**4. Open in your browser:**
Go to http://localhost:8501

---

## 🧠 **Core Components**

- **PDF Parsing:** `pymupdf`
- **Semantic Embeddings:** Ollama (`nomic-embed-text`)
- **Vector Store:** Chroma
- **LLM Q&A:** Ollama (`llama3.2`)
- **Frontend:** Streamlit + PDF.js

---

## 💬 **How to Use**

1. **Upload multiple PDFs**  
   (Math, Chem, Bio, notes, tests—anything with text)

2. **Ask:**  
   - _Show me all calculus questions_  
   - _Find all acid-base reactions_

3. **Get:**  
   - **AI-generated answer**
   - **Snippets from every matching PDF**, with:
     - 📄 **Document name**
     - 📑 **Page number**
     - 🔗 **One-click “Open PDF” link** (opens exact page in PDF.js)

---

## 🏆 **Why This Rocks**

- **Semantic search (not keywords)**
- **Handles any doc set** (no template, no regex)
- **Super simple UI**—drag, drop, chat
- **Full privacy:** everything is on your machine
- **No cloud, no API keys, no vendor lock-in**

---

## ⚠️ **Notes & Gotchas**

- Make sure **PDF.js is running on port 8502** for PDF links to work.
- Requires **Ollama running with `llama3.2` and `nomic-embed-text` models.**
- **Only the latest result’s links are shown** (old chat stays, but no link clutter).
- Chunk size/overlap can be adjusted in `get_texts()` for performance/tuning.

---

## 📋 **Troubleshooting**

- **PDF won’t open?**  
  Check you’re serving `static/` at port 8502 and that PDF.js is in `static/pdf.js/`.

- **No answer from AI?**  
  Make sure Ollama is running, and the needed models are pulled.

- **Broken links or UI glitches?**  
  Check file paths, server ports, and browser console for details.

---

## 👨‍💻 **Credits & Contact**

- **Lead Dev:** Aarsh nandra
- **Contact:** aarsh.singh2020@gmail.com
- **Powered by:** LangChain, Streamlit, Ollama, PyMuPDF, Chroma

---

