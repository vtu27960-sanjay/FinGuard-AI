from fastapi import APIRouter
from pydantic import BaseModel

from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

router = APIRouter()

# Load embeddings
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load FAISS vector database
db = FAISS.load_local(
    "../rag/vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

class ChatRequest(BaseModel):
    question: str


@router.post("/chat")
def chat(request: ChatRequest):

    docs = db.similarity_search(request.question, k=3)

    answer = "\n\n".join([doc.page_content for doc in docs])

    return {
        "question": request.question,
        "answer": answer
    }