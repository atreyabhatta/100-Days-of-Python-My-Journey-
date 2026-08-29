# Day 16 — Match Case Statements

## What is match-case?

Python's `match` statement gives switch-case-like behavior, similar to what
languages like C, C++, or Java have. It compares a variable's value against
different "patterns" (called cases) until one fits.

The three main parts:
1. The `match` keyword
2. One or more `case` clauses (each holding a pattern to check)
3. The statements to run when a case matches

## Syntax

```python
match variable_name:
    case pattern1:
        # statement1
    case pattern2:
        # statement2
    case _:
        # default case, runs if nothing above matched
```

## Example

```python
x = 4
match x:
    case 0:
        print("x is zero")
    case 4 if x % 2 == 0:      # case with an extra condition
        print("x % 2 == 0 and case is 4")
    case _ if x < 10:           # catch-all with a condition
        print("x is < 10")
    case _:                      # default case (like "else")
        print(x)
```
Output: `x % 2 == 0 and case is 4`

The `case 4 if x % 2 == 0` syntax was the interesting part — a case can
combine matching a specific value *and* an additional condition together,
which gives it more flexibility than a plain switch-case in other
languages.

## My takeaway

`match`-`case` feels cleaner than writing long `if-elif-elif...` chains
when there are many possible values to check, especially once conditions
get combined with patterns. That said, it's still fundamentally doing the
same job as `if-else` — just with different, more readable syntax for
certain situations.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
