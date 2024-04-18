class Car:
    # 👇 Static variable
    num_cars = 0

    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        # 👇 Accessing static variable
        Car.num_cars += 1


# Creating instances of Car
car1 = Car("Toyota", "Camry")
car2 = Car("Honda", "Accord")

print("Number of cars created:", Car.num_cars)  # 2
