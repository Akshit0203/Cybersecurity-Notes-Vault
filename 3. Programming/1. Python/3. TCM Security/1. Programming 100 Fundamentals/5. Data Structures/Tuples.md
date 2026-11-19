
not used much 

In Python, a tuple is an ordered collection of elements, similar to a list. However, unlike lists, tuples are immutable, meaning their elements cannot be modified once they are created.

A **tuple** in Python is _immutable_, meaning:

- ❌ You cannot add items
    
- ❌ You cannot remove items
    
- ❌ You cannot modify items
    
- ❌ You cannot reorder items
    

Since `.pop()` removes the last item from a list, Python **does not allow it** on tuples.

```run-python
# Tuples - immutable (cannot be changed) - ()
coordinates = (40.7128, 74.0060) #New york - fixed
red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
student = ("John Doe", 8675309 , "Computer Science" )
print(student[1])

# student.pop() - doesnt work since we cannot change the data
```

```
8675309
```


Tuple Creation:
To create a tuple, you enclose comma-separated values within parentheses `( )`. Here's an example:
```
fruits = ("apple", "banana", "orange")
```

Tuple Access:
You can access individual elements in a tuple using indexing, similar to lists. Indexing starts from 0 for the first element. Here are some examples:
```
print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"
```

Tuple Immutability:
Tuples are immutable, meaning you cannot modify their elements. Once a tuple is created, its values cannot be changed. For example, attempting to assign a new value to an element will result in an error. Here's an example:
```
fruits[1] = "grape"    # This will raise an error
```

Tuple Operations:
Although tuples are immutable, you can perform certain operations on them:
- Concatenation: You can use the `+` operator to concatenate two or more tuples.
- Length: The `len()` function returns the number of elements in a tuple.
- Slicing: You can extract a subtuple from a tuple using slicing.

```
fruits = ("apple", "banana", "orange")
fruits2 = ("grape", "kiwi")

combined = fruits + fruits2
print(combined)         # Output: ("apple", "banana", "orange", "grape", "kiwi")

print(len(fruits))      # Output: 3

subtuple = fruits[1:3]
print(subtuple)         # Output: ("banana", "orange")
```

Tuples are useful in situations where you want to store a collection of values that should not be changed.