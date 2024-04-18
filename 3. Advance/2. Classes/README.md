# Class?

### A class is a blueprint for creating objects (instances) that have attributes (variables) and methods (functions). It acts as a template for creating objects with similar characteristics.

### Basic Syntax

```py
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")

# Creating an object (instance) of the Person class
person1 = Person("Alice", 30)

# Accessing attributes and calling methods of the object
print(person1.name)  # Alice
print(person1.age)   # 30
person1.greet()      # Hello, my name is Alice and I am 30 years old.
```
