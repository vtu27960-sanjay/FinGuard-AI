from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# PDF Path
pdf_path = r"C:\Users\Lenovo\Downloads\bank_policy.pdf"

# Load PDF
loader = PyPDFLoader(pdf_path)
documents = loader.load()

# Split into chunks
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=100
)

chunks = text_splitter.split_documents(documents)

print("Total Chunks:", len(chunks))

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Create FAISS vector database
vector_db = FAISS.from_documents(chunks, embeddings)

# Save database
vector_db.save_local("vectorstore")

print("\n✅ Embeddings Created Successfully!")
print("✅ Vector Database Saved in 'vectorstore' folder")