# Super / Parent / Base Class
class Animal:
    def __init__(self, animal_name):
        self.animal_name = animal_name

    def animal_info(self):
        print(f"Animal Name is: {self.animal_name}")


# Child / Derived / Sub Class
class Dog(Animal):
    def bark(self):
        print("woff woff")


dog = Animal("Dog")
buddy = Dog("Buddy")

dog.animal_info()
buddy.animal_info()
