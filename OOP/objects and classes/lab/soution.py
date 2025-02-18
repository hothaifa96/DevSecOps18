# Lab 1: Book Library

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        self.is_borrowed = False

    def __str__(self):
        return f"Title: {self.title}, Author: {self.author}, Pages: {self.pages}, Borrowed: {self.is_borrowed}"

    def borrow_book(self):
        self.is_borrowed = True

    def return_book(self):
        self.is_borrowed = False

# Tasks for Lab 1
book1 = Book("The Hitchhiker's Guide to the Galaxy", "Douglas Adams", 224)
book2 = Book("Pride and Prejudice", "Jane Austen", 432)
book3 = Book("To Kill a Mockingbird", "Harper Lee", 281)

book1.borrow_book()
book2.return_book()

print(book1)
print(book2)
print(book3)


# Lab 2: Bank Account
import random

class BankAccount:
    def __init__(self, account_holder, balance=0):
        self.account_holder = account_holder
        self.balance = balance
        self.account_number = random.randint(1000000000, 9999999999) # Random 10-digit account number

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds!")
        else:
            self.balance -= amount

    def display_balance(self):
        print(f"Account balance for {self.account_holder}: ${self.balance}")

# Tasks for Lab 2
account1 = BankAccount("Alice", 1000)
account2 = BankAccount("Bob")

account1.deposit(500)
account2.withdraw(200)  # Will print "Insufficient funds!"
account1.withdraw(700)

account1.display_balance()
account2.display_balance()


# Lab 3: Student Grade System

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.courses = {}

    def add_course(self, course):
        self.courses[course] = None  # Initialize with no grade yet

    def add_grade(self, course, grade):
        if 0 <= grade <= 100:
            self.courses[course] = grade
        else:
            print("Invalid grade. Must be between 0 and 100.")

    def calculate_gpa(self):
        if not self.courses:
            return 0  # Handle case with no courses
        total_grades = sum(self.courses.values())
        return total_grades / len(self.courses)

    def display_report_card(self):
        print(f"Report Card for {self.name} (ID: {self.student_id})")
        for course, grade in self.courses.items():
            print(f"- {course}: {grade if grade is not None else 'N/A'}")  # Handle ungraded courses
        print(f"GPA: {self.calculate_gpa():.2f}")

# Tasks for Lab 3
student1 = Student("Charlie", "12345")
student2 = Student("David", "67890")

student1.add_course("Math")
student1.add_course("Science")
student1.add_grade("Math", 85)
student1.add_grade("Science", 92)

student2.add_course("English")
student2.add_course("History")
student2.add_grade("English", 78)
student2.add_grade("History", 95)


student1.display_report_card()
student2.display_report_card()


# Lab 4: Server Management System (Challenge)
import re
import datetime

class Server:
    def __init__(self, hostname, ip_address):
        self.hostname = hostname
        if not self._validate_ip(ip_address):
            raise ValueError("Invalid IP address format.")
        self.ip_address = ip_address
        self._running = False  # Private attribute for status
        self.last_started = None

    @property
    def running(self):
        return self._running

    def start(self):
        if not self._running:
            self._running = True
            self.last_started = datetime.datetime.now()
            return f"Starting server {self.hostname}"
        return f"Server {self.hostname} is already running"

    def stop(self):
        if self._running:
            self._running = False
            return f"Stopping server {self.hostname}"
        return f"Server {self.hostname} is already stopped"

    def check_status(self):
        status = "running" if self._running else "stopped"
        return f"Server {self.hostname} ({self.ip_address}) is {status}"

    def restart(self):
        self.stop()
        return self.start()

    def display_info(self):
        status = "running" if self._running else "stopped"
        last_started_str = self.last_started.strftime("%Y-%m-%d %H:%M:%S") if self.last_started else "Never"
        return (f"Hostname: {self.hostname}\n"
                f"IP Address: {self.ip_address}\n"
                f"Status: {status}\n"
                f"Last Started: {last_started_str}")

    def _validate_ip(self, ip_address): #helper function to validate IP Address
        pattern = r"^(\d{1,3}\.){3}\d{1,3}$"
        return bool(re.match(pattern, ip_address))


# Tasks and Bonus Challenges for Lab 4
web_server = Server("web-01", "192.168.1.100")
db_server = Server("db-01", "192.168.1.101")

print(web_server.start())
print(db_server.stop())

print(web_server.check_status())
print(db_server.check_status())

print(web_server.restart())
print(web_server.display_info())
print(db_server.display_info())

# Example of invalid IP address handling
# try:
#     invalid_server = Server("invalid", "192.168.1")  # This will raise a ValueError
# except ValueError as e:
#     print(f"Error: {e}")