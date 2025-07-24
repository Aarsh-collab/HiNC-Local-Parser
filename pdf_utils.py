import pymupdf
def text_splitter(text, chunk_size=1000, chunk_overlap=200):
    """
    Split text into overlapping chunks of a given size and overlap.
    """
    if len(text) <= chunk_size:
        return [text]

    chunks = []
    start = 0
    while start < len(text):
        end = start + chunk_size
        chunks.append(text[start:end])
        if end >= len(text):
            break
        start += chunk_size - chunk_overlap
    return chunks


def get_texts(uploaded_file, doc_name, chunk_size=1000, chunk_overlap=200):
    """
    Extract and chunk text from all pages of a PDF file.
    :param pdf_path: Path to the PDF file.
    :return: List of dicts with doc_name, page, chunk, and chunk text.
    """
    
    doc = pymupdf.open(stream=uploaded_file.read(), filetype="pdf")
    results = []
    for page_num in range(len(doc)):
        page = doc[page_num]
        text = page.get_text()
        # Chunk each page's text
        chunks = text_splitter(text, chunk_size, chunk_overlap)
        for idx, chunk in enumerate(chunks):
            results.append({
                "doc_name": doc_name,
                "page": page_num + 1,
                "chunk": idx,
                "text": chunk
            })
    doc.close()
    return results





