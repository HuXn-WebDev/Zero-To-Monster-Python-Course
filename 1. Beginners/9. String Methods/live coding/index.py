# str.upper() and str.lower()
text = "Hello, World!"
upper_text = text.upper()
lower_text = text.lower()
print(upper_text)  # HELLO, WORLD!
print(lower_text)  # hello, world!

## str.capitalize() and str.title()
phrase = "python programming is fun"
cap_phrase = phrase.capitalize()
title_phrase = phrase.title()
print(cap_phrase)  # Python programming is fun
print(title_phrase)  # Python Programming Is Fun

## str.strip(), str.lstrip(), and str.rstrip()
sentence = "   Python is fun!   "
stripped_sentence = sentence.strip()
print(stripped_sentence)  # Python is fun!

## str.startswith(prefix) and str.endswith(suffix)
filename = "example.txt"
starts_with = filename.startswith("example")
ends_with = filename.endswith(".txt")
print(starts_with)  # True
print(ends_with)  # True

## str.replace(old, new)
sentence = "I like programming in Java."
new_sentence = sentence.replace("Java", "Python")
print(new_sentence)  # I like programming in Python.


## str.find(substring) and str.index(substring)
phrase = "Python is powerful and Python is easy to learn."
index1 = phrase.find("Python")
index2 = phrase.index("Python")
print(index1)  # 0
print(index2)  # 0

## str.split(separator)
sentence = "Python is a powerful programming language"
words = sentence.split(" ")
print(words)  # ['Python', 'is', 'a', 'powerful', 'programming', 'language']


## str.count(substring)
sentence = "Python is easy. Python is fun. Python is powerful."
count_python = sentence.count("Python")
print(count_python)  # 3
