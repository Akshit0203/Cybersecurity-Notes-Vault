
![Pasted image 20251125200721.png](attachments/Pasted%20image%2020251125200721.png)

In Python, a list is a versatile and mutable data structure that can hold a collection of items. It allows you to store multiple values of different data types in a single variable.

### List

```run-python
# List have brackets [] and everything inside is called an item

movies = ["movie1","movie2","movie3","movie4"]

print(movies[1]) # return the second item in the list - index
print(movies[0])
print(movies[1:3]) #returns the first number given until right before the last number given
print(movies[0:4]) #return 0 to 4
print(movies[1:]) #returns 1 to end
print(movies[:1]) #everything before 1
print(movies[:2])
print(movies[-1]) # grabs the last item
print()

print(len(movies)) #count the items in the list
movies.append("movie9") # adds an item to the list
print(movies)
print()

movies.insert(2,"movie x")
print(movies)
print()

movies.pop() # remove an item from list ; by default last item if not specified
print(movies)
print()

movies.pop(0) #removes the first item
print(movies)
print()

amber_movies = ['Just Go With It', '50 First Dates']
our_favorite_movies = movies + amber_movies #combine lists
print(our_favorite_movies)
print()


```

```
movie2
movie1
['movie2', 'movie3']
['movie1', 'movie2', 'movie3', 'movie4']
['movie2', 'movie3', 'movie4']
['movie1']
['movie1', 'movie2']
movie4

4
['movie1', 'movie2', 'movie3', 'movie4', 'movie9']

['movie1', 'movie2', 'movie x', 'movie3', 'movie4', 'movie9']

['movie1', 'movie2', 'movie x', 'movie3', 'movie4']

['movie2', 'movie x', 'movie3', 'movie4']

['movie2', 'movie x', 'movie3', 'movie4', 'Just Go With It', '50 First Dates']
```

### Nested Lists

```run-python
grades = [["Bob",82], ["Alice",90], ["Jeff",73]] # Nested list , list within a list
bobs_grade = grades[0][1] #In first item of list print element 2
print(bobs_grade)
grades[0][1] = 83 #changed the values in the nested list
print(grades)
print()

nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print(nested_list[1][2])
```

```
82
[['Bob', 83], ['Alice', 90], ['Jeff', 73]]

6
```



List Creation:
To create a list, you enclose comma-separated values within square brackets `[ ]`. Here's an example:
```
fruits = ["apple", "banana", "orange"]
```

List Access:
You can access individual elements in a list using indexing. Indexing starts from 0 for the first element and goes up to the length of the list minus one. Here are some examples:
```
print(fruits[0])    # Output: "apple"
print(fruits[2])    # Output: "orange"
```

List Modification:
Lists are mutable, which means you can modify their elements. You can assign new values to specific positions in the list or use methods to modify the list itself. Here are some examples:
```
fruits[1] = "grape"     # Modifying an element
fruits.append("kiwi")   # Adding an element to the end
fruits.remove("apple")  # Removing an element
```

List Operations:
Python provides various operations that can be performed on lists. Some common operations include:
- Concatenation: You can use the `+` operator to concatenate two or more lists.
- Length: The `len()` function returns the number of elements in a list.
- Slicing: You can extract a sublist from a list using slicing.
- Iteration: You can use a loop to iterate over the elements of a list.

Here are some examples:
```
fruits = ["apple", "banana", "orange"]
fruits2 = ["grape", "kiwi"]

combined = fruits + fruits2
print(combined)         # Output: ["apple", "banana", "orange", "grape", "kiwi"]

print(len(fruits))      # Output: 3

sublist = fruits[1:3]
print(sublist)          # Output: ["banana", "orange"]

for fruit in fruits:
    print(fruit)        # Output: "apple", "banana", "orange"
```