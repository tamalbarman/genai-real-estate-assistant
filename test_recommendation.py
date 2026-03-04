import asyncio
from services.recommendation_engine import RecommendationEngine
from services.llm_service import LocalLLM

engine = RecommendationEngine()
llm = LocalLLM()

query = "Looking for a 2 BHK apartment in Bangalore under 80L with gym"

# results = engine.retrieve_properties(
#     location="Bangalore",
#     max_price=8000000,
#     bedrooms=2,
#     query=query
# )

# prompt = engine.build_prompt(query, results)


# async def run():
#     response = await llm.generate(prompt)
#     print(response)


# asyncio.run(run())

# print("Filtered Count:", len(results))

results = engine.retrieve_properties(
    location="Bangalore",
    max_price=8000000,
    bedrooms=2,
    query=query
)

if not results:
    print("No matching properties found based on your criteria.")
else:
    prompt = engine.build_prompt(query, results)

    async def run():
        response = await llm.generate(prompt)
        print(response)

    asyncio.run(run())