from mesa import Model
from mesa.time import RandomActivation
from agents.donoragent import DonorAgent
from agents.recipientagent import RecipientAgent
from agents.deliveryagent import DeliveryAgent
from core.inventory import Inventory

class FoodRedistributionModel(Model):
    def __init__(self, num_donors=2, num_recipients=2, num_deliveries=1):
        self.schedule = RandomActivation(self)
        self.inventory = Inventory()

        # Créer donateurs
        for i in range(num_donors):
            agent = DonorAgent(i, self)
            self.schedule.add(agent)

        # Créer receveurs
        for i in range(num_donors, num_donors + num_recipients):
            agent = RecipientAgent(i, self)
            self.schedule.add(agent)

        # Créer livreurs
        for i in range(num_donors + num_recipients, num_donors + num_recipients + num_deliveries):
            agent = DeliveryAgent(i, self)
            self.schedule.add(agent)

    def step(self):
        self.schedule.step()
