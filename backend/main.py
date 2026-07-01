from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.routes.upload_routes import (
    router as upload_router
)

from app.routes.chat_routes import (
    router as chat_router
)

from app.routes.auth_routes import (
    router as auth_router
)

app = FastAPI(
    title="AI Multi-Tenant RAG Chatbot API",
    description=(
        "Multi User RAG Chatbot using "
        "FastAPI, FAISS, Cohere and MongoDB"
    ),
    version="2.0.0"
)

# =====================================
# CORS Configuration
# =====================================
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://localhost:5173",
        "http://127.0.0.1:5173",
        "http://localhost:5174",
        "http://127.0.0.1:5174",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# =====================================
# Authentication Routes
# =====================================
app.include_router(
    auth_router,
    prefix="/auth",
    tags=["Authentication"]
)

# =====================================
# Upload Routes
# =====================================
app.include_router(
    upload_router,
    tags=["Documents"]
)

# =====================================
# Chat Routes
# =====================================
app.include_router(
    chat_router,
    tags=["Chat"]
)

# =====================================
# Home Route
# =====================================
@app.get("/")
def home():
    return {
        "message": (
            "AI Multi Tenant RAG Chatbot "
            "Backend Running Successfully"
        ),
        "status": "active",
        "authentication": "enabled"
    }


# =====================================
# Health Check Route
# =====================================
@app.get("/health")
def health():
    return {
        "status": "healthy",
        "backend": "running",
        "vector_store": "ready",
        "mongodb": "connected",
        "authentication": "enabled"
    }