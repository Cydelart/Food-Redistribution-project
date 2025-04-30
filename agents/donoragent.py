from mesa import Agent
from core.fooditem import FoodItem
import random

class DonorAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.donation_history = []

    def step(self):
        # Crée un nouvel aliment à chaque step
        item = FoodItem(
            id=f"item_{self.unique_id}_{len(self.donation_history)}",
            name="Lait",
            type="Dairy",
            quantity=random.randint(1, 10),
            expiry=5
        )
        self.model.inventory.add_item(item)
        self.donation_history.append(item)
        print(f"🧑‍🍳 Donor {self.unique_id} a donné {item.quantity}x {item.name} (type: {item.type}, exp: {item.expiry}j)")

