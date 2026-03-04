# test_filter.py
from app.dataset_loader import PropertyDataset

dataset = PropertyDataset()

results = dataset.filter_properties(
    location="Bangalore",
    max_price=8000000,
    bedrooms=2
)

print(results.head())
print("Count:", len(results))