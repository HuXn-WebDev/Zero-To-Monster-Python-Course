# --------------------------
add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
# --------------------------

# --------------------------
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

# Example of using a lambda function as an argument
result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)
# --------------------------
