# Lab1: Function with Multiple Return Values 
Write a function divide that takes two numbers and returns both the quotient and remainder when dividing the first by the second.
```python 
    quotient, remainder = divide(10, 3)
    print(quotient, remainder)  # Output: 3, 1
```

# Lab2: Function Arguments and Return Values
Write a function calculate_area that takes two arguments length and width and returns the area of a rectangle.

```python 
print(calculate_area(5, 10))  # Output: 50
```

# Lab 3: Variable-Length Arguments
Write a function sum_all that takes a variable number of arguments and returns their sum.

```python 
    print(sum_all(1, 2, 3, 4, 5))  # Output: 15
    print(sum_all())               # Output: 0
```

# Lab 4: Keyword and Positional-Only Arguments 
Write a function format_message that:

Takes a required positional-only argument msg
Accepts a keyword-only argument uppercase (default False)
If uppercase=True, return the message in uppercase. Otherwise, return it as is.

```python 
    print(format_message("hello"))          # Output: "hello"
    print(format_message("hello", uppercase=True))  # Output: "HELLO"
```


# challenges"
## Challenge 1: Most Frequent Word
Write a function most_frequent that takes a list of words and returns the word that appears most frequently.
```python 
print(most_frequent(["apple", "banana", "apple", "orange", "banana", "apple"]))
# Output: "apple"
```

🔹 Constraints: You cannot use built-in functions like Counter from collections.

## Challenge 2: Find the First Non-Repeating Character
Write a function first_unique_char that takes a string and returns the index of the first non-repeating character. If none exists, return -1.

```python
print(first_unique_char("leetcode"))  # Output: 0
print(first_unique_char("loveleetcode"))  # Output: 2
print(first_unique_char("aabb"))  # Output: -1
```