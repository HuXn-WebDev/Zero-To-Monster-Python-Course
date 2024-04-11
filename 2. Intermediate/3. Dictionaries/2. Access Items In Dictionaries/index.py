# Using Square Brackets
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict['name'])  # John
print(my_dict['age'])   # 25

# Using the get() Method
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict.get('name'))  # John
print(my_dict.get('grade', 'Not Available'))  # Not Available

# Using a Variable to Store the Key
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
print(my_dict.get('name'))  # John
print(my_dict.get('grade', 'Not Available'))  # Not Available

# Iterating Through Keys
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key in my_dict:
    print(f"{key}: {my_dict[key]}")

# Iterating Through Items (Key-Value Pairs)
my_dict = {'name': 'John', 'age': 25, 'city': 'New York'}
for key, value in my_dict.items():
    print(f"{key}: {value}")    
