
**Dictionaries are key/value pairs**

In Python, a dictionary is an unordered collection of key-value pairs. It is a versatile and powerful data structure that allows you to store, retrieve, and manipulate data based on unique keys.

```run-python
# Dictionaries - key/value pairs {}
drinks = {"White Russian": 8, "Old fashioned": 12, "Lemon Drop": 5} #drink is key , price is value
print(drinks)

employees = {"Finance": ["Bob", "Linda", "Tina"], "IT": ["Gene","Louise","Teddy"], "HR": ["Jimmy Jr.","Mort"]}
print(employees)
employees["Legal"] = ["Mr. Frond"] #add a new key value pair
print(employees)

employees.update({"Sales": ["Andie","Ollie"]}) #add a new key/pair value
print(employees)

drinks['White Russian'] = 9
print(drinks)

print(drinks.get("White Russian"))
```


```
{'White Russian': 8, 'Old fashioned': 12, 'Lemon Drop': 5}
{'Finance': ['Bob', 'Linda', 'Tina'], 'IT': ['Gene', 'Louise', 'Teddy'], 'HR': ['Jimmy Jr.', 'Mort']}
{'Finance': ['Bob', 'Linda', 'Tina'], 'IT': ['Gene', 'Louise', 'Teddy'], 'HR': ['Jimmy Jr.', 'Mort'], 'Legal': ['Mr. Frond']}
{'Finance': ['Bob', 'Linda', 'Tina'], 'IT': ['Gene', 'Louise', 'Teddy'], 'HR': ['Jimmy Jr.', 'Mort'], 'Legal': ['Mr. Frond'], 'Sales': ['Andie', 'Ollie']}
{'White Russian': 9, 'Old fashioned': 12, 'Lemon Drop': 5}
9
```



Dictionary Creation:
To create a dictionary, you enclose key-value pairs within curly braces `{ }`, separating each pair with a colon `:`. Here's an example:
```
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}
```

Dictionary Access:
You can access the values in a dictionary by referring to their corresponding keys. Keys provide a way to uniquely identify and retrieve values. Here's an example:
```
print(student["name"])   # Output: "Alice"
print(student["age"])    # Output: 20
```

Dictionary Modification:
Dictionaries are mutable, which means you can modify their values by assigning new values to specific keys. Here's an example:
```
student["age"] = 21       # Modifying a value
student["city"] = "London"    # Adding a new key-value pair
```

Dictionary Operations:
Python provides various operations that can be performed on dictionaries. Some common operations include:
- Length: The `len()` function returns the number of key-value pairs in a dictionary.
- Iteration: You can iterate over the keys, values, or key-value pairs of a dictionary using loops.
- Deletion: You can remove a key-value pair from a dictionary using the `del` keyword.

Examples:
```run-python
student = {
    "name": "Alice",
    "age": 20,
    "major": "Computer Science"
}


print(len(student))          # Output: 3


for key in student:
    print(key, student[key])  # Output: "name Alice", "age 20", "major Computer Science"


del student["age"]           # Deleting a key-value pair
```

