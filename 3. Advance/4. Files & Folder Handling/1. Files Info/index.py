# ⚠️ Use terminal ⚠️

# users_info = open("users.txt", mode="r")  # 👈 hover your mouse over this function
# users_info = open("users.txt", r)
# users_info = open("users.txt")
# print(users_info)

# File Info
# print(users_info.name)
# print(users_info.mode)
# print(users_info.readable())  # Boolean
# print(users_info.closed)  # Boolean

# -------------------------------
# With Statement
with open("users.txt") as users:
    print(users)
