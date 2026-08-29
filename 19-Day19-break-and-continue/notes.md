# Day 19 — Break and Continue

## The break statement

`break` lets a program exit a loop immediately, skipping any remaining
iterations — it terminates the specific loop it's inside.

```python
for i in range(1, 101, 1):
    print(i, end=" ")
    if i == 50:
        break
    else:
        print("Mississippi")
print("Thank you")
```

The loop counts up printing "Mississippi" after each number, but as soon as
`i` hits 50, `break` stops the loop entirely — the counting never reaches
100.

## The continue statement

`continue` is different — instead of exiting the loop entirely, it skips
just the rest of the current iteration and moves straight to the next one.

```python
for i in [2, 3, 4, 6, 8, 0]:
    if i % 2 != 0:
        continue
    print(i)
```
Output: `2 4 6 8 0` — odd numbers get skipped (via `continue`), so only the
even numbers actually reach the `print()` line.

## My takeaway

The clearest way I found to remember the difference: `break` = "stop the
whole loop right now", `continue` = "skip just this one round, keep
going". Both are useful for adding exit/skip conditions to a loop without
having to restructure the whole loop's logic with nested if-else blocks.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
