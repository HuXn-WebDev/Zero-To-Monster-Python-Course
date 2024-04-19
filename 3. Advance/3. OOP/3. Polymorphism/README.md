# Polymorphism?

#### Polymorphism is a concept in OOP that allows objects of different classes to be treated as objects of a common interface. It enables a single interface to represent various types or forms, providing flexibility and extensibility in the design of software.

## Purpose

#### The primary purpose of polymorphism is to create a more generalized and adaptable code structure. It allows different classes to share a common interface, and objects of these classes can be used interchangeably. This flexibility is particularly useful when dealing with collections of objects, as polymorphism enables the use of a single piece of code to work with objects of different types.

## Implementation

### 👉 Method Overloading

#### Method overloading in Python involves defining multiple methods in the same class with the same name but different parameters. This is also known as compile-time polymorphism or static polymorphism.

```py
class MathOperations:
    def add(self, x, y):
        return x + y

    def add(self, x, y, z):
        return x + y + z
```

### 👉 Polymorphism with Inheritance

#### Polymorphism is often demonstrated through inheritance and method overriding. Objects of different subclasses can be used interchangeably when they share a common base class.

```py
class Animal:
    def make_sound(self):
        pass

class Dog(Animal):
    def make_sound(self):
        return "Woof!"

class Cat(Animal):
    def make_sound(self):
        return "Meow!"
```

### 👉 Duck Typing

#### In languages like Python, polymorphism is also achieved through duck typing. If an object walks like a duck and quacks like a duck, then it's treated as a duck, regardless of its actual type.

```py
def animal_sound(animal):
    return animal.make_sound()

dog = Dog()
cat = Cat()

print(animal_sound(dog))  # Outputs: Woof!
print(animal_sound(cat))  # Outputs: Meow!
```
