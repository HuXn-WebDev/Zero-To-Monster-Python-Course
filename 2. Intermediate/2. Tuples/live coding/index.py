# ---------------------------
my_tuple = (1, 2, 3, 'hello', 3.14)
# print(my_tuple[0])  # Output: 1
# print(my_tuple[3])  # Output: 'hello'
print(len(my_tuple))

# # This will raise an error since tuples are immutable
# # my_tuple[0] = 5

# # Creating a new tuple with modified content
# new_tuple = my_tuple + (5, 'world')
# print(new_tuple)  # Output: (1, 2, 3, 'hello', 3.14, 5, 'world')
# ---------------------------

# ---------------------------
# Weird Things About Tuples
# nums = 1,2,3,4,5
# print(type(nums)) # tuple

# notTuple = (50)
# isTuple = (50,)
# print(type(notTuple)) # number
# print(type(isTuple)) # tuple
# ---------------------------

# ---------------------------
# Iterating Over Tuple
# friends = ("alex", "michel", "jordan")
# for friend in friends:
#     print(friend)