# Loops?

### Loops allow us to repeatedly execute a block of code as long as a certain condition is met or iterate over a sequence of elements. Python supports two main types of loops: for loops and while loops.

## for loop

#### A for loop is used to iterate over a sequence (such as a list, tuple, string, or other iterable objects) and execute a block of code for each element in the sequence.

## range

#### range is a built-in function that generates a sequence of numbers within a specified range. It is commonly used with for loops to iterate over a sequence of numbers.

```py
for i in range(5):
    print(i)
```

## range(start, stop)

```py
for i in range(2, 8):
    print(i)
```

## range(start, stop, step)

#### range(1, 10, 2): This creates a sequence of numbers starting from 1 up to (but not including) 10, with a step of 2. So, the sequence generated is [1, 3, 5, 7, 9]

```py
for i in range(1, 10, 2):
    print(i)
```
