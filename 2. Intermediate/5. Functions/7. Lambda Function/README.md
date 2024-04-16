# Lambda Function

### Lambda function is a small anonymous function defined using the lambda keyword. It is often referred to as a "lambda expression." Lambda functions are used when you need a simple function for a short period and don't want to formally define a full function using the def keyword.

```py
# lambda arguments: expression

add = lambda x, y: x + y
result = add(3, 5)
print(result)  # Output: 8
```

```py
# Function that takes another function as an argument
def apply_operation(x, y, operation):
    return operation(x, y)

result_addition = apply_operation(5, 3, lambda a, b: a + b)
print("Result of addition:", result_addition)

result_multiplication = apply_operation(5, 3, lambda a, b: a * b)
print("Result of multiplication:", result_multiplication)
```
