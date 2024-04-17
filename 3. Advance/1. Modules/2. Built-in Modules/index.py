# The Python Standard Library 👇
# https://docs.python.org/3/library/index.html

from datetime import datetime

# date = datetime(year=2025, month=4, day=30, hour=5, minute=22, second=53)
# print(date)

# Shorthand 👇
date = datetime(2025, 4, 30, 5, 22, 53)
print(date)

# Getting a specific property
print(f"Year: {date.year}")
print(f"Month: {date.month}")
print(f"Day: {date.day}")
print(f"Hour: {date.hour}")
print(f"Minute: {date.minute}")
print(f"Second: {date.second}")

print(date.now())
print(date.day)
print(date.month)
