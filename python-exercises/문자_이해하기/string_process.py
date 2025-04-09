# string_process.py

# String manipulations
hello = "Hello"
world = "World"

# 1. Concatenate "Hello" and "World"
greeting = hello + " " + world
print(greeting)

# 2. Convert to uppercase
print(greeting.upper())

# 3. Slice "World" from "Hello World"
print(greeting[6:])

# 4. Split "Python is fun" by spaces
split_string = "Python is fun".split()
print(split_string)

# 5. Extract characters at even indices from "abcdef"
even_index_chars = "abcdef"[::2]
print(even_index_chars)

# 6. Repeat "Hello" three times
print(hello * 3)