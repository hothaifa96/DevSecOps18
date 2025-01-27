# Python `while` Loop

The `while` loop is used to execute a block of code as long as a given condition is `True`.

### Basic Syntax

```python
while condition:
    # Code block to execute
```

### Printing "Hello" 5 Times Using `while`

```python
c = 0
while c < 5:
    print('Hello', c)
    c += 1
```

### Printing Odd Numbers from 0 to 100

```python
x = 0
while x < 100:
    if x % 2 == 1:
        print(x)
    x += 1
```

### `while` Loop with `break`

```python
count = 0
while count < 5:
    if count == 3:
        break  # Stops the loop when count is 3
    print(count)
    count += 1
```

### `while` Loop with `continue`

```python
num = 0
while num < 5:
    num += 1
    if num == 3:
        continue  # Skips number 3
    print(num)
```

### Simulating `do-while` Loop in Python

Python does not have a built-in `do-while` loop like other languages. However, it can be simulated using a `while` loop with a `break` condition inside.

```python
while True:
    user_input = input("Enter 'exit' to stop: ")
    if user_input == 'exit':
        break
    print(f'You entered: {user_input}')
```

### Asking for a Password Until Correct

```python
correct_password = "python123"
while True:
    password = input("Enter your password: ")
    if password == correct_password:
        print("Access granted!")
        break
    print("Incorrect password, try again.")
```

---