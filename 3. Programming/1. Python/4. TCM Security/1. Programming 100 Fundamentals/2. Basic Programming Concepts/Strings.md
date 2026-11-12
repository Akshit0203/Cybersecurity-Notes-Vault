
"#" - Good Practise to write comments so that people can review your code again

Strings in Python are immutable, which means they cannot be changed after they are created.

```
# Strings
print("hello world!")
print('hello world!') #can be printed in single quotes also
print("""This string runs 
multiple lines!""") #triple quote for multiple line
print("This is a "+"string!") #we can concatenate strings
print('\n')      #new line
print('Test that new line out')



Output:

hello world!
hello world!
This string runs
multiple lines!
This is a string!


Test that new line out
```


Creation:

- - Example: `my_string = 'Hello, World!'` or `my_string = "Hello, World!"`

Accessing Characters:

- - You can access individual characters within a string using indexing, starting from 0.
    - Example: `print(my_string[0])` would output 'H'.

String Concatenation:

- - You can concatenate (join) two or more strings using the `+` operator.
    - Example: `greeting = 'Hello' + ' ' + 'World!'` would result in 'Hello World!'.

String Length:

- - The `len()` function can be used to determine the length (number of characters) of a string.
    - Example: `print(len(my_string))` would output the length of the string.

String Slicing:

- - You can extract a substring from a string using slicing, specifying the start and end indices.
    - Example: `substring = my_string[7:12]` would extract the substring 'World'.

String Methods:

- - Python provides various built-in methods to manipulate and transform strings. Examples include `upper()`, `lower()`, `strip()`, `split()`, `replace()`, and more.
    - Example: `print(my_string.upper())` would output 'HELLO, WORLD!'.

### 🔹 **1. `upper()`**

Converts all characters in the string to **uppercase**.

**Example:**

`my_string = "Hello, World!" print(my_string.upper())`

**Output:**

`HELLO, WORLD!`

---

### 🔹 **2. `lower()`**

Converts all characters in the string to **lowercase**.

**Example:**

`print("Hello, World!".lower())`

**Output:**

`hello, world!`

---

### 🔹 **3. `strip()`**

Removes **leading and trailing spaces** (or specified characters).

**Example:**

`text = "   Python   " print(text.strip())`

**Output:**

`Python`

---

### 🔹 **4. `split()`**

Splits a string into a **list of substrings** based on a delimiter (default is space).

**Example:**

`msg = "apple banana cherry" print(msg.split())`

**Output:**

`['apple', 'banana', 'cherry']`

---

### 🔹 **5. `replace(old, new)`**

Replaces occurrences of a substring with a new substring.

**Example:**

`sentence = "I like Python" print(sentence.replace("like", "love"))`

**Output:**

`I love Python`


```
my_string = 'Hello, World!'
print(my_string[0])
print(len(my_string))
substring = my_string[7:12]
print(substring)
print(my_string.upper())



H
13
World
HELLO, WORLD!
```





String Formatting:

- - String formatting allows you to embed values within a string. This can be done using the `%` operator or the `format()` method.
    - You can also use f strings as shown in the example below
- Example:

```
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))
print(f"My name is {name} and I'm {age} years old.")
# Both will output: My name is Alice and I'm 30 years old.



My name is Alice and I'm 30 years old.
My name is Alice and I'm 30 years old.
```

## **String Formatting in Python**

String formatting allows you to **insert variables or values inside a string** without manually converting or concatenating them. Python provides multiple ways to do this.

## **1. Using the `%` Operator (Old Style)**

This is one of the earliest ways of formatting strings in Python.

- `%s` → inserts a string
    
- `%d` → inserts an integer
    
- `%f` → inserts a float
    

**Example:**

`name = 'Alice' age = 30 print("My name is %s and I'm %d years old." % (name, age))`

**Output:**

`My name is Alice and I'm 30 years old.`

---

## **2. Using the `format()` Method**

Introduced to make formatting more powerful and readable.

**Example:**

`print("My name is {} and I'm {} years old.".format(name, age))`

You can also number placeholders:

`print("My name is {0} and I'm {1} years old.".format(name, age))`

---

## **3. Using f-Strings (Recommended, Python 3.6+)**

This is the **most modern and preferred** method.  
It is very readable and faster.

**Example:**

`print(f"My name is {name} and I'm {age} years old.")`

**Output:**

`My name is Alice and I'm 30 years old.`

---

### ✔️ Why f-Strings Are Best

- More readable
    
- Faster performance
    
- Can evaluate expressions directly inside `{ }`
    

**Example:**

`print(f"In five years, Alice will be {age + 5} years old.")`


## 🔍 **Why the `f` is needed**

Without the `f`, Python will treat the string as a normal string and will not replace `{name}` with the actual value.

Example **without** `f`:

`name = "Alice" print("My name is {name}")`

Output:

`My name is {name}`

Example **with** `f`:

`print(f"My name is {name}")`

Output:

`My name is Alice`

---

## ✔️ What the `f` does

- Activates **expression evaluation** inside the string
    
- Allows Python to replace variables with their values
    
- Makes formatting clean and readable
    

You can even do math inside it:

`age = 30 print(f"In 5 years, Alice will be {age + 5} years old.")`

Output:

`In 5 years, Alice will be 35 years old.`




