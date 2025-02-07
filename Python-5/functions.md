## Introduction to Functions

Functions are a fundamental building block in Python programming. They allow you to encapsulate code into reusable blocks, making your code more modular, readable, and maintainable. In this tutorial, we will explore various aspects of Python functions, from basic definitions to advanced usage.

## Table of Contents

1. [Basic Function Definition](#basic-function-definition)
2. [Function Arguments and Return Values](#function-arguments-and-return-values)
3. [Default Arguments](#default-arguments)
4. [Variable-Length Arguments](#variable-length-arguments)
5. [Keyword Arguments](#keyword-arguments)
6. [Positional-Only and Keyword-Only Arguments](#positional-only-and-keyword-only-arguments)
7. [Docstrings and Function Documentation](#docstrings-and-function-documentation)
8. [Practical Examples](#practical-examples)


## Basic Function Definition

A function in Python is defined using the `def` keyword. The basic syntax is as follows:

```python
def function_name():
    # Function body
    pass
```

## Example: Simple Function
```python
def greet():
    print('Hello, World!')

greet()  # Output: Hello, World!
```

## Function Arguments and Return Values
Functions can take arguments and return values. Arguments are the inputs to the function, and the return value is the output.

Example: Function with Arguments and Return Value
```python
def add(a, b):
    return a + b

result = add(3, 5)
print(result)  # Output: 8
```

## Default Arguments
You can provide default values for function arguments. If the caller does not provide a value for that argument, the default value is used.

### Example: Default Arguments
```python
def greet(name="Guest"):
    print(f'Hello, {name}!')

greet()  # Output: Hello, Guest!
greet('Alice')  # Output: Hello, Alice!
```

## Variable-Length Arguments
Sometimes, you might want to define a function that can take a variable number of arguments. This can be achieved using *args for positional arguments and **kwargs for keyword arguments.

### Example: Variable-Length Arguments
```python
def print_args(*args):
    for arg in args:
        print(arg)

print_args(1, 2, 3)  # Output: 1 2 3

def print_kwargs(**kwargs):
    for key, value in kwargs.items():
        print(f'{key}: {value}')

print_kwargs(name='Alice', age=25)  # Output: name: Alice age: 25
```
## Keyword Arguments
Keyword arguments allow you to pass arguments by name, which can make your function calls more readable.

### Example: Keyword Arguments
```python
def greet(name, message):
    print(f'{message}, {name}!')

greet(name='Alice', message='Hello')  # Output: Hello, Alice!
```
## Positional-Only and Keyword-Only Arguments
Python allows you to specify that certain arguments must be passed positionally or as keywords.

### Example: Positional-Only and Keyword-Only Arguments
```python
def foo(a, b, /, c, *, d):
    print(a, b, c, d)

foo(1, 2, c=3, d=4)  # Output: 1 2 3 4
```

## Docstrings and Function Documentation
Docstrings are used to document functions. They are enclosed in triple quotes and provide a description of the function's purpose, arguments, and return values.

### Example: Docstrings
```python
def add(a, b):
    """
    This function adds two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b

print(add.__doc__)  # Output: This function adds two numbers...
```

## Practical Examples
### Example: Calculating Area and Perimeter
```python
import math

def calc_area(radius):
    return math.pi * radius ** 2

def calc_perimeter(radius):
    return 2 * math.pi * radius

radius = 5
print(f'Area: {calc_area(radius)}')  # Output: Area: 78.53981633974483
print(f'Perimeter: {calc_perimeter(radius)}')  # Output: Perimeter: 31.41592653589793
```

## Example: Checking if a Number is in Range
```python
def check_in_range(min_limit, max_limit, number):
    if max_limit < min_limit:
        print('Error: max_limit should be greater than min_limit')
        return False
    return min_limit < number < max_limit

print(check_in_range(10, 100, 50))  # Output: True
print(check_in_range(100, 10, 50))  # Output: Error: max_limit should be greater than min_limit
```

