# ------- Public Modifier
# In python here is no explicit "public" access modifier like in some other languages (e.g., Java or C++). By default, all attributes and methods in a class are considered public, meaning they can be accessed from outside the class.


class MyClass:
    def __init__(self, x):
        # 👇 This attribute is public
        self.x = x

    # 👇 This method is public
    def get_x(self):
        return self.x


obj = MyClass(10)
print(obj.get_x())  # 10
print(obj.x)  # 10
