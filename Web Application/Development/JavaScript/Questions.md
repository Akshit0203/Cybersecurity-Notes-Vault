# JavaScript Questions

> Core JavaScript concepts learned through building a "Guess the Number" game.

---

## Variables & Constants

### `let` — Declare Variables (value can change)

```javascript
let tries = 0;
let guess = 0;
```

### `const` — Declare Constants (value cannot change)

```javascript
const secret = Math.floor(Math.random() * 20) + 1;
```

| Keyword | Value Changes? | Use Case                    |
| ------- | -------------- | --------------------------- |
| `let`   | ✅ Yes         | Counters, user input, state |
| `const` | ❌ No          | Fixed values, config, imports |

---

## Generating Random Numbers

```javascript
const secret = Math.floor(Math.random() * 20) + 1; // 1–20
```

| Step               | What It Does                   | Example    |
| ------------------ | ------------------------------ | ---------- |
| `Math.random()`    | Random decimal `[0, 1)`        | `0.372`    |
| `* 20`             | Scale to `[0, 20)`             | `7.44`     |
| `Math.floor()`     | Round down (remove decimals)   | `7`        |
| `+ 1`              | Shift range from `0–19` to `1–20` | `8`     |

---

## Output with `console.log()`

```javascript
console.log("I'm thinking of a number between 1 and 20");
console.log("You got it in", tries, "tries!");  // multiple values separated by commas
```

---

## Reading User Input (Node.js)

Node.js doesn't wait for input by default — it's built for web servers, not CLI programs. You need the `readline` module to override this:

### Setup

```javascript
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });
```

| Line | What It Does |
| ---- | ------------ |
| `import readline` | Borrows the readline module (`/promises` = can pause and wait) |
| `import stdin/stdout` | Gets keyboard (input) and screen (output) |
| `createInterface()` | Creates the conversation channel between user and program |

### Reading Input

```javascript
const text = await rl.question("Take a guess: ");  // pauses until user types
guess = parseInt(text, 10);                          // convert string → integer
```

- `await` — pauses execution until the user responds
- `rl.question()` — displays a prompt and returns the user's text input
- `parseInt(text, 10)` — parses text into a base-10 integer

### Cleanup

Always close the readline interface when done:

```javascript
try {
    // ... game logic
} finally {
    rl.close();  // close the readline interface (like turning off a microphone)
}
```

- `try` — creates a safe block; if something goes wrong, the program won't crash
- `finally` — **always** runs, even if an error occurred — ensures cleanup happens

---

## Conditional Statements (`if / else if / else`)

Conditions are **mutually exclusive** — once one matches, the rest are skipped:

```javascript
if (guess < 1 || guess > 20) {
    console.log("That number is out of range. Try again.");
} else if (guess < secret) {
    console.log("Too low, try again.");
} else if (guess > secret) {
    console.log("Too high, try again.");
} else {
    console.log("You got it in", tries, "tries!");
}
```

| Operator | Meaning  |
| -------- | -------- |
| `<`      | Less than |
| `>`      | Greater than |
| `||`     | OR       |
| `!==`    | Not equal (strict) |

- `else if` — only checked if the previous condition was `false`
- `else` (alone) — runs when **all** previous conditions are `false`

---

## Loops (`while`)

Repeat a block of code **as long as** a condition is true:

```javascript
while (guess !== secret) {
    // keeps running until guess equals secret
}
```

- `!==` means "not equal" (strict comparison)
- The loop body runs **repeatedly** until the condition becomes `false`
- If the condition is `false` from the start, the body never runs

---

## Complete Program

```javascript
import * as readline from "node:readline/promises";
import { stdin as input, stdout as output } from "node:process";

const rl = readline.createInterface({ input, output });

try {
    const secret = Math.floor(Math.random() * 20) + 1; // 1 <= secret <= 20
    let tries = 0;
    let guess = 0;

    console.log("I'm thinking of a number between 1 and 20");

    while (guess !== secret) {
        const text = await rl.question("Take a guess: ");
        guess = parseInt(text, 10);

        tries = tries + 1;

        if (guess < 1 || guess > 20) {
            console.log("That number is out of range. Try again.");
        } else if (guess < secret) {
            console.log("Too low, try again.");
        } else if (guess > secret) {
            console.log("Too high, try again.");
        } else {
            console.log("You got it in", tries, "tries!");
        }
    }
} finally {
    rl.close();
}
```

### Sample Run

```
$ node guess_v3.js
I'm thinking of a number between 1 and 20
Take a guess: 10
Too low, try again.
Take a guess: 15
Too high, try again.
Take a guess: 14
You got it in 3 tries!
```

### How the Program Evolved

| Version | What It Added                  |
| ------- | ------------------------------ |
| v1      | Variables, constants, input    |
| v2      | Conditional feedback           |
| v3      | `while` loop (multiple guesses)|
| v4      | Further improvements (bonus)   |
