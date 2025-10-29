# Python
class Car:
    def __init__(self, model, fuel, efficiency):
        self.model = model
        self.fuel = fuel
        self.efficiency = efficiency

    def calc_range(self):
        return self.fuel * self.efficiency


