# ----------------------------
my_list = [1, 2, 3, 4, 5]

my_list[2] = 10
print(my_list)

# ----------------------------
# Create a 2D list (matrix)
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Print the original matrix
print("Original Matrix:")
for row in matrix:
    print(row)

# Update the element at the second row and third column (index 1, 2)
matrix[1][2] = 10

# Print the updated matrix
print("\nUpdated Matrix:")
for row in matrix:
    print(row)
