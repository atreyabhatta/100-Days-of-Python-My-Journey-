# Day 10 — Taking User Input in Python

## The input() function

Today covered how to take input directly from the user using Python's
built-in `input()` function.

```python
variable = input()
```

Key thing to note — `input()` **always returns a string**, no matter what
the user types (even if they type a number). So if I need that value as an
integer or float, I have to explicitly typecast it — which connects
directly to what I learned on Day 9.

```python
variable = int(input())
variable = float(input())
```

## Displaying a prompt message

`input()` can also take a string argument, which gets displayed to the user
as a prompt — so it takes input and shows a message in one line:

```python
a = input("Enter the name: ")
print(a)
```
Output:


Enter the name: Taben
Taben


## My takeaway

This felt like a natural extension of Day 9's typecasting lesson — since
`input()` always returns a string, forgetting to convert it before doing
math (like adding two "numbers") would just concatenate them as text
instead of adding them. Good reminder that Python won't guess my intent
here — I have to be explicit.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
