import httpx
import json
import re


class LocalLLM:
    def __init__(self, model="llama3.2:3b"):
        self.model = model
        self.url = "http://localhost:11434/api/generate"

    async def generate(self, prompt: str):
        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {
                        "temperature": 0
                    }
                }
            )

        data = response.json()

        if "response" not in data:
            return f"Error: {data}"

        return data["response"]

    async def extract_constraints(self, query: str):

        # 🔥 1. Deterministic extraction first

        import re

        # Extract bedrooms
        bedroom_match = re.search(r"(\d+)\s*bhk", query.lower())
        bedrooms = int(bedroom_match.group(1)) if bedroom_match else None

        # Extract price in lakh
        price_match_lakh = re.search(r"(\d+)\s*(lakh|lac|l)", query.lower())
        price_match_crore = re.search(r"(\d+)\s*(crore|cr)", query.lower())

        if price_match_lakh:
            max_price = int(price_match_lakh.group(1)) * 100000
        elif price_match_crore:
            max_price = int(price_match_crore.group(1)) * 10000000
        else:
            max_price = None

        # 🔥 2. Use LLM only for location

        prompt = f"""
    Extract only the city/location name from the user query.

    Return JSON only:
    {{
    "location": string or null
    }}

    User Query: {query}
    """

        async with httpx.AsyncClient(timeout=120.0) as client:
            response = await client.post(
                self.url,
                json={
                    "model": self.model,
                    "prompt": prompt,
                    "stream": False,
                    "options": {"temperature": 0}
                }
            )

        data = response.json()

        location = None

        if "response" in data:
            try:
                parsed = json.loads(data["response"].strip())
                location = parsed.get("location")
                if location:
                    if str(location).lower() == "null":
                        location = None
                else:
                    location = None
            except:
                location = None

        return {
            "location": location,
            "max_price": max_price,
            "bedrooms": bedrooms
        }