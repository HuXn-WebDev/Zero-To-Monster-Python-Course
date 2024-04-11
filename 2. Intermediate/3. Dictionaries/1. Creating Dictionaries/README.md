# Dictionaries?

### A dictionary is a built-in data type that represents a collection of key-value pairs. It is a highly flexible and efficient data structure used for mapping keys to values.

## Key features of dictionaries

#### 👉 Each element in a dictionary consists of a key and its corresponding value. The key is a unique identifier for the value.

#### 👉 Unlike lists, dictionaries are unordered collections, which means the order of elements is not guaranteed.

#### 👉 Dictionaries can be modified after creation. You can add, remove, or update key-value pairs.

#### 👉 Dictionaries can grow or shrink in size as needed.

#### 👉 Each key in a dictionary must be unique. If you try to add a key that already exists, the new value will overwrite the existing one.

## Empty Dictionary

```py
empty_dict = {}
```

## Dictionary with Key-Value Pairs

```py
student_info = {'name': 'Alice', 'age': 20, 'grade': 'A'}
```

## Using the dict() Constructor

```py
person = dict(name='Bob', age=25, city='London')
```

## Dictionary with Different Data Types

```py
mixed_dict = {'name': 'Charlie', 'age': 30, 'grades': [85, 90, 78], 'is_student': True}
```

## Nested Dictionary

```py
nested_dict = {'person': {'name': 'David', 'age': 22}, 'location': {'city': 'Paris', 'country': 'France'}}
```

## Using a List of Tuples

```py
tuple_list = [('name', 'Eva'), ('age', 28), ('city', 'Berlin')]
from_tuples_dict = dict(tuple_list)
```
