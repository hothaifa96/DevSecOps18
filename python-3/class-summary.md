Python Loops and List Operations Tutorial

Printing "Hello" Five Times

```python
c = 0
while c < 5:
    print('hello', c)
    c += 1
```

Using range() in Python

```python
print(list(range(10)))       # [0,1,2,3,4,5,6,7,8,9]
print(list(range(5,10)))     # [5,6,7,8,9]
print(list(range(0,10,2)))   # [0,2,4,6,8]
print(list(range(0,-10,-1))) # [0,-1,-2,-3,-4,-5,-6,-7,-8,-9]
```

Looping with for

```python
for n in range(5):
    print('hello', n)
```

Printing All Odd Numbers Between 0-100

# Using while loop

```python
x = 0
while x < 100:
    if x % 2 == 1:
        print(x)
    x += 1
```

# Using for loop

```python
for y in range(100):
    if y % 2 == 1:
        print(y)
```

# Using step in range

```python
for z in range(1, 100, 2):
    print(z)
```

Printing Multiples of 7 Up to 1000

```python
for x in range(0, 1000, 7):
    print(x)
```

Printing a Triangle

```python
s = 4
for r in range(4):
    for c in range(4):
        if c <= r:
            print('*', end='')
    print()
```

Alternative:

```python
for i in range(1, 5):
    print('*' * i)
```

Number Pattern

```python
for i in range(1, 10):
    print(f'{i}' * i)
```

Dog's Age Calculator

```python
human_years = int(input('Enter dog age in human years: '))
dog_years = 0
for year in range(1, human_years+1):
    if year <= 2:
        dog_years += 10.5
    else:
        dog_years += 4
print(f"The dog's age in dog years is {dog_years}")
```

Counting Occurrences of 'g' in a String

```python
word = 'google gugugle'
g_c = 0
for c in word:
    if c == 'g':
        g_c += 1
print(word.count('g'))  # Alternative method
print(g_c)
```

Counting Spaces in a User's Favorite Dish Name

```python
dish = input('Enter your favorite dish: ')
c = 0
for n in dish:
    if n == ' ':
        c += 1
print(f'The number of spaces is {c}')
```

PIN Verification System

```python
pin = '0140'
for i in range(3):
    user_pin = input('Enter your PIN: ')
    if user_pin == pin:
        print('Welcome home')
        break
else:
    print('You got it wrong')
```

Password Length Validation

```python
while True:
    password = input('Enter your password: ')
    if len(password) >= 10:
        break
    print('Short password, try again: ')
print('Pass')
```

Processing Odd and Even Numbers

```python
odds_sum = 0
even_multi = 1
while True:
    user_input = int(input('Enter a number: '))
    if user_input == 0:
        break
    if user_input % 2 == 0:
        even_multi *= user_input
    else:
        odds_sum += user_input
print(f'Odds sum: {odds_sum}')
print(f'Even multiplication: {even_multi}')
```

Working with Lists

```python
numbers = [100, 5, 8, 20, 18, 5]
print(numbers)

numbers.append(199)
numbers.insert(1, 99)
numbers[0] = 8888
numbers.append([1,2,3])
numbers.extend([1,2,3,4,5])
print(numbers)
```

Ex Names Collection

```python
exs = []
while True:
    name = input('Enter your ex's name: ')
    if name in exs:
        break
    if 'a' in name:
        exs.append(name)
print(exs)
```

Finding Maximum, Minimum, and Average in a List

```python
numbers = [100, 8, 15, 44, 22, 1776]

# Average
avg = sum(numbers) / len(numbers)
print(f'Average: {avg}')

# Maximum
print(f'Max: {max(numbers)}')

# Minimum
print(f'Min: {min(numbers)}')

Counting Numbers Divisible by 5

c = 0
for n in numbers:
    if n % 5 == 0:
        c += 1
print(c)

Printing First Half of a List

for n in numbers[:len(numbers)//2]:
    print(n)
```
