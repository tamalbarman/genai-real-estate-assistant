import services.llm_service
print("Using LLM file:", services.llm_service.__file__)
import asyncio
from services.llm_service import LocalLLM
from services.recommendation_engine import RecommendationEngine

llm = LocalLLM()
engine = RecommendationEngine()

async def run():

    # Turn 1
    query1 = "Looking for property in Bangalore"
    constraints1 = await llm.extract_constraints(query1)
    engine.update_state(constraints1)

    # Turn 2
    query2 = "Under 1 crore"
    constraints2 = await llm.extract_constraints(query2)
    engine.update_state(constraints2)

    # Turn 3
    query3 = "2 BHK with gym"
    constraints3 = await llm.extract_constraints(query3)
    print("Extracted constraints 3:", constraints3)
    engine.update_state(constraints3)

    results = engine.retrieve_properties(query3)

    if not results:
        print("No matching properties found.")
        return

    prompt = engine.build_prompt(query3, results)
    response = await llm.generate(prompt)
    print(response)

asyncio.run(run())