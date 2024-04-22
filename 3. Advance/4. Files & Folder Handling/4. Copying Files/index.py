users = open("users.txt", "r")
friends = open("friends.txt", "w")

# 1. Read the data
content = users.read()

# 2. Write to "friends.txt" file
friends.write(content)
friends.close()
