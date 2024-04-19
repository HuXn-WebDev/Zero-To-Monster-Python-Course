class Animal:
    def make_sound(self):
        print("Generic animal sound")


class Dog(Animal):
    def make_sound(self):
        print("Woof!")


class Cat(Animal):
    def make_sound(self):
        print("Meow")


dog = Dog()
cat = Cat()

# Calling the overridden method
dog.make_sound()  # Woof!
cat.make_sound()  # Meow
