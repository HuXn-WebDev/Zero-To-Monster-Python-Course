# open()

### The open() function is used to open a file and return a corresponding file object. It is a built-in function that takes two arguments: the file (path) and the (mode) in which to open the file (e.g., read mode, write mode, append mode, etc.).

# close()

# Close function is used to close a file.

# With Statement

# "with" statement is also use to open a file, but when we open a file with "with" statement there is no need to close the file explicitly.

## File Modes

#### r 👉: Read mode. Opens a file for reading only. The file pointer is placed at the beginning of the file.

#### w 👉: Write mode. Opens a file for writing only. Overwrites the file if the file exists. If the file does not exist, creates a new file for writing.

#### a 👉: Append mode. Opens a file for appending data. The file pointer is at the end of the file if the file exists. If the file does not exist, it creates a new file for writing.

#### b 👉: Binary mode. Opens the file in binary mode, which is used for non-text files (e.g., images, videos).

#### + 👉: Read and Write mode. Opens a file for both reading and writing.
