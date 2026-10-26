# from dotenv import load_dotenv
# import langchain_community
# from langchain_google_genai import ChatGoogleGenerativeAI
# # from langchain_community.document_loaders import TextLoader
# from langchain_core.prompts import ChatPromptTemplate
# from langchain_community.document_loaders import PyPDFLoader
# # from langchain_text_splitters import RecursiveCharacterTextSplitter
# load_dotenv()

# data = PyPDFLoader(r"D:\Generative_Ai\PART2\document.loaders\Containers.pdf")
# # # data = TextLoader(r"D:\Generative_Ai\PART2\document.loaders\notes.txt")
# # documents = data.load()

# # splitter = RecursiveCharacterTextSplitter(
# #     chunk_size=1000,
# #     chunk_overlap=150,
# # )   


# # chunks = splitter.split_documents(documents)




# template = ChatPromptTemplate.from_messages(
#     [
#         ('system',"you are the ai that summarize the text"),
        
#         ('human',"{data}")
        
        
#         ]

# )



# llm = ChatGoogleGenerativeAI(
#     model="gemini-3.8-flash"
# )


# prompt = template.format_messages(data = documents[0].page_content )

# result = llm.invoke(prompt)

# print(result.content)


# Exactly this is the project that I am working on, I want to create a vector store database using the above code and then use the database to retrieve the data and then use the retrieved data to summarize it using the above code.
# we have use create_database.py to create the database and then we can use the above code to retrieve the data and then summarize it.
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.prompts import ChatPromptTemplate


load_dotenv()


embedding_model = GoogleGenerativeAIEmbeddings(
    model="gemini-embedding-001"
)

vectorstore = Chroma(
    persist_directory="chroma-db",
    collection_name="learning_docs",
    embedding_function=embedding_model,
)

retriver = vectorstore.as_retriever(
    search_type = "mmr",
    search_kwargs = {"k": 4, "fetch_k": 4, "lambda_mult": 0.5}
)

# google model for summarization

llm = ChatGoogleGenerativeAI(
    model="gemini-3.8-flash"
)

# prompt template

template = ChatPromptTemplate.from_messages(
    [
        ('system',"you are helpful ai that summarize the text use only the data provided to you and do not make up any information, if you don't have enough information to answer the question then say I don't know"),
        
        ('human',"""Context:
         {context}
         
         Question:
         {question}
         
         """)
        
        
        ]

)

print("Rag system created")
print("press 0 to exit")

while True:
    query = input("you : ")
    if(query == '0'):
        break
    
    docs = retriver.invoke(query)
    
    context = "\n\n".join(
        [doc.page_content for doc in docs]
    )
    
    final_prompt = template.invoke({
        "context" :context,
        "question":query
    })
    
    response = llm.invoke(final_prompt)
    print(f"\n AI :  {response.content}")