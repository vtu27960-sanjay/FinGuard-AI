# FinGuard AI – Intelligent Fraud Detection & Banking Assistant

## Project Overview

FinGuard AI is an AI-powered banking application that detects fraudulent transactions using Machine Learning and answers banking-related questions using Retrieval-Augmented Generation (RAG).

The system combines:

- Machine Learning for fraud prediction
- FastAPI backend
- React frontend
- MySQL database
- RAG chatbot using banking PDF documents

---

## Features

- Fraud Detection
- Banking Chatbot
- Transaction History
- Dashboard
- Charts and Analytics
- MySQL Integration
- REST API
- Banking Knowledge Base using PDF

---

## Technologies Used

### Frontend
- React.js
- Bootstrap
- Axios
- Chart.js

### Backend
- FastAPI
- Python

### Database
- MySQL

### Machine Learning
- Scikit-learn
- Pandas
- NumPy

### AI
- LangChain
- FAISS
- Sentence Transformers

---

## Project Structure

```text
FinGuard-AI/
│
├── backend/
├── frontend/
├── database/
├── datasets/
├── documents/
├── models/
├── rag/
├── README.md
```

---

## Installation

### Clone Repository

```bash
git clone https://github.com/vtu27960-sanjay/FinGuard-AI.git
```

---

### Backend

```bash
cd backend
pip install -r requirements.txt
uvicorn app:app --reload
```

---

### Frontend

```bash
cd frontend
npm install
npm start
```

---

### Database

Import:

```
database/schema.sql
```

into MySQL.

---

## API Endpoints

### Predict Fraud

```
POST /predict
```

### Chatbot

```
POST /chat
```

---

## Future Improvements

- User Authentication
- Live Banking APIs
- Email Alerts
- SMS Notifications
- Cloud Deployment
- Admin Dashboard

---

## Author

**Sanjay Thuraka**

B.Tech CSE (AI & ML)

Vel Tech University

---

## License

This project is developed for educational purposes.