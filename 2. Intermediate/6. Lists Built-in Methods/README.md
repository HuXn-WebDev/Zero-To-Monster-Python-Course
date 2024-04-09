# Lists Built-In Methods

## append(x)

#### Adds element at the end of the list.

```py
my_list = [1, 2, 3]
my_list.append(4)
# Result: [1, 2, 3, 4]
```

## extend(iterable)

#### Extends the list by appending elements from the iterable.

```py
my_list = [1, 2, 3]
my_list.extend([4, 5, 6])
# Result: [1, 2, 3, 4, 5, 6]
```

## insert(i, x)

#### Inserts element x at the specified position i.

```py
my_list = [1, 2, 3]
my_list.insert(1, 4)
# Result: [1, 4, 2, 3]
```

## remove(x)

#### Removes the first occurrence of element x.

```py
my_list = [1, 2, 3, 2]
my_list.remove(2)
# Result: [1, 3, 2]
```

## pop([i])

#### Removes and returns the element at the specified position i. If no index is provided, it removes and returns the last element.

```py
my_list = [1, 2, 3]
popped_element = my_list.pop(1)
# Result: popped_element=2, my_list=[1, 3]
```

## count(x)

#### Returns the number of occurrences of element x in the list.

```py
my_list = [1, 2, 3, 2]
count_of_2 = my_list.count(2)
# Result: count_of_2=2
```

## sort(key=None, reverse=False)

#### Sorts the elements of the list in ascending order. The key and reverse parameters are optional.

```py
my_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3]
my_list.sort()
# Result: [1, 1, 2, 3, 3, 4, 5, 5, 6, 9]
```

## reverse()

#### Reverses the elements of the list in place.

```py
my_list = [1, 2, 3]
my_list.reverse()
# Result: [3, 2, 1]
```

## copy()

#### Returns a shallow copy of the list.

```py
original_list = [1, 2, 3]
copied_list = original_list.copy()
# Result: copied_list=[1, 2, 3]
```
