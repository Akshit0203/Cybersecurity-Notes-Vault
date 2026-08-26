In Python, you can interact with the user and receive input using the `input()` function. The `input()` function allows you to prompt the user for input and receive the input as a string. Here's an explanation of user input in Python:

When using user input, keep in mind that it is a string by default.

```
# user input
x = input("Give me a number: ")
y = input("Give me another number: ")
print (x + y)
```

```
Give me a number: 2
Give me another number: 3
23
```

It gives 23 because we took input as a string not an integer
It does concatenation of a string
we have to forcefully convert it to integer

we'll do it when taking input itself

```
# user input
x = int(input("Give me a number: "))
y = int(input("Give me another number: "))
print (x + y)
```

```
Give me a number: 2
Give me another number: 3
5
```

or 

```
age = input("Enter your age: ")
age = int(age)  # Convert the input to an integer

print("You will be " + str(age + 1) + " next year.")
```

```
Enter your age: 3
You will be 4 next year.
```

### to input float values

```
# user input
x = float(input("Give me a number: "))
y = int(input("Give me another number: "))
print (x + y)
```

```
Give me a number: 2.2
Give me another number: 2
4.2
```




