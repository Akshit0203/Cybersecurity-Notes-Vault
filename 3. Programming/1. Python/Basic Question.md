# Basic Questions

> Small practice programs and concepts explored while learning Python.

---
## Guess the Number Game

A beginner program where the computer picks a random number and the player guesses until they find it.

### Key Concepts Used

- `random.randint(a, b)` — pick a random integer between `a` and `b` (inclusive)
- `input()` — read user input (always returns a **string**)
- `int()` — convert string to integer
- `while` loop — repeat until a condition is met
- `if / elif / else` — conditional branching

### Code

```run-python
import random  # gives us tools for picking random numbers

secret = random.randint(1, 20)  # a <= secret <= b
tries = 0
guess = 0  # start with a value that cannot be the secret (since secret is 1..20)

print("I'm thinking of a number between 1 and 20")

# Repeat until the user guesses the secret number.
while guess != secret:
    text = input("Take a guess: ")  # input() returns text (a string)
    guess = int(text)  # convert the text to a number
    
    tries = tries + 1  # add 1 try

    # Give a hint using if / elif / else.
    if guess < 1 or guess > 20:
        print("That number is out of range. Try again.")
    elif guess < secret:
        print("Too low, try again.")
    elif guess > secret:
        print("Too high, try again.")
    else:
        print("You got it in", tries, "tries!")
```

### Q: Why does the secret number stay the same after each guess?

Because `random.randint(1, 20)` runs **once** — before the loop starts. The result is stored in `secret` and never reassigned.

- The `while` loop only re-runs the **body** (the indented code inside it)
- `secret = random.randint(1, 20)` is **outside** the loop, so it doesn't repeat

To make it change every turn, move it **inside** the loop:

```python
while guess != secret:
    secret = random.randint(1, 20)  # now picks a new number each turn
    # ... rest of the code
```

> **Rule:** A variable only changes when you **explicitly reassign** it. Python doesn't re-run previous lines automatically.
