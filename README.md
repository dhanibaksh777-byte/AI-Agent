# AI Agent

A powerful AI Agent built from scratch using FastAPI and Groq, with support for multiple tools and conversation memory.

## Live Demo
Backend: https://ai-agent1-riqx.onrender.com/docs

## Features

- **Web Search** — Real-time web search using Tavily
- **Calculator** — Mathematical expressions evaluation
- **Date & Time** — Current date and time retrieval
- **Note Saver** — Save notes to database
- **Conversation Memory** — Context preserved across messages
- **Pure Function Calling** — No LangChain, no frameworks

## Tech Stack

- **FastAPI** — Backend framework
- **Groq** — LLM provider
- **Tavily** — Web search API
- **PostgreSQL (Neon)** — Database
- **SQLAlchemy** — ORM
- **Alembic** — Migrations

## Setup

1. Clone the repo
2. Create virtual environment
```bash
   python -m venv venv
   venv\Scripts\activate
```
3. Install dependencies
```bash


database_url=your_neon_url
groq_api_key=your_groq_key
tavily_api_key=your_tavily_key

5. Run the server
```bash
   uvicorn main:app --reload
```

## API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/conversation` | Create new conversation |
| POST | `/chat/{conversation_id}` | Send message to agent |
   pip install -r requirements.txt
```
4. Add `.env` file
