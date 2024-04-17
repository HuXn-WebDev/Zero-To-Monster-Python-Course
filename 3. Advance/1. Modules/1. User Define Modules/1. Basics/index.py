# ----------------
# import my_own_math

# print(my_own_math.a)
# print(my_own_math.add_to_numbers(10, 20))
# print(my_own_math.subtract_to_numbers(20, 10))
# print(my_own_math.multiply_to_numbers(20, 10))
# print(my_own_math.divide_to_numbers(20, 10))
# ----------------

# ----------------
# alias
# import my_own_math as math

# print(math.add_to_numbers(10, 20))
# print(math.subtract_to_numbers(10, 20))
# print(math.multiply_to_numbers(10, 20))
# print(math.divide_to_numbers(10, 20))

# ----------------
# Specific Item
# from my_own_math import (
#     intro,
#     add_to_numbers,
#     subtract_to_numbers,
#     multiply_to_numbers,
#     divide_to_numbers,
# )

# intro()

# print(add_to_numbers(10, 20))
# print(subtract_to_numbers(10, 20))
# print(multiply_to_numbers(10, 20))
# print(divide_to_numbers(10, 20))

# ----------------
# Import specific item and provide alias to it
# from my_own_math import (
#     intro,
#     add_to_numbers as plus,
#     subtract_to_numbers as minus,
#     multiply_to_numbers as multiply,
#     divide_to_numbers as divide,
# )

# intro()

# print(plus(10, 20))
# print(minus(10, 20))
# print(multiply(10, 20))
# print(divide(10, 20))

# ----------------
# Import Everything *
from my_own_math import *

print(add_to_numbers(10, 20))
print(subtract_to_numbers(10, 20))
print(multiply_to_numbers(10, 20))
print(divide_to_numbers(10, 20))
