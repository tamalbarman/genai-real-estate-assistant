from app.dataset_loader import PropertyDataset

dataset = PropertyDataset()

df = dataset.get_all()

result = df[
    (df["location"].str.lower() == "bangalore") &
    (df["bedrooms"] == 2) &
    (df["price"] <= 8000000)
]

print(result)
print("Count:", len(result))