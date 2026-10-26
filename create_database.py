#load pdf
#split into chunck
# create the embedding
# store into vectorestore
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma


load_dotenv()


data = PyPDFLoader(r"D:\Generative_Ai\PART2\document.loaders\python-module1-notes.pdf")

documents = data.load()


splitter = RecursiveCharacterTextSplitter(
    chunk_size=1000,
    chunk_overlap=150,
)   


chunks = splitter.split_documents(documents)

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)


vectorstore = Chroma.from_documents(
    documents=chunks,
    embedding=embedding_model,
    persist_directory="./chroma-db",
    collection_name="learning_docs"
)


print("Documents stored in ChromaDB:", vectorstore._collection.count())

# 5. Verify an embedding was created
if chunks:
    sample_text = chunks[0].page_content
    sample_embedding = embedding_model.embed_query(sample_text)

    print("Embedding created successfully!")
    print("Embedding dimensions:", len(sample_embedding))
    print("First 10 values:", sample_embedding[:10])

print("Database creation completed!")