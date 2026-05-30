
### Boolean Expressions

In Python, boolean expressions are expressions that evaluate to either `True` or `False`. They are typically used in conditional statements and logical operations to make decisions based on the truth or falsity of certain conditions.

```
#Boolean expressions (True or False)

bool1 = True
bool2 = 3*3 == 9
bool3 = False
bool4 = 3*3 != 9

print(bool1,bool2,bool3,bool4)
print(type(bool1))
```

```
True True False False
<class 'bool'>
```

### Relational Operators

Relational operators are used to compare values and create boolean expressions. Here's an explanation of boolean expressions and relational operators in Python:

Python provides several relational operators to compare values. Here are the commonly used relational operators:

- Equality (`==`): Checks if two values are equal.
- Inequality (`!=`): Checks if two values are not equal.
- Greater than (`>`): Checks if the left value is greater than the right value.
- Less than (`<`): Checks if the left value is less than the right value.
- Greater than or equal to (`>=`): Checks if the left value is greater than or equal to the right value.
- Less than or equal to (`<=`): Checks if the left value is less than or equal to the right value.

```
# Relational and boolean operators
greater_than = 7 > 5
less_than = 5 < 7
greater_than_equal_to = 7 >=7
less_than_equal_to = 7 <= 7

test_and = True and True #True
test_and2 = True and False #False
test_or = True or True #True
test_or2 = True or False #True

test_not = not True #False
```


Boolean Expressions:

Boolean expressions are formed by combining relational expressions using logical operators. The logical operators in Python are:

- Logical AND (`and`): Returns `True` if both operands are `True`.
- Logical OR (`or`): Returns `True` if at least one operand is `True`.
- Logical NOT (`not`): Negates the value of the operand.

