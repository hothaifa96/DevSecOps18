# Bash Functions Lab Exercises

This document contains a series of progressively challenging exercises to help you master Bash functions. Each exercise is designed to build on concepts from earlier challenges.

## Getting Started

To complete these exercises:

1. Create a new `.sh` file for each exercise
2. Make the file executable with `chmod +x filename.sh`
3. Implement the required function(s)
4. Test your solution
5. Compare with the solution (not provided here)

## Easy Exercises

### Exercise 1: Hello Function

**Objective:** Create a function that prints a simple greeting message.

**Requirements:**
- Create a function called `say_hello`
- The function should print "Hello, World!" to the console
- Call the function in your script

**Expected Output:**
```
Hello, World!
```

### Exercise 2: Personalized Greeting

**Objective:** Create a function that greets a person by name.

**Requirements:**
- Create a function called `greet`
- The function should accept one parameter: a person's name
- The function should print "Hello, [name]!" where [name] is the parameter
- Call the function with at least two different names

**Expected Output:**
```
Hello, John!
Hello, Sarah!
```

### Exercise 3: Simple Calculator

**Objective:** Create a function that performs basic arithmetic.

**Requirements:**
- Create a function called `calculate`
- The function should take three parameters: two numbers and an operation (add, subtract, multiply, or divide)
- The function should perform the specified operation and print the result
- Include proper error handling for division by zero
- Test your function with various inputs

**Expected Output:**
```
10 + 5 = 15
10 - 5 = 5
10 * 5 = 50
10 / 5 = 2
Cannot divide by zero!
```

## Intermediate Exercises

### Exercise 4: File Checker

**Objective:** Create a function that checks if a file exists and reports its properties.

**Requirements:**
- Create a function called `check_file`
- The function should take a filename as a parameter
- The function should check if the file exists
- If the file exists, the function should report whether it's readable, writable, and executable
- If the file doesn't exist, the function should report that
- Test with at least three different files

**Expected Output:**
```
File exists.txt exists:
- Readable: yes
- Writable: yes
- Executable: no

File not-exists.txt does not exist.

File script.sh exists:
- Readable: yes
- Writable: yes
- Executable: yes
```

### Exercise 5: Temperature Converter

**Objective:** Create functions to convert between Celsius and Fahrenheit.

**Requirements:**
- Create two functions: `celsius_to_fahrenheit` and `fahrenheit_to_celsius`
- Each function should take a temperature as a parameter
- The function should return the converted temperature (not print it)
- Create a main function that prompts the user for:
  - A temperature
  - The current unit (C or F)
- The program should convert and display the temperature in the other unit
- Format the output to 1 decimal place

**Expected Output:**
```
Enter temperature: 32
Current unit (C/F): F
32.0°F = 0.0°C

Enter temperature: 100
Current unit (C/F): C
100.0°C = 212.0°F
```

### Exercise 6: Word Counter

**Objective:** Create a function that counts words, lines, and characters in a file.

**Requirements:**
- Create a function called `count_text`
- The function should take a filename as a parameter
- The function should count and return the number of lines, words, and characters in the file
- The main program should display the counts in a formatted way
- Handle the case where the file doesn't exist

**Expected Output:**
```bash
File: sample.txt
- Lines: 5
- Words: 20
- Characters: 100

Error: File not-exists.txt does not exist.
```

## Advanced Exercises

### Exercise 7: Log Parser

**Objective:** Create a function that parses a log file and extracts specific information.

**Requirements:**
- Create a function called `parse_log`
- The function should take a log filename and a search term as parameters
- The function should find all lines containing the search term
- For each matching line, extract and display:
  - The timestamp
  - The log level (INFO, WARNING, ERROR)
  - The log message
- Format the output in a readable way
- Handle file not found errors

**Sample Log Format:**
```
2023-04-12 14:32:45 INFO User logged in successfully
2023-04-12 14:33:12 WARNING Failed login attempt
2023-04-12 14:35:22 ERROR Database connection failed
```

### Exercise 8: Directory Size Analyzer

**Objective:** Create a function that calculates the total size of files in a directory.

