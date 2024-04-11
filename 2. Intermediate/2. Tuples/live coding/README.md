# Tuples?

### Tuple is an ordered, immutable collection of elements. This means that once you create a tuple, you cannot modify its contents - you can't add, remove, or change elements in a tuple after it has been created. Tuples are defined by enclosing a comma-separated sequence of values in parentheses ()

### Basic Syntax

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
print(my_tuple[0])  # Output: 1
print(my_tuple[3])  # Output: 'hello'
```

### Error

```py
my_tuple = (1, 2, 3, 'hello', 3.14)
# This will raise an error since tuples are immutable
# my_tuple[0] = 5

# Creating a new tuple with modified content
new_tuple = my_tuple + (5, 'world')
print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')
```
