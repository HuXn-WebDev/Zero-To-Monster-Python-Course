# ----------------------------------
# Accessing Item
# my_list = [1, 2, 3, 4, 5]

# print(my_list[0])
# print(my_list[2])

# Negative indexing can be used to access items from the end of the list
# print(my_list[-1])
# print(my_list[-2])
# ----------------------------------

# ----------------------------------
# Using Slices
my_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

subset = my_list[2:6]
print(subset)  # [2, 3, 4, 5]

# Omitting start and stop indices
subset = my_list[:5] 
print(subset)  # [0, 1, 2, 3, 4]

subset = my_list[5:]
print(subset)  # [5, 6, 7, 8, 9]

# Using negative indices
subset = my_list[-3:]  # Gets the last 3 elements
print(subset)  # [7, 8, 9]

# Using step
subset = my_list[1:9:2]
print(subset)  # [1, 3, 5, 7]
