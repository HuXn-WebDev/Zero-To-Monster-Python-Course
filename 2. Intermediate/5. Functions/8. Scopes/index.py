# -------------------------------
# Local Scope
global_variable = 10  # This is a global variable

def print_global_variable():
    print(global_variable)

print_global_variable()  # Outputs: 10
# -------------------------------

# -------------------------------
# Local Scope

def my_func():
    local_variable = 5  # This is a local variable
    print(local_variable)

my_func()  # Outputs: 5
# -------------------------------

# -------------------------------
# Nested Scope
def outer_function():
    outer_variable = "I'm in outer function"

    def inner_function():
        print(outer_variable)

    inner_function()

outer_function()  # Outputs: I'm in outer function
# -------------------------------
