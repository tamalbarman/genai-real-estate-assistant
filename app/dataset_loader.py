import pandas as pd


class PropertyDataset:
    def __init__(self, path="data/properties.csv"):
        self.df = pd.read_csv(path)

    def get_all(self):
        return self.df

    def get_available_locations(self):
        return set(self.df["location"].str.lower().unique())

    def filter_properties(self, location=None, max_price=None, bedrooms=None):
        filtered = self.df.copy()

        if location:
            filtered = filtered[
                filtered["location"].str.lower() == location.lower()
            ]

        if max_price:
            filtered = filtered[filtered["price"] <= max_price]

        if bedrooms:
            filtered = filtered[filtered["bedrooms"] == bedrooms]

        return filtered