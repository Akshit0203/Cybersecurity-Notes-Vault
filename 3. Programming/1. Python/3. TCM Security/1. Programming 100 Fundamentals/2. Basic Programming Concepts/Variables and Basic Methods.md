Variables in Python are dynamically typed, meaning their data type can change during program execution.

A method is just basically a function.

```
# Variables and methods
age = 35 #int
name = "Heath" #string
gpa = 3.7 #float

print(int(age))
print(int(35.1))
print(int(35.9)) #It will not round off

quote = "All is fair in love and war."
print(quote)

print(quote.upper()) #uppercase
print(quote.lower()) #lowercase
print(quote.title()) #title case
print(len(quote)) #count characters

# print("My name is "+name+" and I am "+age+" years old.") # wont work
# TypeError: can only concatenate str (not "int") to str
print("My name is "+name+" and I am "+str(age)+" years old.") # have to forcefully convert it to string

age += 1
print(age)

birthday = 1
age += birthday
print(age)
```

```
35
35
35
All is fair in love and war.
ALL IS FAIR IN LOVE AND WAR.
all is fair in love and war.
All Is Fair In Love And War.
28
My name is Heath and I am 35 years old.
36
37
```

```
# Variable assignment
x = 10
name = "John"
is_true = True


# Variable usage
y = x + 5
print("Hello, " + name)
if is_true:
    print("The condition is true")
```

```
Hello, John
The condition is true
```

A method is a block of reusable code that performs a specific task or action. Methods are associated with objects or classes and are called upon to perform certain operations. In Python, methods are commonly referred to as functions. Built-in functions and user-defined functions both fall under the category of methods.

```
# Built-in method example
numbers = [1, 2, 3, 4, 5]
length = len(numbers)
print("Length:", length)


# User-defined method example
def greet(name):
    print("Hello, " + name)


greet("Alice")
```

```
Length: 5
Hello, Alice
```

Variables and methods are essential components in Python programming. Variables store data, while methods encapsulate reusable blocks of code for specific tasks.