# ------- Protected Modifier
# In Python, attributes and methods that start with a single underscore _ are conventionally considered "protected." This means they are not intended to be accessed from outside the class, but there is no strict enforcement of this.


class MyClass:
    def __init__(self, x):
        # 👇 This attribute is protected
        self._x = x

    # 👇 This method is public
    def get_x(self):
        return self._x


obj = MyClass(10)
print(obj.get_x())  # 10
print(obj._x)  # Accessing a protected attribute (not recommended, but possible)
