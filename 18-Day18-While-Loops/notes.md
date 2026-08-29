# Day 18 — While Loops

## The while loop

A `while` loop runs its statements as long as a given condition stays
`True`. As soon as the condition becomes `False`, the loop exits.

```python
count = 5
while count > 0:
    print(count)
    count = count - 1
```
Output: `5 4 3 2 1`

Important thing to remember — the counter variable (`count` here) needs to
be incremented or decremented inside the loop, otherwise the condition
never becomes `False` and the loop runs forever.

## else with while

A `while` loop can also have an `else` block — it runs once the loop
condition becomes `False` and the loop exits normally (not via a `break`).

```python
x = 5
while x > 0:
    print(x)
    x = x - 1
else:
    print('counter is 0')
```
Output: `5 4 3 2 1 counter is 0`

## Do-while (emulated in Python)

Python doesn't have a built-in `do-while` loop like some other languages,
where the loop body runs at least once regardless of the condition, and
the condition is only checked at the end. To get similar behavior, an
infinite `while True` loop is combined with a `break` inside an `if`
condition:

```python
while True:
    number = int(input("Enter a positive number: "))
    print(number)
    if not number > 0:
        break
```

The trick here — `while True` makes it infinite by default, so the loop
always executes at least once. The `break` only fires once the condition
is checked, which mimics a do-while loop's "check at the end" behavior.

## My takeaway

The do-while emulation was the most interesting part today — it's a good
example of how Python doesn't need every construct built-in, since
existing tools (`while True` + `break`) can recreate the same behavior.
This pattern of "loop until a condition is met" is also very close to how
input validation usually works in real programs.

**Course reference:** [100 Days of Python — CodeWithHarry](https://www.youtube.com/watch?v=7wnove7K-ZQ&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg)
