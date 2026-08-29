# Day 20 — Python Functions

## What is a function?

A function is a reusable block of code that performs a specific task
whenever it's called. Instead of writing the same logic repeatedly, a
function lets that logic be written once and reused wherever needed — this
keeps larger programs organized and much easier to read.

There are two types of functions:

1. **Built-in functions** — already defined and pre-coded in Python. Things
   I've already been using without realizing they're "functions" —
   `min()`, `max()`, `len()`, `sum()`, `type()`, `range()`, `print()`, etc.
2. **User-defined functions** — functions I write myself to perform a
   specific task.

## Defining a function

```python
def function_name(parameters):
    # code and statements
    pass
```

- Starts with the `def` keyword, followed by the function name, parentheses
  `()`, and a colon `:`
- Any parameters go inside the parentheses
- Function naming follows the same rules as variable naming
- Everything inside the function must be indented

## Calling a function

```python
def name(fname, lname):
    print("Hello,", fname, lname)

name("Sam", "Wilson")
```
Output: `Hello, Sam Wilson`

## My takeaway

This is the point where I stopped just "learning syntax" and started
thinking about actual program structure — functions are what let a program
scale beyond a few lines without becoming unreadable. Realizing that things
like `print()` and `len()` are functions too (just built-in ones) also made
the whole concept click faster, since I was already using functions since
Day 1 without knowing the term for it.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
