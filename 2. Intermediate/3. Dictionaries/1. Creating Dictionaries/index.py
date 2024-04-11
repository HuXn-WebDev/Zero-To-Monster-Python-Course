# Empty Dictionary
empty_dict = {}
print(type(empty_dict))

# Dictionary with Key-Value Pairs
student_info = {"name": "Alice", "age": 20, "grade": "A"}
print(student_info)
print(len(student_info))

# Using the dict() Constructor
person = dict(name="Bob", age=25, city="London")
print(person)

# Dictionary with Different Data Types
mixed_dict = {"name": "Charlie", "age": 30, "grades": [85, 90, 78], "is_student": True}
print(mixed_dict)

# Nested Dictionary
nested_dict = {
    "person": {"name": "David", "age": 22},
    "location": {"city": "Paris", "country": "France"},
}
print(nested_dict)

# Using a List of Tuples
tuple_list = [("name", "Eva"), ("age", 28), ("city", "Berlin")]
from_tuples_dict = dict(tuple_list)
print(from_tuples_dict)
