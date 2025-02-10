# Python OOP Practice Labs

## Lab 1: Book Library

Create a simple book management system.

### Requirements:

1. Create a `Book` class with the following attributes:

   - title
   - author
   - pages
   - is_borrowed (default False)

2. Implement the following methods:
   - `__init__` method to initialize the book
   - `__str__` method to return book details
   - `borrow_book()` method that changes is_borrowed to True
   - `return_book()` method that changes is_borrowed to False

### Tasks:

1. create the class
2. Create 3 different books
3. Borrow and return books
4. Print the status of each book

## Lab 2: Bank Account

Create a banking system with basic operations.

### Requirements:

1. Create a `BankAccount` class with:

   - account_holder
   - balance
   - account_number (generate randomly)

2. Implement methods for:
   - deposit
   - withdraw (with balance checking)
   - display_balance

### Tasks:

1. build
2. Create accounts for 2 people
3. Perform various transactions
4. Handle invalid operations (like withdrawing more than balance)

## Lab 3: Student Grade System

Create a grade management system for students.

### Requirements:

1. Create a `Student` class with:

   - name
   - student_id
   - courses (dictionary with course:grade pairs)

2. Implement methods for:
   - add_course
   - add_grade
   - calculate_gpa
   - display_report_card

### Tasks:

1. build the class
2. Add validation for grades (0-100)
3. Create multiple students with different courses
4. Generate a report card for each student

## lab 4 (challenge): Creating a Server Management System

Create a basic Server class to manage server instances with basic functionality like starting and stopping servers.

Create a Server class that should:

- Accept hostname and IP address when creating a new server instance
- Keep track of whether the server is running or not
- Include methods to start and stop the server

Create the Server class with:

- An **init** method that takes hostname and ip_address parameters
- A property to track if the server is running
- A start method that changes the server status to running
- A stop method that changes the server status to not running

Create two server instances

- Start one server
- Stop one server
- Print the status of both servers

for testing

```python
    web_server = Server("web-01", "192.168.1.100")
    db_server = Server("db-01", "192.168.1.101")
    # Start servers
    print(web_server.start())  # Should print: "Starting server web-01"

    # Stopping servers
    print(db_server.stop())    # Should print: "Stopping server db-01"
```

### Bonus Challenges

Add a method to check server status that returns a formatted string
Add validation for IP addresses in the **init** method
Add a method to restart the server
Add a last_started timestamp when the server is started
Add a method to display all server information
