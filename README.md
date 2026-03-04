# 🏠 GenAI Real Estate Assistant

An AI-powered real estate recommendation assistant built using **FastAPI, Local LLMs, and Vector Search**.
The system understands natural language queries like:

> _"2 BHK in Bangalore under 1 crore with gym"_

and returns intelligent property recommendations.

This project demonstrates **Hybrid GenAI Architecture** combining deterministic logic with LLM reasoning.

---

# 🚀 Features

- 💬 Natural language property search
- 🧠 Multi-turn conversational memory
- 🔎 Hybrid retrieval (structured filtering + vector search)
- 🤖 Local LLM integration using **Ollama**
- ⚡ FastAPI backend for production APIs
- 🎨 Streamlit chat UI for demo interaction
- 🛑 Hallucination reduction using structured constraints

---

# 🧠 Architecture

The system uses a **hybrid AI pipeline**:

User Query
↓
Constraint Extraction
↓
Structured Filtering (Pandas)
↓
Vector Similarity Search (ChromaDB)
↓
LLM Reasoning (Ollama)
↓
Final Recommendation

This architecture improves reliability compared to pure LLM systems.

---

# 🛠 Tech Stack

| Component       | Technology               |
| --------------- | ------------------------ |
| Backend API     | FastAPI                  |
| UI              | Streamlit                |
| LLM             | Ollama (Llama / Mistral) |
| Vector Database | Chroma                   |
| Embeddings      | SentenceTransformers     |
| Data Processing | Pandas                   |
| Language        | Python                   |

---

# 📂 Project Structure

```
genai-real-estate-assistant/
│
├── api/
│   └── main.py              # FastAPI application
│
├── services/
│   ├── llm_service.py
│   ├── recommendation_service.py
│   ├── dataset_service.py
│   └── vector_service.py
│
├── core/
│   └── memory.py            # Conversation memory
│
├── ui/
│   └── streamlit_app.py     # Chat UI
│
├── data/
│   └── properties.csv
│
├── requirements.txt
└── README.md
```

---

# ⚙️ Installation

### 1️⃣ Clone the repository

```
git clone https://github.com/yourusername/genai-real-estate-assistant.git
cd genai-real-estate-assistant
```

---

### 2️⃣ Create virtual environment

```
python -m venv venv
```

Activate it:

Windows

```
venv\Scripts\activate
```

Mac/Linux

```
source venv/bin/activate
```

---

### 3️⃣ Install dependencies

```
pip install -r requirements.txt
```

---

### 4️⃣ Install Ollama

Download from

https://ollama.com

Pull a model:

```
ollama pull llama3.2:3b
```

---

# ▶️ Run the Application

### Start FastAPI backend

```
uvicorn api.main:app --reload
```

API docs:

```
http://127.0.0.1:8000/docs
```

---

### Start Streamlit UI

```
streamlit run ui/streamlit_app.py
```

---

# 💬 Example Queries

Try asking:

```
2 BHK in Bangalore
Under 1 crore
with gym
```

The assistant maintains conversation state and recommends matching properties.

---

# 🧩 Key AI Concepts Demonstrated

- Retrieval Augmented Generation (RAG)
- Hybrid AI systems
- Vector similarity search
- Conversational memory
- Hallucination mitigation

---

# 📈 Future Improvements

- User authentication
- Property image search
- Map-based recommendations
- Cloud deployment
- Real estate dataset integration

---

# 👨‍💻 Author

Built as a **GenAI portfolio project** demonstrating modern AI application architecture.

Feel free to connect or contribute.
