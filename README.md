
# PDF to MCP AI Chatbot

A Python application that lets users upload PDF documents, retrieve relevant passages, and ask questions using a locally running AI model.

## Features

- Upload PDF documents through a Streamlit interface
- Extract PDF text using PyMuPDF
- Retrieve relevant passages using TF-IDF
- Expose document search through a Model Context Protocol (MCP) tool
- Generate answers using Ollama and the Llama 3.2 model

## Technology Stack

- Python
- Streamlit
- PyMuPDF
- scikit-learn
- Ollama
- Model Context Protocol (MCP)

## Project Files

- `app.py` — Streamlit interface, PDF extraction, MCP client, and AI answers
- `mcp_server.py` — MCP server and PDF search tool
- `test_mcp.py` — Basic MCP client-server integration test
- `requirements.txt` — Python package dependencies

## Prerequisites

- Python installed
- Ollama installed
- The `llama3.2:3b` model downloaded

## Setup

1. Clone or download this repository.
2. Create and activate a Python virtual environment.
3. Install dependencies:

   ```bash
   python -m pip install -r requirements.txt
   ```

4. Download the local AI model:

   ```bash
   ollama pull llama3.2:3b
   ```

5. Start the chatbot:

   ```bash
   python -m streamlit run app.py
   ```

6. Upload a PDF and ask a question.

## Test the MCP Server

Run:

```bash
python test_mcp.py
```

## Current Limitations

- Retrieval uses TF-IDF rather than semantic embeddings.
- Scanned PDFs may require OCR.
- Answers depend on the retrieved passages.
- The application has been tested with sample documents.

## Future Improvements

- Semantic search using embeddings
- PDF page citations
- Better handling of long documents
- Improved error handling and testing
