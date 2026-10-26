# This code is a Python script that demonstrates how to load a text file, split its content into smaller chunks, and print those chunks. It uses the `TextLoader` class from the `langchain_community.document_loaders` module to load the text file and the `CharacterTextSplitter` class from the `langchain_text_splitters` module to split the text into chunks.
# 1. character -based spliting (text splitter)
from langchain_community.document_loaders import TextLoader
from langchain_text_splitters import CharacterTextSplitter

# splitter function is used to split the text into smaller chunks for processing 
splitter = CharacterTextSplitter(
    separator="",
    chunk_size=40, 
    chunk_overlap=4)

# load the text file using the TextLoader class from langchain_community.document_loaders
loader = TextLoader(r"D:\Generative_Ai\PART2\document.loaders\notes.txt")

documents = loader.load()

chunks = splitter.split_documents(documents)


print(len(chunks))
# print(documents)
# print(documents[0].page_content)
# print(documents[0].metadata)

for i in chunks:
    print(i.page_content)
    