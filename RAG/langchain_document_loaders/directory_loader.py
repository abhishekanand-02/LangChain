from langchain_community.document_loaders import DirectoryLoader, PyPDFLoader

loader = DirectoryLoader(
    path=r'C:\Users\abhishek.anand\Desktop\self\LangChain\RAG\langchain_document_loaders\books',
    glob='*.pdf',
    loader_cls=PyPDFLoader
)

# docs = loader.lazy_load()

# for document in docs:
#     print(document.metadata)

docs = loader.load()
print(len(docs))
