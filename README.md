# 🤖 AI Multi-Tenant RAG Chatbot

<div align="center">

### 🚀 Production-Style Retrieval Augmented Generation Platform

🔒 Secure • 📄 Multi-Document • 🧠 Context Aware • 👥 Multi User • ⚡ Fast Retrieval

![Python](https://img.shields.io/badge/Python-3.11+-blue?style=for-the-badge&logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-green?style=for-the-badge&logo=fastapi)
![React](https://img.shields.io/badge/React-Frontend-blue?style=for-the-badge&logo=react)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green?style=for-the-badge&logo=mongodb)
![FAISS](https://img.shields.io/badge/FAISS-VectorDB-orange?style=for-the-badge)
![JWT](https://img.shields.io/badge/JWT-Authentication-purple?style=for-the-badge)

</div>

---

# 🌟 Project Overview

Imagine having your own private ChatGPT that understands **your documents**, remembers conversations, and securely isolates data for every user.

This project is a **production-inspired Multi-Tenant RAG System** built using modern AI engineering principles.

Users can:

✅ Upload PDF documents  
✅ Chat naturally with their documents  
✅ Retrieve context-aware answers  
✅ Maintain conversation memory  
✅ Keep documents isolated per user  
✅ Perform semantic search using vector embeddings  

---

# 🎯 Why This Project Matters

Traditional chatbots answer from generic knowledge.

This system uses **Retrieval Augmented Generation (RAG)**:

```text
User Question
      ↓
Query Expansion
      ↓
Vector Retrieval (FAISS)
      ↓
BM25 Search
      ↓
Reranking
      ↓
LLM Response Generation
      ↓
Final Context Aware Answer
```

This dramatically improves:

- 🎯 Accuracy
- 📚 Context Awareness
- 🚫 Hallucination Reduction
- ⚡ Retrieval Speed

---

# 🏗 Architecture

```text
┌─────────────┐
│ React Frontend │
└──────┬──────┘
       │
       ▼
┌─────────────┐
│ FastAPI API │
└──────┬──────┘
       │
       ▼
┌──────────────────┐
│ Authentication   │
│ JWT Middleware   │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ PDF Processing   │
│ Chunking Engine  │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Embeddings Model │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ FAISS Vector DB  │
└──────┬───────────┘
       │
       ▼
┌──────────────────┐
│ Response Engine  │
└──────────────────┘
```

---

# ✨ Key Features

## 🔐 Authentication System
- JWT Authentication
- Secure Login/Register
- Protected Routes
- User Isolation

## 📄 Intelligent Document Processing
- PDF Upload Support
- Automatic Text Extraction
- Smart Chunking Strategy
- Metadata Preservation

## 🧠 Advanced Retrieval Pipeline
- Semantic Vector Search
- BM25 Hybrid Retrieval
- Query Expansion
- Document Reranking

## 👥 Multi-Tenant Design
- Separate vector databases per user
- Secure document isolation
- Scalable architecture

## 💬 Conversational AI
- Session Memory
- Context Retention
- Follow-up Questions
- Multi-turn Conversations

---

# ⚙ Tech Stack

## 🎨 Frontend
- ⚛ React
- ⚡ Vite
- 🌐 Axios
- 🧭 React Router DOM

## 🛠 Backend
- 🚀 FastAPI
- 🐍 Python
- 🔄 Uvicorn
- 📦 Pydantic

## 🗄 Database
- 🍃 MongoDB
- 🧠 FAISS Vector Store

## 🤖 AI Components
- LangChain
- Cohere Embeddings
- Hybrid Retrieval
- BM25 Search
- Query Expansion

---

# 📂 Project Structure

```text
AI-RAG-CHATBOT
│
├── backend
│   ├── app
│   ├── uploads
│   ├── vector_store
│   ├── main.py
│   └── requirements.txt
│
├── frontend
│   ├── src
│   ├── public
│   └── package.json
│
├── README.md
└── .gitignore
```

---

# 🚀 Getting Started

## Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/AI-RAG-CHATBOT.git
cd AI-RAG-CHATBOT
```

## Backend Setup

```bash
cd backend
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
uvicorn main:app --reload
```

## Frontend Setup

```bash
cd frontend
npm install
npm run dev
```

---

# 🔑 Environment Variables

## Backend `.env`

```env
MONGO_URI=
JWT_SECRET=
COHERE_API_KEY=
```

---

# 📡 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/auth/register` | Register User |
| POST | `/auth/login` | Login User |
| POST | `/upload-pdf` | Upload Documents |
| POST | `/ask` | Ask Questions |

---

# 📸 Screenshots

### 🔐 Login Page
(Add Screenshot)

### 📝 Register Page
(Add Screenshot)

### 💬 Chat Interface
(Add Screenshot)

### 📄 Upload Interface
(Add Screenshot)

---

# 🔮 Future Enhancements

- 📷 OCR Support
- 📑 DOCX Support
- 📊 PPT Support
- 🌊 Streaming Responses
- 📍 Source Citations
- 🐳 Docker Deployment
- ☸ Kubernetes Deployment
- ⚡ Redis Cache
- 📈 Analytics Dashboard

---

# 🎓 Resume Highlights

✔ Built a production-style multi-tenant RAG architecture.

✔ Implemented hybrid retrieval using dense and sparse search.

✔ Designed secure JWT-based authentication.

✔ Developed a full-stack AI application using React and FastAPI.

✔ Integrated semantic search using vector embeddings.

---

# 👨‍💻 Author

## Preetham K R

💼 AI Engineer Aspirant  
🚀 Full Stack + GenAI Developer  
📍 Bangalore, India

---

<div align="center">

## ⭐ If you found this project interesting, consider giving it a star ⭐

Built with ❤️ using AI, FastAPI and React

</div>