**Requirements:**
- Create a function called `dir_size`
- The function should take a directory path and an optional boolean parameter for recursion
- The function should calculate the total size of all files in the directory
- If recursion is enabled, include files in subdirectories
- Return the size in a human-readable format (KB, MB, GB)
- Handle directory not found errors
- The main program should display the results along with the directory path

**Expected Output:**
```bash
Directory: /home/user/documents
Size: 256 MB

Directory (recursive): /home/user/documents
Size: 1.2 GB

Error: Directory not-exists does not exist.
```

### Exercise 9: Backup Script

**Objective:** Create a backup script with multiple functions.

**Requirements:**
- Create the following functions:
  - `check_space`: Check if there's enough space for the backup
  - `create_archive`: Create a compressed archive of a directory
  - `encrypt_file`: Encrypt the archive with a password
  - `transfer_file`: Transfer the file to a backup location (local or remote)
  - `cleanup`: Remove temporary files
  - `log_action`: Log all actions to a log file
- Create a main function that orchestrates the backup process
- Add appropriate error handling throughout
- Make the script configurable with command-line arguments

**Expected Output:**
```bash
Starting backup at 2023-04-12 15:30:45
Checking available space... OK
Creating archive of /home/user/documents... OK
Encrypting backup.tar.gz... OK
Transferring backup.tar.gz.enc to /mnt/backup... OK
Cleaning up temporary files... OK
Backup completed successfully at 2023-04-12 15:32:10
Log written to backup.log
```

### Exercise 10: System Monitor

**Objective:** Create a system monitoring script with functions for different metrics.

**Requirements:**
- Create functions to monitor:
  - `check_cpu`: CPU usage
  - `check_memory`: Memory usage
  - `check_disk`: Disk usage
  - `check_network`: Network usage
  - `check_processes`: Top 5 processes by resource usage
- Create a function to generate a formatted report
- Create a function to detect abnormal values and send alerts
- Create a main function that runs a monitoring cycle
- Add a loop to run the monitoring at specified intervals
- Make the interval and thresholds configurable

**Expected Output:**
```bash
SYSTEM MONITORING REPORT - 2023-04-12 16:00:00

CPU: 35% [OK]
Memory: 65% [WARNING]
Disk: 82% [WARNING]
Network: In: 5.2 MB/s, Out: 1.3 MB/s [OK]

TOP PROCESSES:
1. firefox (PID 1234): CPU 15%, MEM 500MB
2. chrome (PID 2345): CPU 10%, MEM 450MB
3. vscode (PID 3456): CPU 5%, MEM 300MB
4. mysql (PID 4567): CPU 3%, MEM 200MB
5. nginx (PID 5678): CPU 2%, MEM 100MB

ALERTS:
- Memory usage above threshold (65% > 60%)
- Disk usage above threshold (82% > 80%)

Next check in 5 minutes.
```

## Expert Challenge

### Exercise 11: Interactive Menu Framework

**Objective:** Create a reusable framework for building interactive menu-driven Bash scripts.

**Requirements:**
- Create functions for:
  - `display_menu`: Display a dynamic menu based on an array of options
  - `get_user_choice`: Get and validate user input
  - `run_option`: Run the function associated with the menu option
  - `add_option`: Add new options to the menu dynamically
  - `remove_option`: Remove options from the menu
  - `create_submenu`: Create nested submenus
- The framework should support:
  - Multiple levels of nested menus
  - Dynamically changing menu options
  - Input validation
  - Help text for each option
  - Breadcrumb navigation
- Create a demo application using your framework that showcases all features

This challenging exercise will test your function design skills, parameter handling, and overall Bash scripting knowledge.

## Bonus Challenge

### Exercise 12: Library Management

**Objective:** Create a complete Bash function library and demonstrate its use.

**Requirements:**
- Create a library file called `bash_utils.sh` with useful functions:
  - String manipulation functions (trim, uppercase, lowercase, etc.)
  - File handling functions (safe copy, move, delete with confirmation)
  - Input validation functions (validate number, email, IP address, etc.)
  - Logging functions (different log levels, rotation)
  - UI functions (progress bars, spinners, colored output)
- Create proper documentation for each function
- Create a demonstration script that imports your library and uses its functions
- Add error handling and parameter validation to all functions
- Make the library configurable with environment variables

This exercise will test your ability to create reusable, well-documented code that follows best practices.
