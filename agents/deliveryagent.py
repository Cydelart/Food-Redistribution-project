from mesa import Agent

class DeliveryAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.capacity = 10
        self.cargo = []

    def step(self):
        # Livreur vide le stock s’il est plein
        if len(self.cargo) > 0:
            self.cargo.clear()
