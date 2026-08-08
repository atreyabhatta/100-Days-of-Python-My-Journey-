# Single-line comment example
print("This is a print statement.")

"""
Multi-line comment example using a triple-quoted string.
This block explains the if-else check below.
"""
p = 7
if p > 5:
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")

# Escape sequence example - printing a double quote inside a double-quoted string
print("This will \" execute")

# print() with custom sep and end parameters
print("Python", "is", "fun", sep="-")          # custom separator
print("No newline here", end=" ")               # custom end (no line break)
print("continues on the same line")
