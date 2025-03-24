# Bash Scripting: Conditionals and Test Conditions

## Table of Contents
1. [Introduction](#introduction)
2. [Basic Conditional Syntax](#basic-conditional-syntax)
   - [If Statement](#if-statement)
   - [If-Else Statement](#if-else-statement)
   - [If-Elif-Else Statement](#if-elif-else-statement)
   - [Nested Conditionals](#nested-conditionals)
3. [Test Conditions](#test-conditions)
   - [File Test Operators](#file-test-operators)
   - [String Test Operators](#string-test-operators)
   - [Integer Comparison Operators](#integer-comparison-operators)
   - [Logical Operators](#logical-operators)
4. [Using Test Commands](#using-test-commands)
   - [`test` Command](#test-command)
   - [`[` Command](#-command)
   - [`[[` Command (Extended Test)](#-command-extended-test)
5. [Practical Examples](#practical-examples)
   - [File Operations](#file-operations)
   - [String Manipulation](#string-manipulation)
   - [Numeric Comparisons](#numeric-comparisons)
   - [Command Execution Status](#command-execution-status)
6. [Advanced Techniques](#advanced-techniques)
   - [Pattern Matching](#pattern-matching)
   - [Using Multiple Conditions](#using-multiple-conditions)
   - [Command Substitution in Conditionals](#command-substitution-in-conditionals)
7. [Best Practices](#best-practices)
8. [Common Pitfalls](#common-pitfalls)
9. [Reference Table of Test Operators](#reference-table-of-test-operators)

## Introduction

Conditional statements are essential components of any programming language, allowing scripts to make decisions and execute different code blocks based on specified conditions. In Bash, the `if`, `elif` (else if), and `else` statements are used to implement conditional logic. Combined with various test operators, they enable you to create scripts that can intelligently respond to different scenarios.

## Basic Conditional Syntax

### If Statement

The basic syntax for an `if` statement is:

```bash
if [[condition]]; then
    # Commands to execute if condition is true
fi
```

Example:
```bash
#!/bin/bash

if [ -f "/etc/hosts" ]; then
    echo "The hosts file exists."
fi
```

### If-Else Statement

To execute alternative commands when a condition is false, use the `else` clause:

```bash
if condition; then
    # Commands to execute if condition is true
else
    # Commands to execute if condition is false
fi
```

Example:
```bash
#!/bin/bash

if [ -f "/etc/nonexistent.conf" ]; then
    echo "The configuration file exists."
else
    echo "The configuration file does not exist."
fi
```

### If-Elif-Else Statement

For multiple conditions, use the `elif` (else if) clause:

```bash
if condition1; then
    # Commands to execute if condition1 is true
elif condition2; then
    # Commands to execute if condition1 is false and condition2 is true
elif condition3; then
    # Commands to execute if condition1 and condition2 are false and condition3 is true
else
    # Commands to execute if all conditions are false
fi
```

Example:
```bash
#!/bin/bash

score=75

if [ $score -ge 90 ]; then
    echo "Grade: A"
elif [ $score -ge 80 ]; then
    echo "Grade: B"
elif [ $score -ge 70 ]; then
    echo "Grade: C"
elif [ $score -ge 60 ]; then
    echo "Grade: D"
else
    echo "Grade: F"
fi
```

### Nested Conditionals

You can nest conditional statements for more complex logic:

```bash
if condition1; then
    if condition2; then
        # Commands when both condition1 and condition2 are true
    else
        # Commands when condition1 is true but condition2 is false
    fi
else
    # Commands when condition1 is false
fi
```

Example:
```bash
#!/bin/bash

file="/etc/hosts"

if [ -f "$file" ]; then
    if [ -w "$file" ]; then
        echo "The file exists and is writable."
    else
        echo "The file exists but is not writable."
    fi
else
    echo "The file does not exist."
fi
```

## Test Conditions

Bash provides several operators for testing different conditions within `if` statements. These operators are categorized based on what they test.

### File Test Operators

These operators check for file attributes and properties:

| Operator | Description |
|----------|-------------|
| `-e file` | Returns true if file exists. |
| `-f file` | Returns true if file exists and is a regular file. |
| `-d file` | Returns true if file exists and is a directory. |
| `-s file` | Returns true if file exists and has a size greater than zero. |
| `-r file` | Returns true if file exists and is readable. |
| `-w file` | Returns true if file exists and is writable. |
| `-x file` | Returns true if file exists and is executable. |
| `-L file` | Returns true if file exists and is a symbolic link. |
| `-b file` | Returns true if file exists and is a block special file. |
| `-c file` | Returns true if file exists and is a character special file. |
| `-p file` | Returns true if file exists and is a named pipe (FIFO). |
| `-S file` | Returns true if file exists and is a socket. |
| `-g file` | Returns true if file exists and has the set-group-ID bit set. |
| `-u file` | Returns true if file exists and has the set-user-ID bit set. |
| `-k file` | Returns true if file exists and has the sticky bit set. |
| `-O file` | Returns true if file exists and is owned by the effective user ID. |
| `-G file` | Returns true if file exists and is owned by the effective group ID. |
| `-N file` | Returns true if file exists and has been modified since it was last read. |
| `file1 -nt file2` | Returns true if file1 is newer than file2 (according to modification date). |
| `file1 -ot file2` | Returns true if file1 is older than file2. |
| `file1 -ef file2` | Returns true if file1 and file2 refer to the same device and inode numbers. |

Example:
```bash
#!/bin/bash

file="/etc/passwd"

if [ -f "$file" ]; then
    echo "$file is a regular file."
fi

if [ -d "/etc" ]; then
    echo "/etc is a directory."
fi

if [ -r "$file" ] && [ -w "$file" ]; then
    echo "$file is both readable and writable."
fi

if [ -x "/usr/bin/python" ]; then
    echo "Python is executable."
fi

if [ -L "/usr/bin/python" ]; then
    echo "Python is a symbolic link."
fi

if [ ! -e "/nonexistent/file" ]; then
    echo "The nonexistent file does not exist."
fi
```

### String Test Operators

These operators compare and test string values:

| Operator | Description |
|----------|-------------|
| `-z string` | Returns true if the length of string is zero. |
| `-n string` | Returns true if the length of string is non-zero. |
| `string1 = string2` | Returns true if string1 is equal to string2. |
| `string1 != string2` | Returns true if string1 is not equal to string2. |
| `string1 < string2` | Returns true if string1 sorts before string2 lexicographically. |
| `string1 > string2` | Returns true if string1 sorts after string2 lexicographically. |
| `string =~ regex` | Returns true if string matches the regular expression regex (only in `[[` command). |

Example:
```bash
#!/bin/bash

name="Alice"
empty_string=""

if [ -z "$empty_string" ]; then
    echo "The empty string is empty."
fi

if [ -n "$name" ]; then
    echo "The name variable is not empty."
fi

if [ "$name" = "Alice" ]; then
    echo "The name is Alice."
fi

if [ "$name" != "Bob" ]; then
    echo "The name is not Bob."
fi

# Note: < and > must be escaped or quoted in [ ] to prevent them being interpreted as redirections
if [[ "$name" < "Bob" ]]; then
    echo "Alice comes before Bob alphabetically."
fi

# Using regex matching (only in [[ ]])
if [[ "$name" =~ ^A[a-z]+$ ]]; then
    echo "The name starts with A followed by lowercase letters."
fi
```

### Integer Comparison Operators

These operators compare integer values:

| Operator | Description |
|----------|-------------|
| `int1 -eq int2` | Returns true if int1 is equal to int2. |
| `int1 -ne int2` | Returns true if int1 is not equal to int2. |
| `int1 -lt int2` | Returns true if int1 is less than int2. |
| `int1 -le int2` | Returns true if int1 is less than or equal to int2. |
| `int1 -gt int2` | Returns true if int1 is greater than int2. |
| `int1 -ge int2` | Returns true if int1 is greater than or equal to int2. |

Example:
```bash
#!/bin/bash

age=25

if [ $age -eq 25 ]; then
    echo "Age is exactly 25."
fi

if [ $age -ne 30 ]; then
    echo "Age is not 30."
fi

if [ $age -lt 30 ]; then
    echo "Age is less than 30."
fi

if [ $age -le 25 ]; then
    echo "Age is less than or equal to 25."
fi

if [ $age -gt 20 ]; then
    echo "Age is greater than 20."
fi

if [ $age -ge 25 ]; then
    echo "Age is greater than or equal to 25."
fi
```

### Logical Operators

These operators combine multiple conditions:

| Operator | Description |
|----------|-------------|
| `! condition` | Returns true if condition is false. |
| `condition1 -a condition2` | Returns true if both condition1 and condition2 are true (AND). |
| `condition1 -o condition2` | Returns true if either condition1 or condition2 is true (OR). |
| `condition1 && condition2` | Returns true if both condition1 and condition2 are true (AND). Used between commands or in `[[` construct. |
| `condition1 || condition2` | Returns true if either condition1 or condition2 is true (OR). Used between commands or in `[[` construct. |

Example:
```bash
#!/bin/bash

age=25
name="Alice"

# Using -a and -o operators with [ ]
if [ $age -gt 20 -a "$name" = "Alice" ]; then
    echo "Age is greater than 20 AND name is Alice."
fi

if [ $age -lt 20 -o "$name" = "Alice" ]; then
    echo "Age is less than 20 OR name is Alice."
fi

# Using && and || operators with [ ]
if [ $age -gt 20 ] && [ "$name" = "Alice" ]; then
    echo "Age is greater than 20 AND name is Alice."
fi

if [ $age -lt 20 ] || [ "$name" = "Alice" ]; then
    echo "Age is less than 20 OR name is Alice."
fi

# Using ! operator (negation)
if [ ! -f "/nonexistent/file" ]; then
    echo "The file does not exist."
fi

# Using [[ ]] for more complex conditions
if [[ $age -gt 20 && "$name" = "Alice" ]]; then
    echo "Age is greater than 20 AND name is Alice (using [[ ]])."
fi
```

## Using Test Commands

Bash provides several ways to evaluate conditions:

### `test` Command

The `test` command evaluates an expression and returns a status of 0 (true) or 1 (false):

```bash
test -f /etc/hosts && echo "File exists."
```

### `[` Command

The `[` command is a synonym for `test` and must be closed with a matching `]`:

```bash
[ -f /etc/hosts ] && echo "File exists."
```

### `[[` Command (Extended Test)

The `[[` command is an extended test command that provides additional features:

```bash
[[ -f /etc/hosts ]] && echo "File exists."
```

Advantages of `[[` over `[`:
- No word splitting or glob expansion on variables
- The `&&`, `||`, `<`, and `>` operators work without escaping
- Support for pattern matching using `=~`
- Better handling of empty variables

Example comparing test commands:
```bash
#!/bin/bash

filename="my file.txt"  # Note the space

# This might fail due to word splitting
[ -f $filename ] && echo "File exists."

# This works correctly
[ -f "$filename" ] && echo "File exists."

# This also works correctly and is preferred
[[ -f $filename ]] && echo "File exists."

# Regular expression matching (only works with [[]])
if [[ "apple123" =~ ^[a-z]+[0-9]+$ ]]; then
    echo "String matches the pattern."
fi
```

## Practical Examples

### File Operations

```bash
#!/bin/bash

# Check if a file exists and is writable
file="/path/to/file.txt"

if [ -f "$file" ]; then
    if [ -w "$file" ]; then
        echo "$file exists and is writable. Appending content..."
        echo "New data" >> "$file"
    else
        echo "$file exists but is not writable."
    fi
else
    echo "$file does not exist. Creating it..."
    touch "$file"
    echo "Initial content" > "$file"
fi

# Check if a directory exists, create it if not
dir="/path/to/directory"

if [ ! -d "$dir" ]; then
    echo "Directory does not exist. Creating $dir..."
    mkdir -p "$dir"
else
    echo "Directory $dir already exists."
fi

# Compare file modification times
file1="/etc/passwd"
file2="/etc/group"

if [ "$file1" -nt "$file2" ]; then
    echo "$file1 is newer than $file2."
elif [ "$file1" -ot "$file2" ]; then
    echo "$file1 is older than $file2."
else
    echo "The files have the same modification time or at least one doesn't exist."
fi
```

### String Manipulation

```bash
#!/bin/bash

# Check for empty input
read -p "Enter your name: " name

if [ -z "$name" ]; then
    echo "Name cannot be empty."
    exit 1
fi

# Check string equality
if [ "$name" = "admin" ]; then
    echo "Welcome, administrator!"
else
    echo "Welcome, $name!"
fi

# Check string length
if [ ${#name} -lt 3 ]; then
    echo "Name is too short. It should be at least 3 characters."
elif [ ${#name} -gt 20 ]; then
    echo "Name is too long. It should be at most 20 characters."
else
    echo "Name length is acceptable."
fi

# Pattern matching with [[
if [[ "$name" =~ ^[A-Z][a-z]+$ ]]; then
    echo "Name follows proper capitalization (first letter uppercase, rest lowercase)."
fi
```

### Numeric Comparisons

```bash
#!/bin/bash

# Get user input
read -p "Enter your age: " age

# Validate input is a number
if ! [[ "$age" =~ ^[0-9]+$ ]]; then
    echo "Error: Age must be a number."
    exit 1
fi

# Check age categories
if [ "$age" -lt 0 ]; then
    echo "Error: Age cannot be negative."
elif [ "$age" -lt 13 ]; then
    echo "You are a child."
elif [ "$age" -lt 20 ]; then
    echo "You are a teenager."
elif [ "$age" -lt 65 ]; then
    echo "You are an adult."
else
    echo "You are a senior."
fi

# Check eligibility for voting
voting_age=18

if [ "$age" -ge "$voting_age" ]; then
    echo "You are eligible to vote."
else
    years_left=$((voting_age - age))
    echo "You will be eligible to vote in $years_left years."
fi
```

### Command Execution Status

```bash
#!/bin/bash

# Check if a command succeeds
if ping -c 1 google.com &> /dev/null; then
    echo "Internet connection is available."
else
    echo "No internet connection."
fi

# Check if a package is installed
if command -v docker &> /dev/null; then
    echo "Docker is installed."
else
    echo "Docker is not installed."
fi

# Execute a command based on the success of another
if grep -q "^user:" /etc/passwd; then
    echo "User exists in the system."
else
    echo "User does not exist in the system."
fi
```

## Advanced Techniques

### Pattern Matching

Using the `[[` command, you can perform pattern matching against strings:

```bash
#!/bin/bash

text="The quick brown fox jumps over the lazy dog"

if [[ $text == *"fox"* ]]; then
    echo "Text contains 'fox'."
fi

if [[ $text == "The quick"* ]]; then
    echo "Text starts with 'The quick'."
fi

if [[ $text == *"lazy dog" ]]; then
    echo "Text ends with 'lazy dog'."
fi

# Using regular expressions
if [[ $text =~ [a-z]+\s+dog$ ]]; then
    echo "Text ends with a word followed by 'dog'."
fi

# Check file extension
filename="document.pdf"

if [[ $filename == *.pdf ]]; then
    echo "This is a PDF file."
elif [[ $filename == *.txt ]]; then
    echo "This is a text file."
else
    echo "Unknown file type."
fi
```

### Using Multiple Conditions

Combining multiple conditions for complex decision-making:

```bash
#!/bin/bash

file="/etc/hosts"
min_size=100

# Using AND logic
if [ -f "$file" ] && [ -r "$file" ] && [ -s "$file" ]; then
    echo "$file exists, is readable, and has content."
fi

# Using OR logic
if [ ! -f "$file" ] || [ ! -r "$file" ]; then
    echo "$file doesn't exist or is not readable."
fi

# Combining AND and OR
if [ -f "$file" ] && ([ -r "$file" ] || [ -w "$file" ]); then
    echo "$file exists and is either readable or writable."
fi

# Using [[ for complex conditions
if [[ -f "$file" && (-r "$file" || -w "$file") ]]; then
    echo "$file exists and is either readable or writable (using [[]])."
fi

# Check file size
size=$(stat -c %s "$file" 2>/dev/null || echo 0)

if [[ -f "$file" && $size -gt $min_size ]]; then
    echo "$file exists and is larger than $min_size bytes."
fi
```

### Command Substitution in Conditionals

Using command output within conditional statements:

```bash
#!/bin/bash

# Check disk usage
usage=$(df -h / | awk 'NR==2 {print $5}' | sed 's/%//')

if [ "$usage" -gt 90 ]; then
    echo "WARNING: Disk usage is over 90%!"
elif [ "$usage" -gt 75 ]; then
    echo "NOTICE: Disk usage is over 75%."
else
    echo "INFO: Disk usage is ${usage}%."
fi

# Check uptime
uptime_seconds=$(cat /proc/uptime | awk '{print $1}' | cut -d. -f1)
days=$((uptime_seconds / 86400))

if [ "$days" -gt 30 ]; then
    echo "System has been up for more than 30 days. Consider restarting."
fi

# Check number of processes
process_count=$(ps aux | wc -l)

if [ "$process_count" -gt 200 ]; then
    echo "System is running many processes: $process_count"
fi
```

## Best Practices

1. **Always quote variables**
   ```bash
   # Good
   if [ -f "$file" ]; then
       echo "File exists"
   fi
   
   # Bad (fails if $file contains spaces)
   if [ -f $file ]; then
       echo "File exists"
   fi
   ```

2. **Use `[[` instead of `[` for advanced features**
   ```bash
   # Preferred for complex conditions
   if [[ $name == "John" && $age -gt 21 ]]; then
       echo "Welcome, adult John"
   fi
   ```

3. **Check if variables exist before using them**
   ```bash
   if [ -z "$variable" ]; then
       echo "Variable is empty or not set"
       exit 1
   fi
   ```

4. **Use proper exit codes**
   ```bash
   if [ ! -f "$config_file" ]; then
       echo "Error: Config file not found"
       exit 1  # Exit with error code
   fi
   ```

5. **Use a default value if a variable might be empty**
   ```bash
   count=${count:-0}  # Use 0 if count is unset or empty
   
   if [ "$count" -gt 10 ]; then
       echo "Count is greater than 10"
   fi
   ```

## Common Pitfalls

1. **Forgetting to quote variables**
   ```bash
   file="file with spaces.txt"
   
   # This will fail:
   if [ -f $file ]; then
       echo "File exists"
   fi
   ```

2. **Using `=` instead of `-eq` for numeric comparisons**
   ```bash
   # Wrong (string comparison):
   if [ "$count" = 5 ]; then
       echo "Count is 5"
   fi
   
   # Correct (numeric comparison):
   if [ "$count" -eq 5 ]; then
       echo "Count is 5"
   fi
   ```

3. **Using `-a` and `-o` in complex expressions without proper grouping**
   ```bash
   # Confusing and error-prone:
   if [ "$a" = "$b" -o "$c" = "$d" -a "$e" = "$f" ]; then
       echo "Condition met"
   fi
   
   # Better:
   if [ "$a" = "$b" ] || { [ "$c" = "$d" ] && [ "$e" = "$f" ]; }; then
       echo "Condition met"
   fi
   
   # Even better:
   if [[ $a == $b || ($c == $d && $e == $f) ]]; then
       echo "Condition met"
   fi
   ```

4. **Not checking for empty variables**
   ```bash
   # This can cause errors if name is unset:
   if [ "$name" = "John" ]; then
       echo "Hello John"
   fi
   
   # Better:
   if [ -n "$name" ] && [ "$name" = "John" ]; then
       echo "Hello John"
   fi
   ```

5. **Comparing floating-point numbers**
   ```bash
   # Bash doesn't support floating-point arithmetic in [ ]
   # Use bc for floating-point comparisons:
   if (( $(echo "$value > 5.5" | bc -l) )); then
       echo "Value is greater than 5.5"
   fi
   ```

## Reference Table of Test Operators

### File Operators
| Operator | Description |
|----------|-------------|
| `-e file` | True if file exists |
| `-f file` | True if file exists and is a regular file |
| `-d file` | True if file exists and is a directory |
| `-s file` | True if file exists and size > 0 |
| `-r file` | True if file exists and is readable |
| `-w file` | True if file exists and is writable |
| `-x file` | True if file exists and is executable |
| `-L file` | True if file exists and is a symbolic link |

### String Operators
| Operator | Description |
|----------|-------------|
| `-z string` | True if string length is zero |
| `-n string` | True if string length is non-zero |
| `string1 = string2` | True if strings are equal |
| `string1 != string2` | True if strings are not equal |
| `string =~ pattern` | True if string matches pattern (only in `[[`) |

### Integer Operators
| Operator | Description |
|----------|-------------|
| `int1 -eq int2` | True if integers are equal |
| `int1 -ne int2` | True if integers are not equal |
| `int1 -lt int2` | True if int1 < int2 |
| `int1 -le int2` | True if int1 <= int2 |
| `int1 -gt int2` | True if int1 > int2 |
| `int1 -ge int2` | True if int1 >= int2 |

### Logical Operators
| Operator | Description |
|----------|-------------|
| `! expr` | True if expr is false |
| `expr1 -a expr2` | True if both expr1 and expr2 are true (in `[`) |
| `expr1 -o expr2` | True if either expr1 or expr2 is true (in `[`) |
| `expr1 && expr2` | True if both expr1 and expr2 are true (in `[[` or between commands) |
| `expr1 || expr2` | True if either expr1 or expr2 is true (in `[[` or between commands) |