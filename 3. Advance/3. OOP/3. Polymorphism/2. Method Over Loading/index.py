# -------------
# Java Method Overloading Implementation
# class MathOperations:
#     def add(self, x, y):
#         return x + y

#     def add(self, x, y, z):
#         return x + y + z


# add_two_numbers = MathOperations()
# print(add_two_numbers.add(2, 3, 4))
# -------------


# 👇 Method Overloading In Python
class Calculator:
    def add(self, a, b=None):
        if b is None:
            return a
        else:
            return a + b


calc = Calculator()

print(calc.add(1))  # 1
print(calc.add(1, 2))  # 3
