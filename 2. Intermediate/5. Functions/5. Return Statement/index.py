# ---------------------------------
# Example 1
def add_numbers(x, y):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

# Calling the function and storing the returned result
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)
# ---------------------------------

# ---------------------------------
# Example 2
def square_and_cube(x):
    """This function returns both the square and cube of a number."""
    square = x ** 2
    cube = x ** 3
    return square, cube

# Calling the function and storing the returned values
square_result, cube_result = square_and_cube(2)

# Printing the results
print("Square:", square_result)
print("Cube:", cube_result)


