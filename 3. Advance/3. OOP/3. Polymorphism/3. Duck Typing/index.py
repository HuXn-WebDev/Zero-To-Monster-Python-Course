class Dog:
    def speak(self):
        return "Woof!"


class Cat:
    def speak(self):
        return "Meow!"


class Duck:
    def speak(self):
        return "Quack!"


class Gorilla:
    # ❌ Here we don't have the "speak" method
    #  - We only have the "walk" method
    def walk(self):
        return "Grunt"


# Using the function with different objects
dog = Dog()
cat = Cat()
duck = Duck()
gorilla = Gorilla()


# Function that accepts any object with a speak() method
def make_sound(animal):
    return animal.speak()


print(make_sound(dog))  # Woof!
print(make_sound(cat))  # Meow!
print(make_sound(duck))  # Quack!

print(make_sound(gorilla))  # ERROR ❌
