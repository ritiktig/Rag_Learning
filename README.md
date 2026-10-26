# RAG Learning

This repository is a hands-on learning project focused on building a Retrieval-Augmented Generation (RAG) system step by step. The goal is to understand how to:

- load documents from different sources
- split documents into chunks
- generate embeddings
- store them in a vector database
- retrieve relevant context for a user query
- use an LLM to answer based on the retrieved information

This project is designed as a collection of small experiments and examples before moving toward a bigger end-to-end RAG application.

## Project Overview

The repository contains small learning modules that demonstrate the core building blocks of a RAG pipeline:

- document loading
- text chunking
- embedding generation
- vector search using ChromaDB
- prompt-based answer generation with a language model

## Repository Structure

```text
Rag_Learning/
├── .gitignore
├── README.md
├── requirements.txt
├── main.py
├── create_database.py
├── document.loaders/
│   ├── notes.txt
│   ├── Containers.pdf
│   ├── python-module1-notes.pdf
│   ├── page.py
│   ├── pdf.py
│   ├── test.py
│   └── ...
├── vector_store/
│   └── db.py
├── chroma-db/
│   └── chroma.sqlite3
└── ...
```

### Folder Details

#### `document.loaders/`
This folder contains examples of loading different types of documents into the project, such as text and PDF files. These are used to learn how documents are extracted and prepared before they are embedded.

#### `vector_store/`
This folder contains code related to vector database handling and data storage logic.

#### `chroma-db/`
This folder stores the persistent ChromaDB database used for vector search and retrieval.

#### `create_database.py`
This script builds the vector store by:

1. loading documents
2. splitting them into chunks
3. creating embeddings
4. storing them in ChromaDB

#### `main.py`
This script loads the stored vector database and performs retrieval for a user query, then passes the relevant context to a Gemini model to generate the final answer.

## Tech Stack

- Python
- LangChain
- LangChain Community
- ChromaDB
- Google Generative AI / Gemini
- PyPDF
- Python-dotenv

## Setup

### 1. Clone the repository

```bash
git clone https://github.com/ritiktig/Rag_Learning.git
cd Rag_Learning
```

### 2. Create a virtual environment

```bash
python -m venv venv
source venv/bin/activate   # On Windows use: venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure environment variables

Create a `.env` file in the project root and add your Google API key:

```env
GOOGLE_API_KEY=your_api_key_here
```

## How the Project Works

This project follows a basic RAG pipeline:

1. Load source documents from files like PDFs or text files.
2. Split the text into smaller chunks for better retrieval quality.
3. Generate embeddings using a model such as Gemini embeddings.
4. Save embeddings into ChromaDB.
5. Query the vector database to find the most relevant chunks.
6. Send those chunks as context to a generative model.
7. Generate a final answer based on the retrieved content.

## Run the Project

### Create the vector database

```bash
python create_database.py
```

### Start the RAG app

```bash
python main.py
```

Then enter your question in the terminal. Type `0` to exit.

## Example Flow

```text
User Question -> Retrieve relevant chunks -> Combine context -> LLM answer
```

## Learning Goals

This project is meant to teach:

- how RAG systems are built
- how document loaders work
- how vector databases store embeddings
- how retrieval improves LLM answers
- how to build a project gradually from small examples to a full solution

## Notes

This repository is intentionally structured as a learning journey, where each folder and script demonstrates a concept before creating the larger RAG project. The idea is not only to build a working application but also to understand the logic behind the architecture.

## Future Improvements

Possible next steps for this project:

- add more document sources (CSV, JSON, website, APIs)
- add better chunking strategies
- compare multiple embedding models
- add a web UI using Streamlit or FastAPI
- build a more complete production-ready RAG application

## License

This project is for learning and experimentation.
