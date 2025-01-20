# Python Logical Operators and If Statements Tutorial

## Logical Operators
Logical operators are used to combine conditional statements.

### Comparison Operators:
```python
is_hot = True
is_cold = False

print(3 > 6)  # False
print(8 >= 9)  # False

x = 8
y = 9
print(x >= y)  # False

x = int(input('Enter a number (0-9): '))
y = int(input('Enter another number (0-9): '))
print(x >= y)  # Comparison result
```

### Equality Operators:
```python
password = "P@ssw0rd!"
user_password = input('Enter your password: ')
print(password == user_password)  # True if passwords match, otherwise False
```

### Logical Operators:
```python
x = 5
y = 9
z = 8

print(x > y and x > z)  # False (x is not the maximum)
print(y > x or y > z)   # True (y is greater than at least one value)
print(y < x > z)        # True (x is greater than both y and z)
```

### Boolean Values:
```python
a1 = 0  # False
a2 = 1  # True
a3 = -77  # True
b1 = 0.0  # False
b2 = 66.199  # True
c1 = ''  # False
c2 = 'False'  # True

print(bool(c1))  # False
print(bool(c2))  # True
```

## If Statements
```python
is_gas_level_low = False

if is_gas_level_low:
    print('Fill the car up...')
else:
    print('Gas is ok...')
print('Car is on')
```

### Basic If-Else Statement:
```python
number1 = int(input('Enter a number: '))
number2 = int(input('Enter another number: '))

if number1 > number2:
    print(f'{number1} is greater')
else:
    print(f'{number2} is greater')
print('Adios')
```

### If-Elif-Else Statement:
```python
salary = int(input('Enter your salary: '))

if salary > 25000:
    tax = 0.4
elif salary > 10000:
    tax = 0.2
else:
    tax = 0.01

print(salary * (1 - tax))  # Salary after tax deduction
```
# Python If Statement Tutorial

## Introduction to If Statements

`if` statements allow conditional execution of code based on whether an expression evaluates to `True` or `False`.

### Basic If Statement

```python
is_raining = True
if is_raining:
    print("Take an umbrella!")
```

### If-Else Statement

```python
is_gas_level_low = False
if is_gas_level_low:
    print('Fill the car up...')
else:
    print('Gas is ok...')
print('Car is on')
```

### If-Elif-Else Statement

```python
salary = int(input('Enter your salary: '))
if salary > 25000:
    tax = 0.4
elif salary > 10000:
    tax = 0.2
else:
    tax = 0.01
print(salary * (1 - tax))  # Salary after tax deduction
```

## Nested If Statements

```python
age = int(input('Enter your age: '))
if age >= 18:
    print('You are an adult')
    if age >= 65:
        print('You are also a senior citizen')
else:
    print('You are a minor')
```

## Using Logical Operators with If Statements

```python
x = 5
y = 9
z = 8
if x > y and x > z:
    print("x is the greatest")
elif y > x and y > z:
    print("y is the greatest")
else:
    print("z is the greatest")
```

## Checking String Conditions

```python
password = input('Enter a password: ')
if len(password) >= 8:
    print('Password length is sufficient')
else:
    print('Password too short')
```

## Exercise: Temperature Checker

```python
temp = float(input('Enter the temperature: '))
if temp > 50:
    temp = (temp - 32) / 1.8  # Convert Fahrenheit to Celsius
if temp >= 30:
    print('What a hot day!')
else:
    print('Nice and cool!')
```


## Exercises
### Hot or Cool Day Checker
```python
temp = float(input('Enter the temp in your area: '))

if temp > 50:
    temp = (temp - 32) / 1.8  # Convert Fahrenheit to Celsius

if temp >= 30:
    print('What a hot day you got!')
else:
    print('Chill, man. It's a good day!')
```

### Golden Password Checker
A golden password must:
- Be between 10 and 16 characters long
- Contain exactly 3 occurrences of the letter 'a'
```python
password = input('Enter a password to check if it's golden: ')
if 16 >= len(password) >= 10 and password.count('a') == 3:
    print('Golden password')
```

## Math Module
Python provides a `math` module for advanced mathematical operations.
```python
import math
print(math.e)  # Euler's number
print(math.pi)  # Pi constant
print(math.sqrt(144))  # Square root of 144
print(144 ** (1/2))  # Alternative way to find the square root
```

### Additional Math Functions
```python
print(abs(-999))  # Absolute value: 999
print(round(6.6))  # Rounds to nearest integer: 7
print(round(1.2))  # Rounds to nearest integer: 1
print(round(-1.9)) # Rounds to nearest integer: -2
```

