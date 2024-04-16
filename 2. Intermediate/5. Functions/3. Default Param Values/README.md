# Default Param Values

### You can also pass a default value for a parameter in a function. If a value is provided for that parameter when the function is called, it will use the provided value. If no value is provided, the function will use the default value.

## Example 1

```py
def greet_person(name, greeting="Hello"):
    """This function greets a person with a specified greeting (default is Hello)."""
    print(f"{greeting}, {name}!")

greet_person("HuXn") # Uses the default greeting ("Hello")
greet_person("Bob", "Hi there") # Overrides the default greeting with "Hi there"
```

## Example 2

```py
def print_message(message, num_exclamation_marks=3):
    """Print a message with a specified number of exclamation marks."""
    print(message + "!" * num_exclamation_marks)

# Calling the function with different arguments
print_message("Hello") # Prints "Hello!!!" using the default number of exclamation marks
print_message("Hi there", 5) # Prints "Hi there!!!!!" with the specified number of exclamation marks
print_message("Greetings", 10)
```
