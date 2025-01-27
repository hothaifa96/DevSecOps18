# Python `for` Loop 

The `for` loop in Python is used to iterate over sequences such as lists, tuples, strings, or ranges. It is useful when the number of iterations is known or can be determined in advance.

## Basic Syntax
```python
for variable in sequence:
    # Code block to execute
```

## Iterating Over a Range
```python
for i in range(5):  # Iterates from 0 to 4
    print(i)
```

```python
for i in range(2, 10, 2):  # Iterates from 2 to 8 with step 2
    print(i)
```

## Iterating Over a List
```python
fruits = ['apple', 'banana', 'cherry']
for fruit in fruits:
    print(fruit)
```

## Iterating Over a String
```python
word = "Python"
for letter in word:
    print(letter)
```

## Nested `for` Loops
```python
for i in range(3):
    for j in range(2):
        print(f'i={i}, j={j}')
```

## Using `for` with `break`
```python
for num in range(10):
    if num == 5:
        break  # Exits the loop when num is 5
    print(num)
```

## Using `for` with `continue`
```python
for num in range(5):
    if num == 2:
        continue  # Skips iteration when num is 2
    print(num)
```

## `for` with `else`
```python
for num in range(3):
    print(num)
else:
    print("Loop completed successfully")
```

## Using `for` to Find Maximum and Minimum in a List
```python
numbers = [10, 25, 3, 7, 99]
max_num = numbers[0]
for num in numbers:
    if num > max_num:
        max_num = num
print(f'Maximum: {max_num}')
```

## Counting Occurrences of a Character in a String
```python
word = 'banana'
count = 0
for char in word:
    if char == 'a':
        count += 1
print(f'Occurrences of "a": {count}')
```

---