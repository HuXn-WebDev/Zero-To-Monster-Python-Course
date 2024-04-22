import os

# 1. Get Current Working Directory
# print(os.getcwd())

# 2. Make Directory/Folder
# os.mkdir("movies")

# 3. Parent should be available then you'd be able to make another folder inside it.
# os.mkdir("movies/action")  # 👈 Folder inside Folder

# 4. In this case you don't need to have parent, it will create it for you.
# os.makedirs("games/adventure")

# 5. Change directory
# print(os.getcwd())
# os.chdir("games")
# print(os.getcwd())

# 6. Rename Directory
# os.rename("games", "tiktoks")

# 7. Remove Directory
# os.rmdir("tiktoks")  # Folder should be empty, then you can delete it.
# os.rmdir("games/adventure")  # Remove Child Folder

# 8. Remove All
os.removedirs("movies/action")
