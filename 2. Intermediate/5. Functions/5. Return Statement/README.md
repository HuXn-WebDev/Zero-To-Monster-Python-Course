# Return Statement

### The return statement is used within a function to send a value back to the caller. When a function is executed and encounters the return statement, it immediately stops executing, and the specified value is sent back to the caller.

## Example 1

```py
def add_numbers(x, y):
    """This function adds two numbers and returns the result."""
    result = x + y
    return result

# Calling the function and storing the returned result
sum_result = add_numbers(3, 5)
print("Sum:", sum_result)
```

## Example 2

```py
def square_and_cube(x):
    """This function returns both the square and cube of a number."""
    square = x ** 2
    cube = x ** 3
    return square, cube

# Calling the function and storing the returned values
square_result, cube_result = square_and_cube(2)

print("Square:", square_result)
print("Cube:", cube_result)
```
