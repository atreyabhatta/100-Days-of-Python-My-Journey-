# Day 12 — String Slicing & Operations on Strings

## Length of a String

Python's built-in `len()` function returns how many characters a string
contains.

```python
fruit = "Mango"
len1 = len(fruit)
print("Mango is a", len1, "letter word.")
```
Output: `Mango is a 5 letter word.`

## String as an array

Since a string is really a sequence of characters, I can access parts of it
using indexing — including a *range* of characters, not just one at a time.

```python
pie = "ApplePie"
print(pie[:5])   # Apple
print(pie[6])    # i - character at that specific index
```

## Slicing

This method of grabbing a portion of a string using a start:end index is
called **slicing**.

```python
pie = "ApplePie"
print(pie[:5])     # Slicing from the start -> Apple
print(pie[5:])     # Slicing till the end -> Pie
print(pie[2:6])    # Slicing in between -> pleP
print(pie[-8:])    # Slicing using negative index -> ApplePie
```

What clicked for me here — negative indices count backwards from the end of
the string (`-1` is the last character), which is really useful when I
don't know the exact length of a string but know roughly where I want to
slice from relative to the end.

## Looping through a string

Since strings are iterable, a `for` loop can go through each character:

```python
alphabets = "ABCDE"
for i in alphabets:
    print(i)
```

## My takeaway

Slicing feels like one of Python's most practical string features — instead
of manually looping to extract a substring, a single `[start:end]`
expression does it. This is going to come up constantly later when cleaning
messy text data (like stripping prefixes/suffixes from strings in a
dataset).

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
