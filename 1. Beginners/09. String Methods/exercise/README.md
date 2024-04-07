**Challenge 1: Case Conversions**

- Prompts the user to enter a sentence.
- Applies various string methods and prints the results:
  - `upper()`: Converts all characters to uppercase.
  - `lower()`: Converts all characters to lowercase.
  - `capitalize()`: Capitalizes the first letter and makes the rest lowercase.
  - `title()`: Capitalizes the first letter of each word.

**Challenge 2: Cleaning Up Text**

- Prompts the user to enter a sentence.
- Uses `strip()` method to remove leading and trailing spaces.
- Prints the trimmed sentence.

**Challenge 3: Checking String Start and End**

- Prompts the user to enter a string and a character.
- Uses `startswith()` to check if the string starts with the character.
- Uses `endswith()` to check if the string ends with the character.
- Prints messages based on the results.

**Challenge 4: Replacing Substrings**

- Prompts the user to enter a sentence and two words.
- Uses `replace()` method to replace the first (or all) occurrences of the first word with the second word.
- Prints the original and modified sentences.

**Challenge 5: Finding Substring Positions**

- Prompts the user to enter a sentence and a word.
- Uses `find()` to find the first occurrence of the word (returns -1 if not found).
- Uses `index()` to find the first occurrence of the word (raises ValueError if not found).
- Prints the index (if found by `find()`) and handles the potential `ValueError`.
- Demonstrates the difference between `find()` and `index()`.

**Challenge 6: Splitting and Joining Strings**

- Prompts the user to enter a sentence and a delimiter (e.g., comma or space).
- Uses `split()` method to split the sentence into a list based on the delimiter.
- Prints the list of words.
- Uses `join()` method to join the words back into a sentence using a different delimiter.
- Prints the rejoined sentence.

**Challenge 7: Counting Substring Occurrences**

- Prompts the user to enter a sentence and a character.
- Uses `count()` method to count the number of times the character appears in the sentence.
- Prints the count.
