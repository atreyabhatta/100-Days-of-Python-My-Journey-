# Day 7 — Exercise 1: Create a Calculator

## Arithmetic Operators

Before attempting the exercise, today's lesson covered Python's arithmetic
operators — the building blocks needed to actually build a calculator:

| Operator | Name | Example |
|---|---|---|
| `+` | Addition | `15 + 7` |
| `-` | Subtraction | `15 - 7` |
| `*` | Multiplication | `5 * 7` |
| `**` | Exponential | `5 ** 3` |
| `/` | Division | `5 / 3` |
| `%` | Modulus (remainder) | `15 % 7` |
| `//` | Floor Division (rounds down) | `15 // 7` |

The distinction between `/` and `//` was worth noting — `/` always returns a
float (decimal), while `//` returns an integer by rounding down. Similarly,
`%` gives just the remainder of a division, which is useful in a lot of
places (checking even/odd, cyclic patterns, etc.).

## The Exercise

**Task:** Build a calculator that performs addition, subtraction,
multiplication, and division on two numbers, with readable output
formatting.

I kept my version simple — taking two numbers as input and printing the
result of all four operations clearly labeled.

## My takeaway

This was the first "build something yourself" exercise in the course, and
it was a good gut-check on whether I actually understood operators and
`input()` handling, rather than just reading about them. Small exercise,
but it's the kind of thing that builds real muscle memory for writing
programs from a blank file.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
