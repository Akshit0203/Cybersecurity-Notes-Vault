
```
# Functions - reusable block of code (mini program)
def who_am_i():
    name = "heath" #local variable
    age = 30
    print(f"My name is {name} and I am {age} years old")

who_am_i()
```

```
My name is heath and I am 30 years old
```


or we can manually input values every time

```
# Functions - reusable block of code (mini program)
def who_am_i(name,age):
    print(f"My name is {name} and I am {age} years old")

who_am_i("Heath",35)
```

```
My name is Heath and I am 35 years old
```


Examples :

```
def add_one_hundred(num):
    print(num + 100)

add_one_hundred(10)

def add(x,y):
    print(x + y)

add(2,3)

def multiply(x,y):
    return x * y # This will not print it , it will just return the value to be used for later
# used as an exit to the function and send a value back for calling

multiply(7,7)
print(multiply(7,7))

result1 = multiply(3,3)
result2 = multiply(2,2)
print(result1 + result2)


def square_root(x):
    print(x ** 0.5) # x to half power i.e square root

square_root(64)


def nl(): # new line
    print("\n")

nl()
```

```
110
5
49
13
8.0


```

