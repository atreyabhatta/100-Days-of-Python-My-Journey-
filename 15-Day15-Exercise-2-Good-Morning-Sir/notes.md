# Day 15 — Exercise 2: Good Morning Sir

## The Task

Build a program that greets the user with "Good Morning", "Good Afternoon",
or "Good Evening" depending on the current time — using Python's `time`
module to get the current hour.

Sample reference for working with the `time` module:

```python
import time
timestamp = time.strftime('%H:%M:%S')
print(timestamp)
timestamp = time.strftime('%H')   # hour only
print(timestamp)
```

## My approach

I used `time.strftime("%H")` to fetch the current hour, then wrote an
if-elif-else chain (straight from Day 14) to decide the right greeting
based on which time bracket the hour falls into. I also added an
`input()` option to manually test different hour values without waiting
for the actual clock time to change — useful for checking all three
branches work correctly.

## My takeaway

This exercise combined two things I'd learned separately — conditionals
(Day 14) and modules (Day 3) — into one small but complete real-world-style
program. It's a good example of how individual concepts start connecting
into actual working logic once there are enough building blocks.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
