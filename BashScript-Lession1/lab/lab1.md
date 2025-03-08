# Bash Scripting Exercises1

## Exercise 1: File Backup Tool

### Problem
Create a script that takes a filename as an argument ($1) and creates a backup of that file. The script should:
- Check if the file exists
- Ask the user if they want to specify a custom backup location (using read)
- Create a backup with the current date appended to the filename
- Display appropriate messages using echo
### Hint
Use the `date` command to get the current date.

## Exercise 2: User Account Information

### Problem
Create a script that accepts a username as an argument ($1) and displays information about that user account. If no username is provided, it should prompt the user to enter one using read. The script should:
- Check if the user exists on the system
- Display the user's home directory, shell, and last login time
- Allow checking multiple users if provided as additional arguments ($2, $3, etc.)

### Hint
Use the `getent` command to retrieve user information.

## Exercise 3: Interactive Calculator

### Problem
Create a script that functions as a simple interactive calculator. It should:
- Accept an operation as $1 (add, subtract, multiply, divide)
- Accept two numbers as $2 and $3
- If any arguments are missing, prompt the user for them using read
- Validate that the inputs are numeric
- Perform the calculation and display the result
- Ask if the user wants to perform another calculation


## Exercise 4: File Search and Analysis

### Problem
Create a script that searches for files of a specific type in a directory and provides analysis. It should:
- Accept a file extension as $1 (e.g., txt, jpg, pdf)
- Accept a directory path as $2 (default to current directory if not provided)
- Accept an optional action as $3 (count, list, size, newest)
- Prompt the user if arguments are missing
- Validate inputs and handle errors
- Perform the requested analysis and display results

### Hint
Use the `find` command for searching and `stat` for file analysis.

## Exercise 5: System Resource Monitor

### Problem
Create a script that monitors system resources based on user preferences. It should:
- Accept a resource type as $1 (cpu, memory, disk, all)
- Accept a threshold percentage as $2 (alert if usage exceeds this)
- Accept an optional output format as $3 (text, simple, detailed)
- Use defaults if arguments are not provided
- Allow the user to interactively change settings
- Display appropriate resource information

### Hint
Use system commands like `top`, `free`, `df`, and `ps` for resource monitoring