# Strings

### A string is a sequence of characters, and it is one of the fundamental data types used to represent textual data.

```py
# Using single quotes
single_quoted_string = 'Hello, World!'

# Using double quotes
double_quoted_string = "Python Programming"

# Multiline string using triple quotes
multiline_string = '''This is a
multiline
string.'''
```

# Concatenation

```py
str1 = "Hello"
str2 = "World"
concatenated_string = str1 + ", " + str2
print(concatenated_string)  # Hello, World
```

# String Length

```py
string = "Python"
length = len(string)
print(length)  # 6
```

# String Indexing and Slicing

```py
text = "Python"
first_char = text[0]     # Accessing the first character
substring = text[1:4]    # Slicing from index 1 to 3
print(first_char, substring)  # P yth
```

# String Methods

```py
sentence = "   Python is fun!   "
uppercase_sentence = sentence.upper()
lowercase_sentence = sentence.lower()
stripped_sentence = sentence.strip()
print(uppercase_sentence, lowercase_sentence, stripped_sentence)
```

# String Formatting

```py
name = "HuXn"
age = 20
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)
```

# Escape Characters

```py
escaped_string = "This is a line.\nThis is a new line."
print(escaped_string)
```
