from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS

# Load embedding model
embeddings = HuggingFaceEmbeddings(
    model_name="sentence-transformers/all-MiniLM-L6-v2"
)

# Load vector database
db = FAISS.load_local(
    "vectorstore",
    embeddings,
    allow_dangerous_deserialization=True
)

print("=================================")
print(" FinGuard AI Banking Chatbot")
print("=================================")

while True:

    question = input("\nAsk a Banking Question (type 'exit' to quit): ")

    if question.lower() == "exit":
        break

    docs = db.similarity_search(question, k=3)

    print("\n----- AI Answer -----\n")

    for i, doc in enumerate(docs, start=1):
        print(f"Result {i}:\n")
        print(doc.page_content)
        print("\n--------------------------")