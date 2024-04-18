class Person:
    def __init__(self, name, age, location):
        self.name = name
        self.age = age
        self.location = location

    def user_info(self):
        print(f"Name: {self.name}, Age: {self.age}, Location: {self.location}")


huxn = Person("HuXn", 20, "London")
huxn.user_info()

jordan = Person("Jordan", 26, "USA")
jordan.user_info()

alex = Person("alex", 19, "China")
alex.user_info()
