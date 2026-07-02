from langchain_community.document_loaders import PyPDFLoader

# Path to the PDF
pdf_path = r"C:\Users\Lenovo\Downloads\bank_policy.pdf"

# Load the PDF
loader = PyPDFLoader(pdf_path)

documents = loader.load()

print("===================================")
print("PDF Loaded Successfully!")
print("===================================")

print(f"Total Pages: {len(documents)}")

print("\nFirst Page Content:\n")

print(documents[0].page_content)