# Python Object-Oriented Programming Tutorial

## Introduction to Classes and Objects
Object-Oriented Programming (OOP) is a programming paradigm that organizes code into objects, which are instances of classes. In DevOps, OOP is particularly useful for:
- Creating reusable infrastructure components
- Modeling cloud resources
- Building automation tools
- Managing configuration

### Key OOP Concepts
- **Classes**: Blueprints for creating objects
- **Objects**: Instances of classes
- **Attributes**: Data stored in objects
- **Methods**: Functions that belong to objects


## Class Definition and Basic Structure
A class is a blueprint for creating objects. Here's a basic example:

```python
class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
```

- The `class` keyword is used to define a class
- `__init__` is a special method (constructor) that initializes class attributes
- `self` refers to the instance being created

## Creating Objects (Instances)
Objects are instances of a class. You can create them like this:

```python
# Creating a single employee
emp5 = Employee(salary=10000, name='hodi')

# Creating multiple employees from user input
employees = []
for i in range(3):
    while True:
        name = input('please enter the employee name:')
        if name == '' or name.isdigit() or name.isspace():
            continue
        salary = input('enter salary (numbers)')
        if salary.isdigit():
            salary = int(salary)
        else:
            continue
        emp = Employee(name, salary)
        employees.append(emp)
        break
```

## Methods and String Representation
Classes can have methods (functions) that define behavior. The `__str__` method provides a string representation of the object.

```python
class Dog:
    def __init__(self, name, age, breed):
        self.name = name
        self.age = age
        self.breed = breed

    def bark(self):
        if self.age > 3:
            print(f'{self.name} says : whrooph wrooooph')
        else:
            print(f'{self.name} says : howw howww')

    def __str__(self):
        return f'from Class Dog<< name-{self.name} age-{self.age}>>'

# Creating and using Dog objects
dog1 = Dog('jojo', 4, 'husky')
dog2 = Dog('pita', 3, 'nakniik')
```

## Working with Class Methods and Calculations
Classes can include methods that perform calculations:

```python
import math

class Point:
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color
        self.distance = self.calc_distance()

    def __str__(self):
        return f'({self.x},{self.y}) with the color -> {self.color}'
    
    def calc_distance(self):
        dis = math.sqrt(self.x**2 + self.y**2)
        return dis

# Using the Point class
p1 = Point(3, 6, 'black')
p2 = Point(9, 1, 'white')
```

## Class Variables vs Instance Variables
Class variables are shared among all instances, while instance variables are unique to each instance.

```python
class Circle:
    # Class variables
    r = 5
    color = 'Black'

# Creating instances
c1 = Circle()
c2 = Circle()

# Modifying instance variables
c1.r = 103  # This creates a new instance variable for c1
c2.border = 'dotted'  # Adding a new instance variable to c2

print(f'c1.r -> {c1.r}')  # 103
print(f'c2.r -> {c2.r}')  # 5 (original class variable)
```

## Instance Variable Behavior
When you modify an instance variable, it doesn't affect other instances or the class variable:

```python
class Rectangle:
    a = 4
    b = 2

r1 = Rectangle()
r2 = Rectangle()

# Modifying instance vs class variables
r1.b = 10  # Creates instance variable for r1
Rectangle.b = 100  # Modifies class variable

print(r1.b)  # 10 (instance variable)
print(r2.b)  # 100 (class variable)
```

## Key Points to Remember
1. Class variables are shared among all instances
2. Instance variables are unique to each instance
3. The `__init__` method initializes instance attributes
4. The `__str__` method provides string representation
5. Instance methods can access instance variables using `self`
6. Creating an instance variable doesn't affect other instances

## Best Practices
- Use meaningful class and variable names
- Initialize all instance variables in `__init__`
- Use instance variables for unique object properties
- Use class variables for properties shared by all instances
- Include appropriate validation in your methods
- Document your classes and methods