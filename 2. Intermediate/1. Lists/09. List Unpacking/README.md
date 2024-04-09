# List Unpacking

### List unpacking is a feature in Python that allows you to split the elements of a list into individual variables. It is a concise and convenient way to extract values from a list and assign them to multiple variables in a single line.

## Basic Unpacking

```py
my_list = [1, 2, 3]

# Unpacking the list into variables a, b, c
a, b, c = my_list

print(a)  # 1
print(b)  # 2
print(c)  # 3
```

## \*rest

```py
my_list = [1, 2, 3, 4, 5]

# Unpacking the first two elements, and collecting the rest into a variable
first, second, *rest = my_list

print(first) # 1
print(second) # 2
print(rest) # [3, 4, 5]
```
