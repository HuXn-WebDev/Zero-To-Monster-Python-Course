# Named Arguments

### Keyword arguments, aka named arguments, allow you to pass values to a function by explicitly specifying the parameter names along with their values. This can make function calls more readable and allow you to provide arguments in a different order than they appear in the function definition.

## Example 1

```py
def display_info(name, age, city):
    """Display information about a person."""
    print("Name:", name)
    print("Age:", age)
    print("City:", city)

# Using keyword arguments to call the function
display_info(name="HuXn", age=20, city="US")
```

## Example 2

```py
def calculate_rectangle_area(length, width):
    """Calculate the area of a rectangle."""
    area = length * width
    return area

# Using keyword arguments to call the function
area_result = calculate_rectangle_area(length=5, width=3)
print("Rectangle Area:", area_result)
```
