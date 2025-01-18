# Python Lesson 1: Fundamentals

## 🟢 Print and Basic Output
The `print()` function is used to display output in Python.

```python
print("Hello, world!")  # Simple string output
print("Hello\nWorld!")   # Newline character
print("My name is\tHodi")  # Tab space
```

**Multiline Strings:**
```python
print('''Hello and welcome to DevSecOps course.
Today we are working and learning Python.''')
```

**String Repetition:**
```python
print("*" * 10)  # **********
```

---

## 🟢 Variables and Data Types

### **Variable Declaration**
Variables store data and can change throughout the program.

```python
age = 55
name = "Donald Trump"
print(age)  # 55
print(name)  # Donald Trump
```

### **Basic Data Types**
- `int` → Whole numbers: `1, -199, 66`
- `float` → Decimal numbers: `1.1, -0.95`
- `complex` → Complex numbers: `2+3j`
- `str` → Text: `"hello", 'Python'`
- `bool` → Boolean values: `True, False`

```python
x = 10
y = 5.5
z = True
name = "Alice"

print(type(x))  # int
print(type(y))  # float
print(type(z))  # bool
print(type(name))  # str
```

---

## 🟢 Type Casting (Converting Between Types)
We can convert between data types using:
- `int()`
- `float()`
- `str()`
- `bool()`

```python
num = "10"
print(int(num) + 5)  # 15 (Converted from str to int)

x = 5.99
print(int(x))  # 5 (float to int, removes decimal)

y = 100
print(str(y) + " dollars")  # "100 dollars" (int to str)
```

---

## 🟢 Arithmetic Expressions and Operators

| Operator | Meaning  | Example |
|----------|---------|---------|
| `+`  | Addition  | `10 + 5` → `15` |
| `-`  | Subtraction  | `10 - 5` → `5` |
| `*`  | Multiplication | `10 * 4` → `40` |
| `/`  | Division | `10 / 3` → `3.3333` |
| `//` | Floor Division | `10 // 3` → `3` |
| `%`  | Modulus (Remainder) | `10 % 3` → `1` |
| `**` | Exponentiation | `2 ** 3` → `8` |

```python
a = 10
b = 3

print(a + b)  # 13
print(a - b)  # 7
print(a * b)  # 30
print(a / b)  # 3.3333
print(a // b)  # 3
print(a % b)  # 1
print(2 ** 3)  # 8
```

### **Compound Assignment Operators**
```python
y += 6  # Same as y = y + 6
```

---

## 🟢 User Input
The `input()` function allows users to enter data.

```python
name = input("Please enter your name: ")
age = input("Enter your age: ")
print("Hello", name)
print("You are", age, "years old")
```

**Type Casting in Input:**
```python
x = int(input("What is your birth year? "))
print(f"You are {2025 - x} years old.")
```

---

## 🟢 Salary & Taxes Calculation (Example Problem)

```python
name = input("Enter your name: ")
salary = int(input(f"Enter your salary {name} [number only]: "))

taxes = salary * 0.18
fee = (salary - taxes) * 0.13

print(f"Your received salary: {salary}")
print(f"Salary after taxes and fees: {salary - taxes - fee}")
```

---

## 🟢 Strings: Slicing, Length, and Methods

### **Getting Length of a String**
```python
sen = "Cats AND dogs can't play along"
print(len(sen))  # Length of the string
```

### **String Methods**
| Method | Description | Example |
|--------|------------|---------|
| `upper()` | Converts to UPPERCASE | `"hello".upper()` → `"HELLO"` |
| `lower()` | Converts to lowercase | `"HELLO".lower()` → `"hello"` |
| `title()` | Capitalizes each word | `"hello world".title()` → `"Hello World"` |
| `count('x')` | Counts occurrences of `x` | `"banana".count('a')` → `3` |
| `find('x')` | Finds the first index of `x` | `"banana".find('a')` → `1` |

```python
sen = "cats AND dogs cant play along"
print(sen.upper())
print(sen.lower())
print(sen.title())
print(sen.count('a'))
print(sen.find('a'))
```

---

## 🟢 String Slicing

| Slice | Explanation | Example |
|-------|------------|---------|
| `s[:5]` | First 5 characters | `"Python"[:5]` → `"Pytho"` |
| `s[3:]` | From index 3 to end | `"Python"[3:]` → `"hon"` |
| `s[-3:]` | Last 3 characters | `"Python"[-3:]` → `"hon"` |
| `s[::-1]` | Reverse string | `"Python"[::-1]` → `"nohtyP"` |

```python
sen = "cats AND dogs cant play along"
print(sen[::-1])  # Reverse string
```

---

## 🟢 Extracting Email Domain
```python
email = input("Enter your email: ")
print(email[email.find("@") + 1:])  # Extract domain
```

---
## 🎯 Summary
- `print()` for output
- Variables and data types (`int`, `float`, `str`, `bool`)
- Type casting: `int()`, `float()`, `str()`
- Arithmetic operations
- `input()` for user input
- String slicing, `len()`, and methods

Would you like exercises or quizzes based on this? 🚀

