# ------- Private Modifier
# In Python, attributes and methods that start with double underscores __ are considered "private." This means they are not accessible from outside the class. However, Python does not enforce this access restriction strictly;


class MyClass:
    def __init__(self, x):
        self.__x = x  # 👈 This attribute is private

    def get_x(self):
        return self.__x  # 👈 This method is public


obj = MyClass(10)
print(obj.get_x())  # 10
# Accessing a private attribute (not recommended, and name-mangled)
print(obj._MyClass__x)
