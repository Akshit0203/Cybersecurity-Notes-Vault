In Python, looping allows you to repeat a block of code multiple times.
## For loops

The `for` loop is used to iterate over a sequence (such as a list, tuple, string, or range) or any iterable object. It executes a block of code a fixed number of times, based on the elements or items in the sequence. Here's the general syntax:

```
for item in sequence:
    # code to be executed for each item in the sequence
```

Example:
```
fruits = ["apple", "banana", "orange"]
for fruit in fruits:
    print(fruit)
```

In this example, the `for` loop iterates over each item in the `fruits` list, and the block of code inside the loop (`print(fruit)`) is executed for each item. It will output:

```
apple
banana
orange
```

```run-python
# For loops - start to finish of an iterate
vegetables = ["cucumber" , "spinach" , "cabbage"]
for x in vegetables:
    print(x) # for x i.e all values in the array print x

print()

for i in range(5):
    print(i)

print()

word = "Python"
for x in word:
    print(x)
```


```
cucumber
spinach
cabbage

0
1
2
3
4

P
y
t
h
o
n
```

## While Loops

The `while` loop is used to repeatedly execute a block of code as long as a given condition is true. It continues looping until the condition becomes false. Here's the general syntax:
```
while condition:
    # code to be executed while the condition is true
```

Example:
```
count = 0
while count < 5:
    print(count)
    count += 1
```

In this example, the `while` loop will continue executing the code inside the loop (`print(count)`) as long as the condition `count < 5` is true. It will output:
```
0
1
2
3
4
```

Example 1 :

```
# While loops - execute as long as True
i = 1

while i <= 10:
    print(i)
    i += 1
```

```
1
2
3
4
5
6
7
8
9
10
```


Example 2 :

```
password = ""
while password != "spaghetti":
    password = input("Enter the secret password: ")

print("Access granted")
```

```
Enter the secret password: hello
Enter the secret password: passwd
Enter the secret password: spaghetti
Access granted
```


### Break and Continue 

The `break` and `continue` Statements:

Within loops, you can use the `break` statement to exit the loop prematurely and the `continue` statement to skip the current iteration and move to the next one.