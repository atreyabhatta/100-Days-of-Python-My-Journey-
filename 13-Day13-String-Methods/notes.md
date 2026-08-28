# Day 13 — String Methods

## Overview

Today was a big one — a whole toolkit of built-in string methods for
modifying, checking, and searching within strings. Since strings are
**immutable** in Python, none of these methods change the original string
— they all return a *new* string (or a boolean/number).

## Case conversion

- `upper()` — converts to uppercase
- `lower()` — converts to lowercase
- `capitalize()` — capitalizes only the first character, rest lowercase
- `title()` — capitalizes the first letter of every word
- `swapcase()` — flips upper ↔ lower for every character

## Cleaning strings

- `strip()` — removes leading/trailing whitespace
- `rstrip(char)` — removes trailing occurrences of a given character
  (e.g. stripping extra `!` marks off the end of a string)
- `replace(old, new)` — replaces all occurrences of a substring
- `split(separator)` — splits a string into a list based on a separator

## Searching within a string

- `count(value)` — counts how many times a value appears
- `find(value)` — returns the index of the first occurrence, or `-1` if not found
- `index(value)` — same as `find()`, but raises an error if not found instead
  of returning `-1`
- `startswith(value)` / `endswith(value)` — checks if a string starts/ends
  with a given value (both also accept optional start/end index ranges)

## Checking string properties (boolean checks)

- `isalnum()` — True only if all characters are letters or digits
- `isalpha()` — True only if all characters are letters
- `islower()` / `isupper()` — checks case
- `isspace()` — True if the string is entirely whitespace
- `istitle()` — True if every word starts with a capital letter
- `isprintable()` — True if the string contains no non-printable characters
  (a `\n` newline, for example, makes it False)

## Formatting

- `center(width, fillchar)` — centers the string within a given width,
  padding with spaces or a custom character

## My takeaway

The `find()` vs `index()` distinction is worth remembering — `find()`
fails silently (`-1`), while `index()` raises an error. For real-world data
cleaning, `find()` is safer when I'm not sure the substring exists, since I
can check for `-1` instead of wrapping everything in a try/except.

This whole day feels directly useful for Data Science — cleaning messy
text data (extra whitespace, inconsistent casing, unwanted characters) is
exactly what these methods are built for.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
