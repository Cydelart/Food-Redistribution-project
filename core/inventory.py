class Inventory:
    def __init__(self):
        self.items = []

    def add_item(self, food_item):
        self.items.append(food_item)
        

    def remove_expired(self):
        self.items = [item for item in self.items if not item.check_expiry()]

    def step(self):
        self.schedule.step()
        print("📦 Contenu actuel de l'inventaire :", len(self.inventory.items))

