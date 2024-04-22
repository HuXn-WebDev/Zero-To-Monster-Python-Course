# 1. We're reading the data so we can provide 'r' mode
# 2. The file should be existed
# 3. You can also omit the "r" mode because it's the default mode
# users = open("users.txt", "r")

# ----------------------
# Reading All Data
# users = open("users.txt")
# users_content = users.read()
# print(users_content)
# ----------------------

# ----------------------
# Reading just a chunk of data
# users = open("users.txt")
# users_content = users.read(5)  # Hello
# print(users_content)

# ----------------------
# Read Only Single Line
talk = open("talk.txt")
content = talk.readline()
print(content)
