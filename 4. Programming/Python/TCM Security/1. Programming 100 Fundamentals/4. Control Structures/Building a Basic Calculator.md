

```
#Building a calculator
x = float(input("Give me a number: "))
o = (input("Give me an operator: "))
y = float(input("Give me yet another number: "))

if o == "+":
    print(x+y)
elif o == "-" :
    print(x-y)
elif o == "/" :
    print(x/y)
elif o == "*" :
    print(x*y)
elif o == "**" or "^":
    print(x**y)
else :
    print("Unknown operator")
```

```
Give me a number: 2
Give me an operator: ^
Give me yet another number: 3
8.0
```




