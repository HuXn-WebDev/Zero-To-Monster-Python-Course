# In Operator

### The in operator is used to check if a specified value is present in a sequence, such as a string, list, tuple, or dictionary. The result is a boolean value (True or False). The in operator is often used in conditional statements and loops to test membership within a collection.

## In Strings

```py
text = "Hello, World!"
result = 'o' in text
print(result)  # Output: True
```

## In Lists

```py
numbers = [1, 2, 3, 4, 5]
result = 3 in numbers
print(result)  # Output: True
```

## In Tuples

```py
fruits = ('apple', 'banana', 'cherry')
result = 'banana' in fruits
print(result)  # Output: True
```

## In Dictionaries (Checking Keys)

```py
person = {'name': 'John', 'age': 30, 'city': 'New York'}
result = 'age' in person
print(result)  # Output: True

```

## In Sets

```py
colors = {'red', 'green', 'blue'}
result = 'yellow' in colors
print(result)  # Output: False
```

## In Substrings

```py
sentence = "Python is powerful"
result = "power" in sentence
print(result)  # Output: True
```
