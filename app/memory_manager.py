class ConversationState:
    def __init__(self):
        self.state = {
            "location": None,
            "max_price": None,
            "bedrooms": None
        }

    def update(self, extracted_data: dict):
        for key in self.state:
            if key in extracted_data and extracted_data[key] is not None:
                self.state[key] = extracted_data[key]

    def get(self):
        return self.state