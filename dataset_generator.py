import random
import pandas as pd

cities = ["Bangalore", "Mumbai", "Delhi", "Hyderabad", "Chennai", "Pune", "Kolkata", "Ahmedabad", "Jaipur", "Lucknow"]
property_types = ["Apartment", "Villa", "Plot"]
amenities_pool = [
    "Gym", "Parking", "School nearby",
    "Metro access", "Swimming Pool", "Garden"
]

data = []

for i in range(300):
    city = random.choice(cities)
    bedrooms = random.randint(1, 5)
    price = random.randint(30, 200) * 100000  # 30L to 2Cr
    
    amenities = random.sample(amenities_pool, random.randint(2, 4))

    description = (
        f"A {bedrooms} BHK {random.choice(property_types)} in {city} "
        f"with {' and '.join(amenities)}."
    )

    data.append({
        "property_id": f"P{i}",
        "location": city,
        "price": price,
        "bedrooms": bedrooms,
        "property_type": random.choice(property_types),
        "amenities": ", ".join(amenities),
        "description": description
    })

df = pd.DataFrame(data)
df.to_csv("properties.csv", index=False)

print("Dataset created successfully.")