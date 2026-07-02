from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from routes.fraud import router as fraud_router
from routes.history import router as history_router
from routes.chatbot import router as chatbot_router
app = FastAPI(
    title="FinGuard AI",
    description="AI Financial Fraud Detection & Banking Assistant",
    version="1.0.0"
)

# Enable CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register API Routes
app.include_router(fraud_router)
app.include_router(history_router)
app.include_router(chatbot_router)

# Home Route
@app.get("/")
def home():
    return {
        "message": "Welcome to FinGuard AI Backend",
        "status": "Running Successfully"
    }

# Health Check Route
@app.get("/health")
def health():
    return {
        "server": "OK",
        "api": "Working"
    }