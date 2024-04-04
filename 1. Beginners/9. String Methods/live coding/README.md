# String Methods

#### Strings in Python come with a variety of built-in methods that allow you to manipulate and work with them.

## str.upper() and str.lower()

### Converts all characters in a string to uppercase or lowercase.

```py
text = "Hello, World!"
upper_text = text.upper()
lower_text = text.lower()
print(upper_text)  # HELLO, WORLD!
print(lower_text)  # hello, world!
```

## str.capitalize() and str.title()

### capitalize() capitalizes the first letter of a string.

### title() capitalizes the first letter of each word in a string.

```py
phrase = "python programming is fun"
cap_phrase = phrase.capitalize()
title_phrase = phrase.title()
print(cap_phrase)   # Python programming is fun
print(title_phrase) # Python Programming Is Fun
```

## str.strip(), str.lstrip(), and str.rstrip()

### strip() removes leading and trailing whitespace.

### lstrip() removes leading whitespace.

### rstrip() removes trailing whitespace.

```py
sentence = "   Python is fun!   "
stripped_sentence = sentence.strip()
print(stripped_sentence)  # Python is fun!
```

## str.startswith(prefix) and str.endswith(suffix)

### Checks if a string starts or ends with a specified prefix or suffix.

```py
filename = "example.txt"
starts_with = filename.startswith("example")
ends_with = filename.endswith(".txt")
print(starts_with)  # True
print(ends_with)    # True
```

## str.replace(old, new)

### Replaces occurrences of a substring with another substring.

```py
sentence = "I like programming in Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)  # I like programming in Python.
```

## str.find(substring) and str.index(substring)

### find() returns the lowest index of the first occurrence of a substring.

### index() also returns the index of the first occurrence but raises an error if the substring is not found.

```py
phrase = "Python is powerful and Python is easy to learn."
index1 = phrase.find("Python")
index2 = phrase.index("Python")
print(index1)  # 0
print(index2)  # 0
```

## str.split(separator)

### Splits a string into a list of substrings based on a specified separator.

```py
sentence = "Python is a powerful programming language"
words = sentence.split(" ")
print(words) # ['Python', 'is', 'a', 'powerful', 'programming', 'language']
```

## str.join(iterable)

### Concatenates elements of an iterable (e.g., a list) into a string using the original string as a separator.

```py
words = ['Python', 'is', 'awesome']
sentence = ' '.join(words)
print(sentence)  # Python is awesome
```

## str.count(substring)

### Returns the number of occurrences of a substring in the string.

```py
sentence = "Python is easy. Python is fun. Python is powerful."
count_python = sentence.count("Python")
print(count_python)  # 3
```
