# Day 5 — Comments, Escape Sequences & Print in Python

## Comments

Today's focus was on comments — parts of the code that Python simply
ignores when running. They're used to explain code to yourself (or anyone
else reading it later) or to temporarily disable a line while testing.

**Single-line comments** — start with `#`:
```python
# This is a single-line comment
print("This is a print statement.")
```

**Multi-line comments** — either repeat `#` on each line, or use a
triple-quoted string (`"""..."""`), which Python treats as a string literal
that isn't assigned to anything, so it's effectively ignored:
```python
"""
This explains the block below.
It runs an if-else check.
"""
p = 7
if p > 5:
    print("p is greater than 5.")
else:
    print("p is not greater than 5.")
```

I found it useful to think of comments as "notes for humans" — Python
itself doesn't care, but future-me (or anyone reviewing my code) definitely
will.

## Escape Sequence Characters

Some characters can't be typed directly inside a string — like a double
quote inside a string that's also wrapped in double quotes. That's where
**escape sequences** come in: a backslash `\` followed by the character
tells Python "treat this literally, don't break the string."

```python
print("This will \" execute")   # \" lets the quote print without ending the string
```

## More on the print() function

Learned today that `print()` has more going on than just printing text:

```python
print(object(s), sep=separator, end=end, file=file, flush=flush)
```

- **object(s)** — whatever you want to print (converted to string automatically)
- **sep** — how multiple objects are separated (default is a space `' '`)
- **end** — what gets printed at the end (default is a newline `\n`)
- **file** — where the output goes (default is the console / `sys.stdout`)

Only the first parameter (object) is required — the rest are optional but
useful for controlling exactly how output is formatted.

## My takeaway

This day felt like "small details that matter" — comments and print
formatting seem minor, but they directly affect how clean and readable code
looks, which matters a lot once projects get bigger.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
