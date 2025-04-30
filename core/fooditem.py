class FoodItem:
    def __init__(self, id, name, type, quantity, expiry):
        self.id = id
        self.name = name
        self.type = type
        self.quantity = quantity
        self.expiry = expiry  # en jours

    def check_expiry(self):
        return self.expiry <= 0
