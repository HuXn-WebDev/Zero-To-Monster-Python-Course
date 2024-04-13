# Sets?

### A set is an unordered collection of unique elements. Sets are defined by enclosing a comma-separated sequence of values in curly braces {}. Unlike lists or tuples, sets do not allow duplicate elements, and the order of elements is not guaranteed.

## Example of set

```py
my_set = {1, 2, 3, 4, 5}
```

## We can also create a set from a list using the set() constructor

```py
my_list = [1, 2, 2, 3, 4, 4, 5]
converted_set = set(my_list)
print(converted_set)  # Output: {1, 2, 3, 4, 5}
```
