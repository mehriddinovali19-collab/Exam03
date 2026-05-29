class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model 


    def move(self):
        print("Vehicle is moving")

class Car(Vehicle):
    def move(self):
        print("Car is driving")

v1 = Vehicle("BMW", "X5")
c1 = Car("Tesla", "Model S")

v1.move()
c1.move()