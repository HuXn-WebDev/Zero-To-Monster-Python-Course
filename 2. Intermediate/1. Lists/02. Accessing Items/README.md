# Accessing Items

#### Lists are zero index based

```py
my_list = [1, 2, 3, 4, 5]

# Accessing items from the list using indexing
print(my_list[0])  # 1 (indexing starts at 0)
print(my_list[2])  # 3

# Negative indexing can be used to access items from the end of the list
print(my_list[-1])  # 5 (last item)
print(my_list[-2])  # 4 (second to last item)
```

# Using Slices

### slicing is a way to extract a portion of a list (or any iterable) by specifying a range of indices. The basic syntax for slicing is start:stop:step

#### 👉 start: is the index of the first element you want to include (inclusive).

#### 👉 stop is the index of the first element you want to exclude (exclusive).

#### 👉 step is the number of indices between elements (defaults to 1 if not specified).

```py
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

subset = my_list[2:6]  # Gets elements at index 2, 3, 4, 5
print(subset)  # [2, 3, 4, 5]

# Omitting start and stop indices
subset = my_list[:5]  # Gets elements at index 0, 1, 2, 3, 4
print(subset)  # [0, 1, 2, 3, 4]

subset = my_list[5:]  # Gets elements at index 5, 6, 7, 8, 9
print(subset)  # [5, 6, 7, 8, 9]

# Using negative indices
subset = my_list[-3:]  # Gets the last 3 elements
print(subset)  # [7, 8, 9]

# Using step
subset = my_list[1:9:2]  # Gets elements at index 1, 3, 5, 7
print(subset)  # [1, 3, 5, 7]
```
