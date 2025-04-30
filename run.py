from simulation.model import FoodRedistributionModel

if __name__ == "__main__":
    model = FoodRedistributionModel()
    for i in range(5):  # 5 étapes de simulation
        print(f"\n⏱️ Étape {i + 1}")
        model.step()
