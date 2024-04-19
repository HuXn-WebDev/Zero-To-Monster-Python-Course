class Person:
    def __init__(self, name, age, gender):
        self._name = name  # protected attribute
        self.__age = age  # private attribute
        self.__gender = gender  # private attribute

    def get_age(self):
        return self.__age

    def set_age(self, age):
        if age > 0:
            self.__age = age
        else:
            print("Age should be greater than 0")

    def get_gender(self):
        return self.__gender

    def set_gender(self, gender):
        if gender in ["Male", "Female", "Other"]:
            self.__gender = gender
        else:
            print("Invalid gender")


person = Person("HuXn", 20, "Male")

# Accessing protected attribute
print(person._name)  # HuXn

# Accessing private attribute (will raise an error)
# print(person.__age)  # 👈 This will raise an error

# Accessing private attribute using name mangling
print(person._Person__age)  # 20

# Using getter method to access private attribute
print(person.get_age())  # 20

# Using setter method to change the age
person.set_age(30)
print(person.get_age())  # 30

# Using setter method to set an invalid age
person.set_age(-1)  # Age should be greater than 0

# Using setter method to set an invalid gender
person.set_gender("Unknown")  # Invalid gender
