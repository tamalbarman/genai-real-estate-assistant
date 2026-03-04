# test_vector.py

from app.dataset_loader import PropertyDataset
from app.vector_store import PropertyVectorStore

dataset = PropertyDataset()
filtered = dataset.filter_properties(
    location="Bangalore",
    max_price=8000000,
    bedrooms=2
)

vector_store = PropertyVectorStore()
vector_store.build_store(filtered)

results = vector_store.search("Looking for a family apartment with gym")

for r in results:
    print(r.page_content)
    print("------")