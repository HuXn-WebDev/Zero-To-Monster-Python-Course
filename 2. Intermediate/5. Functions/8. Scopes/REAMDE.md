# Scope?

### A scope refers to the region of a program where a particular variable can be accessed or modified. The scope of a variable is determined by where it is defined in the code, and it plays a crucial role in understanding how variables are accessed and manipulated within a program.

## There are two main types of scope in Python:

## 1️⃣ Global Scope

#### Variables defined at the top level are considered to be in the global scope.

#### Global variables can be accessed and modified from any part of the code, including within functions.

```py
global_variable = 10  # This is a global variable

def print_global_variable():
    print(global_variable)

print_global_variable()  # Outputs: 10
```

## 2️⃣ Local Scope

#### Variables defined within a function have local scope and are only accessible within that function.

#### Once the function execution is complete, local variables are typically destroyed, and their values are no longer accessible.

```py
def my_func():
    local_variable = 5  # This is a local variable
    print(local_variable)

my_func()  # Outputs: 5

# Attempting to access the local variable outside the function would result in an error
# print(local_variable)  # Raises a NameError
```

#### There's also another concept of nested scopes (not that much important). If a function is defined within another function, it creates a nested scope. Variables in the outer function can be accessed within the inner function, but not vice versa.

```py
def outer_function():
    outer_variable = "I'm in outer function"

    def inner_function():
        print(outer_variable)

    inner_function()

outer_function()  # Outputs: I'm in outer function
```
