# --------------------------
my_set = set({1,5,6})
my_new_set = {1, 2, 3, 4, 5}
print(type(my_set))
print(type(my_new_set))
print(len(my_new_set))
# 👇 Accessing elements using index is not allowed because sets are unordered ❌
# print(my_set[0]) 
# --------------------------

# --------------------------
# Duplicates not allowed ❌
# Set will totally remove duplicate element and give you only unique.
unique_players = {"alex", "alex", "alex", "jordan", "huxn", "michel", "michel"}
print(unique_players)
# --------------------------

# --------------------------
# Add One Element To The Existing Set
games = {"GTA 6", "Spider Man", "The Wither"}
games.add("Cyberpunk")

# Add Multiple Elements To The Existing Set
games.update(["Tekken 8", "Homeworld 3", "Prince of Persia: The Lost Crown"])
games.update(("Dragon's Dogma II", "Nightingale", "Skull & Bones"))
print(games)
# --------------------------

# --------------------------
# Deleting Elements From Set
movies = {"Deadpool 3", "Kraven the Hunter", "Kingdom of the Planet of the Apes"}
movies.remove("Kraven the Hunter")
movies.clear()
print(movies)
# --------------------------

# --------------------------
# Iterating over sets
songs = {"A lot", "Rockstar", "Houdini"}
for song in songs:
    print(song)
# --------------------------
