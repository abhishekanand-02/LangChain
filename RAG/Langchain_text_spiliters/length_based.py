from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('C:\\Users\\abhishek.anand\\Desktop\\self\\LangChain\\RAG\\langchain_document_loaders\\dl-curriculum.pdf')

docs = loader.load()

splitter  = CharacterTextSplitter(
    chunk_size=1000, 
    chunk_overlap=0,
     separator=''
     )
# result = splitter.split_text(docs)
result = splitter.split_documents(docs)

print(result[1].page_content)