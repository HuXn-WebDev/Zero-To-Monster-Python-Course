# Updating Dictionaries?

### We can update dictionaries by adding, modifying, or removing key-value pairs.

## Adding a New Key-Value Pair

```py
my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'
```

## Modifying an Existing Value

```py
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26
```

## Updating with Another Dictionary

```py
my_dict = {'name': 'John', 'age': 25}
update_dict = {'age': 26, 'city': 'New York'}
my_dict.update(update_dict)
```

## Updating with Keyword Arguments

```py
my_dict = {'name': 'John', 'age': 25}
my_dict.update(age=26, city='New York')
```

## Using setdefault() to Add Default Values

```py
my_dict = {'name': 'John', 'age': 25}
my_dict.setdefault('city', 'New York')
```
