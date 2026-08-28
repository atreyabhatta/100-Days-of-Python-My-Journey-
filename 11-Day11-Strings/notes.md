# Day 11 — Strings

## What are strings?

In Python, anything enclosed in single or double quotes is a string —
essentially a sequence of textual data. Strings are used whenever we're
working with text/Unicode characters.

```python
name = "Bunny"
print("Hello, " + name)
```
Output: `Hello, Bunny`

Good to know — it doesn't matter whether single or double quotes are used,
the output is identical either way.

## Handling quotes within a string

If a string itself contains a quotation mark, using the *other* type of
quote around it avoids conflicts. E.g., to print:
`He said, "I want to eat an apple".`

```python
print('He said, "I want to eat an apple".')
```

Using single quotes around the whole string lets the double quotes inside
it print without breaking anything.

## Multiline strings

Triple quotes (`"""..."""` or `'''...'''`) let a string span multiple
lines — useful for longer blocks of text, or text that naturally contains
line breaks and quotation marks together.

## Accessing characters (indexing)

A string behaves like an array of characters — each character has an
index, starting from **0**. Square brackets `[]` access a specific
character:

```python
print(name[0])   # 'B'
print(name[1])   # 'u'
```

Trying to access an index beyond the string's length (e.g. `name[5]` on a
5-letter string) throws an error, since there's nothing there.

## Looping through a string

Since a string is a sequence, a `for` loop can iterate over it character by
character:

```python
for character in name:
    print(character)
```

## My takeaway

The "string as an array of characters" mental model was the most useful
part of today — it explains why indexing and looping work the way they do.
This is also going to matter later for text cleaning/parsing tasks in Data
Science, where strings rarely come in a clean, ready-to-use format.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
