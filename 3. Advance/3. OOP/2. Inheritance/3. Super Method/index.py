class Animal:
    def __init__(self, breed, size, color, speed):
        self.breed = breed
        self.size = size
        self.color = color
        self.speed = speed
        print("Parent Constructor")
        print(
            f"Breed: {self.breed}, Size: {self.size}, Color: {self.color}, Speed: {self.speed}"
        )


# Super method is used to call parent class constructor to the child class.
class Dog(Animal):
    def __init__(self, animal_name, breed, size, color, speed):
        # 👇 Calling Parent Class Constructor
        super().__init__(breed, size, color, speed)
        self.animal_name = animal_name
        print(f"Name: {self.animal_name}")

    def bark(self):
        print("woff woff")


buddy = Dog("Dog", "IDK", 40, "blue", 50)
buddy.bark()
