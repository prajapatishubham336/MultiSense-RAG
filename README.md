# MultiSense-RAG
MultiSense-RAG is a multimodal RAG assistant that processes PDFs, images, scanned documents and text files to generate context-aware answers using OCR, vector search and Groq LLM.

# 🧠 MultiSense-RAG

### Multimodal Retrieval-Augmented Generation Knowledge Assistant

MultiSense-RAG is an intelligent document question-answering application built using **Generative AI, Retrieval-Augmented Generation (RAG), OCR, vector embeddings and Groq LLM**.

The application allows users to upload different types of documents, extract useful information from them and ask questions in natural language. The system retrieves relevant content from the uploaded files and generates grounded answers with source references.

---

## 🚀 Features

- Upload PDF documents
- Process scanned PDFs using OCR
- Extract text from images
- Support DOCX files
- Support TXT and Markdown files
- Convert extracted content into text chunks
- Generate semantic embeddings
- Store embeddings in ChromaDB
- Retrieve relevant document content
- Generate answers using Groq LLM
- Display source documents used for answering
- Clear the knowledge base
- Interactive Streamlit user interface
- Persistent local vector database

---

## 🏗️ Project Architecture

```text
User Uploads Documents
          │
          ▼
Document Processing
          │
          ├── PDF Text Extraction
          ├── Scanned PDF OCR
          ├── Image OCR
          ├── DOCX Extraction
          └── TXT/Markdown Reading
          │
          ▼
Text Chunking
          │
          ▼
Sentence Transformer Embeddings
          │
          ▼
ChromaDB Vector Database
          │
          ▼
User Question
          │
          ▼
Semantic Similarity Search
          │
          ▼
Relevant Context Retrieval
          │
          ▼
Groq LLM
          │
          ▼
Context-Aware Answer + Sources
🛠️ Technology Stack

Technology

	
Purpose


Python

	
Core programming language


Streamlit

	
Web interface


Groq API


Large Language Model


LangChain-style RAG workflow

	
Retrieval-based generation concept


ChromaDB

	
Vector database


Sentence Transformers
	

Text embeddings


PyMuPDF

	
PDF text extraction


Tesseract OCR

	
Image and scanned PDF text extraction


python-docx

	
DOCX file processing


Pillow
	

Image processing


python-dotenv
	

Environment variable management

📂 Project Structure
MultiSense-RAG/
│
├── app.py
├── rag_pipeline.py
├── document_processor.py
├── requirements.txt
├── .env.example
├── .gitignore
├── README.md
│
└── storage/
    ├── .gitkeep
    └── chroma/
File Description

app.py Streamlit application and user interface.

document_processor.py Extracts text from PDFs, images, DOCX, TXT and Markdown files.

rag_pipeline.py Handles text chunking, embeddings, vector search and Groq-based answer generation.

requirements.txt Contains required Python dependencies.

.env.example Template for storing the Groq API key.

storage/chroma/ Stores the local ChromaDB vector database.

⚙️ Installation
1. Clone the Repository
git clone https://github.com/prajapatishubham336/MultiSense-RAG.git
cd MultiSense-RAG


2. Create a Virtual Environment

For Windows:

python -m venv venv
venv\Scripts\activate

For macOS/Linux:

python3 -m venv venv
source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
4. Configure Groq API Key

Create a file named .env in the project root directory.

Add the following:

GROQ_API_KEY=your_groq_api_key_here

You can obtain your API key from:

https://console.groq.com/ 

Never upload your real API key to GitHub.

🖼️ Install Tesseract OCR

Tesseract OCR is required for:

Image text extraction

Scanned PDF processing

Install Tesseract OCR according to your operating system.

After installation, ensure that the Tesseract executable is available in your system PATH.

▶️ Run the Application

Start the Streamlit application using:

streamlit run app.py

The application will open in your browser.

Usually, it runs at:

http://localhost:8501
📖 How to Use

Open the MultiSense-RAG application.

Upload one or more supported documents.

Click Process Files.

Wait until the documents are indexed.

Enter a question related to the uploaded content.

Click Ask AI.

Read the generated answer and source references.

💡 Example Questions
Summarize this document.

What are the key points mentioned in the uploaded PDF?

Compare the information from two uploaded reports.

Explain the important findings from this document.

What challenges are mentioned in the report?

Extract the main conclusions from the uploaded research paper.
📄 Supported File Formats

File Type

	
Processing Method


PDF

	
PyMuPDF


Scanned PDF

	
Tesseract OCR


PNG

	
OCR


JPG/JPEG

	
OCR


DOCX

	
python-docx


TXT

	
UTF-8 text extraction


Markdown

	
UTF-8 text extraction

🔐 Security Notes

Store API keys only in the .env file.

Never commit .env to GitHub.

Do not expose private documents publicly.

Review generated answers before using them for important decisions.

The system answers based on the content available in the uploaded knowledge base.

⚠️ Limitations

OCR accuracy depends on image quality.

Complex tables and charts may not be extracted perfectly.

The current version primarily converts visual content into text using OCR.

Answers depend on the quality and relevance of retrieved document chunks.

Internet access is required for Groq API requests.

The first embedding-model download may take some time.

🔮 Future Enhancements

Native image understanding using vision-language models

Better table and chart extraction

Multimodal embeddings

Conversation memory

Document comparison dashboard

User authentication

Cloud vector database integration

Multi-user document workspaces

Answer confidence scoring

Advanced citation highlighting

Voice-based question answering

Deployment using Docker and cloud services

🎯 Use Cases

Research paper analysis

Educational document assistant

Company knowledge base

Business report analysis

Legal document exploration

Medical research assistance

Personal document search

Academic study assistant

👨‍💻 Author

**Developed by Shubham Prajapti**

⭐ Project Highlights

This project demonstrates practical implementation of:

Generative AI

Retrieval-Augmented Generation

Semantic Search

Vector Databases

OCR

Document Intelligence

Embeddings

Prompt Engineering

LLM Application Development

Streamlit Deployment

If you find this project useful, consider giving it a ⭐ on GitHub.
