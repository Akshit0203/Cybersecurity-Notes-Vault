
if condition1:
    # code to be executed if condition1 is true
elif condition2:
    # code to be executed if condition1 is false and condition2 is true
else:
    # code to be executed if all conditions are false
### Example 1 :
```run-python
# Conditional statements (if/else)
def drink(money):
    if money >= 2:
        return "You've got yourself a drink"
    else:
        return "No drink for you!"
    
print(drink(3))
print(drink(1))
```

```
You've got yourself a drink
No drink for you!
```

### Example 2 :
```run-python
def alcohol(age,money):
    if (age>=21) and (money>=5):
        return "we're getting a drink"
    elif (age>=21) and (money<5):
        return "Come back with more money"
    elif (age<21) and (money>=5):
        return "nice try kid!"
    else:
        return "Your too young and too poor"
    
print(alcohol(21,5))
print(alcohol(21,4))
print(alcohol(20,5))
print(alcohol(20,4))
```

```
we're getting a drink
Come back with more money
nice try kid!
Your too young and too poor
```

