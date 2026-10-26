from langchain_community.document_loaders import PyPDFLoader
# spliting text based on tokens (token splitter)
# from langchain_text_splitters import TokenTextSplitter


from langchain_text_splitters import RecursiveCharacterTextSplitter

data = PyPDFLoader(r"D:\Generative_Ai\PART2\document.loaders\Containers.pdf")

document = data.load()

# splitter = TokenTextSplitter(chunk_size = 100,
#                              chunk_overlap = 10,
#                              )


splitter = RecursiveCharacterTextSplitter(
    chunk_size =10,
    chunk_overlap = 2,
)


chunks = splitter.split_documents(document)
print(chunks[0].page_content)




print(len(chunks))