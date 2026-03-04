from langchain_community.vectorstores import Chroma
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_core.documents import Document


class PropertyVectorStore:
    def __init__(self):
        self.embeddings = HuggingFaceEmbeddings(
            model_name="all-MiniLM-L6-v2"
        )
        self.vectorstore = None

    def build_store(self, dataframe):
        documents = []

        for _, row in dataframe.iterrows():
            content = f"""
Property ID: {row['property_id']}
Location: {row['location']}
Price: {row['price']}
Bedrooms: {row['bedrooms']}
Type: {row['property_type']}
Amenities: {row['amenities']}
Description: {row['description']}
"""
            documents.append(Document(page_content=content))

        # 🔥 In-memory store (no persistence to avoid contamination)
        self.vectorstore = Chroma.from_documents(
            documents,
            embedding=self.embeddings
        )

    def search(self, query, k=3):
        if not self.vectorstore:
            return []

        return self.vectorstore.similarity_search(query, k=k)