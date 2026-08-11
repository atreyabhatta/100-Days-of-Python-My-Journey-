# Day 6 — Variables and Data Types

## What is a variable?

A variable is basically a container that holds data — Harry compared it to
kitchen containers that hold sugar, salt, etc., which is honestly a great
way to think about it. Creating a variable is as simple as creating a
placeholder in memory and assigning it a value:

```python
a = 1
b = True
c = "Ran"
d = None
```

These four lines create four variables, each holding a different type of
data — an integer, a boolean, a string, and `None` (no value).

## What is a Data Type?

A data type tells Python what kind of value a variable is holding — this
matters because different operations only make sense for certain types
(you can't do arithmetic on a string the same way you would on a number,
for example). Python has a built-in `type()` function to check this:

```python
a = 1
print(type(a))   # <class 'int'>

b = "1"
print(type(b))   # <class 'str'>
```

## Built-in data types I learned today

**1. Numeric data:** `int`, `float`, `complex`
- int → `3`, `-8`, `0`
- float → `7.349`, `-9.0`, `0.0000001`
- complex → `6 + 2i` (this one felt familiar from Physics — complex numbers
  show up a lot in wave equations)

**2. Text data:** `str` → e.g. `"Hello World!!!"`

**3. Boolean data:** just `True` or `False`

**4. Sequenced data:** `list` and `tuple`
- **List** — ordered, and *mutable* (can be changed after creation):
```python
list1 = [8, 2.3, [-4, 5], ["apple", "banana"]]
print(list1)
# [8, 2.3, [-4, 5], ['apple', 'banana']]
```
- **Tuple** — ordered, but *immutable* (cannot be changed once created):
```python
tuple1 = (("parrot", "sparrow"), ("Lion", "Tiger"))
print(tuple1)
# (('parrot', 'sparrow'), ('Lion', 'Tiger'))
```

**5. Mapped data:** `dict` — stores key-value pairs, useful for representing
structured data like a small record:
```python
dict1 = {"name": "Sakshi", "age": 20, "canVote": True}
print(dict1)
# {'name': 'Sakshi', 'age': 20, 'canVote': True}
```

## My takeaway

The list-vs-tuple mutability difference was the most useful thing to
internalize today — I can already see why that distinction matters once
data shouldn't be accidentally changed (tuples) versus data that needs to
be updated as a program runs (lists). This also cleared up why Python feels
so flexible — a single variable isn't locked into one data type forever.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
