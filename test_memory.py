import asyncio
from app.llm_service import LocalLLM

llm = LocalLLM()

async def run():
    result = await llm.extract_constraints(
        "Looking for 2 BHK in Bangalore under 80 lakh"
    )
    print(result)

asyncio.run(run())