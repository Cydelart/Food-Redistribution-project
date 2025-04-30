from mesa import Agent

class RecipientAgent(Agent):
    def __init__(self, unique_id, model):
        super().__init__(unique_id, model)
        self.request_history = []

    def step(self):
        # Fait une demande simple
        self.request_history.append("Requesting food")