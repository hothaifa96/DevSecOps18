# Bash Scripting: Variables, Echo and Read Commands

## Table of Contents
1. [Introduction](#introduction)
2. [Variables in Bash](#variables-in-bash)
   - [Declaring Variables](#declaring-variables)
   - [Variable Naming Rules](#variable-naming-rules)
   - [Accessing Variable Values](#accessing-variable-values)
   - [Environment Variables](#environment-variables)
   - [Variable Scope](#variable-scope)
3. [The Echo Command](#the-echo-command)
   - [Basic Usage](#basic-usage)
   - [Common Options](#common-options)
   - [Printing Variables](#printing-variables)
   - [Using Escape Sequences](#using-escape-sequences)
   - [Color and Formatting](#color-and-formatting)
4. [The Read Command](#the-read-command)
   - [Basic Usage](#basic-usage-1)
   - [Common Options](#common-options-1)
   - [Reading Multiple Values](#reading-multiple-values)
   - [Timing Out Read Operations](#timing-out-read-operations)
   - [Reading Passwords](#reading-passwords)
5. [Practical Examples](#practical-examples)
6. [Best Practices](#best-practices)
7. [Advanced Topics](#advanced-topics)

## Introduction

Variables, `echo`, and `read` are fundamental components of Bash scripting. Variables store data that can be accessed and manipulated throughout your script. The `echo` command outputs text to the terminal, while the `read` command captures user input. Together, these elements form the backbone of interactive and dynamic Bash scripts.

## Variables in Bash

### Declaring Variables

In Bash, variables are declared without a specific type and are assigned using the `=` operator. There should be **no spaces** around the equals sign.

```bash
# Correct way to declare variables
name="John"
age=30
is_active=true
current_date=$(date)
```

### Variable Naming Rules

- Variable names should consist of letters, numbers, and underscores
- Names cannot start with a number
- Names are case-sensitive
- No spaces or special characters (except underscore)
- Convention suggests using lowercase for regular variables and uppercase for constants or environment variables

```bash
# Valid variable names
user_name="Alice"
count123=42
_temporary="temp value"

# Invalid variable names
# 123count=42     # Starts with number
# user-name="Bob" # Contains hyphen
# my variable=10  # Contains space
```

### Accessing Variable Values

To access a variable's value, prefix the variable name with a `$` symbol:

```bash
name="John"
echo $name       # Outputs: John

# Using curly braces (recommended for clarity)
echo ${name}     # Outputs: John

# Using variable within text
echo "Hello, $name!"    # Outputs: Hello, John!
echo "Hello, ${name}!"  # Outputs: Hello, John!
```

Using curly braces `${}` is recommended, especially when the variable name might be ambiguous:

```bash
fruit="apple"
echo "I like ${fruit}s"  # Outputs: I like apples
# Without braces, Bash would look for a variable named 'fruits'
echo "I like $fruits"    # Outputs: I like
```

### Environment Variables

Environment variables are available to all processes and are typically used for system configuration:

```bash
# Common environment variables
echo $HOME       # User's home directory
echo $USER       # Current username
echo $PATH       # Executable search path
echo $PWD        # Present working directory
echo $SHELL      # Path to current shell

# Setting an environment variable (for current session)
export API_KEY="abc123"
```

To list all environment variables:

```bash
env       # Display all environment variables
printenv  # Alternative command
```

### Variable Scope

By default, variables in Bash are global to the script but not to other scripts or the parent shell:

```bash
# Global variable (available throughout the script)
global_var="I am global"

# Local variable (limited to function scope)
function example_function {
    local local_var="I am local"
    echo "Inside function: $local_var"
    echo "Inside function: $global_var"
}

example_function
echo "Outside function: $global_var"
echo "Outside function: $local_var"  # Will be empty
```

## The Echo Command

### Basic Usage

The `echo` command displays text or variable values to the terminal:

```bash
echo "Hello, World!"
```

### Common Options

- `-e`: Enable interpretation of backslash escapes
- `-n`: Do not output a trailing newline

```bash
# Without -e option
echo "Line 1\nLine 2"   # Outputs: Line 1\nLine 2

# With -e option
echo -e "Line 1\nLine 2"
# Outputs:
# Line 1
# Line 2

# Without -n option
echo "No newline"
echo "Next line"

# With -n option
echo -n "No newline"
echo " continued"  # Outputs: No newline continued
```

### Printing Variables

```bash
name="John"
age=30

# Single variable
echo $name                  # Outputs: John

# Multiple variables
echo "$name is $age years old"  # Outputs: John is 30 years old

# Using command substitution
echo "Current date: $(date)"
```

### Using Escape Sequences

With the `-e` option, `echo` interprets several backslash-escaped characters:

```bash
echo -e "Tab\tcharacter"           # Outputs: Tab     character
echo -e "New\nline"                # Outputs text on two lines
echo -e "Carriage\rreturn"         # Replaces "Carriage" with "return"
echo -e "Backslash: \\"            # Outputs: Backslash: \
echo -e "Double quote: \""         # Outputs: Double quote: "
echo -e "Vertical\vtab"            # Vertical tab spacing
echo -e "Bell sound: \a"           # Makes a bell sound (if terminal supports it)
echo -e "Form\ffeed"               # Form feed
echo -e "Escape character: \e"     # Escape character
echo -e "\033[1mBold text\033[0m"  # ANSI escape sequence for bold text
```

### Color and Formatting

ANSI escape sequences allow you to add color and formatting:

```bash
# Text colors
echo -e "\033[31mRed text\033[0m"
echo -e "\033[32mGreen text\033[0m"
echo -e "\033[33mYellow text\033[0m"
echo -e "\033[34mBlue text\033[0m"
echo -e "\033[35mMagenta text\033[0m"
echo -e "\033[36mCyan text\033[0m"

# Background colors
echo -e "\033[41mRed background\033[0m"
echo -e "\033[42mGreen background\033[0m"

# Text formatting
echo -e "\033[1mBold text\033[0m"
echo -e "\033[4mUnderlined text\033[0m"
echo -e "\033[5mBlinking text\033[0m"  # Not supported in all terminals
echo -e "\033[7mReversed text\033[0m"

# Combining formats
echo -e "\033[1;31;43mBold red text on yellow background\033[0m"
```

For better readability, you can store these codes in variables:

```bash
RED='\033[0;31m'
GREEN='\033[0;32m'
NC='\033[0m'  # No Color

echo -e "${RED}This is red text.${NC}"
echo -e "${GREEN}This is green text.${NC}"
```

## The Read Command

### Basic Usage

The `read` command reads input from the user and stores it in a variable:

```bash
echo "What is your name?"
read name
echo "Hello, $name!"
```

### Common Options

- `-p`: Display a prompt before reading input
- `-s`: Silent mode (doesn't echo characters, useful for passwords)
- `-n N`: Read only N characters
- `-t N`: Timeout after N seconds
- `-a`: Read into an array
- `-r`: Raw mode (backslashes are not interpreted as escape characters)

```bash
# Using -p for prompt
read -p "Enter your name: " name
echo "Hello, $name!"

# Using -n to limit input length
read -n 1 -p "Press any key to continue... " key
echo -e "\nYou pressed: $key"

# Using -s for secret input
read -s -p "Enter password: " password
echo -e "\nPassword recorded (not shown)"
```

### Reading Multiple Values

You can read multiple values at once, separated by spaces:

```bash
read -p "Enter first and last name: " first_name last_name
echo "First name: $first_name"
echo "Last name: $last_name"
```

If more values are provided than variables, the last variable gets all remaining values:

```bash
read -p "Enter your full name: " first rest
echo "First name: $first"
echo "Rest of name: $rest"

# Input: John Doe Smith
# Output:
# First name: John
# Rest of name: Doe Smith
```

### Timing Out Read Operations

You can set a timeout for read operations:

```bash
read -t 5 -p "You have 5 seconds to enter your name: " name
if [ -z "$name" ]; then
    echo -e "\nTime's up!"
else
    echo -e "\nHello, $name!"
fi
```

### Reading Passwords

For sensitive information, use the `-s` option to hide input:

```bash
read -s -p "Enter password: " password
echo -e "\nPassword length: ${#password} characters"
```

Reading from a file:

```bash
# Read line by line from a file
while read line; do
    echo "Line: $line"
done < input.txt

# Read entire file into a variable
file_content=$(cat input.txt)
echo "$file_content"
```

## Practical Examples

### User Input Form

```bash
#!/bin/bash

echo "==== User Registration Form ===="
read -p "Enter username: " username
read -s -p "Enter password: " password
echo
read -p "Enter your full name: " fullname
read -p "Enter your age: " age
read -p "Enter your email: " email

echo -e "\n==== Registration Summary ===="
echo "Username: $username"
echo "Name: $fullname"
echo "Age: $age"
echo "Email: $email"
echo "Password is set and hidden"
```

### Interactive Menu

```bash
#!/bin/bash

echo "==== System Information Menu ===="
echo "1) Display Date and Time"
echo "2) Display Hostname and Kernel"
echo "3) Display Disk Usage"
echo "4) Display Memory Usage"
echo "5) Exit"

read -p "Enter your choice [1-5]: " choice

case $choice in
    1)
        echo "Current Date and Time:"
        date
        ;;
    2)
        echo "Hostname: $(hostname)"
        echo "Kernel: $(uname -r)"
        ;;
    3)
        echo "Disk Usage:"
        df -h
        ;;
    4)
        echo "Memory Usage:"
        free -m
        ;;
    5)
        echo "Exiting..."
        exit 0
        ;;
    *)
        echo "Invalid option!"
        ;;
esac
```

### Configuration File Generator

```bash
#!/bin/bash

config_file="app.conf"

read -p "Enter server address: " server_addr
read -p "Enter port number [8080]: " port_num
port_num=${port_num:-8080}  # Default value if empty
read -p "Enable debugging? (y/n): " debug_choice
if [[ "$debug_choice" == "y" ]]; then
    debug_mode="enabled"
else
    debug_mode="disabled"
fi

echo "# Configuration generated on $(date)" > $config_file
echo "SERVER_ADDRESS=$server_addr" >> $config_file
echo "PORT=$port_num" >> $config_file
echo "DEBUG_MODE=$debug_mode" >> $config_file

echo "Configuration saved to $config_file:"
cat $config_file
```

## Best Practices

1. **Always Quote Variables**
   ```bash
   file_name="my file.txt"
   
   # Bad (will break with spaces in filename)
   rm $file_name
   
   # Good (handles spaces and special characters)
   rm "$file_name"
   ```

2. **Use Braces for Clarity**
   ```bash
   name="John"
   echo "${name}'s files"  # Clear where variable ends
   ```

3. **Provide Default Values**
   ```bash
   # Use ${var:-default} for default if var is unset or empty
   echo "Hello, ${name:-World}!"
   
   # Use ${var:=default} to set the variable if it's unset or empty
   name=${name:=World}
   ```

4. **Validate User Input**
   ```bash
   read -p "Enter a number: " num
   if [[ ! "$num" =~ ^[0-9]+$ ]]; then
       echo "Error: Not a valid number!"
       exit 1
   fi
   ```

5. **Use Local Variables in Functions**
   ```bash
   function process_data {
       local temp_var="Local value"
       echo "$temp_var"
   }
   ```

## Advanced Topics

### Variable Indirection

Using one variable to reference another:

```bash
fruit="apple"
apple_count=5

# Using indirect reference
indirect_ref="${!fruit}_count"
echo "We have ${!indirect_ref} ${fruit}s"  # Outputs: We have 5 apples
```

### Parameter Expansion Tricks

```bash
# Length of a variable
name="Alexander"
echo "${#name}"  # Outputs: 9

# Substring extraction
echo "${name:0:4}"  # Outputs: Alex (starts at 0, takes 4 chars)
echo "${name:3:3}"  # Outputs: xan (starts at 3, takes 3 chars)
echo "${name:(-3)}"  # Outputs: der (last 3 chars)

# String replacement
text="Change this to that"
echo "${text/this/that}"  # Outputs: Change that to that (first occurrence)
echo "${text//this/that}"  # Outputs: Change that to that (all occurrences)

# Remove prefix pattern
filename="document.txt.bak"
echo "${filename#*.}"     # Outputs: txt.bak (remove shortest match from beginning)
echo "${filename##*.}"    # Outputs: bak (remove longest match from beginning)

# Remove suffix pattern
echo "${filename%.*}"     # Outputs: document.txt (remove shortest match from end)
echo "${filename%%.*}"    # Outputs: document (remove longest match from end)
```

### Here Documents for Multi-line Input

```bash
cat << EOF > output.txt
This is a multi-line
text block that will be
written to output.txt
EOF

# With variable substitution
name="John"
cat << EOF > greeting.txt
Hello, $name!
Welcome to Bash scripting.
Today is $(date)
EOF

# Without variable substitution
cat << 'EOF' > literal.txt
Variables like $HOME will not be expanded
Neither will commands like $(date)
EOF
```

### Command Substitution with Read

```bash
# Read output from a command line by line
while read -r line; do
    echo "Process: $line"
done < <(ps aux | grep bash)

# Alternative using pipe
ps aux | grep bash | while read -r line; do
    echo "Process: $line"
done
```

### Combining read with IFS (Internal Field Separator)

```bash
# Reading CSV data
csv_line="John,Doe,42,Developer"
IFS=',' read -r first last age profession <<< "$csv_line"
echo "Name: $first $last"
echo "Age: $age"
echo "Job: $profession"

# Temporarily changing IFS
filename="/usr/local/bin/script.sh"
IFS='/' read -ra path_parts <<< "$filename"
echo "Filename: ${path_parts[-1]}"
echo "Directory: /${path_parts[*]:0:${#path_parts[@]}-1}"
```

By mastering variables, `echo`, and `read`, you'll have a solid foundation for creating dynamic and interactive Bash scripts that can handle user input, display informative output, and manage data effectively.