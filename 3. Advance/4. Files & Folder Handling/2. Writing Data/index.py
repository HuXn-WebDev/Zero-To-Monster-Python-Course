# -----------------------
# write()
# users_file = open("users.txt", "w")

# If the file is already created it'll append this data,
# -- If not so it will first create that file then write this data to it.

# users_file.write("I'm writing this text to my file using python.")
# users_file.close()
# ----------------------

# ----------------------
# writelines()

users_list = open("users.txt", "w")
# friends = ["Jordan", "Alex", "Michel", "HuXn"]
friends = ["Jordan\n", "Alex\n", "Michel\n", "HuXn\n"]
users_list.writelines(friends)
users_list.close()
