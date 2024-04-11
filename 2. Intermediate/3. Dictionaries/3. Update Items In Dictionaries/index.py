# Adding a New Key-Value Pair
my_dict = {'name': 'John', 'age': 25}
my_dict['city'] = 'New York'

# Modifying an Existing Value
my_dict = {'name': 'John', 'age': 25}
my_dict['age'] = 26

# Updating with Another Dictionary
my_dict = {'name': 'John', 'age': 25}
update_dict = {'age': 26, 'city': 'New York'}
my_dict.update(update_dict)

# Updating with Keyword Arguments
my_dict = {'name': 'John', 'age': 25}
my_dict.update(age=26, city='New York')

# Using setdefault() to Add Default Values
my_dict = {'name': 'John', 'age': 25}
my_dict.setdefault('city', 'New York')
