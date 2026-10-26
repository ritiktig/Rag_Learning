from dotenv import load_dotenv
from langchain_core.documents import Document
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.vectorstores import Chroma

load_dotenv()

docs = [
    Document(
        page_content="Python is widely used in Artificial Intelligence.",
        metadata={"source": "AI_book"}
    ),
    Document(
        page_content="Pandas is used for data analysis in Python.",
        metadata={"source": "DataScience_book"}
    ),
    Document(
        page_content="Neural networks are used in deep learning.",
        metadata={"source": "DL_book"}
    ),
]

embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma.from_documents(
    documents=docs,
    embedding=embedding_model,
    persist_directory="./chroma-db",
    collection_name="learning_docs"
)

print("Documents stored:", vectorstore._collection.count())
print("Database saved in ./chroma-db")


result = vectorstore.similarity_search("what is used for data analysis", k=2)

for r in result:
    print(r.page_content)
    print(r.metadata)
    
    
# retrival strategy default is similarity search, but you can also use other retrival strategies like keyword search, hybrid search, etc. You can also customize the retrival strategy
# by providing your own retrival function.
retriver = vectorstore.as_retriver()

docs = retriver.invoke("Explain deep learning")

for d in docs:
    print(d.page_content)