# Day 14 — If-Else Conditionals

## Why conditionals matter

Today was about controlling the flow of a program based on whether an
expression evaluates to `True` or `False`. Depending on the result, the
program takes a different path. Conditional statements come in a few forms:

- `if`
- `if-else`
- `if-elif-else`
- nested `if-else`

## if...else

If the condition is `True`, the `if` block runs; otherwise, the `else`
block runs. Only one of the two executes.

```python
applePrice = 210
budget = 200
if applePrice <= budget:
    print("Alexa, add 1 kg Apples to the cart.")
else:
    print("Alexa, do not add Apples to the cart.")
```
Output: `Alexa, do not add Apples to the cart.`

## elif

When there's more than one condition to check, `elif` lets multiple
conditions be evaluated in sequence — the first one that's `True` runs, and
the rest are skipped.

```python
num = 0
if num < 0:
    print("Number is negative.")
elif num == 0:
    print("Number is Zero.")
else:
    print("Number is positive.")
```
Output: `Number is Zero.`

## Nested if statements

`if`/`elif`/`else` blocks can be placed inside one another to check
conditions within conditions — useful when a decision depends on more than
one layer of logic.

```python
num = 18
if num < 0:
    print("Number is negative.")
elif num > 0:
    if num <= 10:
        print("Number is between 1-10")
    elif num > 10 and num <= 20:
        print("Number is between 11-20")
    else:
        print("Number is greater than 20")
else:
    print("Number is zero")
```
Output: `Number is between 11-20`

## My takeaway

This is one of the most fundamental building blocks so far — almost every
useful program needs to make decisions based on data. Nested conditionals
in particular felt like a natural way to model "layered" real-world logic
(like the age-bracket example above), and I can already see how this
connects to things like data validation or filtering rows in a dataset
later on.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
