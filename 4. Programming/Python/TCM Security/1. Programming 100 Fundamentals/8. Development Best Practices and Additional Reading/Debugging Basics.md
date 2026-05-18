When you write code, it’s completely normal to make mistakes—that's part of the learning process! These mistakes are called **bugs**, and figuring out what went wrong and how to fix it is called **debugging**. In this lesson, we’re going to cover some simple ways to debug your Python code.

#### 1. **Using** `**print()**` **to See What’s Happening in Your Code**

One of the easiest ways to find bugs is by using the `print()` function. By printing out the values of variables, you can see if the program is doing what you expect at different stages.

#### Example:

```
def add_numbers(a, b):
    print(f"a: {a}, b: {b}")  # Printing the values of a and b
    return a + b

result = add_numbers(5, 3)
print(f"Result: {result}")
```

In this example, the `print()` statement inside the function will show you the values of `a` and `b` before they’re added together. You can use this to check if the values are what you expect.

**Why is this useful?**: If your program isn’t working, printing the values of variables lets you see where things might be going wrong. It’s a great way to understand how your code is behaving.

---

#### 2. **Commenting Out Code to Find Problems**

If you’re not sure where a bug is, you can **comment out** parts of your code to narrow it down. By temporarily disabling a section, you can figure out which part of the code is causing the issue.

#### Example:

```
def divide_numbers(a, b):
    # result = a / b  # This might be causing an error
    result = a // b   # Let's try integer division instead
    return result

print(divide_numbers(10, 2))

```
In this example, we commented out the line that might be causing a problem. We can test a different version of the code by using integer division (`//`) instead of regular division (`/`).

**Why is this useful?**: Commenting out parts of your code helps you test smaller sections at a time. This can make it easier to figure out exactly where something is going wrong.

---

#### 3. **Understanding Python’s Error Messages**

When your program has an error, Python will give you a **traceback**—a message that tells you where the error happened and what type of error it was. Learning to read these messages is an important skill.

#### Example:

```
def divide_numbers(a, b):
    return a / b

print(divide_numbers(10, 0))  # This will cause a ZeroDivisionError
```

If you try to divide by zero, you’ll get this error:

```
ZeroDivisionError: division by zero
```

The error tells you exactly what went wrong: you tried to divide by zero, which isn’t allowed in Python.

**Why is this useful?**: Error messages are your friend! They tell you what the problem is and where it happened in your code. Instead of being scared of errors, use them as clues to solve the problem.

---
#### 4. **Using** `**assert**` **to Test Your Code**

The `assert` statement is a simple way to check if something is true. If the condition you’re testing isn’t true, Python will stop the program and give you an error. You can use `assert` to make sure your variables have the correct values while your program is running.

#### Example:

```
def square_number(n):
    result = n * n
    assert result >= 0, "Result should never be negative"
    return result

print(square_number(5))
```

In this case, the `assert` checks that the result is never negative. If something goes wrong, Python will raise an error and stop the program.

**Why is this useful?**: `assert` helps you catch problems early by making sure that certain conditions are always true. This is great for catching mistakes in your code before they cause bigger issues.

---

#### 5. **Basic Debugging with Python's Built-in Debugger (**`**pdb**`**)**

Python comes with a built-in tool called **pdb** that lets you pause your program and step through it line by line. This might sound tricky, but you only need to know a couple of basic commands to get started.
#### Example:
```
import pdb

def add_numbers(a, b):
    pdb.set_trace()  # This is where the program will pause
    result = a + b
    return result

print(add_numbers(2, 3))
```

When the program reaches `pdb.set_trace()`, it will pause, and you can enter commands to inspect the program.

Here are some basic commands:
- `n` (next): Go to the next line of code.
- `p <variable>`: Print the value of a variable (e.g., `p a` to see the value of `a`).
- `c` (continue): Resume running the program.

**Why is this useful?**: Using `pdb` lets you check what’s happening in your program at each step, which makes it easier to find where things go wrong. It’s like pausing a movie to take a closer look at the details.

---

#### 6. **Using Debugging Tools in Your IDE**

If you’re using an IDE like **VSCode** or **PyCharm**, there are built-in tools that make debugging even easier. These tools let you set **breakpoints** (places where the program will pause), inspect variables, and step through the code—just like `pdb`, but with a graphical interface.

**How to set breakpoints in VSCode**:

1. Open your Python file.
2. Click next to the line numbers to add a breakpoint (a red dot will appear).
3. Run your program in "debug mode."
4. When the program hits the breakpoint, it will pause, and you can inspect what’s happening.

**Why is this useful?**: IDE debugging tools give you a visual way to see what’s going on in your code without needing to use print statements or manually check variables.

---

#### 7. **Common Python Errors**

Let’s look at some common Python errors and what they mean:

- **SyntaxError**: You might have missed a colon (`:`) or made a typo in your code.
- **TypeError**: You tried to do something with two incompatible types (like adding a string to a number).
- **IndexError**: You tried to access an index in a list that doesn’t exist.

#### Example of an `IndexError`:

```
my_list = [1, 2, 3]
print(my_list[5])  # This will raise an IndexError because index 5 doesn’t exist
```

**Why is this useful?**: Understanding these errors will help you fix them faster. Once you recognize what each error means, you’ll know exactly what to do.

---

### Final Tips for Debugging:

1. **Start with** `**print()**` to see what’s going on in your code.
2. **Comment out code** to figure out which part is causing the problem.
3. **Read error messages** carefully—they tell you what went wrong and where.
4. Use **assert** to check if your assumptions are correct.
5. **Learn to use basic debugging tools**, like `pdb` or your IDE’s built-in debugger.
6. **Familiarize yourself with common Python errors**, so you know how to fix them.

The more you practice debugging, the easier it gets. Mistakes are part of programming, and learning how to fix them is a big step toward becoming a better programmer.