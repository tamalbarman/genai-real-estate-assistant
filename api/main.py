from fastapi import FastAPI
from pydantic import BaseModel
from services.llm_service import LocalLLM
from services.recommendation_engine import RecommendationEngine
import asyncio

app = FastAPI(title="GenAI Real Estate Assistant")

llm = LocalLLM()
engine = RecommendationEngine()


class ChatRequest(BaseModel):
    message: str


@app.post("/chat")
async def chat(request: ChatRequest):
    # Extract constraints
    constraints = await llm.extract_constraints(request.message)
    engine.update_state(constraints)

    # Retrieve properties
    results = engine.retrieve_properties(request.message)

    if not results:
        return {
            "response": "No matching properties found based on your criteria.",
            "state": engine.memory.get()
        }

    prompt = engine.build_prompt(request.message, results)
    answer = await llm.generate(prompt)

    return {
        "response": answer,
        "state": engine.memory.get()
    }