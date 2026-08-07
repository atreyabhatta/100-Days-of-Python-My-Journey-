# Day 3 — Modules and Pip in Python

## What is a Module

Today's concept was about **modules** — basically a module is a piece of code
(written by someone else) that we can "borrow" and use in our own program,
instead of writing everything from scratch ourselves.

I learned there are two types:

1. **Built-in modules** — these come pre-packaged with Python itself. No
   installation needed, just import and use directly (e.g. `os`, `datetime`,
   `math`).
2. **External modules** — these are written by third parties and need to be
   installed separately using a package manager like `pip` or `conda`.
   Since these aren't part of core Python, different versions can exist and
   we can choose which one to install.

This actually connected well with something I already knew from my Physics
background — using external libraries is very similar to how we'd use
pre-built scientific tools instead of reinventing calculations every time.

## The pip command

`pip` is Python's package manager — used to install third-party modules.

Example — installing pandas (a library I'll be using a LOT for Data
Science later):

```bash
pip install pandas
```

## Using a module (import syntax)

Once installed, we bring a module into our code using `import`:

```python
import pandas

# Read and work with a file named 'words.csv'
df = pandas.read_csv('words.csv')
print(df)  # displays the first few rows of the CSV file
```

## My takeaway

This was a short but important lesson — modules are the reason Python is so
powerful for Data Science. Instead of writing data-handling logic from
scratch, libraries like `pandas`, `numpy`, and `scikit-learn` already do the
heavy lifting. Understanding `pip` properly today means I won't struggle
later when installing dependencies for bigger projects.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
