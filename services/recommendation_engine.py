from app.dataset_loader import PropertyDataset
from app.vector_store import PropertyVectorStore
from app.memory_manager import ConversationState


class RecommendationEngine:
    def __init__(self):
        self.dataset = PropertyDataset()
        self.vector_store = PropertyVectorStore()
        self.memory = ConversationState()

    def update_state(self, extracted_constraints: dict):
        valid_locations = self.dataset.get_available_locations()

        location = extracted_constraints.get("location")

        if location and location.lower() not in valid_locations:
            extracted_constraints["location"] = None

        self.memory.update(extracted_constraints)

    def retrieve_properties(self, query: str):
        state = self.memory.get()

        filtered = self.dataset.filter_properties(
            location=state["location"],
            max_price=state["max_price"],
            bedrooms=state["bedrooms"]
        )

        print("Current State:", state)
        print("Filtered Properties:")
        print(filtered[["property_id", "bedrooms", "price"]])

        if filtered.empty:
            return None

        self.vector_store.build_store(filtered)

        results = self.vector_store.search(query, k=3)

        return results

    def build_prompt(self, user_query, retrieved_docs):
        context = "\n\n".join([doc.page_content for doc in retrieved_docs])

        prompt = f"""
You are a smart real estate assistant.

Recommend properties strictly from the list below.
Do NOT invent properties.

User Request:
{user_query}

Available Properties:
{context}

Explain why they match.
"""
        return prompt