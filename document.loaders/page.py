from langchain_community.document_loaders import WebBaseLoader


url = "https://reference.langchain.com/?lang=python"

data = WebBaseLoader(url)

document = data.load()
print(document[0].page_content)
print(len(document))