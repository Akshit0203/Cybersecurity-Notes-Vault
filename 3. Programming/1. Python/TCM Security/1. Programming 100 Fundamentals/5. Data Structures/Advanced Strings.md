
Strings in Python are immutable, which means they cannot be changed after they are created.

Creation:
Example: `my_string = 'Hello, World!'` or `my_string = "Hello, World!"`

Accessing Characters:
You can access individual characters within a string using indexing, starting from 0.
Example: `print(my_string[0])` would output 'H'.

String Concatenation:
You can concatenate (join) two or more strings using the `+` operator.
Example: `greeting = 'Hello' + ' ' + 'World!'` would result in 'Hello World!'.

String Length:
The `len()` function can be used to determine the length (number of characters) of a string.
Example: `print(len(my_string))` would output the length of the string.

String Slicing:
You can extract a substring from a string using slicing, specifying the start and end indices.
Example: `substring = my_string[7:12]` would extract the substring 'World'.

String Methods:
Python provides various built-in methods to manipulate and transform strings. Examples include `upper()`, `lower()`, `strip()`, `split()`, `replace()`, and more.
Example: `print(my_string.upper())` would output 'HELLO, WORLD!'.

String Formatting:
String formatting allows you to embed values within a string. This can be done using the `%` operator or the `format()` method.
Example:
```
name = 'Alice'
age = 30
print("My name is %s and I'm %d years old." % (name, age))
# Output: My name is Alice and I'm 30 years old.
```

| Placeholder | Meaning                      | Example Value        |
| ----------- | ---------------------------- | -------------------- |
| **`%s`**    | string placeholder           | `"Alice"`, `"Hello"` |
| **`%d`**    | integer (number) placeholder | `30`, `100`, `5`     |
`(name, age)` are the actual values that will replace `%s` and `%d`



Examples :

```run-python
#Advanced Strings

my_name = "Heath"
print(my_name[0]) # first letter
print(my_name[-1]) #last letter

sentence = "This is a sentence."
print(sentence[:4])

print(sentence.split()) # delimiter - default is a space
#or
sentence_split = sentence.split()
sentence_join = ' '.join(sentence_split)
print(sentence_join) 
sentence_join = '-'.join(sentence_split)
print(sentence_join) 
```


```run-python
sentence = "192.168.138.1"
print(sentence.split('.'))

sentence_split = sentence.split('.')
sentence_join = '.'.join(sentence_split)
print(sentence_join)
```


```run-python
quote1 = "He said, 'give me all your money'"
quote2 = "He said, \"give me all your money\""
# the backslash '\' here means 'escape next character' , so the next character after it gets omitted rest all line stays same

print(quote1)
print(quote2)
```
so it means character escaping is possible


```run-python
too_much_space = "            hello      "
print(too_much_space.strip())
```


```run-python
print("A" in "Apple") #return true
print("a" in "Apple") #return false - case sensitive

letter = "A"
word = "Apple"
print(letter.lower() in word.lower())

user_input = input("Enter yes or no: ")
if user_input.lower().strip() == "yes": #important convert all characters to lower and strip of extra spaces
    print("You agree!")
else:
    print("You disagree!")
```


```run-python
movie = "The Hangover"
print("My favorite movie is {}.".format(movie))
print("My favorite movie is %s" %movie)
print(f"My favorite movie is {movie}.") #newer and best - to use
```

