# ----------------------------
my_list = [1, 2, 3]

# Unpacking the list into variables a, b, c
a, b, c = my_list

print(a)
print(b)
print(c)
# ----------------------------

# ----------------------------
my_list = [1, 2, 3, 4, 5]

# Unpacking the first two elements, and collecting the rest into a variable
first, second, *rest = my_list

print(first) # 1
print(second) # 2
print(rest) # [3, 4, 5]
# ----------------------------
