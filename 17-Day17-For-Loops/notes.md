# Day 17 — Introduction to Loops (For Loop)

## Why loops?

Loops let a group of statements run repeatedly without writing the same
code again and again. Python has two main types:

- `for` loop
- `while` loop

Today's focus was the `for` loop.

## The for loop

`for` loops iterate over a sequence of iterable objects — which basically
means anything that can be looped through: strings, lists, tuples, sets,
and dictionaries.

**Iterating over a string:**
```python
name = 'Abhishek'
for i in name:
    print(i, end=", ")
```
Output: `A, b, h, i, s, h, e, k,`

**Iterating over a list:**
```python
colors = ["Red", "Green", "Blue", "Yellow"]
for x in colors:
    print(x)
```

The same logic extends to sets and dictionaries too.

## range()

If I want to loop a specific number of times instead of iterating over an
existing sequence, `range()` is the tool for that.

```python
for k in range(5):
    print(k)
```
Output: `0 1 2 3 4` — by default `range()` starts at 0 and goes up to (but
not including) the number given.

`range()` can also take a start and end:
```python
for k in range(4, 9):
    print(k)
```
Output: `4 5 6 7 8`

## Quick Quiz — the third range() parameter

`range()` also accepts a third parameter — the **step** — which controls
how much to increment by on each iteration, instead of the default of 1.

```python
for k in range(1, 12, 3):
    print(k)
```
Output: `1 4 7 10` — it jumps by 3 each time instead of counting every
number.

## My takeaway

The step parameter in `range()` was the most useful discovery today — it
turns a `for` loop into a flexible counter (skip every nth item, count
backwards with a negative step, etc.) rather than just a simple 0-to-n
counter. Small addition, but it removes the need for extra logic inside
the loop just to skip values.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
