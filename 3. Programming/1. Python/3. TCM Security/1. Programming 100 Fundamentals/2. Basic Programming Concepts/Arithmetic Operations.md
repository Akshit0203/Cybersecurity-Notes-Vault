```
#Math
print(50 + 50) #add
print(50 - 50) #subtract
print(50 * 50) #multiply
print(50 / 50) #divide
print(50 + 50 - 50 * 50 / 50) #PEMDAS
print(50 ** 2) #exponents
print(50 % 6) #modulo - takes what is left over
print(50 / 6) #division with decimals
print(50 // 6) #quotient



100
0
2500
1.0
50.0
2500
2
8.333333333333334
8
```


Math Operators:

- Addition (`+`): Adds two numbers.
- Subtraction (`-`): Subtracts one number from another.
- Multiplication (`*`): Multiplies two numbers.
- Division (`/`): Divides one number by another.
- Integer Division (`//`): Performs division and returns the quotient as an integer (rounds down).
- Modulo (`%`): Returns the remainder of division.
- Exponentiation (`**`): Raises a number to a power.


In Python, the `math` module is a built-in module that provides various mathematical functions and constants. It allows you to perform advanced mathematical operations in your Python programs. To use the `math` module, you need to import it first using the `import` statement. Here's an overview of some commonly used math functions and operators in Python:

Math Functions in the `math` Module:

- `math.sqrt(x)`: Calculates the square root of `x`.
- `math.pow(x, y)`: Raises `x` to the power of `y`.
- `math.exp(x)`: Calculates the exponential value of `x` (e^x).
- `math.log(x)`: Calculates the natural logarithm of `x` (base e).
- `math.log10(x)`: Calculates the logarithm of `x` to base 10.
- `math.sin(x)`, `math.cos(x)`, `math.tan(x)`: Calculate the sine, cosine, and tangent of `x`, respectively (where `x` is in radians).
- `math.degrees(x)`: Converts `x` from radians to degrees.
- `math.radians(x)`: Converts `x` from degrees to radians.

```
import math
x = 2
y = 3
print(math.pow(x,y))
print() 
# Using math functions 
print(math.sqrt(25)) # Output: 5.0 
print(math.pow(2, 3)) # Output: 8.0 
print(math.sin(math.pi/2)) # Output: 1.0 



8.0

5.0
8.0
1.0
```


