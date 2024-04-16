# --------------------------------------
# Example 1
def greet_person(name, greeting="Hello"):
    """This function greets a person with a specified greeting (default is Hello)."""
    print(f"{greeting}, {name}!")

greet_person("HuXn") # Uses the default greeting ("Hello")
greet_person("Bob", "Hi there") # Overrides the default greeting with "Hi there"
# --------------------------------------

# --------------------------------------
# Example 2
def print_message(message, num_exclamation_marks=3):
    """Print a message with a specified number of exclamation marks."""
    print(message + "!" * num_exclamation_marks)

# Calling the function with different arguments
print_message("Hello") # Prints "Hello!!!" using the default number of exclamation marks
print_message("Hi there", 5) # Prints "Hi there!!!!!" with the specified number of exclamation marks
print_message("Greetings", 10)
# --------------------------------------
