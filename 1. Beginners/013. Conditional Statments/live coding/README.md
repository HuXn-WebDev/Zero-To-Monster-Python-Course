# Conditional Statements

### Conditional statements are used to control the flow of a program based on certain conditions. They allow you to execute different blocks of code depending on whether a specified condition evaluates to True or False

## if Statement

#### The if statement is used to execute a block of code only if a specified condition is True

```py
x = 10

if x > 5:
    print("x is greater than 5")
```

## if-else Statement

#### The if-else statement allows you to specify two blocks of code: one to be executed if the condition is True, and another if the condition is False.

```py
x = 3

if x % 2 == 0:
    print("x is even")
else:
    print("x is odd")
```

## if-elif-else Statement

#### The if-elif-else statement allows you to check multiple conditions sequentially. It executes the block of code associated with the first condition that is True.

```py
x = 0

if x > 0:
    print("x is positive")
elif x < 0:
    print("x is negative")
else:
    print("x is zero")
```
