# Day 9 — Typecasting in Python

## What is Typecasting?

Typecasting (or type conversion) means converting one data type into
another. Python provides a bunch of built-in functions for this — `int()`,
`float()`, `str()`, `ord()`, `hex()`, `oct()`, `tuple()`, `set()`, `list()`,
`dict()`, etc.

There are two types of typecasting:

1. **Explicit Conversion**
2. **Implicit Conversion**

## Explicit Typecasting

This is when I (the programmer) manually convert a value from one type to
another using a built-in function — Python doesn't do this on its own.

```python
string = "15"
number = 7
string_number = int(string)   # throws an error if the string isn't a valid integer
total = number + string_number
print("The Sum of both the numbers is: ", total)
```
Output: `The Sum of both the numbers is 22`

The important catch here — `int()` will throw an error if the string isn't
actually a valid number (e.g. `int("hello")` would fail). So explicit
conversion needs a bit of care about what data is actually being converted.

## Implicit Typecasting

This is when Python automatically converts a smaller/lower data type into
a bigger/higher one during an operation — without me having to do anything
manually. Python does this to avoid losing data (e.g. converting an `int`
to a `float` instead of the other way around, since a float can hold more
precision).

```python
a = 7
print(type(a))     # <class 'int'>

b = 3.0
print(type(b))     # <class 'float'>

c = a + b           # int + float -> Python auto-converts to float
print(c)             # 10.0
print(type(c))      # <class 'float'>
```

## My takeaway

The key distinction that stuck with me: **explicit = I decide**, **implicit
= Python decides (safely, to avoid data loss)**. This is going to matter a
lot later when working with real datasets in Data Science — knowing whether
a value is being silently converted (implicit) or needs to be manually
cleaned/cast (explicit) is exactly the kind of thing that causes subtle
bugs if ignored.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
