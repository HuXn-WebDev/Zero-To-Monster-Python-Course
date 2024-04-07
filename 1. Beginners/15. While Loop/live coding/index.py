password = ""

while len(password) < 8:
    password = input("Enter a password (at least 8 characters): ")
print("Password set successfully!")

# ------------------------------

# Menu-driven Program
choice = None

while choice != 'q':
    print("1. Option 1")
    print("2. Option 2")
    print("3. Quit")
    choice = input("Enter your choice (or 'q' to quit): ")
# ------------------------------

# Game Loop
game_over = False

while not game_over:
    # Game logic and user input
    user_input = input("Do you want to continue? (yes/no): ")
    if user_input.lower() == 'no':
        game_over = True
# ------------------------------
